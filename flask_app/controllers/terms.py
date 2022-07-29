from flask_app import app
# from flask import jsonify
import os
import requests
from flask import render_template, redirect, request, session
from flask_app.models.term import Term

# Homepage
@app.route('/')
def index():
    if 'user_id' in session:
        data = { 'id': session['user_id'] }
        terms = Term.get_all(data)
        return render_template('index.html', terms=terms)
    else:
        return redirect('/register_or_login')

@app.route('/save_translation', methods=['post'])
def save_translation():
    term = {
        'user_id': session['user_id'],
        'en': request.form['english'],
        'fr': request.form['french'],
        'notes': request.form['notes']
    }
    if Term.validate_inputs(term):
        Term.save(term)
    else:
        print("oh shit")
        return redirect('/')
    print(request.form)
    return redirect('/')

@app.route('/view_term/<id>')
def view_term(id):
    data = { 'id': id }
    term = Term.get_term_by_id(data)
    if term:
        print(term)
        return render_template('view_term.html', term=term)
    else:
        redirect('/')

@app.route('/update_term', methods=['post'])
def update_term():
    data = {
        'id': request.form['id'],
        'notes': request.form['notes']
    }
    Term.update_term(data)
    return redirect(f'/view_term/{request.form["id"]}')

@app.route('/browse_terms')
def browse_terms():
    if 'user_id' in session:
        data = { 'id': session['user_id'] }
        list_of_term_dicts = Term.get_fr_terms_to_browse(data)
        return render_template('browse_terms.html', list_of_term_dicts=list_of_term_dicts)
    else:
        return redirect('/register_or_login')



# @app.route('/get_translation', methods=['post'])
# def get_translation():
#     print("I'm in the python function")
#     params = {
#         "q": "My cats are liquid",
#         "source": "en",
#         "target": "fr",
#         "format": "text",
#         "api_key": os.environ.get("LIBRETRANSLATE_KEY")
#     }

#     r = requests.post("https://libretranslate.com/translate", data=params)
#     if not r.ok:
#         raise Exception(r.text)
#     if r.json().get("error"):
#         return None
#     return r.json()["translatedText"]
