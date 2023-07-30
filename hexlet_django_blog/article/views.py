from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CommentArticleForm
from hexlet_django_blog.article.models import Article


# Create your views here.

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, template_name='articles/index.html', context={
            'articles': articles

        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article
        })


class CommentArticleView(View):

    def get(self, request, *args, **kwags):
        form = CommentArticleForm()
        return render(request,'articles/comment.html', context={
            'form':form
        })