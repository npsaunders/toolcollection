from django.db import models
from django.urls import reverse

PM = (
  ("C", "Clean"), 
  ("R", "Replace worn parts"), 
  ("F", "Full tear-down")
)


class Tool(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("detail", kwargs={"tool_id": self.id})


class Maintenance(models.Model):
  date = models.DateField("maintenance date")
  maintenance = models.CharField(max_length=1, choices=PM, default=PM[0][0])

  tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_maintenance_display()} on {self.date}"


class Meta:
  ordering = ["-date"]
