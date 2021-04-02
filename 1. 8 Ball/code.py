# Fortune telling 8-ball with if/else statements

import random

# Name and question...
name = "Josh"
question = "Am i alive?"

answer = ""
randomNumber = random.randint(1,9)

if randomNumber == 1:
  answer = "Yes - definitely"
elif randomNumber == 2:
  answer = "It is decidedly so"
elif randomNumber == 3:
  answer = "answer3"
elif randomNumber == 4:
  answer = "answer4"
elif randomNumber == 5:
  answer = "answer5"
elif randomNumber == 6:
  answer = "answer6"
elif randomNumber == 7:
  answer = "answer7"
elif randomNumber == 8:
  answer = "answer8"
elif randomNumber == 9:
  answer = "answer9"
else:
  answer = "Answer Error"

print(name + " asks: " + question)
print("Magic balls answer: " + answer)

# Try this in a Python emulator instead of static variables above?
# name = input("What is your name? ")
# question = input("What is your question? ")
