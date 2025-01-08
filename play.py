# What is the project?
# Vocab builder / language learning app that uses spaced repetition to learn and practice new words

# Instructions

# 1. Take definitions.json, read it in as our data and use a spaced repetition algorithm to create a long list where each word is encountered less and less often, thus increasing the spacing between encounters as we strengthen our knowledge of the word.
# 1.1 is to read in the definitions file and process it
# 1.2 create a complex object that keeps track of a whole lot of properties about the word or attributes / therefore we need to define a class for this object
# 1.2.1 we're going to need to define a bunch of methods (functions specific to a class that are kind of like actions - such as a method, that we can use to automatically handle a word encounter)
# 1.3 instantiate this class/object for every word
# 1.4 we can create the spaced repetition algorithm that we'll use to create this long list that cleverly introduces new words, and tests old words at the appropriate intervals
#1.5 save this long list of all our words to a csv file, that can be later read by our game

# 2. Create a game, where a user has to get through as many items in the list (i.e answer them correctly), and when they ultimately fail, then they get a high score and have to start again (forcing them to continue practicing)
# 2.1 Create the files to read both the long list of space-repeated words so that we can loop over them and test the user continuously until they fail, at which point we give them a score, and also the word definitions so that we may show  a user a word definition if it's their first time encountering the word
# define a continuous while loop, that tests the user on each word in the list, one after another in the provided order, and will only exit when each word has been mastered, or the user makes a mistake
# 2.3 print the new high score when they fail or win, and also a command to start again