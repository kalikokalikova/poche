from flask_app import app
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
    return redirect('/')

@app.route('/view_term/<id>')
def view_term(id):
    data = { 'id': id }
    term = Term.get_term_by_id(data)
    if term:
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

@app.route('/search_terms', methods=['post'])
def search_terms():
    data = {
        'user_id': session['user_id'],
        # have to put these bonus %% to make the % show up inside the string quotes in the mysql query
        'search_terms': "%%" + request.form['search_terms'] + "%%"
    }
    results = Term.search_terms(data)
    if results:
        session['search_terms'] = request.form['search_terms']
        session['search_results'] = results
        return redirect('/results')
    else:
        # TODO some error messaging
        return redirect('/browse_terms')

@app.route('/results')
def results():
    if 'user_id' in session:
        return render_template('results.html')
    else:
        return redirect('/register_or_login')

@app.route('/delete/<id>')
def delete_term(id):
    data = {
        'id': id
    }
    response = Term.delete_term(data)
    #TODO messaging if something goes wrong
    return redirect('/')