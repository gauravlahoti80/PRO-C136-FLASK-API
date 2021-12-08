from flask import Flask, jsonify, request
import csv
import json 

data = []
app = Flask(__name__)

with open('new.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)
    
headers = data[0]
headersJ = json.dumps(headers)

planets_data = data[1:]
planets_dataJ = json.dumps(planets_data)

@app.route('/getheaders')
def displayHeaders():
    return jsonify({
        'headers' : headersJ
    })

@app.route('/getplanetsdata')
def getPlanetsData():
    return jsonify({
        'planetsdata' : planets_dataJ
    })
    
if(__name__ == '__main__'):
    app.run(debug=True)