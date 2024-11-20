class Appointment:
	medic = None
	patient = None
	
	agendaID = None
	interval = None
	
	def __init__(SELF, medic, patient, agendaID, interval):
		SELF.medic = medic
		SELF.patient = patient
		
		SELF.agendaID = agendaID
		SELF.interval = interval
		
		return