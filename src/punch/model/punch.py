'''
Created on Mar 19, 2014

@author: baobao
'''
from ..core import db
# from district import District

member_punch = db.Table(
                           'member_punch',
                           db.Column('parent_id', db.Integer(), db.ForeignKey('parent.id')),
                           db.Column('punch_id', db.Integer(), db.ForeignKey('punch.id')))

class Punch(db.Model):
    __tablename__ = 'punch'
    
    id = db.Column(db.Integer(), primary_key=True)