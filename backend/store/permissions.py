from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission so that only the user who created the object can delete or update the object
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request method is safe (GET, HEAD, OPTIONS)
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Ensure that only the user who created the object can delete or update it
            return obj.id == request.user.customer.id

        return False


class IsObjectOwner(BasePermission):
    """
    Custom permission so that only the user who created the object can delete or update the object
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request method is safe (GET, HEAD, OPTIONS)
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Ensure that only the user who created the object can delete or update it
            return obj.customer.id == request.user.customer.id

        return False
