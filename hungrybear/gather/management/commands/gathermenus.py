from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
  help = 'Runs the scraper to get all the menus for the day.'

  def handle(self, *args, **options):
    self.stdout.write("Beginning the fetch of the school menus.")
    self.stdout.write("Ended the fetch of the school menus.")
