
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