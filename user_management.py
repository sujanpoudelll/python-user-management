# Beginner-level Python project
# Focus: file handling, validation, menu-driven program
# Written during early learning stage



def get_valid_age(allow_blank = False, current_age = None):
    while True:   
                try:
                    age_input = input("Enter age: ")

                    if allow_blank and age_input =="":
                        return current_age
                    age = int(age_input)

                    if age <= 0:
                        print("Age can't be negative or zero !")

                    elif age < 18:
                        print("Age need to be atleast 18 !")
                        
                    else:
                        return age
                        
                except ValueError:
                    print("Age should be an integer !")

def save_users(users):
    with open("user_management.txt","w") as file:
            for user in users:
                file.write(f"{user['name']}:{user['email']}:{user['age']}\n")

def add_users():
    """Add a new user to the file with validation."""
    try:
        with open("user_management.txt","a") as file:
            name = input("Enter name: ")
            email = input("Enter email: ")

            if not name or not email:
                print("Name and email cannot be empty!")
                return
            
            age = get_valid_age()

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
    """Search user by name or email."""

    users = load_users()

    if not users:
        print("No users found.")
        return

    found = False
    keyword = input("Enter name or email to search: ").lower().strip()
    if not keyword:
        print("Please enter a valid name or email!")
        return
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
    """Update users data and store ."""
    users = load_users()

    if not users:
        print("No users found.")
        return

    keyword = input("Enter name or email to update: ").lower().strip()
    if not keyword:
        print("Please enter a valid name or email!")
        return
    
    updated = False
    for user in users:
        if keyword in user["name"].lower() or keyword in user["email"].lower():
            print("USER FOUND !\n")
            print(f"Current Name: {user['name']} \n")
            print(f"Current Email: {user['email']} \n")
            print(f"Current Age: {user['age']} \n")
            
            new_name = input("Enter new name (leave blank to keep same): ")
            new_email = input("Enter new email (leave blank to keep same): ")
            new_age = get_valid_age(allow_blank=True, current_age=user["age"])
            
            if new_name:
                user["name"] = new_name
            if new_email: 
                user["email"] = new_email
            user["age"]= new_age

            save_users(users)
            print("User updated successfully!")
            updated = True
            break

    if not updated:
        print("No matching user found !")
               
def delete_users():
    """Delete a user."""
    users = load_users()

    if not users:
        print("No users found.")
        return
    found = False
    keyword = input("Enter name or email to delete: ").lower().strip()
    if not keyword:
        print("Please enter a valid name or email!")
        return
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
                    save_users(users)
                    print("User deleted successfully !")
                    break
                    
                elif confirm == "n":
                    print("User deletion cancelled !")
                    break
                else:
                    print("Invalid entry ! Please enter 'y' or 'n'.")
            found = True
            

    if not found:                
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
            
            option = int(input("Select an option (1-6): "))

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
                while True:
                    exit_confirm = input("Are you sure you want to exit? (y/n): ").lower()
                    if exit_confirm == "y":
                        print("\nThank You !")
                        return
                    elif exit_confirm =="n":
                        break
                    else:
                        print("Invalid entry ! Please enter 'y' or 'n'.")
            
                
            else:
                print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"Error:{e}")

# Program entry point
main_menu()







