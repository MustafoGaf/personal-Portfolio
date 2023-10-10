from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from django.contrib.auth.models import User



class Blog(models.Model):
    title=  models.CharField(max_length=200)
    text = models.TextField()
    date= models.DateTimeField()
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name="blog_post")
    tags = TaggableManager()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", args=[self.id])
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ] 
        
    def __str__(self):
        return f'Comment by {self.name} on {self.blog}'