from django.db import models
from gather.misc import MealTime

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=100) # University of California Berkeley
  shortname = models.CharField(max_length=50) # berkeley
  domain = models.CharField(max_length=50) # berkeley => @berkeley.edu
  menu_site = models.CharField(max_length=1000, default="") # http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp

  def __unicode__(self):
    return self.name

  def dining_halls(self):
    return dict((hall.name, hall) for hall in DiningHall.objects.filter(school=self))

class DiningHall(models.Model):
  school = models.ForeignKey(School)
  name = models.CharField(max_length=100)

  def __unicode__(self):
    return "{0} at {1}".format(self.name, self.school)

class MenuItem(models.Model):
  school = models.ForeignKey(School)
  dining_hall = models.ForeignKey(DiningHall)
  meal_time = models.IntegerField(choices=MealTime.CHOICES)
  last_served = models.DateField(auto_now=True)
  times_served = models.IntegerField(default=1)
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return "{0} served during {2} at {1}".format(self.name, MealTime.time_to_str(self.meal_time), self.dining_hall)
