from zope.interface import Interface
from zope.interface import Attribute
from zope import schema

class IIdentified(Interface):
    """Object that is identifiable"""
    def getId():
        """Return object identifier"""

class INamed(Interface):
    """Object that has a name"""
    name = schema.TextLine(
            title = u'Name',
            description = u'An object name',
            )

class IDescribed(Interface):
    """Object that can be described"""
    description = schema.Text(
            title = u'Description',
            description = u'An object description',
            )

class IDetailed(Interface):
    """Object that can be detailed"""
    details = schema.Text(
            title = u'Details',
            description = u'An object details',
            )

class IEntity(IIdentified,
              INamed,
              IDescribed,
              IDetailed):
    """An identified, named, described, detailed object"""

class IUrlReference(Interface):
    """A reference URL"""
    url = schema.TextLine(
            title = u'URL',
            description = u'A URL related to object',
            )