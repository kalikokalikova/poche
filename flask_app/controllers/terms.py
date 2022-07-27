from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.term import Term

# Homepage
@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        return redirect('/register_or_login')
