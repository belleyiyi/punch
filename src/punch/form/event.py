'''
Created on Apr 24, 2014

@author: baobao
'''
from ..ext.sqlalchemy import ModelAdminModule, model_form
from ..core import db
from ..model import Event

class EventModule(ModelAdminModule):

    name = 'EventModule'
    model = Event
    db_session = db.session
    form_class = model_form(Event, db.session)