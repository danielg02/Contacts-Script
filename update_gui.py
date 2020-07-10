from tkinter import *
from contact import Contact
import database

class UpdateGUI:
    def __init__(self, contact, id):
        self.id = id
        self.name = contact.get_name()
        self.address = contact.get_address()
        self.phone = contact.get_phone()
        self.email = contact.get_email()

        self.window = Tk()
        self.window.title("Contacts")
        self.window.geometry('250x150')

        self.name_lbl = Label(self.window, text="Name")
        self.name_lbl.grid(row=0, sticky=W, pady=(15, 0))
        self.address_lbl = Label(self.window, text="Address")
        self.address_lbl.grid(row=1, sticky=W)
        self.phone_lbl = Label(self.window, text="Phone")
        self.phone_lbl.grid(row=2, sticky=W)
        self.email_lbl = Label(self.window, text="Email")
        self.email_lbl.grid(row=3, sticky=W)

        self.name_entry = Entry(self.window, width=32)
        self.address_entry = Entry(self.window, width=32)
        self.phone_entry = Entry(self.window, width=32)
        self.email_entry = Entry(self.window, width=32)

        self.name_entry.insert(0, contact.get_name())
        self.address_entry.insert(0, contact.get_address())
        self.phone_entry.insert(0, contact.get_phone())
        self.email_entry.insert(0, contact.get_email())

        self.name_entry.grid(row=0, column=1, pady=(15, 0))
        self.address_entry.grid(row=1, column=1)
        self.phone_entry.grid(row=2, column=1)
        self.email_entry.grid(row=3, column=1)

        self.add_btn = Button(self.window, text="Update", bg="white", fg="black", width=20, command=self.clicked_update)
        self.add_btn.grid(row=4, column=1, pady=15)

        self.window.mainloop()

    def clicked_update(self):
        self.name = self.name_entry.get()
        self.address = self.address_entry.get()
        self.phone = self.phone_entry.get()
        self.email = self.email_entry.get()
        contact = Contact(self.name, self.address, self.phone, self.email)
        database.update_contact(self.id, contact)
        self.window.destroy()

