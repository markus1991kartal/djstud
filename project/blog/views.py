from django.shortcuts import render
from django.http import HttpResponse


from .models import Article
from .forms import CommentForm




def art_pub(request):
    articles = Article.objects.filter()
    if request.method =="POST":
        auth = request.POST.get('auth')
        text = request.POST.get('text')
        return HttpResponse("<h2>Hello, {0}</h2>".format(auth))
    else:
        commentform = CommentForm()
        return render(request, 'blog/detail.html', {
                                                'articles': articles,
                                                'empty_form': commentform,
                                                })


#def art_comm(request):
#    commentform = CommentForm()
#    return render(request, 'blog/detail.html', {'empty_form': commentform})


