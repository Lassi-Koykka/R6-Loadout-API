from flask import Flask, request, jsonify, send_file
import json
from functions import *

app = Flask(__name__)

#updateOperatorFiles()

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/<team>')
def getTeam(team):
  team = team.lower()
  operators = readOperators('./' + team + '.json')
  return jsonify(operators)
  
@app.route('/<team>/<name>')
def getOperator(team, name):
  team = team.lower()
  name = name.capitalize()
  operators = readOperators('../teams/' + team + '.json')
  for operator in operators:
    if operator["name"] == name:
      return jsonify(operator)

@app.route('/<team>/<name>/<picture>')
def getPicture(team, name, picture):
  team = team.lower()
  name = name.capitalize()
  operators = readOperators('./teams/' + team + '.json')
  for operator in operators:
    if operator["name"] == name:
      if picture.lower() == "icon":
        return send_file('./opIcons/' + name.capitalize() + 'Icon.png', mimetype='image/png')
  