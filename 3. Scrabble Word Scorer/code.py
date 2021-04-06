# Scrabble - In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letter_to_points = {key:value for key, value in zip(letters,points)}

# Score a word function
def score_word(word):
  word = word.upper()
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  
  return point_total

brownie_points = score_word("BROWNIE!")

# Players and their words
player_to_words = {"player1": ["blue", "tennis", "exit"], "wordnerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "Belly", "HUSKY"], "Prof Reader": ["ZAP", "coma", "period"]};

# Calculate the points per player
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points = player_points + score_word(word)
  player_to_points[player] = player_points

print(player_to_points)
  