'''
Created on Feb 25, 2014

@author: baobao
'''

from flask_wtf import Form
from wtforms import TextField, DateField, \
                    validators,PasswordField,BooleanField,RadioField,SelectField,\
                    FormField,FieldList
from wtforms.validators import Required,optional

class ChildForm(Form):
    c_name = TextField('Name of Child')
    c_gender = SelectField('Gender', choices=[('0','female'),('1','male')])
    c_birth_day = TextField('Birth Day')

class RegistrationForm(Form):
    name = TextField('Name', [validators.Required('name is required')])
    email = TextField('Email Address')
    qq = TextField('QQ')
    phone = TextField('Phone Number',[validators.Length(min=11,max=11),validators.Required('phone is required')])
#     district = SelectField('district')

    gender = SelectField('Gender', choices=[('0','female'),('1','male')])
    first_child = FormField(ChildForm)
    second_child = FormField(ChildForm)
    third_child = FormField(ChildForm)
