from flask import Flask,Blueprint,render_template

mod =Blueprint('auth',__name__,url_prefix='/auth')

@mod.route('/signup')
def signup():
    return render_template('admin/signup.html')