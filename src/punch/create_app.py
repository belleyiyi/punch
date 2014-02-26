'''
Created on Feb 20, 2014

@author: luqin
'''
from flask import Flask
from core import db
from frontend import registration

def create_app():
    app = Flask(__name__)
    app.config.from_object('punch.setting')

#     from yourapplication.model import db
    db.init_app(app)
# 
#     from yourapplication.views.admin import admin
#     from yourapplication.views.frontend import frontend
#     app.register_blueprint(admin)
    app.register_blueprint(registration)

    return app