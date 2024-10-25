from django.contrib import admin
from blog.models import BlogTable

class blogTableAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status', 'image']
    list_filter = ['title', 'author', 'publish']
    prepopulated_fields = {'slug' : ('title',)}
    search_fields = ('status', 'created', 'publish', 'author')



admin.site.register(BlogTable, blogTableAdmin)

