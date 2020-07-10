import tkinter
from tkinter import ttk
import database
from contact import Contact

view_window = tkinter.Tk()
view_window.title("Contacts")
view_window.geometry('870x200')

tree = ttk.Treeview(view_window, selectmode='browse')
tree.pack(side='right')

scroll = ttk.Scrollbar(view_window, orient='vertical', command=tree.yview)
scroll.pack(side='left', fill='y')
tree.configure(yscrollcommand=scroll.set)

tree["columns"] = ("1", "2", "3", "4", "5")
tree["show"] = 'headings'

tree.column("1", width = 50, anchor ='c') 
tree.column("2", width = 200, anchor ='se') 
tree.column("3", width = 200, anchor ='se') 
tree.column("4", width = 200, anchor ='se') 
tree.column("5", width = 200, anchor ='se') 

tree.heading("1", text='ID')
tree.heading("2", text='Name')
tree.heading("3", text='Address')
tree.heading("4", text='Phone')
tree.heading("5", text='Email')

contact_list = database.all_contacts()   
 
count = 0
for contact in contact_list:
    tree.insert('', count, values=(contact.get_id(),  
                contact.get_name(), contact.get_address(), 
                contact.get_phone(), contact.get_email()))
    count+=1
    
view_window.mainloop()



