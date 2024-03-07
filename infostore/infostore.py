from customtkinter import *

# Define the UserDatabase class for managing user data
class UserDatabase:
    def __init__(self):
        self.users = {}  # Initialize user dictionary

    def add_user(self, username, password):
        if username not in self.users:  # Check if username already exists
            self.users[username] = password  # Add new user
            return True
        else:
            return False

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username] == password:  # Check if username and password match
            return True
        else:
            return False

    def get_registered_users(self):
        return list(self.users.keys())  # Return list of registered usernames

# Function to create the main window
def create_main_window():
    main_window = CTk()  # Create main window
    main_window.geometry("500x400")  # Set window size
    main_window.title("NVR MAIN")  # Set window title
    main_window.resizable(False, False)  # Disable window resizing
    main_window.iconbitmap("lgo.ico")  # Set window icon

    frame = CTkFrame(master=main_window, fg_color="#000000", border_color="#30004a", border_width=3.5)  # Create frame
    frame.pack(fill="both", expand=True)  # Pack frame into main window
    
    return main_window, frame  # Return main window and frame

# Function to handle login or registration
def login_or_register():
    username = entry.get()  # Get username input
    password = entry2.get()  # Get password input
    if db.authenticate_user(username, password):  # Check user authentication
        print("Login successful")  # Print login success message
        main_window, frame = create_main_window()  # Create main window and frame
        users = db.get_registered_users()  # Get list of registered users
        for user in users:  # Iterate over registered users
            user_label = CTkLabel(master=frame, text=user)  # Create label for each user
            user_label.pack(anchor="w", padx=10, pady=5)  # Pack label into frame
        app.destroy()  # Destroy login window
        main_window.mainloop()  # Run main window loop
    else:
        print("Invalid username or password")  # Print invalid login message

# Function to handle user registration
def register_user():
    username = entry.get()  # Get username input
    password = entry2.get()  # Get password input
    if db.add_user(username, password):  # Attempt to register user
        print("User registered successfully")  # Print registration success message
    else:
        print("Username already exists")  # Print registration failure message

# Create application instance
app = CTk()
app.geometry("200x230")  # Set application size
app.resizable(False, False)  # Disable application resizing
app.iconbitmap("lgo.ico")  # Set application icon
app.title("NVR LOGIN")  # Set application title

# Create user database instance
db = UserDatabase()

# Create frame for UI elements
frame = CTkFrame(master=app, fg_color="#000000", border_color="#30004a", border_width=3.5)
frame.pack(expand=True)  # Pack frame into application

# Create UI elements: label, entry fields, and buttons
label = CTkLabel(master=frame, text="Login Or Register")
entry = CTkEntry(master=frame, placeholder_text="Username", fg_color="#000000")
entry2 = CTkEntry(master=frame, placeholder_text="Password", fg_color="#000000")
btn_login = CTkButton(master=frame, text="Login", fg_color="#30004a", command=login_or_register)
btn_register = CTkButton(master=frame, text="Register", fg_color="#30004a", command=register_user)

# Pack UI elements into frame
label.pack(anchor="s", expand=True, pady=10, padx=30)
entry.pack(anchor="s", expand=True, pady=10, padx=30)
entry2.pack(anchor="s", expand=True, pady=10, padx=30)
btn_login.pack(anchor="n", expand=True, pady=10, padx=20)
btn_register.pack(anchor="n", expand=True, pady=10, padx=20)

app.mainloop()  # Run application loop

