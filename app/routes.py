from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import TestForm
import sqlite3 as sql


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    title = 'Components Library'
    form = TestForm()
    if form.validate_on_submit():
        # Capturing form input
        name = form.name.data
        part = form.part.data
        description = form.description.data
        project = form.project.data
        location = form.location.data

        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("""INSERT INTO components (name,part,description,project,location)
                        VALUES(?, ?, ?, ?, ?)""", (name, part, description, project, location))

        flash(f"Name: {name} Part # {part}, Location: {location}, Project: {project}", 'success')
        return redirect(url_for('form'))

    return render_template('form.html', title=title, form=form)


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("select * from components")

    rows = cur.fetchall()

    return render_template("list.html", rows=rows)


@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search = request.form['search']

        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute(
                'SELECT * FROM components WHERE part LIKE ? OR name LIKE ? OR project LIKE ?',
                ["%" + search + "%", "%" + search + "%", "%" + search + "%"]
            )
            results = cur.fetchall()

            return render_template("index.html", results=results)


@app.route("/delete_user/<string:id>", methods=['GET'])
def delete_user(id):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("delete from components where id=?", (id,))
    con.commit()
    flash('component Deleted', 'warning')
    return redirect(url_for("list"))
