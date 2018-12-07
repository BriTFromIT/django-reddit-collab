from django.db import models


# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField()
    title = models.CharField(max_length=400)
    picture = models.CharField(max_length=400, null=True, blank=True)
    content = models.CharField(max_length=350)
    site_url = models.CharField(max_length=400, null=True, blank=True)
    vote_total = models.IntegerField()


class Comment(models.Model):
    created_at = models.DateTimeField()
    content = models.CharField(max_length=500)
    vote_total = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
