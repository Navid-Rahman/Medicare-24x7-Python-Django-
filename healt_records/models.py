from django.db import models

# Create your models here.
from accounts.models import *


class AdviceModel(models.Model):
    """
    This class represents the Advice model.
    This class is responsible for creating the data model for the Advice model.

    Attributes:
        author: The user who created the advice.
        title: The title of the advice.
        content: The description of the advice.
        image: The image of the advice.
        date_posted: The date and time when the advice was created.
        slug: The unique identifier of the advice.
        totalViewCount: The total number of views of the advice.
    """
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    totalViewCount = models.IntegerField(default=0)

    def __str__(self):
        return self.title
