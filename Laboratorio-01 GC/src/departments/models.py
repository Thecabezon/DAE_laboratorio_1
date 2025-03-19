from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    supervisor = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
