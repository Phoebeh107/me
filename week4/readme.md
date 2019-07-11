TODO: Reflect on what you learned this week and what is still unclear.
OPEN DATA SET PROJECT
to do:
    3. outliers
    4. histogram + other ways

2 ways to pick paths:
    Dataset first:
        1. find interesting Datase
        2. then find interesting question to answer
        3. tell what you found and how you got there
    Question
        1. have a burning question you want to answer
        2. and then find the dataset that will help you answer interesting
        3. tell us what you found and how you got there
    
TUTORIAL:
    my_list = [54,32,1]
    another_list = ["my_string","!","2"]
    another_list[1]

    #dictionary
    my_dict = {"key":"value"}

    my_dict["key"] 


File handling
# can always just google how to handle each type of file
# to read either: .read or .readlines


Pokedex Function notes:
# status code 200 means everything is all good keep going --> makes sure its going to be a real url
    if r.status_code is 200:

# the_json = json.loads(r.text) #this gets us everthing we want to access --> can then index values and data from inside after this
    the_json = r.json()
    height_current=the_json["height"]
    
# keep the height and the ID of the tallest pokemon to return later..
    if height_current > height_tallest:
        height_tallest = height_current
        ID_tallest = pokemon_id
    else:
        pass
