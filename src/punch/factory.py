# -*- coding: utf-8 -*-
"""
    overholt.factory
    ~~~~~~~~~~~~~~~~

    overholt factory module
"""

import os
from flask import Flask, session
# from .middleware import HTTPMethodOverrideMiddleware
# from .helpers import register_blueprints
from .core import db
from helpers import register_form
from admin import Admin
# from form import UserModule


# def generate_csrf_token():
#     if '_csrf_token' not in session:
#         session['_csrf_token'] = some_random_string()
#     return session['_csrf_token']




def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the Overholt platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('punch.config')
    app.config.from_object(settings_override)
#     app.jinja_env.globals['csrf_token'] = generate_csrf_token  

#     db.init_app(app)
#     
#     db.create_all()
    db.init_app(app)
    
    
    
    with app.app_context():
        register_form(app,package_name,package_path)
#         admin = Admin(app, title="my business")
# 
#         user_module = admin.register_module(UserModule, '/users', 'users',
#                     'users')
        db.create_all()

    

    return app

# 
# def create_celery_app(app=None):
#     app = app or create_app('overholt', os.path.dirname(__file__))
#     celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])
#     celery.conf.update(app.config)
#     TaskBase = celery.Task
# 
#     class ContextTask(TaskBase):
#         abstract = True
# 
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)
# 
#     celery.Task = ContextTask
#     return celery
