# import beautifulsoup4
from gather.misc import Item

# this method should return a list of tuples
def run():
  menu_items = []
  menu_items.append(Item('crossroads', 'breakfast', 'eggs'))
  menu_items.append(Item('crossroads', 'breakfast', 'bacon'))
  menu_items.append(Item('crossroads', 'lunch', 'pizza'))
  menu_items.append(Item('crossroads', 'dinner', 'nachos'))
  return menu_items
