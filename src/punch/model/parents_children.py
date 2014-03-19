# -*- coding: utf-8 -*-
'''
Created on Feb 20, 2014

@author: luqin
'''

from ..core import db
from ..helpers import JsonSerializer


Parents_Chidren = db.Table(
                           'parents_children',
                           db.Column('parent_id', db.Integer(), db.ForeignKey('parent.id')),
                           db.Column('child_id', db.Integer(), db.ForeignKey('child.id')))

class Parent(db.Model):
    __tablename__ = 'parent'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    qq = db.Column(db.String(10))
    phone_number = db.Column(db.String(11))
    email = db.Column(db.String(50))
    gender = db.Column(db.Boolean())
    address = db.Column(db.String(256))
    child = db.relationship('Child',
                            secondary=Parents_Chidren,
                            backref=db.backref('parent', lazy='joined'))
    
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District',
                           backref=db.backref('parent', lazy='dynamic'))
    
    
class Child(db.Model):
    __tablename__='child'
    
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    birth_day = db.Column(db.String(10))
    gender = db.Column(db.Boolean())
