from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations
from zope.annotation.interfaces import IAnnotatable
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.component import adapts
from zope.component.factory import Factory
from zope.interface import implements
from zope import schema
from zope.schema import getFields
from zope.schema.fieldproperty import FieldProperty
from interfaces import IIdentified
from interfaces import IEntity
from interfaces import IOwner
from interfaces import IUrlReference
from interfaces import IKeyphraseTags

class SparcEntity(object):
    """A basic Sparc entity"""
    implements(IEntity, IAttributeAnnotatable)
    
    def __init__(self, **kwargs):
        self.id = kwargs['id'] # required
        if 'name' in kwargs: self.name = kwargs['name']
        if 'description' in kwargs: self.description = kwargs['description']
        if 'details' in kwargs: self.details = kwargs['details']

    #IEntity
    id = FieldProperty(IIdentified['id'])
    def getId(self):
        return self.id
    
    name = FieldProperty(IEntity['name'])
    description = FieldProperty(IEntity['description'])
    details = FieldProperty(IEntity['details'])
sparcEntityFactory = Factory(SparcEntity)

class SparcEntityOwnerForAnnotableObjects(object):
    implements(IOwner)
    adapts(IAnnotatable)
    
    def __init__(self, context):
        self.context = context
        self.annotations = IAnnotations(context).\
                                setdefault('IOwner', OOBTree())
        if 'owner' not in self.annotations:
            self.annotations['owner'] = None
    
    @property
    def owner(self):
        return self.annotations['owner']
    @owner.setter
    def owner(self, value):
        getFields(IOwner)['owner'].validate(value)
        self.annotations['owner'] = value


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
        self.annotations['url'] = value


class SparcEntityKeyphraseTagsForAnnotableObjects(object):
    implements(IKeyphraseTags)
    adapts(IAnnotatable)
    
    def __init__(self, context):
        self.context = context
        self.annotations = IAnnotations(context).\
                                setdefault('IKeyphraseTags', OOBTree())
        if 'tags' not in self.annotations:
            self.annotations['tags'] = set()
    
    @property
    def tags(self):
        return self.annotations['tags']
    @tags.setter
    def tags(self, value):
        getFields(IKeyphraseTags)['tags'].validate(value)
        self.annotations['tags'] = value