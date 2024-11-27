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

@app.route('/api/medic/<medic_id>/schedule', methods = ['GET'])
def get_schedule():
	schedule = [
		{'start': '08:00', 'end': '09:00'},
		{'start': '09:00', 'end': '10:00'},
		{'start': '10:00', 'end': '11:00'},
		{'start': '11:00', 'end': '12:00'},
		{'start': '12:00', 'end': '13:00'},
		{'start': '13:00', 'end': '14:00'},
		{'start': '14:00', 'end': '15:00'},
		{'start': '15:00', 'end': '16:00'},
		{'start': '16:00', 'end': '17:00'},
		{'start': '17:00', 'end': '18:00'},
		{'start': '18:00', 'end': '19:00'},
		{'start': '19:00', 'end': '20:00'},
		{'start': '20:00', 'end': '21:00'},
		{'start': '21:00', 'end': '22:00'}
	]

	return jsonify(schedule)

@app.route('/medic/<medic_id>')
def medic_page(medic_id):
	# Buscar datos del médico en la base de datos
	medic = next((m for m in database.getMedics() if m.name == medic_id), None)

	if medic:
		return render_template('medic.html', medic=medic)
	else:
		return "Médico no encontrado", 404

@app.route('/api/medics/filter/<speciality>', methods=['GET'])
def getMedicsBySpeciality(speciality):
	medics = database.getMedics()
	filtered_medics = [medic for medic in medics if medic.area.lower() == speciality.lower()]
	medicsData = [{'name': medic.name, 'speciality': medic.area} for medic in filtered_medics]
	return jsonify(medicsData)


@app.route('/')
def index():
	return render_template('catalog.html')

if __name__ == "__main__":
	app.run(debug = True)