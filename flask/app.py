from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content'] # Para que el contenido de la entrada sea el mismo que se ingresó
        new_task = Todo(content=task_content) # Objetos de la clase Todo
        try:
            db.session.add(new_task) # Agregar a la base de datos
            db.session.commit() # Guardar en la base de datos
            return redirect('/')
        except:
            return 'Sin asuntos en task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # Examinar el contenido de la BD en el orden que se creó
        return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:id>') #ejecutar la acción de eliminar
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error al eliminar esa task'

@app.route('/update/<int:id>', methods = ['GET', 'POST']) #ejecutar la acción de actualizar
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/') #redirigir a la página principal
        except:
            return 'Error al actualizar la task'
    else:
        return render_template('update.html', task = task)

@app.route('/schedules/<int:doctor_id>')
def show_schedules(doctor_id):
    return render_template('schedules.html', doctor_id=doctor_id)

if __name__ == "__main__":
    app.run(debug=True)