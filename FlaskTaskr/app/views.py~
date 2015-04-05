#View
from forms import AddTaskForm

from functools import wraps
from flask import Flask, flash, redirect, render_template, request, \
				session, url_for
from flask.ext.sqlalchemy import SQLAlchemy


#Config
app = Flask(__name__)
app.config.from_object('_config')
db = SQLAlchemy(app)

from models import Task

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

@app.route('/logout/')
def logout():
	session.pop('logged_in', None)
	flash('You are logged out. Bye. :(')
	return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
			return render_template('login.html', error=error)
		else:
			session['logged_in'] = True
			return redirect(url_for('tasks'))
	if request.method == 'GET':
		return render_template('login.html')


@app.route('/tasks/')
@login_required
def tasks():
	"""
	Query the database for open and closed tasks. 
	Pass the query to two variables, open_tasks and closed_tasks,
	and then passing those variables to the tasks.html to populate
	open and closed task lists.
	"""
	open_tasks = db.session.query(Task).filter_by(status="1").order_by(Task.due_date.asc())
	closed_tasks = db.session.query(Task).filter_by(status="0").order_by(Task.due_date.asc())
	return render_template("tasks.html", 
			       form=AddTaskForm(request.form),
			       open_tasks=open_tasks,
			       closed_tasks=closed_tasks
	)
	

@app.route('/add/', methods=['GET', 'POST'])
@login_required
def new_task():
	form = AddTaskForm(request.form)
	if request.method == "POST":
		if form.validate_on_submit():
			new_task = Task(
				form.name.data,
				form.due_date.data,
				form.priority.data,
				'1'
				)
			db.session.add(new_task)
			db.session.commit()
			flash('New entry was successfull.')
	return redirect(url_for('tasks'))



@app.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
	"""
	Mark tasks as complete by
	updating the database using a query.
	"""
	new_id = task_id
	db.session.query(Task).filter_by(task_id=new_id).update({"status": "0"})
	db.session.commit()
	flash('The task was marked as complete.')
	return redirect(url_for('tasks'))


@app.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
	new_id = task_id
	db.session.query(Task).filter_by(task_id=new_id).delete()
	db.session.commit()
	flash('The task was marked as deleted.')
	return redirect(url_for('tasks'))
