from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("slug",)
    search_fields = ("title", "description", )
    

class LoctationAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "location")
    list_filter = ("author",)
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LoctationAdmin)
admin.site.register(Post, PostAdmin)
