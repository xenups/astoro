from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class FeedBackPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'get':
            print('list umaaaaaaaaaaaaaade')
            return True
        if request.method == 'list':
            print('list umaaaaaaaaaaaaaade')
            return True
        elif request.method == 'create':
            print('create umaaaaaaaaaaaaaade')
            return True


class IsAuthenticatedNotPost(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        if request.method == 'GET' and request.user and request.user.is_staff:
            return True
        return super(IsAuthenticatedNotPost, self).has_permission(request, view)
