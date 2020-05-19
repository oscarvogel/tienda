from django.contrib import admin

# Register your models here.
from apps.blog.models import BlogDetail, Blog


class BlogDetailInLine(admin.TabularInline):
    model = BlogDetail

class BlogAdmin(admin.ModelAdmin):
    list_per_page = 20
    date_hierarchy = 'created'
    inlines = [BlogDetailInLine]
    search_fields = ['title']

admin.site.register(Blog, BlogAdmin)