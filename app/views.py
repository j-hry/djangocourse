from django.shortcuts import render, redirect
from app.models import Article
from app.forms import CreateArticleForm


# Create your views here.
def home(request):
    # created models come with an object manager by default
    # allow interactions with table, eg filtering and querying
    articles = Article.objects.all()  # django ORM (obj r/s model)

    # to render HTML template and insert articles inside it
    # pass in request for template to use and template name: "app/home.html"
    # and context {}dict, use the key "articles" to access all articles objects in list
    return render(request, "app/home.html", {"articles": articles})

# user uses GET request to request form to be rendered
# user uses POST request to send data via form
# use the differing web request to differentiate btwn types of form views
def create_article(request):
    if request.method == "POST":
       
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            # use incoming request data to create article model
            form_data = form.cleaned_data
            # key of form_data has to match the names of the form fields
            # i.e. "title"
            new_article = Article(
                title = form_data["title"],
                status = form_data["status"],
                content = form_data["content"],
                word_count = form_data["word_count"],
                twitter_post = form_data["twitter_post"],
            )
            new_article.save()
            # best practice to direct user to page to see new article or home page
            # after form submission
            return redirect("home")
        
    else: # return form rendered as HTML for GET
        form = CreateArticleForm()
    # create new template to display form, pass in context {"form":form}
    return render(request, "app/article_create.html", {"form":form} )

