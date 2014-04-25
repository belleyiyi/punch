'''
Created on Apr 21, 2014

@author: baobao
'''
import wtforms
from werkzeug import OrderedMultiDict
from sqlalchemy.orm import aliased, contains_eager
from ..ext.sqlalchemy import ModelAdminModule, model_form
from ..core import db
from ..model import User
# 
# UserForm = 

# 
# class User_Form(UserForm):
#     """Embeds OneToOne has FormField."""
#     district = wtforms.FormField(model_form(District, db.session))


class UserModule(ModelAdminModule):
    name = 'UserModule'
    model = User
    db_session = db.session
#     district_alias = aliased(District)
# 
#     list_fields = OrderedMultiDict((
#         ('id', {'label': 'id', 'column': User.id}),
#         ('kid_name', {'label': 'kid name', 'column': User.kid_name}),
#         ('kid_birth_day', {'label': 'kid bitrhday', 'column': User.kid_birth_day}),
#         ('kid_gender', {'label': 'kid gender', 'column': User.kid_gender}), 
#         ('username', {'label': 'user name', 'column': User.username}), 
#         ('gender', {'label': 'gender', 'column': User.gender}),
#         ('qq', {'label': 'qq', 'column': User.qq}),    
#         ('email', {'label': 'email', 'column': User.email}),    
#         ('phone', {'label': 'phone', 'column': User.phone}),    
#         ('district.name', {'label': 'district', 'column': district_alias.name}),
#         ('address', {'label': 'address', 'column': User.address}), 
#     ))
# 
#     list_title = 'user list'
# 
#     searchable_fields = ['username', 'qq', 'phone','kid_name','email','district.name']
# 
#     order_by = ('id', 'desc')
# 
#     list_query_factory = model.query\
#            .outerjoin(district_alias, 'district')\
#            .options(contains_eager('district', alias=district_alias))\

    form_class = model_form(User, db.session, exclude=['password','event'])