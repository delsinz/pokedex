# -*- coding: utf-8 -*-
"""
Created on 14 Apr 2016
Last updated on 19 May 2016

Author: Nguyen Ho hon2@student.unimelb.edu.au

Function:
    This script downloads pokemon sprite and artwork images of the first 6 
    generations of pokemon and saves by pokemon id in the current directory.

Dependencies:
    gen5.csv:
        A csv file of generations 1-5 with pokemon name in the first column 
        and id in the second
    
    gen6.csv:
        A csv file of generations 6 with pokemon name in the first column 
        and id in the second

Note:
    Images are pulled from the Pokemon Database (http://img.pokemondb.net/) and 
    thus this script will no longer work if the URL path to these images is 
    modified.
    As of 19 May 2016 it will not retrieve pokemon:
    29, 32, 83, 122, 386.jpg, 413.jpg, 439, 479.jpg, 487.jpg, 555.jpg, 648.jpg
    669, 678.jpg, 719.png, 720, 721.jpg
"""
from urllib import FancyURLopener
import csv

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()

# opens a csv file containing the names and ids of pokemon from gen1-5
ifile = open('gen5.csv', "r")
reader = csv.reader(ifile)
for row in reader:
    sprite_tag = str(row[1])
    sprite_URL = "http://img.pokemondb.net/sprites/black-white/normal/" + row[0].lower().split('\n')[0] + ".png\n"
    myopener.retrieve(sprite_URL, sprite_tag+".png")
    artwork_tag = str(row[1])
    artwork_URL = "http://img.pokemondb.net/artwork/" + row[0].lower().split('\n')[0] + ".jpg\n"
    myopener.retrieve(artwork_URL, artwork_tag+".jpg")
ifile.close()

# opens a csv file containing the names and ids of pokemon from gen6
ifile2 = open('gen6.csv', "r")
reader = csv.reader(ifile2)
for row in reader:
    sprite_tag = str(row[1])
    sprite_URL = "http://img.pokemondb.net/sprites/x-y/normal/" + row[0].lower().split('\n')[0] + ".png\n"
    myopener.retrieve(sprite_URL, sprite_tag+".png")    
    artwork_tag = str(row[1])
    artwork_URL = "http://img.pokemondb.net/artwork/" + row[0].lower().split('\n')[0] + ".jpg\n"
    myopener.retrieve(artwork_URL, artwork_tag+".jpg")
ifile2.close()
