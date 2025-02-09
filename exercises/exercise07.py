# Create a class named User with attributes: name, age, and email address.
# Initialize an empty list users to store all user objects.
#
# When the program runs, present two options:
#
# 1-Signup: Allow users to create a new User object and save it in the list.
# 2-Show All Users: Print all users stored in the list. for example:
# 01-name: Matin - age: 20 - email: example@gmail.com
# 3-exit
#
# At the beginning of the project, initialize the list of users: users = [].
#
# If the user chooses option 1, prompt for user details (name, age, email) and save the new user in the list.
#
# If the user chooses option 2, display all users in the specified format.
#
# The program should continue running until the user decides to exit.


"""
add username and password to sign up process 
add login functionality
store classes and functions in a different file and import them here
use a database to store users (sqlite3)
clean code
"""
from models.user import User


users: list[User] = []

def signup():
    name = input("Enter your name: ")
    age = input("enter your age: ")
    email = input("Enter your email: ")
    new_user: User = User(name, age, email)
    users.append(new_user)
    print("You are registered successfully!\n")

def show_all_users():
    if len(users) == 0:
        print("NO USER")
    else:
        for user in users:
            print(user)

def main():
    while True:
        print("Menu: ")
        print("1. signup")
        print("2. Show All Users")
        print("3. Exit")

        option = int(input("Choose an option: "))
        if option == 1:
            signup()

        elif option == 2:
            show_all_users()

        elif option == 3:
            print("Goodbye")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()