import random

# Main function to run the code
def main():
    print(make_sentence(1,"past") + ' (Singular past)')
    print(make_sentence(1,"present") + ' (Singular present)')
    print(make_sentence(1,"future") + ' (Singular future)')
    print(make_sentence(2,"past") + ' (Plural past)')
    print(make_sentence(2,"present") + ' (Plural present)')
    print(make_sentence(2,"future") + ' (Plural future)')

# Returns a randomly chosen determiner based on the quantity input
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """

    # Determing which list is used based upon the input of quantity
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

# Return a randomly chosen noun.
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    # Depending on input of quantity, determine the list to be used
    if quantity == 1:
        # Create a list of strings and assign the list to a variable named words.
        words = ["bird", "boy", "car", "cat", "child", 
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", 
                 "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun
    word = random.choice(words)
    return word

# Return a randomly chosen verb.
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    # Determing which list is used based upon the input of quantity
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", 
                 "ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks", 
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif quantity != 1 and tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

# Return a randomly chosen preposition.
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    word = random.choice(words)
    return word

# Return a randomly chosen prepositional phrase.
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    
    prepositional_phrase = get_preposition() + ' ' + get_determiner(quantity) + ' ' + get_noun(quantity)

    return prepositional_phrase

# Return a randomly chosen adjective.
def get_adjective():
    """Return a randomly chosen adjective.

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    # Create a list of strings and assign the list to a variable named words.
    words = ["claen", "silly", "pitiful", "scrawny", "calm", 
            "glamorous", "clumsy", "jolly", "agreeable", "short"]


    # Randomly choose and return a noun
    word = random.choice(words)
    return word

# Return a randomly chosen adverb.
def get_adverb():
    """Return a randomly chosen adjective.

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    # Create a list of strings and assign the list to a variable named words.
    words = ["always", "frequently", "never", "also", "cheerfully", 
                "hardly", "now", "soon", "accordingly", "finally"]

    # Randomly choose and return a noun
    word = random.choice(words)
    return word

# Returns a completed sentance that pulls from the other functions: get_determiner, 
# get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective, get_adverb
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    # For stretch assignment build out {Determiner} {adjective} {noun} {prepositional_phrase} {adverb} {verb} {determiner} {adjective} {noun} {prepositional_phrase}.
    sentance = get_determiner(quantity) + ' ' + get_adjective() + ' ' + get_noun(quantity) + ' ' + get_prepositional_phrase(quantity) + ' ' + get_adverb() + ' ' + get_verb(quantity, tense) + ' ' + get_determiner(quantity) + ' ' + get_adjective() + ' ' + get_noun(quantity) + ' ' + get_prepositional_phrase(quantity) + '.'
    cap_sentance = sentance.capitalize()
    return cap_sentance

main()