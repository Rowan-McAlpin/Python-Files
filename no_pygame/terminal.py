username = "default"
password = "pythonterminal"

print("This program is copyright of Mcalpin Programming, Inc.")
print("The default password is 'pythonterminal'.")
print("Type 'help' for a list of commands.")
print("")

def CLIcommand():
    def command():
        inputCommand = input(username + "@pythonterminal:~ $ ")
        
        if inputCommand == "exit":
            quit()
        
        elif inputCommand == "print-data":
            print(" Your name is " + username + ".")
        
        elif inputCommand == "help":
            print(" The commands you can use are:")
            print("     exit - quit the terminal - Once typed, hit enter 2 times.")
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
                check = "correct"
            else:
                check = "incorrect"
            if password == "correct":
                userName = input("What would you like the username to be? ")
            else:
                print("Sorry, the password is incorrect.")
        
        elif inputCommand == "change-password":
            print("This command requres superuser privileges.")
            inputPassword = input("What is your password? ")
            if inputPassword == password:
                check = "correct"
            else:
                check = "incorrect"
            if check == "correct":
                password = input("What would you like the password to be? ")
            else:
                print("Sorry, the password is incorrect.")
        
        else:
            print(" Bash: " + inputCommand + ": command not found.")
    while True:
        command()
CLIcommand()
