# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname ="dsad", middlename ="fdsf", lastname ="vcxv", nickname ="fdsff", title ="vcxv", company="vcxv", address ="bvcbb", home ="bvcb", mobile ="cxzc", work ="test",
                               fax ="test", email = "hg", emai12 = "re", emai13 = "ee", homepage ="ee", bday = "17", bmonth = "December", byear = "32", aday ="15", amonth = "August", ayear ="33", address_2 = "fd",
                               phone_2 = "gfd", notes = "gfd"))

def test_add_other_contact(app):
    app.contact.create(Contact(firstname ="", middlename ="", lastname ="", nickname ="", title ="", company ="", address ="", home ="", mobile ="", work ="",
                               fax ="", email = "", emai12 = "", emai13 = "", homepage ="", bday = "12", bmonth = "December", byear = "5", aday ="13", amonth = "April", ayear ="6", address_2 = "",
                               phone_2 = "", notes = ""))


