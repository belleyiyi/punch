# -*- coding: utf-8 -*-
'''
Created on Feb 20, 2014

@author: luqin
'''

from ..core import db

class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    kid_name = db.Column(db.String(50))
    kid_birth_day = db.Column(db.Date())
    kid_gender = db.Column(db.Boolean())
    username = db.Column(db.String(255))
    gender = db.Column(db.Boolean())
    qq = db.Column(db.String(10))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(50))
    address = db.Column(db.String(256))
    password = db.Column(db.String(255))
    is_volunteer = db.Column(db.Boolean(),default=0)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District',
                           backref=db.backref('user', lazy='dynamic'))
    
