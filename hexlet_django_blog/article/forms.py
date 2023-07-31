from hexlet_django_blog.article.models import ArticleComment, Article
from django.forms import ModelForm

class CommentArticleForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']