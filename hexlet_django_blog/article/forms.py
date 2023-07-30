from hexlet_django_blog.article.models import ArticleComment
from django.forms import ModelForm

class CommentArticleForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']
