import sqlite3

from flask import Flask, g, request, jsonify
from wtforms import Form, StringField, validators, IntegerField

DATABASE = 'database.db'

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g.db = sqlite3.connect(DATABASE)
        # Foreign key support is disabled by default. One needs to set it up
        # once for each connection. More on this topic can be found here:
        # https://www.sqlite.org/foreignkeys.html (point 2.).
        db.execute('PRAGMA foreign_keys = 1')
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, error, status_code=None, payload=None):
        super().__init__(self)
        self.error = error
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['error'] = self.error
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/cities', methods=['GET', 'POST'])
def cities():
    if request.method == 'GET':
        return get_cities()
    else:
        return post_new_city()


# https://wtforms.readthedocs.io/en/stable/
class CitiesValidationForm(Form):
    country_name = StringField(validators=[validators.optional()])
    per_page = IntegerField(validators=[validators.optional(),
                                        validators.number_range(min=1)])
    page = IntegerField(validators=[validators.optional(),
                                    validators.number_range(min=1)])


def get_cities():
    db = get_db()

    form = CitiesValidationForm(request.args)

    if not form.validate():
        return jsonify(error=form.errors)

    per_page = form.data['per_page'] or -1
    limit = per_page

    page = form.data['page'] or 0
    page_index = page - 1
    offset = page_index * per_page

    if form.data['country_name']:
        cities_rows = db.execute(
            'SELECT city.city FROM city '
            'JOIN country ON city.country_id = country.country_id '
            'WHERE country.country = ? COLLATE NOCASE '
            'ORDER BY city.city COLLATE NOCASE '
            'LIMIT ? OFFSET ?;',
            (form.data['country_name'], limit, offset)
        )
    else:
        cities_rows = db.execute(
            'SELECT city FROM city '
            'ORDER BY city COLLATE NOCASE '
            'LIMIT ? OFFSET ?;',
            (limit, offset)
        )
    return jsonify([row[0] for row in cities_rows.fetchall()])


def post_new_city():
    db = get_db()

    new_city = request.get_json()
    country_id = new_city.get('country_id')
    city_name = new_city.get('city_name')

    # Check if all required parameters are provided
    if country_id is None:
        raise InvalidUsage(f'missing "country_id" in request data')
    if city_name is None:
        raise InvalidUsage(f'missing "city_name" in request data')

    # # A -------------------------------------------------------------------- >
    # # Check if specified country exists.
    # country_id_exists = bool(
    #     db.execute(
    #         'SELECT * FROM country '
    #         'WHERE country.country_id = ?;',
    #         (country_id,)
    #     ).fetchone()[0]
    # )
    # if not country_id_exists:
    #     raise InvalidUsage(f'No country for country_id: "{country_id}"')
    #
    # # Check if specified city already exists in the country.
    # duplicate = bool(
    #     db.execute(
    #         'SELECT count(*) FROM city '
    #         'WHERE city = :city_name '
    #         'AND country_id = :country_id;',
    #         new_city
    #     ).fetchone()[0]
    # )
    # if duplicate:
    #     raise InvalidUsage(f'City called {city_name} already exists in the '
    #                        f'country with country_id = {country_id}')
    #
    # # === What could possibly go wrong here? ===
    #
    # # Now we can add our city.
    # db.execute(
    #     'INSERT INTO city (city, country_id) '
    #     'VALUES (:city_name, :country_id);',
    #     new_city
    # )
    #
    # # At least we think we can...
    # db.commit()
    # # /A < -------------------------------------------------------------------

    # B -------------------------------------------------------------------- >
    try:
        db.execute(
            'INSERT INTO city (city, country_id) '
            'VALUES (:city_name, :country_id);',
            new_city
        )
        db.commit()
    except sqlite3.IntegrityError as error:

        db.rollback()
        error_reason = error.args[0]

        if error_reason.startswith('UNIQUE constraint failed'):
            raise InvalidUsage(f'City called {city_name} already exists in '
                               f'a country with country_id = {country_id}')

        elif error_reason.startswith('FOREIGN KEY constraint failed'):
            raise InvalidUsage(f'No country with country_id = {country_id}')

        else:
            raise error
    # /B < -------------------------------------------------------------------

    db_city = db.execute(
        'SELECT city_id, city as city_name, country_id FROM city '
        'WHERE city.city = :city_name AND city.country_id = :country_id;',
        new_city
    ).fetchone()

    return jsonify(dict(db_city))


@app.route('/lang_roles')
def lang_roles():
    db = get_db()
    # Only INNER JOIN or LEFT JOIN sqlite.
    lang_roles_rows = db.execute(
        'SELECT language.name, count(film_actor.film_id) '
        'FROM language '
        'LEFT JOIN film ON language.language_id = film.language_id '
        'LEFT JOIN film_actor ON film.film_id = film_actor.film_id '
        'GROUP BY language.name;'
    ).fetchall()
    return jsonify(dict(lang_roles_rows))


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False)
