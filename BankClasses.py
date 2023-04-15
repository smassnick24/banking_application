import customtkinter as ctk
import tkinter as tk


class RegisterBankAccountFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)

        self.header = ctk.CTkLabel(self, text="REGISTER ACCOUNT", font=self.header_font)

        self.switch = ctk.CTkButton(self, text="Register Account", corner_radius=10)

        self.header.pack()
        self.switch.pack()


class ViewAccountFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)

        self.header = ctk.CTkLabel(self, text="ACCOUNT", font=self.header_font)
        self.account_label = ctk.CTkLabel(self, text="Account Number: ", font=self.font)
        self.routing_label = ctk.CTkLabel(self, text="Routing Number: ", font=self.font)
        self.account_type_label = ctk.CTkLabel(self, text="Account Type: ", font=self.font)
        self.balance_label = ctk.CTkLabel(self, text="Balance: ")
        self.switch = ctk.CTkButton(self, text="Register Account", corner_radius=10)

        self.header.place(x=450, y=0)
        self.account_label.place(x=400, y=100)
        self.routing_label.place(x=400, y=175)
        self.account_type_label.place(x=400, y=250)
        self.balance_label.place(x=400, y=325)
        self.switch.place(x=400, y=400)

    def _display_data(self, account, routing, acct_type, balance):
        self.account_label.configure(text=f"Account Number: {account}")
        self.routing_label.configure(text=f"Routing Number: {routing}")
        self.account_type_label.configure(text=f"Account Type: {acct_type}")
        self.balance_label.configure(text=f"Balance: {balance:.2f}")


if __name__ == '__main__':
    test = ctk.CTk()
    view = ViewAccountFrame(master=test)

    test.geometry("1072x603")

    view.pack(expand=True, fill=ctk.BOTH)

    test.mainloop()
