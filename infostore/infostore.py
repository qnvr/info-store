from customtkinter import *


class UserDatabase:
    def __init__(self):
        self.users = {}  # Dictionary to store user data {username: password}

    def add_user(self, username, password):
        if username not in self.users:
            self.users[username] = password
            return True
        else:
            return False

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False

    def get_registered_users(self):
        return list(self.users.keys())


def create_main_window():
    main_window = CTk()
    main_window.geometry("500x400")
    main_window.title("NVR MAIN")
    main_window.resizable(False, False)
    main_window.iconbitmap("lgo.ico")

    frame = CTkFrame(master=main_window, fg_color="#000000", border_color="#30004a", border_width=3.5)
    frame.pack(fill="both", expand=True)
    
    return main_window, frame


def login_or_register():
    username = entry.get()
    password = entry2.get()
    if db.authenticate_user(username, password):
        print("Login successful")
        main_window, frame = create_main_window()
        users = db.get_registered_users()
        for user in users:
            user_label = CTkLabel(master=frame, text=user)
            user_label.pack(anchor="w", padx=10, pady=5)
        app.destroy()
        main_window.mainloop()
    else:
        print("Invalid username or password")


def register_user():
    username = entry.get()
    password = entry2.get()
    if db.add_user(username, password):
        print("User registered successfully")
    else:
        print("Username already exists")


app = CTk()
app.geometry("200x230")
app.resizable(False, False)
app.iconbitmap("lgo.ico")
app.title("NVR LOGIN")

db = UserDatabase()  # Creating an instance of UserDatabase

frame = CTkFrame(master=app, fg_color="#000000", border_color="#30004a", border_width=3.5)
frame.pack(expand=True)

label = CTkLabel(master=frame, text="Login Or Register")
entry = CTkEntry(master=frame, placeholder_text="Username", fg_color="#000000")
entry2 = CTkEntry(master=frame, placeholder_text="Password", fg_color="#000000")
btn_login = CTkButton(master=frame, text="Login", fg_color="#30004a", command=login_or_register)
btn_register = CTkButton(master=frame, text="Register", fg_color="#30004a", command=register_user)

label.pack(anchor="s", expand=True, pady=10, padx=30)
entry.pack(anchor="s", expand=True, pady=10, padx=30)
entry2.pack(anchor="s", expand=True, pady=10, padx=30)
btn_login.pack(anchor="n", expand=True, pady=10, padx=20)
btn_register.pack(anchor="n", expand=True, pady=10, padx=20)

app.mainloop()
