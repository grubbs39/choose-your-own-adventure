def kitchen1():
    print("\nYou awake in a kitchen.")
    print("You look down, you see you need to bake a cake.")
    print("As you look around you see you have no ingredients, and need to go to the store.")
    print("How will you get to the store?")
    print("1) car")
    print("2) Bicycle")

    answer = input(">")

    if answer == "1":
        game_over("There was a gridlock, you made it to the store as it closed.")
    elif answer == "2":
        store_main()
    else:
        game_over("Go and learn how to type a number.")


def store_main():
    print("\nYou made it to the store.")
    print("You will need to get 1 egg, 1 bag of flour, 1 gallon of milk")
    print("Which way will you go?")
    print("1) 2 lefts")
    print("2) 2 rights")

    answer = input(">")

    if answer == "1":
        egg_aisle()
    elif answer == "2":
        game_over("You hit a brick wall.")
    else:
        game_over("Go and learn how to type a number.")

def egg_aisle():
    print("\nYou made it the egg aisle!")
    print("You got the egg!")
    print("1) 2 steps over")
    print("2) end of the aisle")

    answer = input(">")

    if answer == "1":
        milk_aisle()
    elif answer == "2":
        game_over("You passed the milk.")
    else:
        game_over("Go and learn how to type a number.")

def milk_aisle():
    print("\nYou see the milk!")
    print("You grab the milk!")
    print("1) Follow the cosplayer")
    print("2) Go get the bag of flour")

    answer = input(">")

    if answer == "1":
        game_over("Looks like you entered a different adventure.")
    elif answer == "2":
        flour_aisle()
    else:
        game_over("Go and learn how to type a number.")

def flour_aisle():
    print("\nYou made it to the Flour!")
    print("You grab the Flour!")
    print("1) go home")
    print("2) pay for the food")

    answer = input(">")

    if answer == "1":
        game_over("You're meant to pay for that!")
    elif answer == "2":
        Payment_home()
    else:
        game_over("Go and learn how to type a number.")

def Payment_home():
    print("You managed to pay and go home.")
    print("Now what?")
    print("1) Mix ingredients and set timer for baking.")
    print("2) Mix ingredients and put in oven and lie down.")

    answer = input(">")

    if answer == "1":
        Timer()
    elif answer == "2":
        game_over("The cake catches fire and burns the house down.")
    else:
        game_over("Go and learn how to type a number.")

def Timer():
    print("The timer goes off. now what?")
    print("1) watch the cake go in flames.")
    print("2) Take the cake out of the oven.")

    answer = input(">")

    if answer == "1":
        game_over("This is fine.")
    elif answer == "2":
        print("YAY!! You have a cake!")
        play_again()
    else:
        game_over("Go and learn how to type a number.")

def game_over(reason):
  print("\n" + reason)
  print("Game Over!")

  play_again()

def play_again():
    print("\nDo you want to play again? (y or n)")

    answer = input(">").lower()

    if "y" in answer:
        kitchen1()
    elif "n" in answer:
        exit()
    else:
        exit()

kitchen1()
