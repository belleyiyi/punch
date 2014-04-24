# -*- coding: utf-8 -*-
'''
Created on Feb 20, 2014

@author: luqin
'''

from ..core import db

class Event(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    day_time = db.Column(db.String(256))
    theme = db.Column(db.String(256))
    
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    site = db.relationship('Site',
                           backref=db.backref('event', lazy='dynamic'))
    
    volunteer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    volunteer = db.relationship('User',
                           backref=db.backref('event', lazy='dynamic'))
#     

    

