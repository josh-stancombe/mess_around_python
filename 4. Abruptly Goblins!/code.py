#    -- Introduction -- 
# Opening your comic book store, the Sorcery Society, has been a lifelong dream come true. You quickly diversified your shop offerings to include miniatures, plush toys, collectible card games, and board games. Eventually, the store became more a games store with a selection of this week's newest comic books and a small offering of graphic novel paperbacks. Completing your transformation means offering space for local tabletop gamers. They love to play their favorite RPG, "Abruptly Goblins!" and will happily pay you per chair to secure the space to do it. Unfortunately, planning the game night has fallen to you. If you pick the wrong night, not enough people will come and the game night will be cancelled. You decide it's best that you automate the game night selector to get the most people through the door. 
 
game = "Abruptly Goblins!"

## Setting up the gamers
gamers = []

def add_gamer(gamer, gamers_list):
    varName = gamer["name"]
    varAvailability = gamer["availability"]
    
    if varName is not None or varAvailability is not None:
        gamers_list.append(gamer)

kimberly = {"name":"kimberly", "availability":["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


## Finding the perfect availability
def build_daily_frequency_table():
    return {"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0,}

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)

def find_best_night(availability_table):
    highestVal = 0
    highestKey = ""
    for day in availability_table:
        if availability_table[day] > highestVal:
            highestVal = availability_table[day]
            highestKey = day
    return highestKey

game_night = find_best_night(count_availability)
print("")
print("The best night for a game of '" + game + "' is " + game_night)  

def available_on_night(gamers_list, day):
    lst = []
    for gamer in gamers_list:
        for available in gamer["availability"]:
            if available == day:
                lst.append(gamer["name"])
    return lst

attending_game_night = available_on_night(gamers, game_night)

## Generating an E-mail for the Participants
def form_email(name, day_of_week, game):
    return "> Hi {name}! We are hosting a game of {game} on {day}. Hope you can join us!".format(name=name, day=day_of_week, game=game)

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email(gamer, day, game))

print("")
print("Here is a list of the email notificatiosn to the participants:")
send_email(attending_game_night, game_night, game)
