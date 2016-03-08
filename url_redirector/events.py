# Copyright (c) 2015 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

from zope.interface import implementer
from zope.interface.interfaces import IObjectEvent
from zope.interface import Attribute


class IObjectMoved(IObjectEvent):
    """ An event type sent when an object is moved """
    obj = Attribute('The object being meved')


@implementer(IObjectMoved)
class ObjectMoved(object): # pragma: no cover
    """ An event sent when an object has been moved."""
    def __init__(self, obj, old_parent, new_parent, old_name):
        self.obj = obj
        self.old_parent = old_parent
        self.new_parent = new_parent
        self.old_name = old_name


class IObjectReplaced(IObjectEvent):
    """ An event type sent when an object is replaced """
    old_object = Attribute('The object being replaced')

    new_object = Attribute('The object being of replacement')


@implementer(IObjectReplaced)
class ObjectReplaced(object): # pragma: no cover
    """ An event sent when an object has been replaced."""
    def __init__(self, old_object, new_object):
        self.old_object = old_object
        self.new_object = new_object


class IObjectRemoved(IObjectEvent):
    """ An event type sent when an object is removed """
    obj = Attribute('The object being meved')

    parent = Attribute('The parent')


@implementer(IObjectRemoved)
class ObjectRemoved(object): # pragma: no cover
    """ An event sent when an object has been removed."""
    def __init__(self, obj, parent):
        self.object = obj
        self.parent = parent
