from flask import Flask, jsonify, render_template
from back import *

app = Flask(__name__)

# Endpoint para obtener todos los médicos
@app.route('/api/medics', methods=['GET'])
def get_medics():
    database = DataBase()
    medics = database.get_all_medics()  # Asegúrate de tener este método en tu clase DataBase
    medic_list = [{'name': medic.name, 'speciality': medic.area} for medic in medics]
    return jsonify(medic_list)

# Página principal para graficar
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
