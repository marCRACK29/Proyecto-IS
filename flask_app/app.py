from flask import Flask, render_template
import psycopg2
from config import DATABASE_URL

app = Flask(__name__)

def ejecutar_script_sql():
    """Ejecuta el script-BD.sql para poblar la base de datos."""
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Leer el archivo script-BD.sql
    with open('sql/script-BD.sql', 'r') as file:
        script = file.read()

    try:
        # Ejecutar el script
        cursor.execute(script)
        conn.commit()
        print("Script SQL ejecutado correctamente.")
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Llamar a la función para ejecutar el script al iniciar la aplicación
ejecutar_script_sql()

# Ruta para mostrar el catálogo de médicos
@app.route('/')
def mostrar_catalogo():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, especialidad FROM "proyect".medico')
    medicos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('catalog.html', medicos=medicos)

if __name__ == '__main__':
    app.run(debug=True)

