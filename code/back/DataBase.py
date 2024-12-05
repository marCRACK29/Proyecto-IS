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
	
	def getAppointments(SELF, medic):
		appointments = [Appointment(None, None, None, None)]
		
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
	
	def deleteAppointment(SELF, appointment):
		return