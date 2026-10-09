import tokens.keywords as keywords
import tokens.operators as operators
import tokens.identifiers as identifiers
import tokens.numbers as numbers
import tokens.symbols as symbols
import tokens.comments as comments


print("Enter test file number (1-5):")
test_file_num = input()

# Open selected test file
file_name = "tests/test" + test_file_num + ".source"
file = open(file_name, "r")

token_count = 0

# Read file line by line, I am not sure which one we want
line = file.readline()
while line:
    print(line)
    line = file.readline()

    # Runs every time a line is read
    token_count += keywords.tokenize_keywords(line)
    token_count += operators.tokenize_operators(line)
    token_count += symbols.tokenize_symbols(line)
    token_count += identifiers.tokenize_identifiers(line)
    # token_count += numbers.tokenize_numbers(line)
    token_count += comments.tokenize_comments(line)

# Read file character by character
#while 1:
#    char = file.read(1)
#    if not char:
#        break
    # DO STUFF WITH CHARACTER HERE
    # Feed each character into every token function???
    

print("Token Count: " + str(token_count))
print()


# Close the file
file.close()
