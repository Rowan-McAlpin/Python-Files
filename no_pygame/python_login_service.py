# Define the functions used in the program ('createUser()', 'checkPassword()', and 'checkPin()'):
# checkPassword()

def checkUser() {
  def checkPassword() {
    #Check the password:
    if password = newPassword {
    print("Your favorite thing is " + fave)
  } else {
    print("Login is incorrect. :-(")
    quit()
  }
  }
  # checkPin()
  def checkPin {
    #Check the pin:
  }
}

#createUser()
def createUser() {
  newUsername = input("To create a user, type your username. Don't use your real name! ")
  newPassword = input("Now for your password. It should be at least 8 characters long. ")
  fave = input("What is your favorite thing? ")
}


# Startup (Get input):
  username = input("Username: ")
  password = input("Password: (Leave blank if you use a pin.) ")

# If user uses a pin, get that instead:
  if password = "" {
    pin = input("What is your pin, then? ")
  } elif password = " " {
    pin = input("What is your pin, then? ")
  }

  if password != "" {
    usePassword = True
  } elif password != " " {
    usePassword = True
  } else {
    usepassword = False
  }

# Check the password / pin:

  if usepassword = True {
    checkPassword()
     if loginCorrect = True {
      
    } else {
      newUser()
    }
  } else {
    checkPin()
    if loginCorrect = True {
      
    } else {
      newUser()
    }
  }
  
