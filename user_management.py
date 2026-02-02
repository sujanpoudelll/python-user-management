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
        

        if not users:
            print("No users found.")
            return

        print("\n**********USER DETAILS**********")
        count = 1
        for data in users:

            name, email, age = data.strip().split(":")
            print(f"{count}.\nName: {name}\nEmail: {email}\nAge: {age}\n")
            count += 1

    except FileNotFoundError:
        print("No users or file found yet! Please add.")




def load_users():
    """Load all users from the file."""
    users = []
    try:
        with open("user_management.txt","r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) != 3:
                    continue

                name, email, age = parts
                users.append({
                    "name":name,
                    "email":email,
                    "age":int(age),

                })

    except FileNotFoundError:
        print("File Not Found !")
    
    return users



def search_users():
    """Load and display specific users by using name or email."""

    users = load_users()

    if not users:
        print("No users found.")
        return


    found = False
    keyword = input("Enter name or email to search: ").lower().strip()
    for user in users:
        if keyword in user["name"].lower() or keyword in user["email"].lower():
            print("\nUSER FOUND !\n")
            print(f"Name: {user['name']} \n")
            print(f"Email: {user['email']} \n")
            print(f"Age: {user['age']} \n")
            found = True
    if not found:
        print("No Matched User Found !")



def update_users():
    """Load and update users data and store ."""
    users = load_users()

    if not users:
        print("No users found.")
        return

    keyword = input("Enter name or email to update: ").lower().strip()
    updated = False
    for user in users:
        if keyword in user["name"].lower() or keyword in user["email"].lower():
            print("USER FOUND !\n")
            print(f"Current Name: {user['name']} \n")
            print(f"Current Email: {user['email']} \n")
            print(f"Current Age: {user['age']} \n")
            
            new_name = input("Enter new name (leave blank to keep same): ")
            new_email = input("Enter new email (leave blank to keep same): ")
            while True:   
                    
                    new_age = (input("Enter age (leave blank to keep same): "))

                    if new_age == "":
                        new_age = user["age"]
                        break
                                       
                    try:
                        new_age = int(new_age)

                        if new_age <= 0:
                            print("Age can't be negative or zero !")

                        elif new_age < 18:
                            print("Age need to be atleast 18 !")
                            
                        else:
                            break

                    except ValueError:
                        print("Age should be an integer !")
            

            if new_name:
                user["name"] = new_name
            if new_email: 
                user["email"] = new_email
            user["age"]= new_age
            

            updated = True
            break

    if not updated:
        print("No matching user found.")
    
    else:
            
        with open("user_management.txt","w") as file:
            for user in users:
                file.write(f"{user['name']}:{user['email']}:{user['age']}\n")

        print("User updated successfully!")



def delete_users():
    """Delete users data."""
    users = load_users()

    if not users:
        print("No users found.")
        return
    
    keyword = input("Enter name or email to delete: ").lower().strip()
    deleted = False
    for user in users:
        if keyword in user["name"].lower() or keyword in user["email"].lower():
            print("USER FOUND !\n")
            print(f"Name: {user['name']} \n")
            print(f"Email: {user['email']} \n")
            print(f"Age: {user['age']} \n")

            while True:
                confirm = input("Are you sure you want to delete this user? (y/n): ").lower()
                if confirm == "y":
                    users.remove(user)
                    print("User deleted successfully !")
                    deleted = True
                    break
                if confirm == "n":
                    print("User deletion cancelled !")
                    break
                else:
                    print("Invalid entry ! Please enter 'y' or 'n'.")
             

  
                
    if deleted:    
        with open("user_management.txt","w") as file:
            for user in users:
                file.write(f"{user['name']}:{user['email']}:{user['age']}\n")
    else:
        print("No matching user found !")



        
        


def main_menu():       

    """Main menu loop."""

    while True:
        try:
            
            print("#######USER MANAGEMENT SYSTEM########")
            print("1. ADD USERS")
            print("2. VIEW USERS")
            print("3. SEARCH USER")
            print("4. UPDATE USER")
            print("5. DELETE USER")
            print("6. EXIT")
            
            option = int(input("Select an option (1, 2, 3, 4, 5, 6): "))

            if option == 1:
                add_users()
                
            elif option == 2:
                view_users()
            
            elif option == 3:
                search_users()
            
            elif option == 4:
                update_users()

            elif option == 5:
                delete_users()
                
            elif option == 6:
                print("\nThank You !")
                break
                
            else:
                print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"Error:{e}")


# Program entry point
main_menu()

