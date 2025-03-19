from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
