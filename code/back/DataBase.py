import psycopg
from .Medic import Medic

class DataBase:
	cursor = None
	connection = None
	
	def __init__(SELF):
		uri = "postgres://default:di4nXveHD5uj@ep-still-mountain-a42h25z8.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
		SELF.medics = []
		
		try:
			SELF.connection = psycopg.connect(uri, autocommit = True)
			SELF.cursor = SELF.connection.cursor()
		
		except Exception as exception:
			raise Exception("[ERROR]")
		
		return
	
	def __del__(SELF):
		SELF.cursor.close()
		SELF.connection.close()

		return
	
	def createAppointment(SELF, medic, patient, start, finish):
		query = "INSERT INTO appointment (medic, patient, start, finish) VALUES (%s, %s, %s, %s);"
		data = (medic.rut, patient.rut, start, finish)
		SELF.medics.append(medic)
		
		try:
			SELF.cursor.execute(query, data)
			
			print("APPOINTMENT CREATED")
		
		except Exception as exception:
			raise Exception("[ERROR]")
		
		return

	def get_all_medics(SELF) -> list:
		#return SELF.medics
		return [Medic(213472349, "Antonio", "Traumatología"), Medic(123456789, "Juan", "Pediatría"), Medic(987654321, "María", "Cardiología")]