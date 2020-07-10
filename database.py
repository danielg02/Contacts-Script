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
    name = c.get_name()
    address = c.get_address()
    phone = c.get_phone()
    email = c.get_email()
    cursor.execute ("""
                    UPDATE contacts
                    SET name=%s, address=%s, phone=%s, email=%s
                    WHERE id=%s
                    """, (name, address, phone, email, id))
    db.commit()

def get_contact(id):
    cursor.execute("SELECT * FROM contacts WHERE id=%s", (id, ))
    row = cursor.fetchall()
    return Contact(row[0][1], row[0][2], row[0][3], row[0][4], row[0][0])

def clear_contacts():
    cursor.execute("DELETE FROM contacts")
    db.commit()

def all_contacts():
    contact_list = []
    cursor.execute("SELECT * FROM contacts")
    for row in cursor.fetchall():
        contact_id = row[0]
        contact_name = row[1]
        contact_address = row[2]
        contact_phone = row[3]
        contact_email = row[4]
        contact_list.append(Contact(contact_name, contact_address,
                    contact_phone, contact_email, contact_id))
    return contact_list
    


