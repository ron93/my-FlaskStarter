from flask import Flask,Blueprint,render_template

module =Blueprint('auth',__name__,url_prefix='/auth')

@module.route('/signup')
def signup():
    return render_template('auth/signup.html')