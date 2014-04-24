import os
import flask_wtf
# from flask import Flask, session
# from .middleware import HTTPMethodOverrideMiddleware
# from core import db
# from admin import Admin
# from helpers import register_form
import factory



# def generate_csrf_token():
#     if '_csrf_token' not in session:
#         session['_csrf_token'] = some_random_string()
#     return session['_csrf_token']


def create_app(settings_override=None):
    """Returns the Overholt dashboard application instance"""
    app = factory.create_app(__name__, __path__, settings_override)

    flask_wtf.CsrfProtect(app)
    # Register custom error handlers
#     if not app.debug:
#         for e in [500, 404]:
#             app.errorhandler(e)(handle_error)

    return app
# 
# def create_app(package_name, package_path, settings_override=None,
#                register_security_blueprint=True):
#     """Returns a :class:`Flask` application instance configured with common
#     functionality for the Overholt platform.
# 
#     :param package_name: application package name
#     :param package_path: application package path
#     :param settings_override: a dictionary of settings to override
#     :param register_security_blueprint: flag to specify if the Flask-Security
#                                         Blueprint should be registered. Defaults
#                                         to `True`.
#     """
#     app = Flask(package_name, instance_relative_config=True)
# 
#     app.config.from_object('punch.config')
#     app.config.from_object(settings_override)
# #     app.jinja_env.globals['csrf_token'] = generate_csrf_token  
# 
# #     db.init_app(app)
# #     
# #     db.create_all()
#     db.init_app(app)
#     
#     with app.app_context():
#         db.create_all()
# 
#     register_form(app,package_name,package_path)
# 
#     return app