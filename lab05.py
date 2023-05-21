# DEFINE FUNCTIONS HERE
# ==============================================#

# This is the Rendering function that takes an input and returns a rendition
def R(is_homograph):
    
    if not is_homograph:
        
        return "\nResult: Not Homograph!"
    
    return ("\nResult: Homograph.")

# Here is Canonicalization function

def C(file_name):

    file_to_split = file_name.split("\\")
    
    # Loop to check and remove single period file path: 
    for data in file_to_split:
        
        if data == '.':
            
            file_to_split.remove(data)
    
    array_data = []
    
    
    # Loop to check and remove double period file path: 
    for data in file_to_split:
        if data == "..":
            if array_data and array_data[-1] != "..":
                array_data.pop()
            
            else:
                array_data.append('..')
        
        else:
            array_data.append(data)
    

    cannonized_path = '\\'.join(array_data)
    
    # if file_name.startswith("C:")
    
    return cannonized_path

# Here is Homograph function:
def H (canonized_path_1, canonized_path_2):
#     print("Use " + c + "in comparing two file paths are the same")
    
    if canonized_path_1 != canonized_path_2:
        
        return False
    
    return True
    
# NEED/WANT? non-homographic test cases (this is where all the different test cases will be held)

# NEED/WANT? homographic test cases (this is where all the different homographic test cases will be)


### This is option 1 in the menu ###
def run_test_cases():

    FORBIDDEN_FILE = "C:\\secret\\password.txt"
    
    """
    For each Test case run Steps 1-3:
    
    HOMOGRAPHS:                        
        1)	
            a)	Location 1:
            b)	Location 2:

        2)	../
            a)	Location 3:
            b)	Location 4:

        3)	./../
            a)	Location 5:
            b)	Location 6:


        NON-HOMOGRAPHS
        4)	./
            a)	Location 1:
            b)	Location 2:

        5)	../
            a) Location 1:
            b)	Location 2:

        6)	./../
            a) Location 1:
            b) Location 2:
    """
# Define Homograph Test Cases

    # Homograph Test Dictionary:
    # 1. Call the C()

    # 2. Call the H()

    # 3. Display results: H OR Non-H?
    
    homograph_set = {
        
        "Case 1a" : "C:\\secret\\..\\secret\\password.txt", 
        "Case 1b" : "\\..\\C:\\secret\\password.txt", 
        "Case 2a" : "C:\\.\\secret\\..\\secret\\..\\secret\\..\\secret\\password.txt", 
        "Case 2b" : "C:\\.\\secret\\password.txt", 
        "Case 3a" : "C:\\.\\secret\\..\\..\\C:\\secret\\..\\secret\\.\\password.txt", 
        "Case 3b" : "C:\\secret\\.\\..\\secret\\password.txt"
        
        }
    
    for item in homograph_set.values():
        
        cannonized_item = C(item)
        result = H(cannonized_item, FORBIDDEN_FILE)
        print (R(result))

    # Non-homograph Dictionary:
    # 1. Call the C()

    # 2. Call the H()

    # 3. Display results: H OR Non-H?
    
    non_homograph_set = {
        
        "Case 4a":"secret\\password_1.text", 
        "Case 4b":"..\.\secret_1\\password.txt", 
        "Case 5a":"..\.\secret_1\\password_2.txt", 
        "Case 5b":"..\..\.\.\passwords.txt", 
        "Case 6a":"secrets\\password.txt", 
        "Case 6b":"C:\\secrets\\..\\secret\\password_1.txt"
        
        }
    
    for item in non_homograph_set.values():
        
        # Print Case # for the user, and print it's subsequent Value
        # EX Terminal "Case 4a: "secret\\password_1.text"
        #              Result: Non-homograph
        cannonized_item = C(item)
        result = H(cannonized_item, FORBIDDEN_FILE)
        
        # Build format print of Dictionary values:
        
        
        print (R(result))
        print("\n") # Blank space
    
### This is option 2 in the menu ###
def run_manual_compare():

    """Forbidden file - this is the path you should copy/paste 
    on the terminal for the input value of filename1 
    when comparing to filename2 input: C:\secret\password.txt"""
    # Get file names from user
    first_Filename = input(str("\nPlease enter first filename: "))
    second_Filename = input(str("\nPlease enter second filename: "))
    

    # Call C() for both filenames
    canonized_filename1 = C(first_Filename)
    canonized_filename2 = C(second_Filename)

    # Call H(), pass in both user's filenames
    print("\nNow comparing", first_Filename, " and ", second_Filename)
    result = H(canonized_filename1, canonized_filename2)

    # Print the R(), passing in the H()'s result
    print(R(result), "\n")



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







    
