import re

def tokenize_identifiers(input):
    token_count = 0

    # must start with a letter and it can not have any special characters (barring '_')
    tokenPattern = re.compile(r'\b[a-zA-Z][a-zA-Z0-9_]*\b')

    identifiers = tokenPattern.findall(input)
    token_count += len(identifiers)
    for t in identifiers: 
            print("Token: " + t + ", Type: Identifier")

    return token_count