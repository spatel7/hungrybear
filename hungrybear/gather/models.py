from django.db import models

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=100) # University of California Berkeley
  shortname = models.CharField(max_length=50) # berkeley
  domain = models.CharField(max_length=50) # berkeley => @berkeley.edu
  menu_site = models.CharField(max_length=1000, default="") # http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp

  def __unicode__(self):
    return school.name
