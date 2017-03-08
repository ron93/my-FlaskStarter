from flask import Flask, render_template,app
import config 

import admin,home

from app.home.controllers import mod
from app.admin.controllers import mod

app = Flask(__name__)
# configurations
app.config.from_object('config.DevelopmentConfig')





# register blueprints

# home page blueprint
app.register_blueprint(home.controllers.mod)

# admin blueprint
app.register_blueprint(admin.controllers.mod)

