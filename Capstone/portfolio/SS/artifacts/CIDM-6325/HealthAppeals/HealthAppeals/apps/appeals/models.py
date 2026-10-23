from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=100, default="Default Template")
    text = models.TextField(
        default="Write a first-level insurance appeal letter."
    )

    def __str__(self):
        return self.name
