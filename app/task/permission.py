from rest_framework import permissions


# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user
#
#
# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return bool(request.user and request.user.is_staff)
#
#
# # class IsOwnerOrReadOnly(permissions.BasePermission):
# #     def has_object_permission(self, request, view, obj):
# #         if request.method in permissions.SAFE_METHODS:
# #             return True
# #         return obj.user == request.user
#
# class IsOwner(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of profile to view or edit it.
#     """
#     def has_object_permission(self, request, view, obj):
#         return obj.pk == request.user.pk