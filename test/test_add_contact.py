# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app,db, check_ui):
    #contact = json_contacts
    old_contacts = db.get_contact_list()
    contact = Contact(firstname ="dsad", middlename ="fdsf", lastname ="vcxv", nickname ="fdsff", title ="vcxv", company="vcxv", address ="bvcbb", home ="bvcb", mobile ="cxzc", work ="test",
                               fax ="test", email = "hg", email2 = "re", email3 = "ee", homepage ="ee", bday = "17", bmonth = "December", byear = "32", aday ="15", amonth = "August", ayear ="33", address_2 = "fd",
                               phone_2 = "gfd", notes = "gfd")
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.group.get_contact_list(),key = Contact.id_or_max)




