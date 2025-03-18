from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

# Register your models here.

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User
    list_display = ('email', 'username', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')

# Apply custom admin interface globally (not tied to individual users)
admin.site.site_header = 'Super Admin Panel'
admin.site.site_title = 'Super Admin Portal'
admin.site.index_title = 'Welcome to Super Admin Portal'
admin.site.site_url = 'https://www.mywebsite.com/admin' # Change this to your website URL
admin.site.enable_nav_sidebar = True # Hide the sidebar

admin.site.register(User, CustomUserAdmin)
