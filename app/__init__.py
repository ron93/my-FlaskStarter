from flask import Flask, render_template,app
import config 

import admin,home,auth

from app.home.controllers import module
from app.admin.controllers import module
from app.auth.controllers import module

app = Flask(__name__)
# configurations
app.config.from_object('config.DevelopmentConfig')





# register blueprints

# home page blueprint
app.register_blueprint(home.controllers.module)

# admin blueprint
app.register_blueprint(admin.controllers.module)

#auth blueprint
app.register_blueprint(auth.controllers.module)

