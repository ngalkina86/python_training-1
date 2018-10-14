from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="firstname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New contact")
    app.contact.modify_contact_by_index(index,contact)
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_middlename(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(middlename="middlename"))
    #app.contact.modify_first_contact(Contact(middlename="New middlename"))