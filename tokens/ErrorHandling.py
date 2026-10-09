import re

def find_errors(line):
    error_count = 0

    #find all the valid tokes and subtract them from our line
    leftover = line
    leftover = re.sub(r"//.*", "", leftover)                                                # comments
    leftover = re.sub(r"\b(?:IF|ELSE|WHILE|PRINT|INTEGER|FLOAT|GET)\b", " ", leftover)      # keywords
    leftover = re.sub(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+(?![\w.])", " ", leftover) # numbers
    leftover = re.sub(r"\b[a-zA-Z][a-zA-Z0-9_]*\b", " ", leftover)                          # identifiers
    leftover = re.sub(r">=|<=|==|!=|\|\||[><+\-*/=&!]", " ", leftover)                      # operators
    leftover = re.sub(r"[(){};]", " ", leftover)                                            # symbols


    # classify invalid
    for bad in leftover.split():
        if re.fullmatch(r"\d[\w.]*|\.\d+", bad):
            #if it has a number its a bad number format
            print("Error: illegal number format '" + bad + "'")
        elif re.fullmatch(r"\w+", bad):
            #if it is a word its an illegal identifier
            print("Error: illegal identifier '" + bad + "'")
        else:
            # unkowns
            print("Error: invalid character '" + bad + "'")
        error_count += 1

    return error_count