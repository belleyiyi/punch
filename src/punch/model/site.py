# -*- coding: utf-8 -*-
'''
Created on Feb 20, 2014

@author: luqin
'''

from ..core import db

class Site(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(256))
    address = db.Column(db.String(256))
    contract_phone = db.Column(db.String(11))
    contract_manager = db.Column(db.String(100))
    comment = db.Column(db.String(256))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District',
                           backref=db.backref('site', lazy='dynamic'))
    

    

    

