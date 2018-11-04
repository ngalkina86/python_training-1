from model.contact import Contact
import time
from random import randrange
import random

def test_del_some_contact(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname ="firstname"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(1)
    new_contacts = db.get_contact_list()
    assert len (old_contacts) -1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.group.get_contact_list(),key = Contact.id_or_max)


