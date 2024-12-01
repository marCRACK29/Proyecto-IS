import sys
import json

from flask import Flask, jsonify, render_template

from back import *

app = Flask(__name__)

access = json.loads(open(sys.path[0] + "/back/db/db-data.json").read())
database = DataBase(access)

@app.route('/api/medics', methods = ['GET'])
def getMedics():
	medics = database.getMedics()
	medicsData = []
	
	for medic in medics:
		print(f"{medic.rut} {medic.name} {medic.area}")
		
		medicsData.append({
			'name': medic.name,
			'speciality': medic.area,
			'rut': medic.rut
		})
	
	return jsonify(medicsData)
###
@app.route('/api/medic/<rut>/agenda', methods=['GET'])
def getMedicAgenda(rut):
    try:
        query = "SELECT ID, rutM, start, free FROM Agenda WHERE rutM = %s;"
        database.cursor.execute(query, (rut,))
        data = database.cursor.fetchall()
        agenda_list = [
            {"id": row[0], "rutM": row[1], "start": row[2], "free": row[3]}
            for row in data
        ]
        return jsonify(agenda_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
###
@app.route('/')
def index():
	return render_template('catalog.html')

if __name__ == "__main__":
	app.run()