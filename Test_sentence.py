from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    single_determiners = ["a", "one", "the"]
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = ["some", "many", "the"]

    for _ in range(4):
        word = get_determiner(2)
        assert word.lstrip() in plural_determiners

def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():
    Past_verb = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(1, "past")
        assert word in Past_verb

    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, "present")
        assert word in single_present_verbs
    
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb( 2, "present")
        assert word in plural_present_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    for _ in range(4):
        word = get_verb( 1, "future")
        assert word in future_verbs
    
def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_preposition()
        assert word in prepositions

def test_get_prepositional_phrase():
    plural_determiners = ["some", "many", "the"]
    single_determiners = ["a", "one", "the"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    single_nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    words = get_prepositional_phrase(1,1).split(" ")
    assert len(words) == 3
    assert words[0] in prepositions
    assert words[1] in single_determiners or plural_determiners
    assert words[2] in single_nouns or plural_nouns
    words = get_prepositional_phrase(1,0).split(" ")
    assert len(words) == 3
    assert words[2] in prepositions
    assert words[0] in single_determiners or plural_determiners
    assert words[1] in single_nouns or plural_nouns



pytest.main(["-v", "--tb=line", "-rN", __file__])