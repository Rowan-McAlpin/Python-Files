# Define the functions used in the program
# ('createUser()', 'checkPassword()', and 'checkPin()'):
# checkPassword()
print("This program is copyright of Mcalpin Programming, Inc.")
print("The default password is 'pythonterminal'.")
print("Type 'help' for a list of commands.")
print("")


def login(data):
    username = input('Username: ')
    if data['username'] == username:
        password = input('Password: ')
        if data['password'] == password:
            return True
        else:
            print('Password incorrect. Please try again.')
            return False
    else:
        print('Username incorrect. Please try again.')
        return False

if login(data):
    
    def command(data):
        input_command = input(data['username'] + "@pythonterminal:~ $ ")
        if input_command == "exit":
            quit()
            
        elif input_command == "print-data":
            print(" Your name is " + data['username'] + ".")
            
        elif input_command == "help":
            print(" The commands you can use are:")
            print("     exit - quit the terminal - This doesn't work in MU 1.0.2.")
            print("     help - opens the help page")
            print("     print-data - View your data")
            print("     change-user - Change the username")
            print("     change-password - Change the password")
            print("     sudo change-user - Change the username, but this time it'll work")
            print("     sudo change-password - Change the password, but this time it'll work")
    
        elif input_command == "":
            return False
            
        elif input_command == "change-user":
            print("Needs to be sudo. Try sudo change-user.")
    
        elif input_command == "change-password":
            print("Needs to be sudo. Try sudo change-password.")
        
        elif input_command == "sudo change-user":
            print("This command requires superuser privileges.")
            if login(data):
                result = data
                result['username'] = input(
                    "What would you like the username to be? ")
                return result
            else:
                print("Sorry, the password is incorrect.")
        elif input_command == "sudo change-password":
            print("This command requres superuser privileges.")
            if login(data):
                result = data
                result['password'] = input(
                    "What would you like the password to be? ")
                return result
            else:
                print("Sorry, the password is incorrect.")
        else:
            print(" Bash: " + input_command + ": command not found.")
        return False

else:
    def command(data):
        input_command = input(data['username'] + "@pythonterminal:~ $ ")
        if input_command == "exit":
            quit()
            
            
        elif input_command == "help":
            print(" The commands you can use are:")
            print("     exit - quit the terminal - This doesn't work in MU 1.0.2.")
            print("     help - opens the help page")
    
        elif input_command == "":
            return False
        
        else:
            print(" Bash: " + input_command + ": command not found.")
        return False

data = {
    'username': 'terminal',
    'password': 'pythonterminal'
}
while True:
    changes = command(data)
    if changes:
        data = changes
