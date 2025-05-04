SUBSTITUTIONS = {
    '@': 'a', '$': 's', '0': 'o', '1': 'i', '!': 'i', '3': 'e', '7': 't', '5': 's', '4': 'a'
}

def normalize_password(password):
    return ''.join(SUBSTITUTIONS.get(c.lower(), c.lower()) for c in password)
