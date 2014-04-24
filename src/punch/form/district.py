'''
Created on Apr 24, 2014

@author: baobao
'''
'''
Created on Apr 21, 2014

@author: baobao
'''
import wtforms
from ..ext.sqlalchemy import ModelAdminModule, model_form
from ..core import db
from ..model import District


class DistrictModule(ModelAdminModule):
    name = 'DistrictModule'
    model = District
    db_session = db.session
    form_class = model_form(District, db.session, only=['name'])