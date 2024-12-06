import sys
import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session

from back import *

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Cargar base de datos
access = json.loads(open(sys.path[0] + "/back/db/db-data.json").read())
database = DataBase(access)

def traducir_dia(dia_ingles):
	dias_traduccion = {
		'Monday': 'Lunes',
		'Tuesday': 'Martes',
		'Wednesday': 'Miércoles',
		'Thursday': 'Jueves',
		'Friday': 'Viernes',
		'Saturday': 'Sábado',
		'Sunday': 'Domingo'
	}
	return dias_traduccion[dia_ingles]

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
	session.clear()  # Limpiar la sesión
	if request.method == 'POST':
		rut = request.form.get('rut')
		name = request.form.get('name')

		# Verificar si es paciente
		query_patient = "SELECT * FROM Patient WHERE rut = %s;"
		database.cursor.execute(query_patient, (rut,))
		patient = database.cursor.fetchone()

		# Si es paciente, se guarda en la sesión y se redirige al catálogo
		if patient:
			session['user'] = {"rut": rut, "name": patient[1], "role": "patient"}
			return redirect(url_for('index'))

		# Verificar si es médico
		query_medic = "SELECT * FROM Medic WHERE rut = %s;"
		database.cursor.execute(query_medic, (rut,))
		medic = database.cursor.fetchone()

		# Si es médico, se guarda en la sesión y se redirige al dashboard del médico
		if medic:
			session['user'] = {"rut": rut, "name": medic[1], "role": "medic"}
			return redirect(url_for('medic_dashboard'))

		# Si no es paciente ni médico, se redirige al registro
		return redirect(url_for('register', rut=rut))

	return render_template('login.html')

# Se utiliza en catalog.html y medic_dashboard.html para cerrar la sesión y volver al login
@app.route('/logout')
def logout():
	session.clear()  # Limpiar la sesión
	return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		rut = request.form.get('rut')
		name = request.form.get('name')

		# Inserción del nuevo usuario en la base de datos, incluyendo la contraseña
		query = "INSERT INTO Patient (rut, name) VALUES (%s, %s);"
		database.cursor.execute(query, (rut, name))
		session['user'] = {"rut": rut, "name": name}

		return redirect(url_for('index'))

	return render_template('register.html')

@app.route('/medic/dashboard')
def medic_dashboard():
	if 'user' not in session or session['user']['role'] != 'medic':
		return redirect(url_for('login'))

	rut = session['user']['rut']
	agendas = database.getAgenda(rut)  # Obtiene todas las entradas de la agenda del médico

	# Organizar la agenda en un diccionario por días y horas
	agenda_semanal = {day: {hour: {'free': True} for hour in range(8, 18)}
					  for day in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']}

	for agenda in agendas:
		day = traducir_dia(agenda.start.strftime('%A'))  # Obtener el día en texto
		hour = agenda.start.hour
		
		agenda_semanal[day][hour] = {'free': agenda.free}
		
		print(agenda_semanal)

	return render_template('medic_dashboard.html', agenda=agenda_semanal, user=session['user'])

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


@app.route('/api/createAppointment', methods=['POST'])
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
		if(not agenda.free):
			continue
		
		data.append({
			'ID': agenda.ID,
			'rutM': agenda.rutM,
			'day': agenda.start.strftime("%d"),
			'month': agenda.start.strftime("%B"),
			'year': agenda.start.strftime("%Y"),
			'time': agenda.start.strftime("%H:%M"),
		})

	return jsonify(data)

# API para obtener las citas del usuario (es específico, no global).
@app.route('/api/user/appointment', methods=['GET'])
def user_appointment():
	if 'user' not in session or session['user']['role'] != 'patient':
		return jsonify({'error': 'No autenticado'}), 401

	rut = session['user']['rut']

	try:
		appointments = database.getAppointments(rut)

		# Depuración: imprime las citas que se están devolviendo
		print("Citas obtenidas:", appointments)

		return jsonify(appointments)
	except Exception as e:
		print('Error al obtener citas:', e)
		return jsonify({'error': 'Error al obtener citas'}), 500


def get_appointment(self, patient):
	query = """
        SELECT 
            medic.name AS doctor_name,
            medic.area AS doctor_area,
            agenda.start AS agenda_date,
            agenda.start AS agenda_time,
            agenda.ID AS agendaID  -- Agregamos el campo agendaID
        FROM APPOINTMENT
        JOIN medic ON appointment.rutM = medic.rut
        JOIN agenda ON appointment.agendaID = agenda.ID
        WHERE appointment.rutP = %s
    """
	data = None

	try:
		# Ejecutamos la consulta
		self.cursor.execute(query, (patient,))
		data = self.cursor.fetchall()

	except Exception as e:
		# Lanzamos una excepción detallada si algo falla
		raise Exception('Error al obtener citas:', e)

	appointments = []

	# Procesamos los resultados
	for row in data:
		medic_name = row['doctor_name']
		medic_area = row['doctor_area']
		agenda_date = row['agenda_date']
		agenda_time = row['agenda_time']
		agenda_id = row['agendaID']  # Extraemos agendaID

		# Creamos objetos para el médico y la cita
		medic = Medic(medic_name, medic_area)
		appointment = Appointment(medic, patient, agenda_date, agenda_time, agenda_id)

		appointments.append(appointment)

	return appointments

@app.route('/api/cancelAppointment', methods=['POST'])
def cancelAppointment():
	try:
		data = json.loads(request.data)
		agendaID = data.get("agendaID")

		if not agendaID:
			raise KeyError("agendaID faltante o inválido.")

		rutP = session['user']['rut']
		database.deleteAppointment(agendaID, rutP)

		return jsonify({"success": True})
	except KeyError as e:
		print(f"Clave faltante en los datos enviados: {e}")
		return jsonify({"error": f"Clave faltante: {e}"}), 400
	except Exception as e:
		print(f"Error al cancelar la cita: {e}")
		return jsonify({"error": "Error al cancelar la cita."}), 500


@app.route('/my-appointments')
def my_appointments():
    return render_template('appointments.html')


if __name__ == "__main__":
	app.run(debug = True)