import random
turn=5
guess=0

number=random.randrange(100)+1
print("The computer is guessing a number between 1 to 10 and You have 5 turns to guess it ")

while guess!=number and turn>0:
     print("Turn remaining:",turn)
     guess=int(input("Guess a number:"))
     if guess<number:
        print("Enter a greater number")
     elif guess>number:
          print("Enter a lower number")
     turn=turn-1

if guess==number:
     print("congratulations !!! You won.")

if guess!=number:
     print("sorry ,You ran out of turns ,and computer guessed,",number)


