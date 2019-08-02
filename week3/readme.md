TODO: Reflect on what you learned this week and what is still unclear.
LECTURE:
#Recap: 
    >>>another_list
    [{'taste': 'Delicious', 'name': 'Cake'},
    [1, 2, 3, 4, 5] ]
        to call 'Delicious' from another_list:
            another_list[0]["taste"]
        to call 2 from another_list
            another_list[1][1]

#Sytax:
    in
        5 in [1,2,3]    --> False
        "oh in "oh hai" --> True
        7 in {"key": 7, "otherKey":5} --> False (it thinks you are referring to keys not values)
    Catching error
        try: 
            do_a_dumb()
        except Exception as e:
            print("you did a dumb", e)
        finally:
            print("we still love you")
#ALGORITHMS
    Select a point at which to run the algorithm from
#Big O --> worst case running time
    O(1)
        Given a = [1, 2, 3]
        Getting a[0]

    O(n)
        Given a = [1, 2, 3]
        Getting len(a) # Naively

    Spotting O(n^2)
        def square_loop()
            for x in range(5):
                for y in range(9):
                    for z in range(9):
                        print('*') 


ADMIN:
#Course Outline: 
    weeks 1-5 exercises
    week 3 (today) Introduction to the data project
    week 6 First week of data project tutorials --> MAIN PROJECT
        find an open data set: .gov webside (around the world/aus)
        honiet?? website(syd uni website)- good example
            different lines around Sydney: latte line/fast food line --> map to social groups/socioeconomic
        past: all of real estate --> looks like done on tuesday
            permanently broken wind centre 
        pic something from real world: eg. running-- strava data sets, do runners go to different places to cyclist
                aviation: drone flying restrictions
            TO FIND: strava - API
                ASK!!!!! - open data sets from government open data sets(often rubbish) -- airbnb?
                TWITTER! - geotagged where do people read/do a lot of things
                Gold standard - compare 2 sets - usually too hard (can do: suburbs and streets- simple stuff)
                GPS TRACKING OF SPORTS PLAYERS - ask for info from teams
    week 7 ML assignment
    week 8 exam - rising rate--> not supposed to finish it necessarily
    week 9 no class
    week 10 data project tutorials
    week 12 data project presentations
#Tests:
    Red - shoudln't pass before you've written anything
    Green - write code to achieve what the tests want you to do
    Refactor - make the code simpler and make more sense over and over while you know you its correct and passing
#Git flow:
    git status --> git add file_name.py --> git commit -m "make this even cooler,fix #666" --> git status (circular flow)
    if help is needed --> git status and send them the output
        can add git push after git commit



EXERCISES:
#def stubborn_asker(low, high):
    found = False
    while found == False:
        my_input=int(input("Give me a number "))
        if my_input > low and my_input < high:
#           #print('OK') - shows us when we are in this if statment
            found = True
#           #print('your input was' + str(my_input)) - same thing, while debugging shows us what the inputs currently stored are in an easier to read format
        else:
            print("try again")
    return int(my_input)

#LIST.append('*')
this puts a * in the relevant position in the list/array LIST

#Extra functions that were tried for guessing game:
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


def noot_num(my_input):
    number=None
    if not isinstance(my_input, str) and not isinstance(my_input, int):
        found = False
    else:
        try:
            number=int(my_input)
            found = True        
        except ValueError:
            found = False
    return found
    '''           

