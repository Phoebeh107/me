"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will create a list containing the strings: what, does, this, line, do, ?
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #created a list with the words inside

# This will print each word from the list some_words until there are no words left in some_words to print
for word in some_words: #printed each word from the list in order until it had printed all words
    print(word)

#x is the index of some words so will print the words in some_words until there are no more words/index's
for x in some_words: #the same thing as the function above just assigning each word to 'x' rather than 'word'
    print(x)

#will print the whole array/list 'some_words'
print(some_words) #printed some_words in its form - an array/list

#will check to see if there are more entries in some_words than 3 and if so it will tell you that 'some_words contains more than 3 word'
if len(some_words) > 3:
    print('some_words contains more than 3 words') #printed some_words contains more than 3 words, therefore some_words has more than 3 entries

#returns the namedtuple containing information about my computer and its operating system; specifically (system, node=computer name, release, version, machine and processor)
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #printed the computer and operating system informations; (system='Windows', node='Phoebe', release='10', version='10.0.17134', machine='AMD64', processor='Intel64 Family 6 Model 61 Stepping 4, GenuineIntel')

usefulFunction()
