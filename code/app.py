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
	print(f"Medics retrieved: {medics}")
	for medic in medics:
		print(f"{medic.rut} {medic.name} {medic.area}")
		
		medicsData.append({'name': medic.name, 'speciality': medic.area})
	
	return jsonify(medicsData)

@app.route('/medic/<medic_id>')
def medic_page(medic_id):
	# Buscar datos del médico en la base de datos
	medic = next((m for m in database.getMedics() if m.name == medic_id), None)

	if medic:
		return render_template('medic.html', medic=medic)
	else:
		return "Médico no encontrado", 404


@app.route('/')
def index():
	return render_template('catalog.html')

if __name__ == "__main__":
	app.run(debug = True)