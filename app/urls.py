from django.urls import path
# from app.views import home, create_article # for function based views
from app.views import home, ArticleCreateView

urlpatterns = [
    path("", home, name="home"),
    # include name to refer to url elsewhere in app
    path("articles/create/", ArticleCreateView.as_view(), name="create_article")
]
