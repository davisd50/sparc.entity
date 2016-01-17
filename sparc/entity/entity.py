from zope.interface import implements
from interfaces import IEntity

class SparcEntity(object):
    """A basic Sparc entity"""
    implements(IEntity)
    
    def __init__(self, id, name, description):
        self._id = id
        self.name = name
        self.description = description
    
    def getId(self):
        return self._id
    