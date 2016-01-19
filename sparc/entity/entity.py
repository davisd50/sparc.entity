from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations
from zope.annotation.interfaces import IAnnotatable
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.component import adapts
from zope.interface import implements
from zope.schema import getFields
from zope.schema.fieldproperty import FieldProperty
from interfaces import IEntity
from interfaces import IUrlReference

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

class SparcEntityUrlForAnnotableObjects(object):
    implements(IUrlReference)
    adapts(IAnnotatable)
    
    def __init__(self, context):
        self.context = context
        self.annotations = IAnnotations(context).\
                                setdefault('IUrlReference', OOBTree())
        if 'url' not in self.annotations:
            self.annotations['url'] = None
    
    @property
    def url(self):
        return self.annotations['url']
    @url.setter
    def url(self, value):
        getFields(IUrlReference)['url'].validate(value)
        #IUrlReference.url.validate(value)
        self.annotations['url'] = value