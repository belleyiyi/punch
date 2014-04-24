'''
Created on Apr 24, 2014

@author: baobao
'''
from ..ext.sqlalchemy import ModelAdminModule, model_form
from ..core import db
from ..model import Site

class SiteModule(ModelAdminModule):

    name = 'SiteModule'
    model = Site
    db_session = db.session
    form_class = model_form(Site, db.session)