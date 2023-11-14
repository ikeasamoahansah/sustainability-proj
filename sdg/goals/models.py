import uuid
from django.db import models

from accounts.models import CustomUser
from challenges.models import Challenge

from .helper import BaseModel
from .choices import choices

# Create your models here.

class Goals(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, default=uuid.uuid4)
    title = models.CharField(blank=False, max_length=64)
    image = models.ImageField(blank=False, upload_to="images/")
    description = models.TextField(blank=False)
    goal = models.CharField(choices=choices, default="17", max_length=100)


    def __str__(self):
        return f"{self.author}: {self.challenge.title}"