from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='files')
    content = models.TextField()
    id_html = models.CharField(max_length=20, default='')
    date_created = models.DateTimeField(auto_now_add=True)
