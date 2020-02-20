from django.db import models
from django.utils import timezone



class Article(models.Model):
    title_text = models.CharField(max_length=100)
    body_text = models.TextField()
    by_auth = models.CharField(max_length=100)
    pub_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title_text

#class Comment(models.Model):
#    comment = models.ForeignKey(Article, on_delete=models.Cascade, related_name='comments')
#    comment_text = models.TextField()
