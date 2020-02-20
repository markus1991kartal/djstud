from django.urls import path


from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.art_pub, name='art_pub'),
#    path('', views.art_comm, name='art_comm'),
]
