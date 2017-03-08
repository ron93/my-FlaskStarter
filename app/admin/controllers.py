from flask import Flask,Blueprint,render_template

module =Blueprint('admin',__name__,url_prefix='/admin',template_folder='templates')

@module.route('/')
def admin():
    return render_template('admin/admin.html')