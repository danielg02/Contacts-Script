from contact import Contact
import database

def menu():
    choice = 0
    menu_choices = ('Press:' + 
                    '\n1 to add contact' +
                    '\n2 to delete contact' +
                    '\n3 to update contact' +
                    '\n4 to view all contacts' + 
                    '\n5 to clear all contacts' + 
                    '\n6 to exit\n')
    while choice not in [1, 2, 3, 4, 5, 6]:
        try:
            choice = int(input(menu_choices))
        except ValueError:
            print('Not an option!')
    return choice

def choose(choice):
    if choice == 1:
        name = input('Enter name: ')
        address = input('Enter address: ')
        phone = input('Enter phone: ')
        email = input('Enter email: ')
        c = Contact(name, address, phone, email)
        database.insert_contact(c)
    elif choice == 5:
        will_continue = check_certainty()
        if will_continue:
            database.clear_contacts()            
    elif choice == 6:
        exit()

def check_certainty():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input('Are you sure? (y/n)')
    if choice == 'y':
        return True
    else:
        return False


choose(menu())
