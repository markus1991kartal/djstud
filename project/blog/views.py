from django.shortcuts import render


from .models import Article
from .forms import CommentForm




def art_pub(request):
    articles = Article.objects.filter()
    commentform = CommentForm()
    return render(request, 'blog/detail.html', {
                                                'articles': articles,
                                                'empty_form': commentform,
                                                })


#def art_comm(request):
#    commentform = CommentForm()
#    return render(request, 'blog/detail.html', {'empty_form': commentform})


