from zope.annotation.interfaces import IAttributeAnnotatable
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from interfaces import IEntity

class SparcEntity(object):
    """A basic Sparc entity"""
    implements(IEntity, IAttributeAnnotatable)
    
    def __init__(self, **kwargs):
        self._id = kwargs['id'] # required
        if 'name' in kwargs: self.name = kwargs['name']
        if 'description' in kwargs: self.description = kwargs['description']
        if 'details' in kwargs: self.details = kwargs['details']
    
    def getId(self):
        return self._id
    
    name = FieldProperty(IEntity['name'])
    description = FieldProperty(IEntity['description'])
    details = FieldProperty(IEntity['details'])
