import random


def main():
    # defining variables!
    distance_traveled = 0
    distance_natives_traveled = -20
    rider_thirst = 0
    number_of_drinks = 5
    camel_fatigue = 100

    # basic instruction to player
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    # print and loop choices, ask for input
    done = False
    while done == False:
        # defining random number variables
        natives_random = random.randrange(7, 14)
        full_speed_random = random.randrange(10, 20)
        fatigue_random = random.randrange(1, 3)
        moderate_speed_random = random.randrange(5, 12)
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        player_choice = input("What is your choice? ")

        # carry out choice a
        if player_choice.lower() == "a":
            if number_of_drinks != 0:
                print("You took a drink!")
                number_of_drinks -= 1
                rider_thirst = 0
            if number_of_drinks == 0:
                print("There are no more drinks remaining!")

        # carry out choice b
        if player_choice.lower() == "b":
            print("You traveled forward at moderate speed!")
            distance_traveled += moderate_speed_random
            print("Distance Traveled: ", distance_traveled)
            rider_thirst += 1
            camel_fatigue += 1
            distance_natives_traveled += natives_random

        # carry out choice c
        if player_choice.lower() == "c":
            print("You traveled forward at full speed!")
            distance_traveled += full_speed_random
            print("Distance Traveled: ", distance_traveled)
            rider_thirst += 1
            camel_fatigue += fatigue_random
            distance_natives_traveled += natives_random

        # carry out choice d
        if player_choice.lower() == "d":
            print("You took a rest, the camel is happy!")
            camel_fatigue = 0
            distance_natives_traveled += natives_random

        # carry out choice e
        if player_choice.lower() == "e":
            print("Number of Drinks: ", number_of_drinks)
            print("Distance Traveled: ", distance_traveled)
            print("Distance Natives Traveled: ", distance_natives_traveled)

        # carry out choice q
        if player_choice.lower() == "q":
            done = True
            print("Game Over")

        # thirst levels
        if rider_thirst > 4:
            print("You are thirsty!")
        elif rider_thirst > 6:
            print("You die of thirst!")
            done = True

        # camel tiredness
        if camel_fatigue > 5:
            print("Your camel is getting tired!")
        elif camel_fatigue > 8:
            print("Your camel is dead!")
            done = True

        # natives distance
        if distance_natives_traveled == distance_traveled:
            print("The Natives have caught you!")
            done = True
        if distance_traveled - distance_natives_traveled < 15:
            print("The Natives are getting close!")

        # win the game
        if distance_traveled >= 200:
            print("You've won! Congrats!")
            done = True

# calling the function
main()
