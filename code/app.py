import sys
import json

from flask import Flask, jsonify, render_template

from back import *

app = Flask(__name__)

access = json.loads(open(sys.path[0] + "/back/db/db-data.json").read())
database = DataBase(access)

@app.route('/api/medics', methods = ['GET'])
def getMedics():
	medics = database.getMedics()
	medicsData = []
	
	for medic in medics:
		print(f"{medic.rut} {medic.name} {medic.area}")
		
		medicsData.append({'name': medic.name, 'speciality': medic.area})
	
	return jsonify(medicsData)

@app.route('/')
def index():
	return render_template('catalog.html')

if __name__ == "__main__":
	app.run()