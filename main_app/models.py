from django.db import models
from django.urls import reverse


class Tool(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("detail", kwargs={"tool_id": self.id})
  

