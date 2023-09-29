'''
We want a phonebook which holds our contacts
'''
class PhoneBook():
    def __init__(self):
        self.contact_list = []

    def add(self,contact):
        self.contact_list.append(contact)

    def open_phonebook(self):
        return self.contact_list


class Contact():
    def __init__(self, name, number):
        self.name = name
        self.number = number