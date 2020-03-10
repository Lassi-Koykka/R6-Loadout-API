from flask import Flask, request, jsonify
import json
from functions import *

app = Flask(__name__)

#updateOperatorFiles()

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/<team>/<name>')
def getOperator(team, name):
  team = team.lower()
  name = name.capitalize()
  operators = readOperators('../' + team + '.json')
  for operator in operators:
    if operator["name"] == name:
      return jsonify(operator)
  