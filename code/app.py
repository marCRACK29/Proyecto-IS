from back import *

from datetime import datetime

def main():
	testCreateAppointment()
	
	return

def testCreateAppointment():
	database = DataBase()
	
	medic = Medic(222222222, "Antonio", None)
	patient = Patient(111111111, "Jose")
	
	start = datetime.today()
	finish = datetime.today()
	
	database.createAppointment(medic = medic, patient = patient, start = start, finish = finish)
	
	return

if __name__ == "__main__":
	main()