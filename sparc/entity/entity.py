from zope.interface import implements
from interfaces import IEntity

class SparcEntity(object):
    """A basic Sparc entity"""
    implements(IEntity)
    
    def __init__(self, **kwargs):
        self._id = kwargs['id']
        self.name = kwargs['name']
        self.description = kwargs['description']
    
    def getId(self):
        return self._id
    