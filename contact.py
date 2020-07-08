class Contact:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address
    
    def get_address(self):
        return self.address

    def set_phone(self, phone):
        self.phone = phone
    
    def get_phone(self):
        return self.phone

    def set_email(self, email):
        self.email = email
    
    def get_email(self):
        return self.email

    def __str__(self):
        return (str(self.name) + ', ' + str(self.address) + ', ' + 
            str(self.phone) + ', ' + str(self.email))
