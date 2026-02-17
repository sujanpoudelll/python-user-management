# Beginner-level Python project
# Focus: file handling, validation, menu-driven program
# Written during early learning stage

import json
import os
import uuid


#-------------Logging----------------------------

def log(message):
    print(f"[LOG] {message}")

def log_error(message):
    print(f"[ERROR] {message}")

#------------Helper Functions--------------------

def load_users():
    """Loads users from the file"""
    try:
        if not os.path.exists("users.json"):
            log("load_users():users.json not found, returning empty list")
            return []
        
        with open("users.json","r") as file:
            try:
                users = json.load(file)
                if users is None:
                    return[]
                users.sort(key=lambda u: u["name"].lower())
                return users
            except json.JSONDecodeError:
                log_error("load_users():users.json is corrupted")
                users = []
        return users
    except Exception as e:
        log_error(f"load_users(): {e}")
        return []
    
def add_users_to_list(users, name, email, age, phone):
    user= {
        "id":str(uuid.uuid4()),
        "name":name,
        "email":email,
        "age":age ,
        "phone":phone
    }
    users.append(user)
    return user

def save_users(users):

    """Save users list to users.json file."""
    try:
        with open("users.json","w") as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        log_error(f"save_users(): {e}")

def input_name():
    while True:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty!")
            continue
        break
    return name

def input_email(users):
    return get_valid_email(users) 

def input_phone(users,selected_user=None,allow_blank=False,current_phone=None):
   return get_valid_phone(users,selected_user,allow_blank,current_phone)
   
def email_exists(users, email):
    """Checks if email exists already or not"""
    for user in users:
        if user["email"].lower() == email.lower():
            return True
    return False        

def phone_exists(users, phone):
    """Checks if phone number exists already or not"""
    for user in users:
        if user["phone"] == phone:
            return True
    return False

def get_valid_phone(users, selected_user=None, allow_blank = False, current_phone = None):
    while True:
            phone = input("Enter phone number: ").strip()
            if allow_blank and phone=="":
                return current_phone
            if not phone:
                print("Phone number cannot be empty !")
                continue
        
            if not phone.isdigit() or len(phone) != 10:
                 print("Please enter 10-digits phone number!")
                 continue
                

            if selected_user is None:
                if phone_exists(users, phone):
                    print("Phone number already exists. Try another !")
                    continue
            else:
                if phone_exists(users,phone) and phone != selected_user["phone"]:
                    print("Phone number already exists ! Try  new one or leave blank for old  !")
                    continue

            return phone
            
def is_valid_age(age):
    return isinstance(age, int) and age>=18

def input_age(allow_blank = False,current_age = None):
    while True:
        age_input = input("Enter age: ").strip()
        if allow_blank and age_input=="":
            return current_age
        try:
            age = int(age_input)
            if is_valid_age(age):
                return age
            print("Age must be positive and greater than 17  !")

        except ValueError:
            print("Enter a number !")
           
def get_valid_email(users,selected_user=None,allow_blank = False, current_email = None):
    """Validates email"""
    while True:
            email_input = input("Enter email: ").strip()
            if allow_blank and email_input =="":
                return current_email
            if not email_input:
                print("Email cannot be empty!")
                continue
            if " " in email_input:
                print("No space allowed !")
                continue 
            if "@" not in email_input or "." not in email_input:
                print("Invalid email format ! e.g: coderguy@something.com")
                continue

            if selected_user is None:
                if email_exists(users,email_input):
                    print("Email already exists ! Try another !")
                    continue
            else:
                if email_exists(users, email_input) and email_input != selected_user["email"]:
                    print("Email already exists ! Try  new one or leave blank for old  !")
                    continue

            return email_input.lower()

