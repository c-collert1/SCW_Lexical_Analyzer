import re

operators = [">=","<=","==", "!=", "||", ">", "<",  "/", "-", "+", "*", "=" , "&", "!"]

def tokenize_operators(input): 
    token_count = 0

    search = "|".join(re.escape(i) for i in operators)

    tokens = re.findall(search, input)

    for t in tokens: 
        print("Token: " + t + ", Type: Operator")
    
    token_count += len(tokens)

    return token_count