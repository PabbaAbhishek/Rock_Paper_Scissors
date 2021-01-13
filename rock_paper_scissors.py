from os import system
from time import sleep 
import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gestures=[rock,paper,scissors]
should_continue=True
print("\nLet's play Rock-Paper-Scissors with me\n")
while should_continue:
  user=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
  print("You choose")
  print(gestures[user])
  print("CPU choose")
  cpu=random.randint(0,2)
  print(gestures[cpu])
  if cpu==0 and user==1 or cpu==1 and user==2 or cpu==2 and user==0:
    print("You won")
  elif cpu==0 and user==0 or cpu==1 and user==1 or cpu==2 and user==2:
    print("It's a draw")
  else:
    print("You lose")
  result=input("Type 'Y'to play again otherwise type 'N':\n").lower()
  if result=='n':
    should_continue=False
    print("We'll meet again")
    sleep(2)
    system('cls')
  else:
    system('cls')