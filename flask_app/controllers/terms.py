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
        return render_template('index.html')
    else:
        return redirect('/register_or_login')

@app.route('/save_translation', methods=['post'])
def save_translation():
    term = {
        'users_id': session['user_id'],
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
