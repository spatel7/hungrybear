from django.core.management.base import BaseCommand, CommandError
from gather.models import School
import os, sys

class Command(BaseCommand):
  help = 'Runs the scraper to get all the menus for the day.'

  def handle(self, *args, **options):

    for school in School.objects.all():
      sys.path.append(os.path.join(os.path.dirname(__file__), "../scrapers")) # get the scrapers
      self.stdout.write("Found school: {0}".format(school))
      scraper = __import__(school.shortname)
      menu_items = scraper.run()
