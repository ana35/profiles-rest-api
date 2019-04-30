#checks if the user has access to perform the operation that it is asing for.
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit their own profile."""

    def has_object_permission(self, request, view, object):
        """Check user is trying to update their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.id == request.user.id
