import customtkinter as ctk
import tkinter as tk
import sqlite3
import re


# --- LOGIN FRAME ---
class LoginFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # House-Keeping stuff
        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)
        self.master = master
        self.hidden = 1

        # defining variables
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        # defining labels
        self.status = ctk.CTkLabel(self, text="Status: Normal", font=self.font, corner_radius=25)
        self.header = ctk.CTkLabel(self, text="LOGIN", font=self.header_font, corner_radius=25)
        self.user_label = ctk.CTkLabel(self, text="Username: ", font=self.font)
        self.pass_label = ctk.CTkLabel(self, text="Password: ", font=self.font)

        # entry widgets with cool masking feature
        self.username_entry = ctk.CTkEntry(self, textvariable=self.user_var, font=self.font, corner_radius=25)
        self.password_entry = ctk.CTkEntry(self, textvariable=self.pass_var, font=self.font, show="*", corner_radius=25)
        self.show_password = ctk.CTkButton(self, text="Show", font=self.font, command=self._show_password, corner_radius=25, width=10)
        self.submit = ctk.CTkButton(self, text="Submit", font=self.font, command=lambda: self._login(), corner_radius=25)

        # LoginFrame's database methods
        self.connection = sqlite3.connect("bank_storage.db")
        self.cursor = self.connection.cursor()

        self.header.place(x=500, y=0)
        self.user_label.place(x=400, y=100)
        self.username_entry.place(x=500, y=100)
        self.pass_label.place(x=400, y=175)
        self.password_entry.place(x=500, y=175)
        self.show_password.place(x=650, y=175)
        self.submit.place(x=500, y=250)
        self.status.place(x=500, y=325)

    def _show_password(self):
        if self.hidden == 1:
            self.password_entry.configure(show="")
            self.hidden = 0
        else:
            self.password_entry.configure(show="*")
            self.hidden = 1

    def _login(self, *args, **kwargs):
        if len(self.user_var.get()) == 0 or len(self.pass_var.get()) == 0:
            self.status.configure(text="Status: Invalid")
        else:
            self.status.configure(text="Status: Valid")
            user_temp: str = self.user_var.get()
            pass_temp: str = self.pass_var.get()
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            print(f"Username: {user_temp}\nPassword: {pass_temp}")


# --- Register Frame ---
class RegisterFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # House-Keeping Stuff
        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)
        self.master = master
        self.hidden = 1

        # defining variables
        self.user_reg_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        # entry widgets with cool masking feature
        self.username_entry = ctk.CTkEntry(self, textvariable=self.user_reg_var, font=self.font, corner_radius=25)
        self.password_entry = ctk.CTkEntry(self, textvariable=self.pass_var, font=self.font, show="*", corner_radius=25)
        self.email_entry = ctk.CTkEntry(self, textvariable=self.email_var, font=self.font, corner_radius=25)
        self.show_password = ctk.CTkButton(self, text="Show", font=self.font, command=self._show_password, corner_radius=25, width=10)
        self.submit = ctk.CTkButton(self, text="Submit", font=self.font, command=lambda: self._register(), corner_radius=25)

        # defining labels
        self.status = ctk.CTkLabel(self, text="Status: Normal", font=self.font, corner_radius=25)
        self.header = ctk.CTkLabel(self, text="REGISTER", font=self.header_font, corner_radius=25)
        self.user_label = ctk.CTkLabel(self, text="Username: ", font=self.font)
        self.pass_label = ctk.CTkLabel(self, text="Password: ", font=self.font)
        self.email_label= ctk.CTkLabel(self, text="Email: ", font=self.font)

        # LoginFrame's database methods
        self.connection = sqlite3.connect("bank_storage.db")
        self.cursor = self.connection.cursor()

        self.header.place(x=500, y=0)
        self.user_label.place(x=400, y=100)
        self.username_entry.place(x=500, y=100)
        self.email_label.place(x=400, y=175)
        self.email_entry.place(x=500, y=175)
        self.pass_label.place(x=400, y=250)
        self.password_entry.place(x=500, y=250)
        self.show_password.place(x=650, y=250)
        self.submit.place(x=500, y=325)
        self.status.place(x=500, y=400)


    def _show_password(self):
        if self.hidden == 1:
            self.password_entry.configure(show="")
            self.hidden = 0
        else:
            self.password_entry.configure(show="*")
            self.hidden = 1

    def _register(self, *args, **kwargs):
        if len(self.user_reg_var.get()) == 0 or len(self.pass_var.get()) == 0 or len(self.email_var.get()) == 0:
            self.status.configure(text="Status: Invalid Entry")
        else:
            if self._is_valid_email(self.email_var.get()):
                print(f"Username: {self.user_reg_var.get()}")
                print(f"Email: {self.email_var.get()}")
                print(f"Password: {self.pass_var.get()}")
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
            else:
                self.status.configure(text="Status: Invalid Email")

    def _is_valid_email(self, email: str) -> bool:
        email_validation = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        match = re.match(email_validation, email)
        return bool(match)


if __name__ == "__main__":
    test = ctk.CTk()

    login = LoginFrame(master=test)
    register = RegisterFrame(master=test)

    test.geometry("1072x603")

    # login.pack(expand=True, fill=tk.BOTH)
    register.pack(expand=True, fill=tk.BOTH)

    test.mainloop()
