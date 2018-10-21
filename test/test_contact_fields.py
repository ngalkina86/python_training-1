from model.contact import Contact
import re
from random import randrange

def test_contact_fields_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="firstname",lastname = "lastname", address= "address", home = "home",
                                   mobile = "mobile", work = "work", phone_2 = "phone_2", email = "email", email2 = "email2",
                                   email3= "email3"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


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
