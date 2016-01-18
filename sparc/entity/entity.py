from zope.annotation.interfaces import IAttributeAnnotatable
from zope.interface import implements
from interfaces import IEntity

class SparcEntity(object):
    """A basic Sparc entity"""
    implements(IEntity, IAttributeAnnotatable)
    
    def __init__(self, **kwargs):
        self._id = kwargs['id'] # required
        self.name = kwargs['name'] if 'name' in kwargs else None
        self.description = kwargs['description'] \
                            if 'description' in kwargs else None
    
    def getId(self):
        return self._id
    