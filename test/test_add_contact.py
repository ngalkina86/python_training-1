# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username ='admin', password = "secret")
    app.contact.create(Contact(firstname ="dsad", middlename ="fdsf", lastname ="vcxv", nickname ="fdsff", title ="vcxv", company_name ="vcxv", address ="bvcbb", home ="bvcb", mobile ="cxzc", phone_work ="test",
                               fax ="test", email = "hg", email_12 = "re", email_13 = "ee", homepage ="ee", bday = "17", bmonth = "December", byear = "32", aday ="15", amonth = "August", ayear ="33", address_2 = "fd",
                               phone_2 = "gfd", notes = "gfd"))
    app.session.logout()


def test_add_other_contact(app):
    app.session.login(username ='admin', password = "secret")
    app.contact.create(Contact(firstname ="", middlename ="", lastname ="", nickname ="", title ="", company_name ="", address ="", home ="", mobile ="", phone_work ="",
                               fax ="", email = "", email_12 = "", email_13 = "", homepage ="", bday = "12", bmonth = "December", byear = "5", aday ="13", amonth = "April", ayear ="6", address_2 = "",
                               phone_2 = "", notes = ""))
    app.session.logout()



