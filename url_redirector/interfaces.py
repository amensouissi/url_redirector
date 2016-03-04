
from zope.interface import Interface


class IRedirectionStorage(Interface):
    """A storage for items where the old and the new location are known.

    Will be registered as a local utility.
    """

    def add(old_path, new_path):
        """Remember that the object at old_path is now at new_path.

        Any redirects that already pointed at old_path will now point to
        new_path as well.
        """

    def remove(old_path):
        """Forget all redirects from old_path to any new path
        """

    def destroy(new_path):
        """Forget all redirects to new_path.

        Normally called if the object at new_path is removed
        """

    def has_path(old_path):
        """Determine if there are any redirects from old_path in effect.
        """

    def get(old_path, default=None):
        """Get the new path to the object that used to be at old_path.

        Will return the default value (None, unless set otherwise) if old_path
        is not found.
        """

    def redirects(new_path):
        """Get a list of paths that redirect to new_path.

        Will return an empty list if nothing redirects to new_path.
        """

    def __iter__():
        """Iterate over all existing paths."""
