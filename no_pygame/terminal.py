print("This program is copyright of Mcalpin Programming, Inc.")
print("The default password is 'pythonterminal'.")
print("Type 'help' for a list of commands.")
print("")
username = "terminal"
password = "pythonterminal"
def command():
    inputCommand = input(username + "@pythonterminal:~ $ ")
    if inputCommand == "exit":
        quit()
        
    elif inputCommand == "print-data":
        print(" Your name is " + username + ".")
        
    elif inputCommand == "help":
        print(" The commands you can use are:")
        print("     exit - quit the terminal - This doesn't work in MU 1.0.2.")
        print("     help - opens the help page")
        print("     print-data - View your data")
        print("     change-user - Change the username")
        print("     change-password - Change the password")

    elif inputCommand == "":
        command()
        
    elif inputCommand == "change-user":
        print("This command requres superuser privileges.")
        inputPassword = input("What is your password? ")
        if inputPassword == password:
            check = True
        else:
            check = False
        if check == True:
            username = input("What would you like the username to be? ")
            origUser = False
        else:
            print("Sorry, the password is incorrect.")

    elif inputCommand == "change-password":
        print("This command requres superuser privileges.")
        inputPassword = input("What is your password? ")
        if inputPassword == password:
            check = True
        else:
            check = False
        if check == True:
            password = input("What would you like the password to be? ")
            origPassword = False
        else:
            print("Sorry, the password is incorrect.")

    else:
        print(" Bash: " + inputCommand + ": command not found.")
username = "terminal"
password = "pythonterminal"
while True:
    command()
