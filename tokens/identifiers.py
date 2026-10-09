import re

keywords = ["IF", "ELSE", "WHILE", "PRINT", "INTEGER", "FLOAT", "GET"]

def tokenize_identifiers(input):
    token_count = 0

    tokenPattern = re.compile(r'\b[a-zA-Z][a-zA-Z0-9_]*\b')

    identifiers = tokenPattern.findall(input)
    for t in identifiers: 
        # skip keywords
        if t in keywords:
            continue
        token_count += 1
        print("Token: " + t + ", Type: Identifier")

    return token_count