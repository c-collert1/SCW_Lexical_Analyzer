import re

symbols = ["(", ")", "{", "}", ";"]

def tokenize_symbols(input): 
    token_count = 0

    search = "|".join(re.escape(i) for i in symbols)

    tokens = re.findall(search, input)

    for t in tokens: 
        print("Token: " + t + ", Type: Symbol")
    
    token_count += len(tokens)

    return token_count
