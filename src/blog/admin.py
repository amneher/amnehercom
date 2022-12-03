from django.contrib import admin

from .models import Post, User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created', 'updated')
	list_filter = ('author', 'created', 'updated')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'is_employee')
	list_filter = ('is_employee', 'username')