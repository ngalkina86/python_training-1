from model.contact import Contact
from random import randrange
import random

def test_modify_contact_firstname(app,db,check_ui):
    #contact = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname ="firstname"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    id = contact.id
    old_contacts.remove(contact)
    new_contact = Contact(firstname="New contact")
    old_contacts.append(new_contact)
    app.contact.modify_contact_by_id(id,new_contact)
    new_contact.id = contact.id
    new_contact.lastname = contact.lastname
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.group.get_contact_list(),key = Contact.id_or_max)

#def test_modify_contact_middlename(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(middlename="middlename"))
    #app.contact.modify_first_contact(Contact(middlename="New middlename"))