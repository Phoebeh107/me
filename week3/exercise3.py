"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    *-- a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = not_number_rejector("Enter a lower bound: ")
    upperBound = not_number_rejector("Enter an upper bound: ")
    while bounds(lowerBound, upperBound) == False:
        print('new bounds needed')
        lowerBound = not_number_rejector("Enter a lower bound: ")
        upperBound = not_number_rejector("Enter an upper bound: ")
    # ask for new input if not a number, or lower bound and upper bound not appropriate
    print("OK then, a number between {} and {} ?".format(lowerBound,upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)
    
    actualNumber = random.randint((lowerBound + 1), (upperBound-1))
    guessed = False
    found = None
    while not guessed:
        guessedNumber = not_number_rejector("Guess a number: ")
        print("You guessed {},".format(guessedNumber),)
        found = super_asker(lowerBound, upperBound, guessedNumber)
        if found[1] == True: 
            #guessedNumber = number
            if  int(guessedNumber) == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif int(guessedNumber) < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


def super_asker(low, high, my_input):
    number=[]   
    if not isinstance(my_input, str) and not isinstance(my_input, int):
        print("Thats not a number!")
        found = False
        return False 
    else:
        try:
            number=int(my_input)
            if number > low and number < high:
                #print("yay!")
                found = True
                return [number, True]
            else:
                print("Thats not even in the bounds")
                found = False
                return number, found      
        except ValueError:
            print("Thats not a number!")
            found = False
            return number, found

def bounds(lowerBound, upperBound):
    if int(lowerBound) == int(upperBound):
        return False
    elif (int(upperBound)-(int(lowerBound))) == 1:
        return False
    elif int(lowerBound) < (int(upperBound) - 1):
        return True
    else:
        return False


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    number=[]
    found = False
    while found == False:
        my_input=input(message)
        if not isinstance(my_input, str) and not isinstance(my_input, int):
            print('try again')
        else:
            try:
                number=int(my_input)
                found = True        
            except ValueError:
                print('try again')
    return int(number)


if __name__ == "__main__":
    print(advancedGuessingGame())

