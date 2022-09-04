
def get_username():
    user_name = input("What is your user name? Enter 'End' to quit: ")
    return user_name

def get_pass():
    pwd = input("Enter your password: ")
    return pwd

def get_role():
    role = input("Enter role, User or Admin: ")
    while True:
        if (role.upper() == "ADMIN" or role.upper() == "USER"):
            return role # remember that return exits the function, otherwise this loop would run infintely
        else:
            role = input("Enter role, User or Admin: ")

def printinfo():#used in our last line of code to print the data entered
    userFile = open("users.txt", "r") #open and read
    while True:
        userDetail = userFile.readline() #user file is created in the main program
        if not userDetail:
            break
        userDetail = userDetail.replace("\n", "") #removing the carriage
        userList = userDetail.split('|')
        user_name = userList[0]
        user_pwd = userList[1]
        user_role =userList[2]# these lines of code read the user details and revoves the "|" and the carriage "New Line" at the end before printing the data
        print("User Name: ", user_name, "Password: ", user_pwd, "Role: ", user_role)

if __name__ == "__main__":
    userFile = open ("users.txt", "a+") #creates (if nessesary) and writes to file
    while True:
        user_name = get_username()
        if(user_name.upper() == "END"):
            break
        user_pwd = get_pass()
        user_role = get_role() # getting our info from the functions above

        userDetail = user_name + "|" + user_pwd + "|" + user_role + "|" + "\n"
        userFile.write(userDetail) #userFile is then written into and made into the format that userDetail created when it was declared and filled
    userFile.close() #close saves automatically
    printinfo()



        
