

'''STEP 2: VULNERABILITIES'''
## TODO: Generate test cases (one for each member) that demostrates a tautology attack

## TODO: Create a function that feeds these test cases through the query function and
## Displays the output.

''' DO STEP 2 FOR UNION QUERY ATTACK, AN ADDITIONAL STATEMENT ATTACK, AND A COMMENT
    ATTACK.'''
## TODO: Union Query Attack test case and function

## TODO: Additional Statement Attack test cases and function

## TODO: Comment Attack test cases and function


'''STEP 3: WEAK MITIGATION'''

## TODO: Create a function to provide weak mitigation against ALL four attacks (one function!)
## Show that all four malicious inputs are mitigated based on the test cases.

'''STEP 4: STRONG MITIGATION'''

## TODO: Create a function that provides strong mitigation against all command
## injection attacks. Show that all four malicious inputs are mitigated based on
## test cases.

### DEFINE FUNCTIONS and TEST CASE ARRAYS HERE ###

'''STEP 1: QUERY GENERATION '''
## DONE: Write a function to accept username/password parameters. 
## This function should return a single SQL string representing the
## query used to determine if a user is authenticated on a given system.
def gen_query(username, password):
    return f"SELECT * FROM Authtable WHERE Username='{username}' AND Password='{password}';"

## TODO: Generate a set of test cases (one for each team member). It 
# will represent valid input where the username and the password consist 
# of letters, numbers, and underscores

'''PLEASE SEPARATE USERNAME AND PASSWORD WITH A /
   EXAMPLE: chasemoses/password1234'''
valid_inputs = [
"pad_akl1025/Padakliath_1025", # Chase's Test Case VALID INPUT.
# " ", # Vilma's Test Case VALID INPUT
# " ", # Alma's Test Case VALID INPUT
# " " # Darcy's Test Case VALID INPUT
]

## DONE: Create a function that feeds the test cases into the query function
# and displays the resulting query.
def valid_test():

    usernames = []
    passwords = []
    
    # Gather usernames and passwords from valid_input array by splitting each input in the array.
    for input in valid_inputs:
        temp_input = input.split("/")
        usernames.append(temp_input[0])
        passwords.append(temp_input[1])

    print("Testing Valid inputs: \n")

    for i in range(len(usernames)):
        print(f'Test Case {i + 1}: \n Username: {usernames[i]} \n Password: {passwords[i]}')
        print(f'Query: {gen_query(usernames[i], passwords[i])}')

    



### THIS FUNCTION IS THE ENTRY POINT FOR ALL OTHER FUNCTIONS ###
def start_sql_simulation():
    
    # TEST VALID INPUT
    valid_test()


    # TEMPORARY BLANK LINE
    print('\n')







### ENTRY POINT OF FILE - MENU ###

while(True):
    print("Please select option to continue:\n")

    # Create options, place them into an array, and loop through the array, printing each option.
    menu_options = ["1. Run prebuilt test cases","2. End Program"]
    for option in menu_options:
        print(option)

    # Wait for user input
    print() # Blank line
    option = input("~ ")

    # create array of valid options, in this case whatever is presented in menu list.
    valid_options = ["1","2"]

    # If the input does not match what is in the array, display error message and begin loop again.
    if(option not in valid_options):
        print("Sorry, you have entered in a wrong value. Please look at the menu again and enter a number value")
        print() # Blank line
        continue
    
    # Use swtich case now since user input is a valid option at this point.
    match int(option):
        case 1: # Option 1 is to run the team's assembled test cases
            start_sql_simulation()

        case 2: # Option 2 ends the program, so break out of while loop
            break