"""
Welcome to ROCK-PAPER-SCISSORS
"""

user_choice=raw_input("Enter either Rock, Paper, or Scissors:  ")
from random import randint
import time

things=["Rock","Paper","Scissors"]
comp_choice=things[randint(0,2)]
print "Your choice is "+user_choice
print "Computer's choice is "
time.sleep(1)
print "."
time.sleep(1)
print "."
time.sleep(1)
print "."
print comp_choice

if user_choice=="Scissors" and comp_choice=="Paper":
  print "You win"
elif user_choice=="Paper" and comp_choice=="Scissors":
  print "Comp wins"
  
elif user_choice=="Rock" and comp_choice=="Scissors":
  print "You win"
elif user_choice=="Scissors" and comp_choice=="Rock":
  print "Comp wins"
  
elif user_choice=="Paper" and comp_choice=="Rock":
  print "You win"
elif user_choice=="Rock" and comp_choice=="Paper":
  print "Comp wins"

else:
  print "It is a Tie!"
