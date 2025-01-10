# 1. Take definitions.json, read it in as our data and use a spaced repetition algorithm to create a long list where each word is encountered less and less often, thus increasing the spacing between encounters as we strengthen our knowledge of the word.
import json
import csv




# 1.1 is to read in the definitions file and process it
def load_vocab_from_json(file_path):
    # load vocab data from json file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # use a for loop, to loop over every word and instantiate a new instance of the class for that word, and add it to the dictionary
    result = {}           # write information to dictionary/object
    for word, definition in data.items(): 
        result[word] = VocabCard(word, definition)
    return result 



# 1.2 create a complex object that keeps track of a whole lot of properties about the word or attributes / therefore we need to define a class for this object
class VocabCard: 
    #represents a single vocab card
    def __init__(self, word, definition, repetitions = 0, interval = 1, ease_factor = 2.5, review_counter = 0, is_new = True):
        # This method defines the arguments or properties expected when we create an instance of this class i.e a vocab card
        self.word = word
        self.definition = definition
        self.repetitions = repetitions
        self.interval = interval
        self.ease_factor = ease_factor
        self.review_counter = review_counter # When this reaches 0, the word is due for review
        self.is_new = is_new
    
    def update_card(self):
        #This method is responsible for handling an encounter with the word and updating when we should encounter it next and a few other things
        if self.repetitions == 0:
            self.interval = 2
        elif self.repetitions == 1:
            self.interval = 4
        else:
            self.interval = round(self.interval * self.ease_factor)

        self.repetitions += 1
        self.is_new = False

        self.ease_factor = max(1.3, self.ease_factor + 0.1) #increment ease factor slightly

        self.review_counter = self.interval

        
    
    def is_learned(self):
        #Telling us if this word is learned completely which is based off a max_repetitions parameter that we will define later
        return







# 1.2.1 we're going to need to define a bunch of methods (functions specific to a class that are kind of like actions - such as a method, that we can use to automatically handle a word encounter)
# 1.3 instantiate this class/object for every word
# 1.4 we can create the spaced repetition algorithm that we'll use to create this long list that cleverly introduces new words, and tests old words at the appropriate intervals
#1.5 save this long list of all our words to a csv file, that can be later read by our game


if __name__ == '__main__':
    vocab_cards = load_vocab_from_json('definitions.json')
    print('Starting vocab learning session...')
