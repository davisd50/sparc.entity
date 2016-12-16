from zope import interface
from persistent import Persistent
from zope.component.factory import Factory
from sparc.entity import IEntity
from sparc.entity.entity import SparcEntity

@interface.implementer(IEntity)
class PersistentSparcEntity(SparcEntity, Persistent):
    """A Sparc Entity that can be persisted in a ZODB"""
persistentSparcEntityFactory = Factory(PersistentSparcEntity)