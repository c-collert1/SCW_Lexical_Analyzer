import tokens.keywords as keywords
import tokens.operators as operators
import tokens.identifiers as identifiers
import tokens.numbers as numbers
import tokens.symbols as symbols
import tokens.comments as comments
import tokens.ErrorHandling as errors



print("Enter test file number (1-5):")
test_file_num = input()

# Open selected test file
file_name = "tests/test" + test_file_num + ".scw"
file = open(file_name, "r")

keyword_count = 0
operator_count = 0
symbol_count = 0
identifier_count = 0
number_count = 0
error_count = 0

# Read file line by line
line = file.readline()
while line:

    # Read and remove comments first so we dont tokenize them
    comments.tokenize_comments(line)
    code = comments.remove_comments(line)

    keyword_count += keywords.tokenize_keywords(code)
    identifier_count += identifiers.tokenize_identifiers(code)
    operator_count += operators.tokenize_operators(code)
    number_count += numbers.tokenize_numbers(code)
    symbol_count += symbols.tokenize_symbols(code)
    
    error_count += errors.find_errors(line)
    line = file.readline()



# Read file character by character
#while 1:
#    char = file.read(1)
#    if not char:
#        break
    # DO STUFF WITH CHARACTER HERE
    # Feed each character into every token function???
    

token_count = keyword_count + operator_count + symbol_count + identifier_count + number_count

print("Total Tokens: " + str(token_count) 
      + ", Keywords: " + str(keyword_count) 
      + ", Operators: " + str(operator_count) 
      + ", Symbols: " + str(symbol_count) 
      + ", Identifiers: " + str(identifier_count) 
      + ", Numbers: " + str(number_count) 
      + ", Errors: " + str(error_count))
print()


# Close the file
file.close()