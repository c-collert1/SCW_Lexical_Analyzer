import re

operators = [">=","<=","==", "!=", "||", ">", "<",  "/", "-", "+", "*", "=" , "&", "!"]

def tokenize_operators(input): 
    token_count = 0

    # Adds an or to each of the operators, that way when searching it finds the operators.
    # Also makes it so that the special characters are ignoresd.
    search = "|".join(re.escape(i) for i in operators) 

    # Uses the search variable
    tokens = re.findall(search, input)

    #For each item found it prints the token.
    for t in tokens: 
        print("Token: " + t + ", Type: Operator")
    
    token_count += len(tokens)

    return token_count