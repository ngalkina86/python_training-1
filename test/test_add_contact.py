# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Contact(firstname ="", middlename ="", lastname ="", nickname ="", title ="", company ="",
                    address ="", home ="", mobile ="", work ="",fax ="", email = "", email2 = "",
                    email3 = "", homepage ="",address_2 = "",phone_2 = "", notes = "")] + [
    Contact(firstname =random_string("firstname",10), middlename =random_string("middlename",15),
           lastname =random_string("lastname",15),nickname =random_string("nickname",15), title =random_string("title",15),
           company=random_string("company",15), address =random_string("address",15), home =random_string("home",15),
           mobile =random_string("mobile",15), work =random_string("work",15), fax =random_string("fax",15),
           email = random_string("email",15),email2 = random_string("email2",15), email3 = random_string("email3",15),
           homepage =random_string("homepage",15), bday = random_string("17",15), bmonth = random_string("Desember",15),
           byear = random_string("32",15), aday =random_string("18",15),
           amonth = random_string("August",15), ayear =random_string("33",15), address_2 = random_string("adress_2",15),
           phone_2 = random_string("phone_2",15), notes = random_string("notes",15))
    for i in range (5)
]

@pytest.mark.parametrize("contact",testdata, ids= [repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname ="dsad", middlename ="fdsf", lastname ="vcxv", nickname ="fdsff", title ="vcxv", company="vcxv", address ="bvcbb", home ="bvcb", mobile ="cxzc", work ="test",
                               fax ="test", email = "hg", email2 = "re", email3 = "ee", homepage ="ee", bday = "17", bmonth = "December", byear = "32", aday ="15", amonth = "August", ayear ="33", address_2 = "fd",
                               phone_2 = "gfd", notes = "gfd")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


