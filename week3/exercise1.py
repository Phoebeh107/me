# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    output=[]
    current=start
    while current < stop:
        output.append(current)
        current = current + step
    return output


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    basket_of_stuff=[]
    for i in range(start,stop,step):
        basket_of_stuff.append(i)
    return basket_of_stuff


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    buckets=[]
    for j in range(start,stop,2):
        buckets.append(j)
    return buckets


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """

    found = False
    while found == False:
        my_input=int(input("Give me a number "))
        if my_input > low and my_input < high:
            #print('OK')
            found = True
            #print('your input was' + str(my_input))
        else:
            print("try again")
    return int(my_input)
    




def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    number=[]
    found = False
    while found == False:
        my_input=input("Give me a number ")
        if not isinstance(my_input, str) and not isinstance(my_input, int):
            print('try again')
        else:
            try:
                number=int(my_input)
                found = True        
            except ValueError:
                print('try again')
    return int(number)

   


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    
    number=[]
    found = False
    while found == False:
        my_input=input("Give me a number ")
        if not isinstance(my_input, str) and not isinstance(my_input, int):
            print('try again')
        else:
            try:
                number=int(my_input)
                if number > low and number < high:
                    found = True
                else:
                    found = False
                    print("try again")      
            except ValueError:
                print('try again')                
    return int(number)
    


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
