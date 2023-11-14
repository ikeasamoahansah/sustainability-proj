import uuid

from django.db import models

from accounts.models import CustomUser

# Create your models here.

class Challenge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=False)

    def __str__(self) -> str:
        return f"{self.company.username} - {self.title}"