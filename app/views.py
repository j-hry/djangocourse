from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app.models import Article

# from app.forms import CreateArticleForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

# FBV for home
# def home(request):
#     # created models come with an object manager by default
#     # allow interactions with table, eg filtering and querying
#     articles = Article.objects.all()  # django ORM (obj r/s model)

#     # to render HTML template and insert articles inside it
#     # pass in request for template to use and template name: "app/home.html"
#     # and context {}dict, use the key "articles" to access all articles objects in list
#     return render(request, "app/home.html", {"articles": articles})


# mixin just adds some functionality/methods, (articlelistview is just a list view)
# loginmixin protects the class view, requires login to access the view
class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"  # provides context for home.html

    def get_queryset(self) -> QuerySet[Any]:
        # filter for articles created by user
        # minus created_at sorts by newest articles at top
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")


#### CLASS BASED VIEWS approach
# does not require forms.py
# django knows that this is to create a model, auto create a form
# view will render the form and handle receiving form data
class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/article_create.html"
    model = Article  # specify model
    # can give list or tuple of fields
    fields = ["title", "status", "content", "twitter_post"]  # form fields
    # specify where to go when article is successfully created
    # use reverse_lazy instd of redirect to calculate view to go to
    # destination calculated when article is created and sent to function
    # use reverse_lazy instd of reverse as home function may not be init as view when destination is calculated
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # set article model creator to be current user
        form.instance.creator = self.request.user
        return super().form_valid(form)


# updating article is similar to create except form should not be empty
# use userpassestest mixin to check that user is the one that created the article
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]  # form fields
    success_url = reverse_lazy("home")
    context_object_name = "article"

    # override test_func
    def test_func(self) -> bool | None:
        # returns true if user created article
        return self.request.user == self.get_object().creator


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "app/article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"

    def test_func(self) -> bool | None:
        # returns true if user created article
        return self.request.user == self.get_object().creator


#### FUNCTION BASED VIEWS approach
# user uses GET request to request form to be rendered
# user uses POST request to send data via form
# use the differing web request to differentiate btwn types of form views
# def create_article(request):
#     if request.method == "POST":

#         form = CreateArticleForm(request.POST)
#         if form.is_valid():
#             # use incoming request data to create article model
#             form_data = form.cleaned_data
#             # key of form_data has to match the names of the form fields
#             # i.e. "title"
#             new_article = Article(
#                 title = form_data["title"],
#                 status = form_data["status"],
#                 content = form_data["content"],
#                 word_count = form_data["word_count"],
#                 twitter_post = form_data["twitter_post"],
#             )
#             new_article.save()
#             # best practice to direct user to page to see new article or home page
#             # after form submission
#             return redirect("home")

#     else: # return form rendered as HTML for GET
#         form = CreateArticleForm()
#     # create new template to display form, pass in context {"form":form}
#     return render(request, "app/article_create.html", {"form":form} )
