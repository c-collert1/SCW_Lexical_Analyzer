import re

symbols = ["(", ")", "{", "}", ";"]

def tokenize_symbols(input): 
    token_count = 0
    # Adds an or to each of the symbols, that way when searching it finds the symbols.
    # Also makes it so that the special characters are ignoresd.
    search = "|".join(re.escape(i) for i in symbols)

    tokens = re.findall(search, input)

    #For each item found it prints the token.
    for t in tokens: 
        print("Token: " + t + ", Type: Symbol")
    
    token_count += len(tokens)

    return token_count
