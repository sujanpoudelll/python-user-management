## Python User Management System

A beginner-level Python project focused on **file handling**, **data validation**, **password security**, and a **menu-driven interface**. Users are stored in a JSON file (`users.json`) with unique IDs, and you can **add, view, search, update, and delete users**.

### Features
- Add users with unique **ID**, **name**, **email**, **age**, and **phone number**  
- View all users with a formatted display  
- Search users by **name**, **email**, or **phone number**  
- Update user details (name, email, age, phone number)  
- Only **admins** can delete users  
- Delete users with **confirmation**  
- Input validation (e.g., age must be an integer ≥18)  
- Persistent storage using `users.json`  
- Program checks if the user is **admin** or **user** during login  
- **Password hashing** to avoid storing plain-text passwords  
- **Hidden password input** for added security  
- **Role-based menu visibility** (admin sees delete option, user does not)

### Purpose
This project was created during my Python learning journey to practice **real-world programming concepts**, including:  

- File handling with JSON  
- Input validation  
- Menu-driven CLI  
- CRUD operations (Create, Read, Update, Delete)  
- Password hashing and security  
- Writing reusable helper functions  

### Updates in this version
- Improved **Command-Line Interface (CLI)** for better readability  
- Users are now automatically **sorted by name** when displayed  
- Added **email duplication check** when adding or updating a user  
- Added **password hashing** to secure user credentials  
- Added **hidden password input** while typing
- Added **login attempt limit with temporary block**   
- Implemented **role-based menu** visibility  

### Author
***Sujan Poudel***  
Bachelor’s in Software Engineering  
Beginner Python Developer
