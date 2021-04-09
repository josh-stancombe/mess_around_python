# Restaurant Menu Class
class Menu():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{} menu available from {} until {}".format(self.name, self.start_time, self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

# Franchise Class
class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "This is the {} restaurant".format(self.address)
  
  def available_menus(self, time):
    available = []
    for item in self.menus:
      if time >= item.start_time and time <= item.end_time:
        available.append(item.name)
    print("Menu's currently available are: {}".format(available))

# Business Class
class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


# Available Menu Items
brunch_items = { 'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50 }

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

# Menu items into Menu class objects
brunch = Menu("brunch", brunch_items, 1100, 1600)
early_bird = Menu("early_bird", early_bird_items, 1500 , 1800)
dinner = Menu("dinner", dinner_items, 1700, 2300)
kids = Menu("kids", kids_items, 1100, 2100)
arepas_menu = Menu("arepa", arepa_items, 1000, 2000)

# Restaurant Franchises
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Creating Businesses
basta_fazoolin_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepa_business = Business("Take a' Arepa", [arepas_place])


#Testing functions:

# -- Calculate Bill Testing --
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

# -- Testing available menus --
#flagship_store.available_menus(2030)

# Testing Businesses
#print(arepa_business.franchises[0].menus[0])
