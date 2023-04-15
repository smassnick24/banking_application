from UserClasses import RegisterFrame, LoginFrame
from BankClasses import ViewAccountFrame, RegisterBankAccountFrame
import customtkinter as ctk
import tkinter as tk
import ttkbootstrap


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Banking with Sam")
        self.geometry("1072x603")
        self.configure(theme="dark")

        self.menu_bar = tk.Menu(master=self, tearoff=0)
        self.configure(menu=self.menu_bar)
        self.options_menu = tk.Menu(master=self.menu_bar, tearoff=0)
        self.options_menu.add_cascade(label="Login", command=self.load_user_login)
        self.options_menu.add_cascade(label="Register", command=self.load_user_register)
        self.options_menu.add_separator()
        self.options_menu.add_cascade(label="View Account", command=self.load_bank_view)
        self.options_menu.add_cascade(label="Register Bank Account", command=self.load_bank_register)

        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, fill=ctk.BOTH)

        # defining the frames of the GUI
        self.user_register = RegisterFrame(self.container)
        self.user_login = LoginFrame(self.container)
        self.bank_view = ViewAccountFrame(self.container)
        self.bank_register = RegisterBankAccountFrame(self.container)

    def load_user_login(self):
        self.user_login.pack(fill=ctk.BOTH, expand=True)
        self.user_register.pack_forget()
        self.bank_view.pack_forget()
        self.bank_register.pack_forget()

    def load_user_register(self):
        self.user_register.pack(fill=ctk.BOTH, expand=True)
        self.user_login.pack_forget()
        self.bank_view.pack_forget()
        self.bank_register.pack_forget()

    def load_bank_view(self):
        self.bank_view.pack(fill=ctk.BOTH, expand=True)
        self.user_register.pack_forget()
        self.user_login.pack_forget()
        self.bank_register.pack_forget()

    def load_bank_register(self):
        self.bank_register.pack(fill=ctk.BOTH, expand=True)
        self.user_register.pack_forget()
        self.bank_view.pack_forget()
        self.user_login.pack_forget()


if __name__ == '__main__':
    t = GUI()
    t.mainloop()
