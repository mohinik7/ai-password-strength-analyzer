SUBSTITUTIONS = {
    '@': 'a', '$': 's', '0': 'o', '1': 'i', '!': 'i', '3': 'e', '7': 't', '5': 's', '4': 'a',
    '8': 'b', '9': 'g', '|': 'l', '+': 't', '2': 'z', '6': 'g', '?': 'q', '%': 'x', '#': 'h'
}

def normalize_password(password):
    # Replace leet characters and collapse repeated characters
    normalized = ''.join(SUBSTITUTIONS.get(c.lower(), c.lower()) for c in password)
    # Collapse repeated characters (e.g., 'aaa' -> 'a')
    import re
    normalized = re.sub(r'(.)\1+', r'\1', normalized)
    return normalized
