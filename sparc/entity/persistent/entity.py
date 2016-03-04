from zope.interface import implements
from persistent import Persistent
from zope.component.factory import Factory
from sparc.entity import IEntity
from sparc.entity.entity import SparcEntity

class PersistentSparcEntity(SparcEntity, Persistent):
    """A Sparc Entity that can be persisted in a ZODB"""
    implements(IEntity)
persistentSparcEntityFactory = Factory(PersistentSparcEntity)