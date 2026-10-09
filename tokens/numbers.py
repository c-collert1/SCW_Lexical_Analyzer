import re

def tokenize_numbers(input):
    token_count = 0

    # Finds decimal numbers 
    tokens = re.findall("[+-]?[0-9]+\.[0-9]+", input)
    if len(tokens) > 0:
        for i in range(len(tokens)):
            print("Token: " + str(tokens[i]) + ", Type: Decimal")
    token_count += len(tokens)

    # Find integer numbers
    tokens = re.findall("[+-]?(?<![\d.])[0-9]+(?![\d.])", input)
    if len(tokens) > 0:
        for i in range(len(tokens)):
            print("Token: " + str(tokens[i]) + ", Type: Integer")
    token_count += len(tokens)
    
    # Comments are ignored for end token count
    return token_count