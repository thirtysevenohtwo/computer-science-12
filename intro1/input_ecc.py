# Wrote a small "module" to handle and detect errors in input
# Used in both other files, instead of copying and pasting

def try_in(prompt="default", expect="str"): # Take in the prompt for input, and the type of answer you're expecting
    while True:                             # While True loop that is broken when we correctly return our expected data
        value = input(prompt)               # Actually grab our input from the user, with the passed in prompt
        match expect:                       # Match/Case for our expected types
            case "str": # Handle input as a string
                if not type(value) is str:  # If it isn't a string, return it as one.
                    return str(value)
            case "int": # Handle input as an integer
                if not type(value) is int:  # If data isn't an integer;
                    try:
                        return int(value)   # Try converting it into one
                    except:
                        print("Unexpected input type!") # If we get an error, just try again until the user sorts their shit out.
                elif type(value) is int:    # If our data IS an integer, just return it. 
                    return value
            case "float":   # Handle input as a float
                if not type(value) is float:    # Same idea as the integer processing.
                    try:
                        return float(value)
                    except:
                        print("Unexpected input type!")
                elif type(value) is float:
                    return value