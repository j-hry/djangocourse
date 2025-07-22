# from django import forms
# from app.models import Article


# html form can be defined by hand OR

# class CreateArticleForm(forms.Form):
#     ARTICLE_STATUS = (
#         ("draft", "draft"),
#         ("inprogress", "in progress"),
#         ("published", "published"),
#     )
#     title = forms.CharField(max_length=100)
#     status = forms.ChoiceField(choices=ARTICLE_STATUS)
#     content = forms.CharField(widget=forms.Textarea)
#     word_count = forms.IntegerField()
#     twitter_post = forms.CharField(widget=forms.Textarea, required=False)


# OR use ModelForm to take care of data parsing and auto create a model 
# when form is validated
# class CreateArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         # define which fields from model that html widgets should be created
#         fields = ("title", "status", "content", "word_count", "twitter_post")
    
    
