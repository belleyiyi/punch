'''
Created on Apr 24, 2014

@author: baobao
'''
import wtforms
from werkzeug import OrderedMultiDict
from sqlalchemy.orm import aliased, contains_eager
from ..ext.sqlalchemy import ModelAdminModule, model_form
from ..core import db
from ..model import Event,User,Site

class EventModule(ModelAdminModule):

    name = 'EventModule'
    model = Event
    db_session = db.session
    form_class = model_form(Event, db.session)
    
    users_aliased = aliased(User)
    sites_aliased = aliased(Site)
 
    list_fields = OrderedMultiDict((
        ('id', {'label': 'id', 'column': Event.id}),
        ('theme', {'label': 'theme', 'column': Event.theme}),
        ('time', {'label': 'time', 'column': Event.day_time}),
        ('username', {'label': 'name', 'column': users_aliased.username}),
        ('site_name', {'label': 'site_name', 'column': sites_aliased.name}), 
    ))
 
    list_title = 'event list'
 
    searchable_fields = ['theme', 'username']
 
    order_by = ('id', 'desc')
 
#     list_query_factory = model.query\
#            .outerjoin(users_aliased, 'users')\
#            .options(contains_eager('users', alias=users_aliased))\
