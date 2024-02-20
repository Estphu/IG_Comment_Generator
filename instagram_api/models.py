from django.db import models

class InstagramPost(models.Model):
    ''' Custom Model Class for Instagram Post URL '''
    url = models.URLField(unique=True)
 
class Comment(models.Model):
    ''' Custom Model Class for comments takes "post" as a FK and "text" as a comment '''
    post = models.ForeignKey(InstagramPost, on_delete=models.CASCADE)
    text = models.TextField()