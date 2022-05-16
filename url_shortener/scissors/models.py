from django.db import models


class Url(models.Model):
    original = models.URLField(verbose_name='original path')
    path = models.CharField(
        max_length=50, verbose_name='shortenerd path', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)
