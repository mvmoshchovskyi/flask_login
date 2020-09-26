from flask import redirect, url_for, render_template
from flask_login import login_user, logout_user
from .models import UserModel

from app import app

@app.route('/')
def home():
    return redirect('admin',)


@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/login_user')
def login_u():
    user =UserModel.query.get(1)
    login_user(user)
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
