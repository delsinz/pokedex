#Returns a list of pokemon as JSON

import csv

pokemon = [] 
# Each individual pokemon is stored as a dictionary then converted to JSON
individual = {}
#Headings in the CSV
headings = []
attribute = ''

# Initialize CSV reader
file = open('app/static/data/pokemon.csv','r')
fileReader = csv.reader(file)
headings = next(fileReader)

def getJSON():
	#Iterate over each row
	for row in fileReader:
		for i in range(len(row)):
			attribute = row[i]
			if headings[i] == 'Height' or headings[i] == 'Weight':
				attribute = row[i].split('(')[1][:-1]
			# Individual is assigned attribute:value ie "Height":"0.71m"
			individual[headings[i]] = attribute

		pokemon.append(individual.copy())

	return pokemon


