from rest_framework import permissions


class IsAdAdvertiser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.advertiser.name == request.user.username