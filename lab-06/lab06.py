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
"med_eps5425/Zlwhrw_10T25", # Vilma's Test Case VALID INPUT
"al_caes3708/Jqoevtr_3901", # Alma's Test Case VALID INPUT
"tu_lin22171/Medli_ww2003" # Darcy's Test Case VALID INPUT
]

## DONE: Create a function that feeds the test cases into the query function
# and displays the resulting query.
def test_valid(query_function):

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
        print(f'Query: {query_function(usernames[i], passwords[i])}')


'''STEP 2: VULNERABILITIES - TAUTOLOGY'''
## TODO: Generate test cases (one for each member) that demostrates a tautology attack
tautology_test_cases = [
    "pad_akl_1025/Padakliath1025' OR 'x' = 'x", # Chase's tautology test case
    "tu_lin22171/Medli_ww2003' OR 'w' = 'w'", # Darcy's  tautology test case
    "med_eps5425/Zlwhrw_10T25' OR 1 = 1", # Vilma's  tautology test case
    "al_caes3708/Jqoevtr_3901'  OR 'a'= 'a'", # Alma's tautology test case
     

]


## DONE: Create a function that feeds these test cases through the query function and
## Displays the output.
def test_tautology(query_function):
    usernames = []
    passwords = []
    
    # Gather usernames and passwords from valid_input array by splitting each input in the array.
    for input in tautology_test_cases:
        temp_input = input.split("/")
        usernames.append(temp_input[0])
        passwords.append(temp_input[1])

    print("\nTesting Tautology inputs: \n")

    for i in range(len(usernames)):
        print(f'Test Case {i + 1}: \n Username: {usernames[i]} \n Password: {passwords[i]}')
        print(f'Query: {query_function(usernames[i], passwords[i])}')



'''STEP 2: VULNERABILITIES - UNION ATTACK'''
## TODO: Generate test cases (one for each member) that demostrates a union attack
union_test_cases = [
    "chasemoses/nothing' UNION SELECT authenticate FROM passwordList", # Chase's Union Attack Test Case
    "darcymer/empty' UNION SELECT authenticate FROM secretList",  #Darcy's Union Attack Test Case
    "vilmacam/loquesea' UNION SELECT * FROM userPaylocity",  #Vilma's Union Attack Test Case
    "alcaes/password'  UNION SELECT authenticate FROM passwordList", # Alma's Union Attack Test Case
    
    
]

## DONE: Create a function that feeds these test cases through the query function and
## Displays the output.
def test_union(query_function):
    usernames = []
    passwords = []
    
    # Gather usernames and passwords from valid_input array by splitting each input in the array.
    for input in union_test_cases:
        temp_input = input.split("/")
        usernames.append(temp_input[0])
        passwords.append(temp_input[1])

    print("\nTesting Union Attack inputs: \n")

    for i in range(len(usernames)):
        print(f'Test Case {i + 1}: \n Username: {usernames[i]} \n Password: {passwords[i]}')
        print(f'Query: {query_function(usernames[i], passwords[i])}')

'''STEP 2: VULNERABILITIES - ADDITIONAL STATEMENT ATTACK'''
## TODO: Generate test cases (one for each member) that demostrates a additional statement attack
additional_test_cases = [
    "chasemoses/nothing'; INSERT INTO passwordList (username, password) VALUES 'Chase', 'pass", # Chase's Vulnerability Attack Test Case
    "'darcymer/empty'; INSERT INTO secretList (username,password) VALUES 'Darcy, 'toon", # Darcy's Vulnerability Attack Test Case
    "'vilmacam/loquesea'; INSERT INTO secretList (username,password) VALUES 'Vilma, '~scrub", # Vilma's Vulnerability Attack Test Case
    "'alcaes/nothing'; INSERT INTO passwordList (username,password) VALUES 'Alma, '1234", # Alma's Vulnerability Attack Test Case
]
## DONE: Create a function that feeds these test cases through the query function and
## Displays the output.
def test_additional(query_function):
    usernames = []
    passwords = []
    
    # Gather usernames and passwords from valid_input array by splitting each input in the array.
    for input in additional_test_cases:
        temp_input = input.split("/")
        usernames.append(temp_input[0])
        passwords.append(temp_input[1])

    print("\nTesting Additional Attack inputs: \n")

    for i in range(len(usernames)):
        print(f'Test Case {i + 1}: \n Username: {usernames[i]} \n Password: {passwords[i]}')
        print(f'Query: {query_function(usernames[i], passwords[i])}')

'''STEP 2: VULNERABILITIES - COMMENT ATTACK'''
## TODO: Generate test cases (one for each member) that demostrates a comment attack
comment_test_cases = [
    "chasemoses'; --/nothing" # Chase's comment attack test case
    "darcymer'; --/null" #Darcy's comment attack test case
    "vilmacamp'; --/admin'#" #Vilma's comment attack test case
]
## DONE: Create a function that feeds these test cases through the query function and
## Displays the output.
def test_comment(query_function):
    usernames = []
    passwords = []
    
    # Gather usernames and passwords from valid_input array by splitting each input in the array.
    for input in additional_test_cases:
        temp_input = input.split("/")
        usernames.append(temp_input[0])
        passwords.append(temp_input[1])

    print("\nTesting Comment Attack inputs: \n")

    for i in range(len(usernames)):
        print(f'Test Case {i + 1}: \n Username: {usernames[i]} \n Password: {passwords[i]}')
        print(f'Query: {query_function(usernames[i], passwords[i])}')

