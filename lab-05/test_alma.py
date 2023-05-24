
def test_function(file_name):
    # C:\Users\chsmoses\secret\password.txt

    file_to_split = file_name.split("\\")
   
    
    array_data = []

    for data in file_to_split:
        if data == "..":
            if array_data and array_data[-1] != "..":
                array_data.pop()
            
            else:
                array_data.append('..')
        
        else:
            array_data.append(data)
    

    cannonized_path = '\\'.join(array_data)
    return cannonized_path


file_path_1 = "C:\\Git\\..\\Git\\Security-Expert-Wannabes-CSE453" # C:\Security    
file_path_2 = "C:\\Git\\Security-Expert-Wannabes-CSE453"
canonized_path_1 = test_function(file_path_1)
canonized_path_2 = test_function(file_path_2)

# paths = [canonized_path_1,canonized_path_2]

# for value in paths:

if canonized_path_1 == canonized_path_2:
    
    print("Homograph set")
    
else:
    print("Files are different")
    
    print("Thanks, bye")    

    # f_name = input(str())
    # f_folder = input(str())
    # master_folder = input(str())
    # Init_source_strt = input(str())

    # file_Check = {f"Init_source_strt"+"/master_folder"+"/f_folder"+"/f_name"}
    #Simple code to compare the two homograpghs
    # path1 = input("What is your first file path?")
    # path2 = input("What is your second file path?")

    # if path1 == path2:
    #     print("The sets are homographs")
    # else:
    #     print("Files are diffrent")

    # print("Have a good day")


    # user_string_path = []

    # if user_string_path



# Git\Security-Expert-Wannabes-CSE453



# DEFINE FUNCTIONS HERE
# ==============================================#

# This is the Rendering function that takes an input and returns a rendition
def R(is_homograph):
    
    if not is_homograph:
        
        return "\nFiles are not a Homograph!"
    
    return ("\nFiles are a Homograph.")

# Here is Canonicalization function

def C(file_name):
    # \secret\password.txt

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
        "Case 2a" : "..\password.txt", 
        "Case 2b" : ".\secret\\password.txt", 
        "Case 3a" : "..\\..\\secret\\password.txt", 
        "Case 3b" : ".\\password.txt"
        
        }
    
    for item in homograph_set.values():
        
        C(item)
        result = H(item, FORBIDDEN_FILE)
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
        
        C(item)
        result = H(item, FORBIDDEN_FILE)
        print (R(result))
    
### This is option 2 in the menu ###
def run_manual_compare():
    firstFilename = input("Please enter first filename: ")
    print() # Blank space
    secondFilename = input("Please enter second filename: ")
    if firstFilename == secondFilename:
        print("The sets are homographs")
    else:
        print("Files are diffrent")


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







    
