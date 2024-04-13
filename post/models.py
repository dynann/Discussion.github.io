from django.db import models
from django.conf import settings
from django.urls import reverse 


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE #delete author affect things belong to author 
    )
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    