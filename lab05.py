# DEFINE FUNCTIONS HERE
# ==============================================#

# NEED: Canonicalization function

# NEED: homograph function

# NEED/WANT? non-homographic test cases (this is where all the different test cases will be held)

# NEED/WANT? homographic test cases (this is where all the different homographic test cases will be)

### This is option 1 in the menu ###
def run_test_cases():
    print("Test Case!") # Test to make sure function works

    # Function for running non-homographic test cases?

    # Function for running homographic test cases?

### This is option 2 in the menu ###
def run_manual_compare():
    firstFilename = input("Please enter first filename: ")
    print() # Blank space
    secondFilename = input("Please enter second filename: ")


### MAIN ENTRY OF PROGRAM -- MENU ###
# ================================================#
# While loop forever because we don't want to exit unless the user wants to (by selecting option 3) 
while(True):
    print("Please select option to continue:")
    print() # blank line

    # Create options, place them into an array, and loop through the array, printing each option.
    menu_options = ["1. Run prebuilt test cases","2. Enter two filenames manually", "3. End Program"]
    for option in menu_options:
        print(option)

    # Wait for user input
    print() # Blank line
    option = input("~ ")

    # create array of valid options, in this case whatever is presented in menu list.
    valid_options = ["1","2","3"]

    # If the input does not match what is in the array, display error message and begin loop again.
    if(option not in valid_options):
        print("Sorry, you have entered in a wrong value. Please look at the menu again and enter a number value")
        print() # Blank line
        continue

    
    # Use swtich case now since user input is a valid option at this point.
    match int(option):
        case 1: # Option 1 is to run the team's assembled test cases
            run_test_cases()

        case 2: # Option 3 is to manually compare 2 filenames
            run_manual_compare()
        
        case 3: # Option 3 ends the program, so break out of while loop
            break







    
