import sys
import json

from datetime import datetime

from back import *

def main():
	access = json.loads(open(sys.path[0] + "/back/db/db-data.json").read())
	database = DataBase(access)
	
	testGetMedics(database)
	testCreateAppointment(database)
	
	return

def testGetMedics(database):
	for medic in database.getMedics():
		print(f"{medic.rut} {medic.name} {medic.area}")

def testCreateAppointment(database):
	agendaID = 1
	
	medic = Medic("100000000", None, None, None)
	patient = Patient("000000001", None)
	
	database.createAppointment(agendaID = agendaID, medic = medic, patient = patient)
	
	return

if __name__ == "__main__":
	main()