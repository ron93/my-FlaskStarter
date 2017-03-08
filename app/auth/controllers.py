from flask import Flask,Blueprint,render_template

module =Blueprint('auth',__name__,url_prefix='/auth',static_folder='static' ,template_folder='templates')

@module.route('/')
def auth():
    return render_template('auth/auth.html')

@module.route('/signup')
def signup():
    return render_template('auth/signup.html')