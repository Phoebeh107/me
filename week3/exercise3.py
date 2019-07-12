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
    lowerBound = input("Enter a lower bound: ")
    upperBound = input("Enter an upper bound: ")
    
    print("OK then, a number between {} and {} ?".format(lowerBound,upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)
    
    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False
    found = None
    while not guessed:
        guessedNumber = input("Guess a number: ")
        print("You guessed {},".format(guessedNumber),)
        number, found = super_asker(lowerBound, upperBound, guessedNumber)
        if found == True: 
            guessedNumber = number
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
                print("yay!")
                found = True
                return number, found
            else:
                print("Thats not even in the bounds")
                found = False
                return number, found      
        except ValueError:
            print("Thats not a number!")
            found = False
            return number, found
           

def bounds(lowerBound, upperBound):
    found_1 = noot_num(lowerBound)
    found_2 = noot_num(upperBound)
    if found_1 and found_2 == False:
        pass
    else:
        if int(lowerBound) < int(upperBound + 1):
            return lowerBound, upperBound
        
def noot_num(my_input):
    if not isinstance(my_input, str) and not isinstance(my_input, int):
        found = False

if __name__ == "__main__":
    print(advancedGuessingGame())

'''
        number=[]
        found = False
        while found == False:
            my_input=guessedNumber
            if not isinstance(my_input, str) and not isinstance(my_input, int):
                print('try again')
            else:
                try:
                    number=int(my_input)
                    if number > lowerBound and number < upperBound:
                        found = True
                        break
                    else:
                        found = False
                        print("Thats not even in the bounds!")      
                except ValueError:
                    print('try again')
                    found = False 
                    '''           