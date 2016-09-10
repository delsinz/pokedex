# This is the routing script to route to different pages

from flask import render_template, request
from app import app
from app import pokeJSON
from app import pivotGenerator
import json

#Pokedex Page
@app.route('/')
@app.route('/index')
@app.route('/pokemon')
def pokemon():
    pokemon = pokeJSON.getJSON()
    return render_template('pokemon.html',pokemon=pokemon,title='Pokedex')

#Data Table Page
@app.route('/data')
def data():
    return render_template('data.html',title='Data Table')

#Pivot Table Page
@app.route('/pivot')
def pivot():
    return render_template('pivot.html',title='Pivot Table')

#Pivot Table Ajax Handler
@app.route('/ajax-handler', methods=['POST'])
def handler():
    payload = request.data
    json_request = json.loads(payload)
    rowcol = json_request['rowcol']
    aggregate = json_request['aggregate']
    filter_val = json_request['filter']
    hybrid = json_request['hybrid']
    if rowcol == "gen-type":
        row = "gen"
        column = "type"
    elif rowcol == "type-gen":
        row = "type"
        column = "gen"
    # note: pivotGenerator returns (xLabels, yLabels, values)
    response = pivotGenerator.genTable(column, row, filter_val, aggregate, hybrid)
    return (json.dumps({"xLabels": response[0], "yLabels": response[1],
                        "values": response[2], }))

# Comparisons Page
@app.route('/compare')
def compare():
    pokemon = pokeJSON.getJSON()
    return render_template('compare.html',pokemon=pokemon, title='Comparison')

# Observations Page
@app.route('/observations')
def observations():
    pokemon = pokeJSON.getJSON()
    return render_template('observations.html',pokemon=pokemon,title='Observations')