'''STEP 3: WEAK MITIGATION'''

## TODO: Create a function to provide weak mitigation against ALL four attacks (one function!)
## Show that all four malicious inputs are mitigated based on the test cases.
def gen_query_weak(username, password):

    # Valid Mitigation Code here?
    # CHECK FOR SPECIAL KEY WORDS IN THE INPUT
    no_allowed = ["OR", "UNION", "~", ";","AND", "--", "#", "\"", "/", "$", "@", "="]
    correcto = 1
    for y in no_allowed:
        # INVALID CHARACTER CHECK - USE OF UPPER CASE
        if(y in username.upper() or y in password.upper()):
            print(f"\tThe entered {username} is invalid, the use of {y} is NOT allowed.")
            correcto = 0
    if correcto == 1:
        print("\tThe entered credential PASSED the test!. They are valid!")
 
    #return (username, password)
    return f"SELECT * FROM Authtable WHERE Username='{username}' AND Password='{password}';"


    # # Tautology Mitigation Code here
    # no_allowed_Tau = ["OR", " OR ", "="]
    # correcto = 1
    # for y in no_allowed_Tau:
    #     # INVALID CHARACTER CHECK - USE OF UPPER CASE
    #     if(y in username.upper() or y in password.upper()):
    #         print(f"\tThe entered {username} is invalid, the use of {y} is NOT allowed.")
    # return (username, password)

    # # Union Mitigation Code here
    # no_allowed_Union = ["UNION"]
    # correcto = 1
    # for y in no_allowed_Union:
    #     # INVALID CHARACTER CHECK - USE OF UPPER CASE
    #     if(y in username.upper() or y in password.upper()):
    #         print(f"\tThe entered {username} is invalid, the use of {y} is NOT allowed.")
    # return (username, password)

    # # Additional Statement Mitigation Code Here
    # no_allowed_Addit = ["~", ";","AND", "--","\"", "/", "$", "@", "="]
    # correcto = 1
    # for y in no_allowed_Addit:
    #     # INVALID CHARACTER CHECK - USE OF UPPER CASE
    #     if(y in username.upper() or y in password.upper()):
    #         print(f"\tThe entered {username} is invalid, the use of {y} is NOT allowed.")
    # return (username, password)

    # # Comment Mitigation Code here 
    # no_allowed_comment = ["--","@", "=", "#"]
    # correcto = 1
    # for y in no_allowed_comment:
    #     # INVALID CHARACTER CHECK - USE OF UPPER CASE
    #     if(y in username.upper() or y in password.upper()):
    #         print(f"\tThe entered {username} is invalid, the use of {y} is NOT allowed.")

    # return (username, password)
    # #return "This is the weak mitigation function"

'''STEP 4: STRONG MITIGATION'''

## TODO: Create a function that provides strong mitigation against all command
## injection attacks. Show that all four malicious inputs are mitigated based on
## test cases.
def gen_query_strong(username, password):
    
    # Valid Mitigation Code here?


    # Tautology Mitigation Code here


    # Union Mitigation Code here


    # Additional Statement Mitigation Code Here


    # Comment Mitigation Code here 

    
    return "This is the strong mitigation function"


### THIS FUNCTION IS THE ENTRY POINT FOR ALL OTHER FUNCTIONS ###
def start_sql_simulation():
    
    # This section is to test NO MITIGATION using gen_query()
    print("NOW TESTING NO MITIGATION\n")
    test_valid(gen_query)
    test_tautology(gen_query)
    test_union(gen_query)
    test_additional(gen_query)
    test_comment(gen_query)

    # This section is to test WEAK MITIGATION using gen_query_weak()
    print("\n\nNOW TESTING WEAK MITIGATION\n")
    test_valid(gen_query_weak)
    test_tautology(gen_query_weak)
    test_union(gen_query_weak)
    test_additional(gen_query_weak)
    test_comment(gen_query_weak)

    # This section is to test STRONG MITIGATION using gen_query_strong()
    print("\n\nNOW TESTING STRONG MITIGATION\n")
    test_valid(gen_query_strong)
    test_tautology(gen_query_strong)
    test_union(gen_query_strong)
    test_additional(gen_query_strong)
    test_comment(gen_query_strong)

    # TEMPORARY BLANK LINE
    print('\n')

# 

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
    # match int(option):
    #     case 1: # Option 1 is to run the team's assembled test cases
    #         start_sql_simulation()

    #     case 2: # Option 2 ends the program, so break out of while loop
    #         break

    if int(option) == 1:
        start_sql_simulation()
    
    elif int(option) == 2:
        break