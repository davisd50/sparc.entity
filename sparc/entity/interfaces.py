from zope.interface import Interface
from zope.interface import Attribute


class IIdentified(Interface):
    """Object that is identifiable"""
    def getId():
        """Return object identifier"""

class INamed(Interface):
    """Object that has a name"""
    name = Attribute("The name of the object")

class IDescribed(Interface):
    """Object that can be described"""
    description = Attribute("The object description")

class IEntity(IIdentified,
              INamed,
              IDescribed):
    """An identified, named, described object"""