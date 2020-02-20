from django.shortcuts import render
from .models import Article




def art_pub(request):
    articles = Article.objects.filter()
    return render(request, 'blog/detail.html', {'articles': articles})

