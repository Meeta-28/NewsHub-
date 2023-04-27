from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    summary = models.TextField(max_length=200)
    img_url = models.URLField(blank=True)
    source_url = models.URLField(max_length=200)
    source_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    




