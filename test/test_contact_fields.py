from model.contact import Contact
import re
from random import randrange

def test_contact_fields_on_home_page(app,db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="firstname",lastname = "lastname", address= "address", home = "home",
                                   mobile = "mobile", work = "work", phone_2 = "phone_2", email = "email", email2 = "email2",
                                   email3= "email3"))
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id= contact.id, firstname=strip(contact.firstname),
                       lastname=strip(contact.lastname), address=strip(contact.address),
                       all_phones_from_home_page=merge_phones_like_on_home_page(contact),
                       all_emails_from_home_page=merge_emails_like_on_home_page(contact))
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)

def strip(s):
    if s is not None:
        return s.strip()
    else:
        return None

def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x:clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone_2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: x.strip(),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
