from model.contact import Contact
import time

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="firstname"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    time.sleep(1)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


