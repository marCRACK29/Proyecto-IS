import psycopg

from .Medic import Medic
##
from .Agenda import Agenda
from .Appointment import Appointment
##

class DataBase:
	cursor = None
	connection = None
	
	def __init__(SELF, access):
		user = access["user"]
		host = access["host"]
		database = access["database"]
		password = access["password"]
		
		try:
			SELF.connection = psycopg.connect(user = user, host = host, dbname = database, password = password, autocommit = True)
			SELF.cursor = SELF.connection.cursor()
		
		except Exception as exception:
			raise Exception("[ERROR]")
		
		return
	
	def __del__(SELF):
		SELF.cursor.close()
		SELF.connection.close()
		
		return
	
	def userExists(SELF, rut):
		query = "SELECT * FROM patient WHERE rut = %s;"
		data = None

		try:
			SELF.cursor.execute(query, (rut, ))
			
			data = SELF.cursor.fetchone()
		
		except Exception as exception:
			raise Exception(f"[ERROR] {exception}")
		
		if data:
			return True
		
		return False
	
	def medicExists(SELF, rut):
		query = "SELECT * FROM medic WHERE rut = %s;"
		data = None

		try:
			SELF.cursor.execute(query, (rut, ))
			
			data = SELF.cursor.fetchone()
		
		except Exception as exception:
			raise Exception(f"[ERROR] {exception}")
		
		if data:
			return True
		
		return False

	##
	def agendaExists(SELF, rut):
		exists = True
		
		return exists
	##
	
	def createUser(SELF, rut, name):
		query = "INSERT INTO patient (rut, name) VALUES (%s, %s)"
		
		try:
			SELF.cursor.execute(query, (rut, name))
		
		except Exception as exception:
			raise Exception(f"[ERROR] {exception}")
		
		return

	def getAgenda(SELF, rutM):
		query = "SELECT ID, rutM, start, free FROM agenda WHERE rutM = %s;"
		data = None

		try:
			SELF.cursor.execute(query, (rutM, ))
			
			data = SELF.cursor.fetchall()
		
		except Exception as exception:
			raise Exception(f"[ERROR] {exception}")

		agendas = []
		
		for row in data:
			agenda_item = Agenda(row[0], row[1], row[2], row[3])
			
			agendas.append(agenda_item)
		
		return agendas

	def getMedics(SELF):
		query = "SELECT * FROM medic;"
		data = None
		
		try:
			SELF.cursor.execute(query)
			
			data = SELF.cursor.fetchall()
		
		except Exception as exception:
			raise Exception(f"[ERROR] {exception}")
		
		medics = []
			
		for row in data:
			medic = Medic(row[0], row[1], row[2], None)
			
			medics.append(medic)
		
		return medics

	def getAppointments(self, patient):
		query = """
	        SELECT 
	            medic.name, medic.area, agenda.start 
	        FROM appointment
	        JOIN medic ON appointment.rutM = medic.rut
	        JOIN agenda ON appointment.agendaID = agenda.ID
	        WHERE appointment.rutP = %s;
	    """
		data = None

		try:
			self.cursor.execute(query, (patient,))
			data = self.cursor.fetchall()

		except Exception as exception:
			raise Exception(f"[ERROR] {exception}")

		appointments = []

		for row in data:
			# Creamos la instancia de Appointment con los detalles obtenidos
			medic_name = row[0]
			medic_area = row[1]
			appointment_datetime = row[2]

			# Asumiendo que `appointment_datetime` es un tipo datetime que contiene fecha y hora
			appointment_date = appointment_datetime.strftime('%d-%m-%Y')  # Fecha formateada
			appointment_time = appointment_datetime.strftime('%H:%M')  # Hora formateada

			# Crear el objeto de la cita con los detalles del médico, fecha y hora
			medic = Medic(None, medic_name, medic_area, None)  # Asumiendo que la clase `Medic` tiene un constructor así
			appointment = Appointment(medic, patient, row[2], appointment_date, appointment_time)

			appointments.append({
				'medic': appointment.medic.name,  # Accediendo al nombre del médico
				'speciality': appointment.medic.area,  # Accediendo al área del médico
				'appointment_date': appointment.appointment_date,
				'appointment_time': appointment.appointment_time
			})

		return appointments

	def createAppointment(SELF, agendaID, rutM, rutP):
		query = "INSERT INTO appointment (agendaID, rutM, rutP) VALUES (%s, %s, %s);"
		data = (agendaID, rutM, rutP)

		try:
			SELF.cursor.execute(query, data)

			print("APPOINTMENT CREATED")

		except Exception as exception:
			raise Exception("[ERROR]")

		return

	def deleteAppointment(SELF, agendaID, rutP):
		query = "DELETE FROM appointment WHERE agendaID = %s AND rutP = %s;"
		data = (agendaID, rutP)

		try:
			SELF.cursor.execute(query, data)
			print("APPOINTMENT DELETED")
		except Exception as exception:
			print(f"Error al cancelar la cita: {exception}")
			raise Exception("[ERROR]")






