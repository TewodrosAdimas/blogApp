from django.contrib import admin
from .models import UserProfile
from .models import Post 
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'bio')

# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')  # Customize the fields to display in the list
    search_fields = ('title', 'content')  # Add search functionality

admin.site.register(Post, PostAdmin)

