
from pyramid.events import subscriber
from pyramid.traversal import resource_path, find_root

from url_redirector.events import (
    ObjectMoved, ObjectReplaced,
    ObjectRemoved)


def get_storage(resource):
    root = find_root(resource)
    return root.get('urls_storage', None)


@subscriber(ObjectMoved)
def objectMoved(event):
    """Tell the redirection storage that an object moved
    """
    moved_object = event.obj

    if event.old_parent is not None and \
       event.new_parent is not None and event.old_name is not None:
        storage = get_storage(moved_object)
        if storage is not None:
            old_path = "%s/%s" % (resource_path(event.old_parent),
                                  event.old_name)
            new_path = resource_path(moved_object)
            storage.add(old_path, new_path)


@subscriber(ObjectReplaced)
def objectReplaced(event):
    """Tell the redirection storage that an object replaced
    """
    old_object = event.old_object
    new_object = event.new_object
    if old_object is not None and new_object is not None:
        storage = get_storage(new_object)
        if storage is not None:
            old_path = resource_path(old_object)
            new_path = resource_path(new_object)
            storage.add(old_path, new_path)


@subscriber(ObjectRemoved)
def objectRemoved(event):
    """Tell the redirection storage that the object was removed
    """
    storage = get_storage(event.parent)
    if storage is not None:
        path = resource_path(event.obj)
        storage.destroy(path)
