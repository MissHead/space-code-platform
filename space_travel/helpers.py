import random


def certification_generate():
    while True:
        certification = [random.randint(0, 6) for i in range(6)]
        if certification != certification[::-1]:
            break
    value = sum((certification[num] * ((6 + 1) - num) for num in range(0, 6)))
    digit = ((value * 10) % 7) % 10
    certification.append(digit)
    result = ''.join(map(str, certification))
    return result


def planet_name_generate():
    planets = []
    with open("space_travel/planets.txt", "r") as f:
        raw = f.read()
    planets = raw.split("\n")
    total_syllables = 0
    syllables = []
    for p in planets:
        lex = p.split("-")
        total_syllables += len(lex)
        for l in lex:
            if l not in syllables:
                syllables.append(l)
    size = len(syllables) + 1
    freq = [[0] * size for i in range(size)]
    for p in planets:
        lex = p.split("-")
        i = 0
        while i < len(lex) - 1:
            freq[syllables.index(lex[i])][syllables.index(lex[i+1])] += 1
            i += 1
        freq[syllables.index(lex[len(lex) - 1])][size-1] += 1
    planet_name = ""
    suffixes = [
        "prime", "",
        "B", "",
        "alpha", "",
        "proxima", "",
        "IV", "",
        "V", "",
        "C", "",
        "VI", "",
        "VII", "",
        "VIII", "",
        "X", "",
        "IX", "",
        "D", ""
    ]
    length = random.randint(2, 3)
    initial = random.randint(0, size - 2)
    while length > 0:
        while 1 not in freq[initial]:
            initial = random.randint(0, size - 2)
        planet_name += syllables[initial]
        initial = freq[initial].index(1)
        length -= 1
    suffix_index = random.randint(0, len(suffixes) - 1)
    planet_name += " "
    planet_name += suffixes[suffix_index]
    return planet_name


def resource_name_generate():
    resource = []
    with open("space_travel/objects.txt", "r") as f:
        raw = f.read()
    resource = raw.split("\n")
    total_syllables = 0
    syllables = []
    for r in resource:
        lex = r.split("-")
        total_syllables += len(lex)
        for l in lex:
            if l not in syllables:
                syllables.append(l)
    size = len(syllables) + 1
    freq = [[0] * size for i in range(size)]
    for r in resource:
        lex = r.split("-")
        i = 0
        while i < len(lex) - 1:
            freq[syllables.index(lex[i])][syllables.index(lex[i+1])] += 1
            i += 1
        freq[syllables.index(lex[len(lex) - 1])][size-1] += 1
    resource_name = ""
    suffixes = [
        "of mermaid", "",
        "of light", "",
        "of fire", "",
        "oxygen", "",
        "potassium", "",
        "chlorine", "",
        "carbon", "",
        "of time", "",
        "III", "",
        "VIII", "",
        "X", "",
        "IX", "",
        "D", "",
        "gold", ""
        "", ""
    ]
    length = random.randint(2, 3)
    initial = random.randint(0, size - 2)
    while length > 0:
        while 1 not in freq[initial]:
            initial = random.randint(0, size - 2)
        resource_name += syllables[initial]
        initial = freq[initial].index(1)
        length -= 1
    suffix_index = random.randint(0, len(suffixes) - 1)
    resource_name += " "
    resource_name += suffixes[suffix_index]
    return resource_name


def description_generate():
    nouns = ("oxygen", "gold", "robot", "planet", "space", "credit", "pilot", "resource", "weight", "box")
    verbs = ("runs", "hits", "jumps", "drives", "chunks", "changes", "describes", "adores", "enables", "wishes") 
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.", "brightly.", "carefully.", "firmly.", "lightly.", "weirdly.")
    adj = ("disgusting", "small", "dirty", "odd", "stupid", "worse", "extraordinary", "attractive", "defeated", "good")
    return nouns[random.randrange(0,10)] + ' ' + verbs[random.randrange(0,10)] + ' ' + adj[random.randrange(0,10)] + ' ' + nouns[random.randrange(0,10)] + ' ' + adv[random.randrange(0,10)]
