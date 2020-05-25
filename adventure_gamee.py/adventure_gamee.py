import time
import random


enemy = ["vampire", "werewolve", "hybrid", "witch"]
demon = random.choice(enemy)
items = []

def print_pause(message):
    print(message)
    time.sleep(2)

def restart_game():
    if "mundanes" in items:
        items.remove("mundanes")
    response = input("Would you like to play again? (y/n)")

    if response == 'y':
       shadow_hunters()

    elif response == 'n':
        print_pause("Thanks for playing! See you next time.")

    else:
        restart_game()


def intro():
    print_pause("You find yourself standing in a jumgle, filled with spikey grasses,wild animals,dark heay trees and yellow wildflowers.")  
    print_pause("Rumor has been spread that there is {demon} somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you,there's a famous haunting castle known as 'ALMORA'.")
    print_pause("To your right,there's a SILENT BROTHER'S cave.")
    print_pause("In your hand you hold your trusty (but not very effective) sword.\n")



def jungle():
    # Things that happen when the player runs back to the field
    print_pause("Enter 1 to the jump into the haunting castle 'ALMORA'.")
    print_pause("Enter 2 to sneak into the cave.")
    print("what would you like to do?")

    response = (input("(please enter 1 or 2).\n"))

    if response == '1':
        castle()
    elif response == '2':
        cave()
    else:
        jungle()

def castle():
    # Things that happen to the player in the house.
    print_pause("You approach the door of the castle 'ALMORA'.")
    print_pause(f"You are about to jump off the wall and suddenly the big door opens and steps out a {demon}.")
    print_pause(f"Eep! This is the {demon}'s castle!!!!")
    print_pause(f"The {demon} attacks you!")

    

    if "mundanes" in items:
        print_pause(f"As the {demon} moves to attack, you unsheath your angelic mundane from a crystal ball and take out the sword as well.")
        print_pause("The mundane from angelic IRON SISTERS shines horrificly besides you as you brace yourself for the attack.")
        print_pause(f"But the {demon} takes a look at your shiny new toy and it felt shattered in his eyes and he runs away!")
        print_pause(f"You have rid yourself,the town and the jungle of the {demon}.One part of the battle you won "
                     "untill that demon came back and try to get his castle back,"
        print_pause(" You are victorious!.....VICTORY OWNS YOU")
        restart_game()
    
    elif "mundanes" not in items:
        print_pause("You feel a bit under-prepared for this, with having only the sword not the angelic crystal.")
        response = input("Would you like to (1) fight or (2) run away?\n")

        if response == '1':
            print_pause("You do your best...")
            print_pause(f"But your sword became weak in front of the {demon}.")
            print_pause("You have been defeated!!!")
            restart_game()

        elif response == '2':
            print_pause("You run back into the jungle. Luckily, you don't seem to have "
                        "been followed in the dark wild trees as you thouroughly know the map of the jungle.\n")
            jungle()

def cave():
    # Things that happen to the player goes in the cave
    if "mundanes" in items:
        print_pause("You sneak cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff also with werewolve venom."
                    " It's just an empty cave now with werewolve shit and bones")
        print_pause("You walk back out towards the dark jungle.")
        jungle()
    else:
        print_pause("You sneak cautiously into the cave.")
        print_pause("It turns out to be a very deep cave inside.")
        print_pause("Your eye catches a neon sparkling eyes behind a rock.")
        print_pause("You have found a werewolve glaring into your eyes as its gonna tears you apart")
        print_pause("You took your sword onto the shoulder and attacks the werewolve untill he dies .")
        print_pause("You found a new crafted most vulnerable and veteran sword which was protected by werewolve.")
        print_pause("You took the sword and walk back out to the jungle.\n")
        items.append("mundanes")
        jungle()

# def fight():
    # Things that happen when the player fights

def shadow_hunters():
    intro()
    jungle()

shadow_hunters()
