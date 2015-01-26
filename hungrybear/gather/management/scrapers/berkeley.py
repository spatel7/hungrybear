# import beautifulsoup4
from bs4 import BeautifulSoup, Comment
from gather.misc import Item
from datetime import datetime
import urllib2

# this method should return a list of tuples
def run():
  response = urllib2.urlopen('http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp')
  html = response.read()

  #trash.py - go for <!-- -->
  content = BeautifulSoup(html, 'html5lib').find_all(id = 'content')[2].tbody.find_all('tr', {"valign":"top"})

  LOCATIONS = {0: "crossroads", 1: "cafe 3", 2: "foothill", 3: "clark kerr"}
  #FOODTYPE = {u'#800040': 'Vegan', u'#008000': 'Vegetarian', u'#000000': 'Regular'}
  #more than one vegetarian color o__O

  menu_items = []

  for time in content: #b/l/d
    for l, loc in enumerate(time.find_all('td')): #cr/c3/fh/ck
      meal = unicode(loc.find('b').string) #meals bolded
      #TRASH.PY
      if meal == u"Lunch/Brunch":
        meal = u"Lunch"
      entrees = loc.find_all('a')      #all meals linked to nutrition
      for entree in entrees:
        name = unicode(entree.string)
        #ftype = FOODTYPE[unicode(entree.font['color'])]
        dininghall = LOCATIONS[l]
        name = str(name)

        menu_items.append(Item(dininghall, meal, name))

  return menu_items

