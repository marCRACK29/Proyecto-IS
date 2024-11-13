class Appointment:
	ID = None
	
	medic = None
	patient = None
	
	start = None
	finish = None
	
	def __init__(SELF, ID, medic, patient, start, finish):
		SELF.ID = ID
		
		SELF.medic = medic
		SELF.patient = patient
		
		SELF.start = start
		SELF.finish = finish
		
		return