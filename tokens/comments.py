import re

def tokenize_comments(input):
    token_count = 0

    tokens = re.findall("//", input)
    if len(tokens) > 0:
        print("Token: " + str(tokens[0]) + ", Type: Comment")
    token_count += len(tokens)
    
    # Comments are ignored for end token count
    return 0

def remove_comments(input):
    return re.sub(r"//.*", "", input)