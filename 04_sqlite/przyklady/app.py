from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    url_for,
)
import sqlite3

app = Flask(__name__)


DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/films')
def films_list():
    db = get_db()
    data = db.execute('SELECT title FROM film').fetchall()
    return render_template('films.html', films=data)


@app.route('/films/<int:film_id>')
def single_film(film_id):
    db = get_db()
    data = db.execute(
        'SELECT title, release_year, description FROM film WHERE film_id = :film_id',
        {'film_id': film_id}).fetchone()
    return render_template('single_film.html', film=data)


@app.route('/films_with_category')
def films_with_category_list():
    db = get_db()
    data = db.execute('''
    SELECT title, name from film
    JOIN film_category ON film.film_id = film_category.film_id
    JOIN category ON film_category.category_id = category.category_id;
    ''').fetchall()
    return render_template('films_with_category.html', films=data)


@app.route('/films_with_category_order')
def films_with_category_order_list():
    db = get_db()
    data = db.execute('''
    SELECT title, name from film
    JOIN film_category ON film.film_id = film_category.film_id
    JOIN category ON film_category.category_id = category.category_id
    order by category.name;
    ''').fetchall()
    return render_template('films_with_category.html', films=data)


@app.route('/actors/add/sqli', methods=['GET', 'POST'])
def add_actor_version_1():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        db = get_db()
        # DO NOT WRITE QUERIES LIKE THIS!!!11!1!
        db.executescript(
            'INSERT INTO actor (first_name, last_name) VALUES ("{}", "{}")'
            .format(first_name, last_name)
        )
        db.commit()
        return redirect(url_for('actors_list'))
    else:
        return render_template('add_actor_sqli.html')


@app.route('/actors/add', methods=['GET', 'POST'])
def add_actor_version_2():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        db = get_db()
        db.execute(
            'INSERT INTO actor (first_name, last_name) VALUES (?, ?)',
            (first_name, last_name)
        )
        db.commit()
        return redirect(url_for('actors_list'))
    else:
        return render_template('add_actor.html')


@app.route('/actors/edit/<int:actor_id>', methods=['GET', 'POST'])
def edit_actor(actor_id):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        db = get_db()
        db.execute(
            'UPDATE actor SET first_name = ?, last_name = ? WHERE actor_id = ?',
            (first_name, last_name, actor_id)
        )
        db.commit()
        return redirect(url_for('actors_list'))
    else:
        db = get_db()
        actor = db.execute(
            'SELECT first_name, last_name from actor WHERE actor_id = ?',
            (actor_id,)).fetchone()
        return render_template('edit_actor.html', actor=actor, actor_id=actor_id)


@app.route('/actors')
def actors_list():
    db = get_db()
    data = db.execute('SELECT first_name, last_name FROM actor ORDER BY last_update DESC').fetchall()
    return render_template('actors.html', actors=data)


@app.route('/actors/delete/<int:actor_id>', methods=['GET', 'POST'])
def delete_actor(actor_id):
    if request.method == 'POST':
        db = get_db()
        db.execute('DELETE FROM actor WHERE actor_id = ?', (actor_id,))
        db.commit()
        return redirect(url_for('actors_list'))
    else:
        db = get_db()
        actor = db.execute(
            'SELECT first_name, last_name from actor WHERE actor_id = ?',
            (actor_id,)).fetchone()
        return render_template('delete_actor.html', actor=actor, actor_id=actor_id)


@app.route('/actors_count')
def actors_list_with_count():
    db = get_db()
    data = db.execute('SELECT first_name, last_name FROM actor ORDER BY last_update DESC').fetchall()
    count = db.execute('SELECT COUNT(*) FROM actor').fetchone()
    return render_template('actors_count.html', actors=data, count=count[0])


@app.route('/')
def main_view():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
