import random

def main(quantity, tense):
    print(f"{get_prepositional_phrase(quantity, 0)} {get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity,1)}.")

def get_determiner(quantity):

    if quantity == 1:
        words = ["a", "one", "the"]

    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man",
         "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children","dogs", "girls",
         "men", "rabbits", "women"]
            
    word = random.choice(words)
    return word
       
def get_verb(quantity, tense):
    if tense.lower() == "past":
         words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept",
          "talked", "walked", "wrote"]
    elif quantity == 1 and tense.lower() == "present":
            words = ["drinks", "eats", "grows", "laughs", "thinks","runs",
             "sleeps", "talks", "walks", "writes"]
    elif quantity > 1 and tense.lower() == "present":
            words = ["drink", "eat", "grow", "laugh", "think","run", "sleep",
             "talk", "walk", "write"]
    elif tense.lower() =="future":
           words = ["will drink", "will eat", "will grow", "will laugh",
           "will think", "will run", "will sleep", "will talk","will walk",
            "will write"]
    word = random.choice(words)
    return word

def get_preposition():
    words =["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity, when):
    if when == 0:
        phrase = (f"{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_preposition()}")
    elif when == 1:    
        phrase = (f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}")
    return phrase


main(1, "past")
main(1, "present")
main(1, "future")
main(2, "past")
main(2, "present")
main(2, "future")
