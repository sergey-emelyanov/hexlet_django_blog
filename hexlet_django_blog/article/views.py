from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import CommentArticleForm, ArticleForm
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
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id)
        return render(request, 'articles/show.html', context={
            'article': article,
            'article_id': article_id
        })


class CommentArticleView(View):

    def get(self, request, *args, **kwags):
        form = CommentArticleForm()
        return render(request, 'articles/comment.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/create.html', context={
            'form': form
        })


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', context={
            'form': form,
            'article_id': article_id
        })

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/update.html', context={
            'form': form,
            'article_id': article_id
        })


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')
