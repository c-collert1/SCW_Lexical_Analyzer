import tokens.comments as comments

print("Enter test file number (1-5):")
test_file_num = input()

# Open selected test file
file_name = "tests/test" + test_file_num + ".source"
file = open(file_name, "r")

token_count = 0

# Read file line by line, I am not sure which one we want
#line = file.readline()
#while line:
#    print(line)
#    line = file.readline()

# Read file character by character
while 1:
    char = file.read(1)
    if not char:
        break
    # DO STUFF WITH CHARACTER HERE
    # Feed each character into every token function???
    token_count += comments.tokenize_comments(char)

print("Token Count: " + str(token_count))

# Close the file
file.close()

### import tokens
# This gets run just from importing??
import tokens.keywords as keywords
