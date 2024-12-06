class Appointment:
	medic = None
	patient = None
	agendaID = None
	appointment_date = None
	appointment_time = None

	def __init__(SELF, medic, patient, agendaID, appointment_date, appointment_time):
		SELF.medic = medic
		SELF.patient = patient
		SELF.agendaID = agendaID
		SELF.appointment_date = appointment_date
		SELF.appointment_time = appointment_time

		return