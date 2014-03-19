# -*- coding: utf-8 -*-
'''
Created on Feb 20, 2014

@author: luqin
'''

from ..core import db
from ..helpers import JsonSerializer

class District(db.Model):
    __tablename__ = 'district'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(256))

    

