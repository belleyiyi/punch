'''
Created on Feb 25, 2014

@author: baobao
'''

from flask_wtf import Form, TextField, DateField, Required, \
    Optional,validators,PasswordField,BooleanField,RadioField,SelectField,\
    FormField,FieldList

class ChildForm(Form):
    c_name = TextField('Name of Child')
    c_gender = SelectField('Gender', choices=[('0','female'),('1','male')])
    c_birth_day = TextField('Birth Day')

class RegistrationForm(Form):
    first_name = TextField('First Name', [validators.Required()])
    last_name = TextField('Last Name', [validators.Required()])
    email = TextField('Email Address')
    qq = TextField('QQ')
    phone = TextField('Phone Number',[validators.Length(min=11,max=11),validators.Required()])
    
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6)
    ])
    confirm = PasswordField('Repeat Password',
                            [validators.Required(),
                            validators.Length(min=6)])
    gender = SelectField('Gender', choices=[('0','female'),('1','male')])
    first_child = FormField(ChildForm,[validators.Required()])
    second_child = FormField(ChildForm)
    third_child = FormField(ChildForm)   
