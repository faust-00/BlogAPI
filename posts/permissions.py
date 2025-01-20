from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Faqat ko'rish uchun ruxsat
        if request.method in permissions.SAFE_METHODS:
            return True

        # o'zgartirish uchun ruxsatnoma faqatgina post muallifiga beriladi
        return obj.author == request.user
