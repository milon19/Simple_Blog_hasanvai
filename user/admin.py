from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User

admin.site.site_header = 'Simple Blog'
admin.site.unregister(Group)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'is_staff', 'is_active', 'profile_pic', 'cover_photo', 'title', 'bio')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password', 'profile_pic', 'cover_photo', 'title', 'bio')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active', 'profile_pic', 'cover_photo')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
