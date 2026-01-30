# Beginner-level Python project
# Focus: file handling, validation, menu-driven program
# Written during early learning stage



def add_users():
    """Add a new user to the file with validation."""
    try:
        with open("user_management.txt","a") as file:
            name = input("Enter name: ")
            email = input("Enter email: ")

            #Validate age
            while True:   
                try:
                    age = int(input("Enter age: "))
                    if age <= 0:
                        print("Age can't be negative or zero !")

                    elif age < 18:
                        print("Age need to be atleast 18 !")
                        
                    else:
                        break

                except ValueError:
                    print("Age should be an integer !")
                    
            
            file.write(f"{name}:{email}:{age}\n")
            print("User added successfully!")
            

    except Exception as error:
        print(f"Error while adding user:", error)   

def view_users():
    """Read and display all users from the file."""
    try:
        with open("user_management.txt","r") as file:
            users = file.readlines()

       


       
        print("\n**********USER DETAILS**********")
        count = 1
        for data in users:

            name, email, age = data.strip().split(":")
            print(f"{count}.\nName: {name}\nEmail: {email}\nAge: {age}\n")
            count += 1

    except FileNotFoundError:
        print("No users or file found yet! Please add.")


def main_menu():       

    """Main menu loop."""

    while True:
        try:
            
            print("#######USER MANAGEMENT SYSTEM########")
            print("1. ADD USERS")
            print("2. VIEW USERS")
            print("3. EXIT")
            
            option = int(input("Select an option (1, 2, 3): "))

            if option == 1:
                add_users()
                
            elif option == 2:
                view_users()
                
            elif option == 3:
                print("\nThank You !")
                break
                
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"Error:{e}")


# Program entry point
main_menu()

