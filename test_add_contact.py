# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_1 import Application

@pytest.fixture
def app(request):
        fixture = Application()
        request.addfinalizer(fixture.destroy)
        return fixture

def test_add_contact(app):
        app. open_home_page()
        app.login(username ='admin', password = "secret")
        app.creat_new_contact(Contact(firstname = "dsad", middlename ="fdsf", lastname = "vcxv",nickname = "fdsff",title = "vcxv",company_name = "vcxv",address = "bvcbb",home = "bvcb",mobile = "cxzc",phone_work = "test",
                               fax ="test", email = "hg",email_12 = "re",email_13 = "ee", homepage ="ee",bday = "17",  bmonth = "December",byear = "32", aday ="15",amonth = "August", ayear ="33", address_2 = "fd",
                               phone_2 = "gfd", notes = "gfd"))
        app.return_to_home_page()
        app.logout()


def test_add_other_contact(app):
        app.open_home_page()
        app.login(username ='admin', password = "secret")
        app.creat_new_contact(Contact(firstname = "", middlename ="",lastname = "",nickname = "",title = "",company_name = "",address = "",home = "",mobile = "",phone_work = "",
                               fax ="", email = "",email_12 = "",email_13 = "", homepage ="",bday = "12",  bmonth = "December",byear = "5", aday ="13",amonth = "April", ayear ="6", address_2 = "",
                               phone_2 = "", notes = ""))
        app.return_to_home_page()
        app.logout()


