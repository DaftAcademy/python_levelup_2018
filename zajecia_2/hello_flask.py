from flask import Flask, request, render_template, make_response
import sys
sys.stderr


persons = {
	'Jan': {
		'name': 'Jan',
		'surname': 'Kowalski',
		'occupation': 'Warszawa',
	},
}

app = Flask(__name__)


@app.route("/")
def hello():
    print('lol')
    return 'hello from flask'


@app.route("/request_query_string_discovery")
def print_request():
    print('\n')
    print(dir(request))
    print('\n')
    print('request.args:', str(request.args))
    print('type(request.args):', type(request.args))
    print('request.query_string:', request.query_string)
    return 'lol'


@app.route('/request_query_string_based_response')
def print_request_2():
    print('\n')
    line_tmpl = '{}: {}'
    lines = []
    for key in request.args.keys():
        lines.append(line_tmpl.format(key, request.args[key]))
        lines.append('lool')
    print('\n'.join(lines))
    return '\n'.join(lines)


@app.route('/request_query_string_based_response_with_template')
def print_request_3():
    query_string_data = dict(request.args)
    return render_template('querystring_render_tmpl.html', query_string_data=query_string_data)


@app.route("/simple_path_tmpl/<sample_variable>")
def simple_path_tmpl(sample_variable):
    print(sample_variable)
    print(type(sample_variable))
    print(app.url_map)
    return render_template(
        'route_description_tmpl.html',
        value=sample_variable,
        my_type=type(sample_variable),
        my_id=id(sample_variable),
    )


@app.route("/simple_path_int/<int:sample_variable>")
def simple_path_int(sample_variable):
    print(sample_variable)
    print(type(sample_variable))
    print(app.url_map)
    return render_template(
        'route_description_tmpl.html',
        value=sample_variable,
        my_type=type(sample_variable),
        my_id=id(sample_variable),
    )


@app.route("/path/<path:my_path>")
def path_all(my_path):
    print(my_path)
    print(type(my_path))
    print(app.url_map)
    return render_template(
        'route_description_tmpl.html',
        value=my_path,
        my_type=type(my_path),
        my_id=id(my_path),
    )


@app.route("/person/<person_name>", methods=['GET', 'POST'])
def person_info(person_name):
    print(request.method)
    if request.method == 'GET':
        return get_person_info(person_name)
    elif request.method == 'POST':
        return post_person_info(person_name)


def get_person_info(person_name):
    # do samodzielnego zastanowienia się, czy to bezpieczne
    person = persons.get(person_name)
    return render_template(
        'person_tmpl.html',
        name=person.get('name'),
        surname=person.get('surname'),
        occupation=person.get('occupation'),
    )


def post_person_info(person_name):
    data = request.get_json()
    new_person = {
        'name':data.get('name'),
        'surname':data.get('surname'),
        'occupation':data.get('occupation')
    }
    global persons
    persons[data.get('name')] = new_person
    return 'OK'


@app.route("/my_cookies")
def cookies():
    cookie_secret = request.cookies.get('cookie_secret')
    resp = make_response(
        render_template(
            'cookies_tmpl.html', cookie_secret=cookie_secret
        )
    )
    resp.set_cookie('cookie_secret', 'I am cookie')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
