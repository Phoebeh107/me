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

url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={word_len}"
    
    list_of_words = []
    list_odd = []
    list_even = []

    for i in range (3, 21):
        url_get = url.format(word_len=i)            #changes the word lenght between 3 and 20
        r = requests.get(url_get)
        if r.status_code is 200:
            random_word = str(r.content)
            x = random_word.split("'")
            if int(i) %2 == 0:
                list_even.append(x[1])
            else:
                list_odd.append(x[1])
        elif random_word is None: 
            pass
    list_even.reverse()
    list_of_words.extend(list_odd)
    list_of_words.extend(list_even)
    print(list_of_words)
    return list_of_words