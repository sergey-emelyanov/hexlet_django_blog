from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from hexlet_django_blog.article.models import Article


# Create your views here.

class IndexView(View):

    def get(self, request):
        articles = Article.objects.all()
        return render(request, template_name='articles/index.html', context={
            'articles': articles

        })

# def root(request):
#     return redirect(reverse('article', kwargs={
#         'tags': 'python',
#         'article_id': 42
#     }))
