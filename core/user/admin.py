from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.user.models import User, PasswordHistoryUser


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'cargo',
        'cedula',
        'is_active', 
        'is_staff',
        'date_joined'
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    search_fields = (
        'username', 
        'first_name', 
        'last_name', 
        'email', 
        'cedula', 
        'cargo',
        'cellphone'
    )
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ('date_joined', 'last_login', 'slug')
    
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': (
                'first_name', 
                'last_name', 
                'email',
                'email_person',
                'cedula',
                'cargo',
                'cellphone',
                'address_user',
                'date_birth',
                'photo',
            )
        }),
        ('Permisos', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        ('Información del Sistema', {
            'fields': (
                'slug',
                'last_login',
                'date_joined',
            ),
            'classes': ('collapse',)
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 
                'password1', 
                'password2',
                'first_name',
                'last_name',
                'email',
                'cargo',
                'is_staff',
                'is_active'
            ),
        }),
    )
    
    list_per_page = 25


@admin.register(PasswordHistoryUser)
class PasswordHistoryUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'pass_date')
    list_filter = ('pass_date',)
    search_fields = ('username__username', 'username__email')
    readonly_fields = ('username', 'old_pass', 'pass_date')
    ordering = ('-pass_date',)
    list_per_page = 50
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
