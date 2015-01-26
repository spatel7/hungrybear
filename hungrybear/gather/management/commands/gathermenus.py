from django.core.management.base import BaseCommand, CommandError
from gather.models import School, DiningHall, MenuItem
from gather.misc import MealTime, Item
from datetime import datetime
import os, sys

class Command(BaseCommand):
  help = 'Runs the scraper to get all the menus for the day.'

  def handle(self, *args, **options):
    sys.path.append(os.path.join(os.path.dirname(__file__), "../scrapers")) # get the scrapers
    for school in School.objects.all():
      self.stdout.write("Scraping for school: {0}".format(school))
      scraper = __import__(school.shortname)
      menu_items = scraper.run()
      dining_halls = school.dining_halls()
      for item in menu_items:
        dining_hall = dining_halls[item.location]
        meal_time = MealTime.str_to_time(item.meal)
        try:
          menu_item = MenuItem.objects.get(school=school, dining_hall=dining_hall, meal_time=meal_time, name=item.name)
          if menu_item.last_served != datetime.today().date():
            menu_item.times_served = menu_item.times_served + 1
        except MenuItem.DoesNotExist:
          menu_item = MenuItem(school=school, dining_hall=dining_hall, meal_time=meal_time, name=item.name)
        menu_item.save()
        self.stdout.write("Just saved {0}".format(menu_item))
