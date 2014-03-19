'''
Created on Feb 20, 2014

@author: baobao
'''
from base import Service
from ..model import Parent,Child

class ChildService(Service):
    __model__= Child

class ParentService(Service):
    __model__ = Parent

    def __init__(self, *args, **kwargs):
        super(ParentService, self).__init__(*args, **kwargs)
        self.children = ChildService()

    def _preprocess_params(self, kwargs):
        kwargs = super(ParentService, self)._preprocess_params(kwargs)
        children = kwargs.get('children', [])
        if children and all(isinstance(c, int) for c in children):
            kwargs['children'] = self.categories.get_all(*children)
        return kwargs