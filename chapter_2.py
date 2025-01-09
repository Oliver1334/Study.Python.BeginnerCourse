# 1. Take definitions.json, read it in as our data and use a spaced repetition algorithm to create a long list where each word is encountered less and less often, thus increasing the spacing between encounters as we strengthen our knowledge of the word.
import json
import csv




# 1.1 is to read in the definitions file and process it
def load_vocab_from_json(file_path):
    # load vocab data from json file
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data # COME BACK AND FINISH THIS LATER



# 1.2 create a complex object that keeps track of a whole lot of properties about the word or attributes / therefore we need to define a class for this object
# 1.2.1 we're going to need to define a bunch of methods (functions specific to a class that are kind of like actions - such as a method, that we can use to automatically handle a word encounter)
# 1.3 instantiate this class/object for every word
# 1.4 we can create the spaced repetition algorithm that we'll use to create this long list that cleverly introduces new words, and tests old words at the appropriate intervals
#1.5 save this long list of all our words to a csv file, that can be later read by our game

