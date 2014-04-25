# -*- coding: utf-8 -*-
'''
Created on Feb 20, 2014

@author: luqin
'''

from ..core import db

# event_user = db.Table(
#     'event_user', db.Model.metadata,
#     db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
# )

class Event(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    day_time = db.Column(db.String(256))
    theme = db.Column(db.String(256))
#     users = db.relationship("User", secondary=event_user,
#         backref=db.backref("event", lazy='dynamic'))
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    site = db.relationship('Site',
                           backref=db.backref('event', lazy='dynamic'))

    

