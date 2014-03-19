'''
Created on Mar 19, 2014

@author: baobao
'''
from base import Service
from ..model import Event
from parents import ParentService

class EventService(Service):
    __model__= Event
    
    def __init__(self, *args, **kwargs):
        super(ParentService, self).__init__(*args, **kwargs)
        self.volunteer = ParentService()

    def _preprocess_params(self, kwargs):
        kwargs = super(ParentService, self)._preprocess_params(kwargs)
        volunteer = kwargs.get('volunteer', [])
        if volunteer and all(isinstance(c, int) for c in volunteer):
            kwargs['volunteer'] = self.categories.get_all(*volunteer)
        return kwargs