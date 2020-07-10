import mysql.connector
from contact import Contact

db = mysql.connector.connect(
    host="localhost",
    user="danielg02",
    password="apple123",
    database="contacts_database"
    )

cursor = db.cursor()

def insert_contact(c):
    name = c.get_name()
    address = c.get_address()
    phone = c.get_phone()
    email = c.get_email()
    cursor.execute("INSERT INTO contacts (name, address, phone, email) VALUES (%s,%s,%s,%s)", (name, address, phone, email))
    db.commit()

def delete_contact(id):
    cursor.execute("DELETE FROM `contacts` WHERE id=%s", (id, ))
    db.commit()

def update_contact(id, c):
    pass

def clear_contacts():
    cursor.execute("DELETE FROM contacts")
    db.commit()

def all_contacts():
    cursor.execute("SELECT * FROM contacts")
    return cursor



