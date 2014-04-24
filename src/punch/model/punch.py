'''
Created on Mar 19, 2014

@author: baobao
'''
from ..core import db

member_punch = db.Table(
                           'user_punch',
                           db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                           db.Column('punch_id', db.Integer(), db.ForeignKey('punch.id')))

class Punch(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
