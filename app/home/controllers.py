from flask import Blueprint,render_template,abort 
from jinja2 import TemplateNotFound


home_mod = Blueprint('home', __name__, url_prefix='/home'
               ,template_folder='templates')


@home_mod.route('/')
def home():
    
    return render_template('home/home.html')
   
