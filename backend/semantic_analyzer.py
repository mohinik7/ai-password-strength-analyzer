from nltk.corpus import wordnet
import nltk

# Ensure WordNet is downloaded
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
    nltk.download('omw-1.4')

def semantic_match(password):
    try:
        words = [''.join(filter(str.isalpha, part)) for part in password.split()]
        matches = []
        for word in words:
            if word and len(word) > 2:  # Only check words longer than 2 characters
                try:
                    if wordnet.synsets(word):
                        matches.append(word)
                except Exception as e:
                    print(f"Error checking word '{word}': {str(e)}")
                    continue
        return matches
    except Exception as e:
        print(f"Error in semantic_match: {str(e)}")
        return []
