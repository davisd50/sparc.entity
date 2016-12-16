from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations
from zope.annotation.interfaces import IAnnotatable
from zope.annotation.interfaces import IAttributeAnnotatable
from zope import component
from zope.component.factory import Factory
from zope import interface
from zope.schema import getFields
from zope.schema.fieldproperty import FieldProperty
from .interfaces import IIdentified
from .interfaces import IEntity
from .interfaces import IOwner
from .interfaces import IUrlReference
from .interfaces import IKeyphraseTags

class BaseSchemaObject(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

@interface.implementer(IEntity, IAttributeAnnotatable)
class SparcEntity(object):
    """A basic Sparc entity"""
    
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

@interface.implementer(IOwner)
@component.adapter(IAnnotatable)
class SparcEntityOwnerForAnnotableObjects(object):
    
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


@interface.implementer(IUrlReference)
@component.adapter(IAnnotatable)
class SparcEntityUrlForAnnotableObjects(object):
    
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


@interface.implementer(IKeyphraseTags)
@component.adapter(IAnnotatable)
class SparcEntityKeyphraseTagsForAnnotableObjects(object):
    
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