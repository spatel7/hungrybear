class MealTime(object):

  BREAKFAST = 1
  LUNCH = 2
  DINNER = 3
  LATENIGHT = 4

  CHOICES = (
      (BREAKFAST, "breakfast"),
      (LUNCH, "lunch"),
      (DINNER, "dinner"),
      (LATENIGHT, "late night")
    )

  SELECTABLE = { BREAKFAST: 'breakfast', LUNCH: 'lunch', DINNER: 'dinner', LATENIGHT: 'late night' }
  SELECTABLE2 = { 'breakfast': BREAKFAST, 'lunch': LUNCH, 'dinner': DINNER, 'late night': LATENIGHT }

  @staticmethod
  def time_to_str(time):
    if time not in MealTime.SELECTABLE:
      return None
    return MealTime.SELECTABLE[time]

  @staticmethod
  def str_to_time(str1):
    if str1 not in MealTime.SELECTABLE2:
      return None
    return MealTime.SELECTABLE2[str1]

class PairList(object):

  def __init__(self, tuples):
    self.tuples = tuples

  def contains(self, obj):
    for t in self.tuples:
      if t[0] == obj:
        return t[1]
      elif t[1] == obj:
        return t[0]
    return None

class Item:

  def __init__(self, location, meal, name):
    self.location = location.lower()
    self.meal = meal.lower()
    self.name = name.lower()

  def __repr__(self):
    return self.name + " at " + self.location + " for " + self.meal
