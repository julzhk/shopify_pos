from django.db import models


class Inventory(models.Model):
    title = models.TextField(max_length=256, blank=True)
    body_html = models.TextField(blank=True)
    image = models.URLField(blank=True)

