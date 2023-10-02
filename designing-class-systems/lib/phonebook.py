'''
We want a phonebook which holds our contacts
'''
class PhoneBook():
    def __init__(self):
        self.contact_list = []

    def add(self,contact):
        self.contact_list.append(contact)

    def open_phonebook(self):
        return '\n\n'.join([contact.format_contact() for contact in self.contact_list])
    
    def get_number(self, name):
        #compares input name with name in contact
        #returns a list of contact names which match and their numbers
        return


class Contact():
    def __init__(self, name, number):
        if not number.isnumeric() :
            raise ValueError("The phone number must have only numeric digits.")
        
        if len(number) != 11 :
            raise ValueError("The phone number must have 11 digits.")
        self.name = name
        self.number = number
        
    def format_contact(self):
        return f'{self.name}: {self.number}'