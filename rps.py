import random
import pdb
import sys
from datetime import datetime
import logging

now = datetime.now()
date_time = now.strftime("%Y-%d-%m %H_%M_%S")
filename = date_time + ".txt"
f = open(filename, "w")

logging.basicConfig(filename= date_time + ".txt", level=logging.INFO, format='%(message)s')

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

def play(user):
    computer = random.choice(['r', 'p', 's'])


    return_message = "You chose " + define_user(user) + " and the computer chose " + define_user(computer) + "."
    if user == computer:
        logging.info("You both chose " + define_user(user) + ". It's a tie!")
        print("You both chose " + define_user(user) + ". It's a tie!")

    # r > s, s > p, p > r
    if win(user, computer):
        logging.info(return_message + " You win!")
        print(return_message + " You win!")

    if loss(user, computer):
        logging.info(return_message + " You lose!")
        print(return_message + " You lose!")

def win(user, computer):
    # return true if player wins
    # r > s, s > p, p > r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

    return False

def loss(user, computer):
    # return true if player wins
    # r > s, s > p, p > r
    if (user == 'r' and computer == 'p') or (user == 's' and computer == 'r') or (user == 'p' and computer == 's'):
        return True

def define_user(name):
    user_chose = ""
    if name == scissors[:1]:
        user_chose = scissors
    if name == rock[:1]:
        user_chose = rock
    if name == paper[:1]:
        user_chose = paper

    return(user_chose)


def set_user():

    logging.info("'r' for rock, 'p' for paper, 's' for scissors or q to quit ")
    user = input("'r' for rock, 'p' for paper, 's' for scissors or q to quit ")
    if define_user(user) == "" and user.lower() != "q":
        logging.info("invalid selection")
        print("invalid selection")

        return "0"


    return user

user = set_user()
while user == "0":
   user = set_user()

while user.lower() != "q":
    #pdb.set_trace()
    play(user.lower())
    print("\n")
    user = set_user()

   # pdb.set_trace()
logging.info("You have exited the game")
print("You have exited the game.")
