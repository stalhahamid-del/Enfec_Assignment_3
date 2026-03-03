from django.db import models
from django.contrib.postgres.fields import JSONField  # or models.JSONField in Django 3.1+

class Agent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capabilities = models.JSONField()  # e.g., ["math", "summarization"]
    endpoint_url = models.URLField()
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.name