import sys
import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session

from back import *

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Cargar base de datos
access = json.loads(open(sys.path[0] + "/back/db/db-data.json").read())
database = DataBase(access)


# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		rut = request.form.get('rut')
		name = request.form.get('name')

		if database.userExists(rut):
			# Guardar información del usuario en la sesión
			session['user'] = {"rut": rut, "name": name}
			return redirect(url_for('index'))
		else:
			return render_template('login.html', error="Rut o nombre incorrecto.")

	# Mostrar formulario de login
	return render_template('login.html')


# Ruta del catálogo (restringida)
@app.route('/')
def index():
	if 'user' not in session:
		return redirect(url_for('login'))
	return render_template('catalog.html')


# API para obtener médicos
@app.route('/api/medics', methods=['GET'])
def getMedics():
	medics = database.getMedics()
	medicsData = []

	for medic in medics:
		medicsData.append({
			'name': medic.name,
			'speciality': medic.area,
			'rut': medic.rut
		})

	return jsonify(medicsData)


@app.route('/api/createAppointment', methods=['PUT'])
def createAppointment():
	data = json.loads(request.data)
	
	agendaID = data["agendaID"]
	
	rutM = data["rutM"]
	rutP = session['user']['rut']
	
	database.createAppointment(agendaID, rutM, rutP)
	
	return jsonify(data)

# API para obtener agenda de un médico
@app.route('/api/medic/<rut>/agenda', methods=['GET'])
def getMedicAgenda(rut):
	agendas = database.getAgenda(rut)
	data = []
	
	for agenda in agendas:
		data.append({
			'ID': agenda.ID,
			'rutM': agenda.rutM,
			'day': agenda.start.strftime("%A %d"),
			'month': agenda.start.strftime("%B"),
			'year': agenda.start.strftime("%Y"),
			'time': agenda.start.strftime("%H:%M"),
		})
	
	return jsonify(data)

if __name__ == "__main__":
	app.run()
