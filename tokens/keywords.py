import re

def tokenize_keywords(input):
    token_count = 0

    # \b is a boundry, matching standalone words \w was matching words as subset of words
    # i.e GET was getting matched in TARGET during testing
    tokenPattern = re.compile(r'\b(?:IF|ELSE|WHILE|PRINT|INTEGER|FLOAT|GET)\b')

    identifiers = tokenPattern.findall(input)
    token_count += len(identifiers)

    return token_count
