from django.db import models

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=100) # University of California Berkeley
  shortname = models.CharField(max_length=50) # berkeley
  domain = models.CharField(max_length=50) # berkeley => @berkeley.edu

  def __unicode__(self):
    return school.name
