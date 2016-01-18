from interfaces import IDescribed
from interfaces import IEntity
from interfaces import IIdentified
from interfaces import INamed
from interfaces import ITaggable

from entity import SparcEntity

# Configuration (this package only)
from importlib import import_module
from sparc.configuration.zcml import Configure as SparcConfigure
def Configure():
    SparcConfigure([import_module('zope.annotation')])