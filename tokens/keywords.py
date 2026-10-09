import re

def tokenize_keywords(input):
    token_count = 0

    # \b is a boundry, matching standalone words \w was matching words as subset of words
    # i.e GET was getting matched in TARGET during testing
    tokenPattern = re.compile(r'\b(?:IF|ELSE|WHILE|PRINT|INTEGER|FLOAT|GET)\b')

    keywords = tokenPattern.findall(input)
    token_count += len(keywords)

    for t in keywords: 
        print("Token: " + t + ", Type: Keyword")

    return token_count
