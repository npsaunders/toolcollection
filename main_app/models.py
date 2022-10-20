from django.db import models
from django.urls import reverse

PM = (
  ("C", "Clean"), 
  ("R", "Replace worn parts"), 
  ("F", "Full tear-down")
)

# Create a Storage model; this will be where the tool can be stored
# The user will be able to enter/view/update/delete storage locations.
class Storage(models.Model):
  #create a name field in the database that is of type CharField
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  #This sets a canonical URL for the model & is required when using the 
  #reverse() function. It lets you refer to a model in the templates
  #rather than hard-coding them. In this case we're defining a URL path
  #to the storage detail html page
  def get_absolute_url(self):
  #The reverse function allows you to retrieve the URL details from the 
  #urls.py file through the name value provided (in this case "storage_detail")
    return reverse("storages_detail", kwargs={"pk": self.id})
  
  def __str__(self):
    return self.name
  

class Tool(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  storages = models.ManyToManyField(Storage)

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
