from django.contrib import admin
from app.models import Article, UserProfile

# Register your models here.
# allows us to create and edit models in the admin panel
admin.site.register(Article)

# need to tell django to use the UserProfile model we created and not the user model in Auth app 
# edit settings.py by defining AUTH_USER_MODEL as our UserProfile model 
admin.site.register(UserProfile)
