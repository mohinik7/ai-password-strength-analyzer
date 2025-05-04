from nltk.corpus import wordnet

def semantic_match(password):
    words = [''.join(filter(str.isalpha, part)) for part in password.split()]
    matches = []
    for word in words:
        if wordnet.synsets(word):
            matches.append(word)
    return matches
