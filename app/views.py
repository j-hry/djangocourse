from django.shortcuts import render
from app.models import Article


# Create your views here.
def home(request):
    # created models come with an object manager by default
    # allow interactions with table, eg filtering and querying
    articles = Article.objects.all() # django ORM (obj r/s model)
    
    # to render HTML template and insert articles inside it
    # pass in request for template to use and template name: "app/home.html"
    # and context {}dict, use the key "articles" to access all articles objects in list
    return render(request, "app/home.html", {"articles": articles} )
    
