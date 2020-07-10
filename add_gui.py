from tkinter import *
from contact import Contact
import database

def clicked_add():
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    contact = Contact(name, address, phone, email)
    database.insert_contact(contact)
    add_window.destroy()

add_window = Tk()
add_window.title("Contacts")
add_window.geometry('250x150')

name_lbl = Label(add_window, text="Name")
name_lbl.grid(row=0, sticky=W, pady=(15, 0))
address_lbl = Label(add_window, text="Address")
address_lbl.grid(row=1, sticky=W)
phone_lbl = Label(add_window, text="Phone")
phone_lbl.grid(row=2, sticky=W)
email_lbl = Label(add_window, text="Email")
email_lbl.grid(row=3, sticky=W)

name_entry = Entry(add_window, width=32)
address_entry = Entry(add_window, width=32)
phone_entry = Entry(add_window, width=32)
email_entry = Entry(add_window, width=32)

name_entry.grid(row=0, column=1, pady=(15, 0))
address_entry.grid(row=1, column=1)
phone_entry.grid(row=2, column=1)
email_entry.grid(row=3, column=1)

add_btn = Button(add_window, text="Add", bg="white", fg="black", width=20, command=clicked_add)
add_btn.grid(row=4, column=1, pady=15)

add_window.mainloop()
