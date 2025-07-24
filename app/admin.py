from django.contrib import admin
from app.models import Article, UserProfile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "word_count", "status", "created_at", "updated_at")
    list_filter = ("status",) # have to be a tuple
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("created_at",) # have to be a tuple
    readonly_fields = ("word_count", "created_at", "updated_at")
        
# Register your models here.
# allows us to create and edit models in the admin panel
admin.site.register(Article, ArticleAdmin)

# need to tell django to use the UserProfile model we created and not the user model in Auth app 
# edit settings.py by defining AUTH_USER_MODEL as our UserProfile model 
admin.site.register(UserProfile)
