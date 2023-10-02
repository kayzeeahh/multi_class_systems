from lib.phonebook import *

def test_add_to_phonebook():
    phonebook = PhoneBook()
    contact = Contact("Alan", "07361913542")
    phonebook.add(contact)
    assert phonebook.contact_list == [contact]
    
def test_open_phonebook():
    phonebook = PhoneBook()
    contact = Contact("Alan", "07361913542")
    phonebook.add(contact)
    phonebook.open_phonebook()
    assert phonebook.open_phonebook() == "Alan: 07361913542"
    
def test_lemgth_of_phone_number():
    contact = Contact("Alan", "0736191354")
    
    assert contact 