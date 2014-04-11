
from flask import render_template
# from flask_wtf.csrf import CsrfProtect
from .. import factory



# csrf = CsrfProtect()

def create_app(settings_override=None):
    """Returns the Overholt dashboard application instance"""
    app = factory.create_app(__name__, __path__, settings_override)
#     csrf.init_app(app)
    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

    return app


def handle_error(e):
    return render_template('errors/%s.html' % e.code), e.code