def input_display(users,action):
    """Search user by keyword and display matched results"""
    
    if not users:
        return None

    keyword = input(f"Enter name or email or phone number to {action}: ").lower().strip()
    if not keyword:
        print("Please enter a valid name or email or phone number!")
        return None

    matched_user = []
    for user in users:
        if keyword in user["name"].lower() or keyword in user["email"].lower() or keyword in user["phone"]: 
            matched_user.append(user)

    if matched_user:
        print(f"\n==============={len(matched_user)} USER/S FOUND =================\n")
        count = 1
        for userfound in matched_user: 
            print("-" * 44)
            print(f"{count}.\n")
            print(f"ID: {userfound['id']}")
            print(f"Name: {userfound['name']}")
            print(f"Email: {userfound['email']}")
            print(f"Age: {userfound['age']}")
            print(f"Phone: {userfound['phone']}")
            print("-" * 44,"\n")
            count += 1
    else:
        print("No Matching User Found !")
        return None

    return matched_user
    
def choice_input(output, action): 
    """User selection for operation"""
    
    if not output:
        return None
    
    if len(output) !=1:  
            while True:
                try:    
                    choice = int(input(f"Enter the no. of user you want to {action}: "))

                    if not (1<=choice<=len(output)):
                        print("Invalid Selection. Operation Cancelled !")
                        return None
                    selected_user = output[choice -1]
                    return selected_user    
                
                except ValueError:
                    print("Please enter a valid number!")
                    continue
    else:
        return output[0]
        
def delete_input(users, selected_user):
    """Deletes the selected user"""
    
    if not selected_user:
        return None
    while True:
            confirm = input("Are you sure you want to delete this user? (y/n): ").lower()
            if confirm == "y":
                users.remove(selected_user)
                save_users(users)
                print("User deleted successfully !")
                break   
            elif confirm == "n":
                print("User deletion cancelled !")
                break
            else:
                print("Invalid entry ! Please enter 'y' or 'n'.")
                continue
    
def update_input(users,selected_user):
    """Updates the selected user"""
 
    if not selected_user:
        print("Operation cancelled.")
        return None
    print("Leave blank to keep same !")
    new_name = input("Enter new name: ").strip()
    if new_name:
        selected_user["name"] = new_name
    new_email = get_valid_email(users,selected_user,allow_blank=True,current_email=selected_user["email"])
    selected_user["email"]=new_email

    
    new_age = input_age(allow_blank = True,current_age = selected_user["age"])
    selected_user["age"]= new_age
    new_phone = input_phone(users,selected_user,allow_blank=True, current_phone= selected_user["phone"])
    selected_user["phone"] = new_phone
    save_users(users)
    print("User updated successfully!")

   
#--------------Core Functions--------------------

def add_users():
    """Add a new user with unique ID."""

    users = load_users()

    name = input_name()
    email = input_email(users)
    age = input_age(allow_blank=False)
    phone = input_phone(users)
  
    new_user = add_users_to_list(users, name, email, age, phone)
    save_users(users)
    print(f"User added successfully ! ID: {new_user['id']}")

def view_users():
    """Read and display all users from the file."""

    users = load_users()
    if not users:
        print("No users found.")
        return
    
    print("\n=============== USER LIST ==================\n")
    count = 1
    for user in users:  
        print("-" * 44)
        print(f"{count}. User Details\n")
        print(f"ID    : {user['id']}")
        print(f"Name  : {user['name']}")
        print(f"Email : {user['email']}")
        print(f"Age   : {user['age']}")
        print(f"Phone : {user['phone']}")
        print("-" * 44,"\n")
        count += 1

def search_users():
    """Search user by name or email."""
    users = load_users()
    input_display(users, "search")
    
def update_users():
    """Updates user by name or email."""

    users = load_users()
    output = input_display(users,"update")
    if not output:
        return 
    selected_user= choice_input(output, "update")
    update_input(users,selected_user)
    
def delete_users():
    """Delete a user."""

    users = load_users()
    output = input_display(users,"delete")
    if not output:
        return
    selected_user= choice_input(output, "delete")
    delete_input(users,selected_user)

#--------------Main Menu----------------------
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
                        log("main_menu(): Invalid option input.")
                        continue
            else:
                print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")
                log("main_menu(): Invalid option input.")
                
        except ValueError:
            print("Please enter a valid integer.")
            log("main_menu(): Non-numeric menu input")
        except Exception as e:
            print("Something went wrong ! Please Try Again !")
            log_error(f"main_menu(): {e}")

main_menu()





