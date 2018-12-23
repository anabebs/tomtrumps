import random
import shutil
import os      #here I have imported all necessary functions for the following code to work
import array
import time

allowedresponses = ["Exercise","Intelligence","Friendliness","Drool"] #this allows me to make sure both the user and the computer select only the values available
cardcount = 0
usercards = 0           #the following variables are used for later
computercards = 0
x = 1
y = 0


play = input("Welcome to Celebrity Dogs Top Trumps! Press S to start, or Q to quit: ")
play = play.upper()
while x==1:
if play == "S" or play == "s":
        print("Great! Lets play!")
        x+=1                                #here the user is given the option to play the game or quit. Pressing Q will immediatley end the the program, whilst pressing S will start it.
    elif play == "Q" or play == "q":        #x = 1 variable is used to end the while loop, permitted the user enters an appropriate answer
        print("OK, bye")
        quit
        x+=1
    else:
        print("That's not a valid answer. Please try again")
        play = input("Welcome to Celebrity Dogs Top Trumps! Press S to start, or Q to quit: ")

cardcount = int(input("How many cards in this game? Please pick an even number between 4 and 30: "))  #the following section of code asks the to select the number of cards they want played
while x==2:
    if cardcount < 4:
        print("Thats too small! Please try again!") #the programs tells the user to select again if they have picked a number smaller than 4
        cardcount = int(input("How many cards in this game? Please pick an even number between 4 and 30: "))
    elif cardcount > 30:
        print("Thats too big! Please try again!") #the programs tells the user to select again if they have picked a number larger than 30
        cardcount = int(input("How many cards in this game? Please pick an even number between 4 and 30: "))
    if cardcount % 2 != 0:
        print("Thats an odd number! Please try again!")#the programs tells the user to select again if they have picked a number that can't be divided by 2 with no remainders, essentially forcing only even numbers
        cardcount = int(input("How many cards in this game? Please pick an even number between 4 and 30: "))
    else:
        print("Perfect! Onwards!")
        x+=1 #once again I have used the x variable to allow the user to continue if they have selected a number that fits the requirements

time.sleep(1)

print("----------------------------------------------------------------------")

print("Rules: 1) For exercise, intelligence and friendliness, the highest value wins. For drool, lowest wins")
print("       2) If there is a draw, the player that picked the value wins and gets the cards")
shutil.copyfile('dogs.txt','celebdogs.txt') #this creates a copy of the dogs text file. It is mainly for if I ever need to edit a file with the dogs in,, the origin file is never changed.

topdogs = [] #here I have created an array for the dogs 
inp = open('celebdogs.txt','r') #I have used python's text file edits to import everything in the newly made celebdogs text file into an array, in order to import it later
for line in inp.readlines():
    topdogs.append([])
    for i in line.split():
        topdogs[-1].append(i)
inp.close()

deck = [] #here I have created an array for the deck of cards that will be used in the game

print("----------------------------------------------------------------------")

for index in range(0,cardcount): #this part of the code tells the program to repeat the following until the number of cards selected by the user is in the deck
    deck.insert([index][0], [(random.choice(topdogs))])#h
    deck[index].append("Exercise: ")
    deck[index].append(random.randint(0,5))
    deck[index].append("Intelligence: ")
    deck[index].append(random.randint(0,100))
    deck[index].append("Friendliness: ")
    deck[index].append(random.randint(0,10))
    deck[index].append("Drool: ")
    deck[index].append(random.randint(0,10))

time.sleep(1)

playerDeck=[]
computerDeck=[]

while len(deck)>0:
    playerDeck.append(deck.pop(0))
    computerDeck.append(deck.pop(0))

time.sleep(1)

print("This is your deck: ")
print(playerDeck)

playerTurn = True

print("----------------------------------------------------------------------")

time.sleep(1)

print("This is your first card: ")
print(playerDeck[0])

if playerTurn == True:
    answer = input("Please select an attack (Exercise, Intelligence, Friendliness and Drool): ")
    while allowedresponses.count(answer) == 0:
        answer = input("That isn't a valid choice, please try again: ")

else:
    answer = random.choice(allowedresponses)
    print("Computer chooses", answer)

print("Computer Card: ")
print(computerDeck[0])


if playerDeck == cardcount:
    print("You win!!!!")

if computerDeck == cardcount:
    print("Computer wins!!!!")

os.remove('celebdogs.txt')