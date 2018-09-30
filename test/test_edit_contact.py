from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username='admin', password="secret")
    app.contact.edit_first_contact(Contact(firstname ="TEST", middlename ="", lastname ="", nickname ="", title ="", company_name ="", address ="", home ="", mobile ="", phone_work ="",
                               fax ="", email = "", email_12 = "", email_13 = "", homepage ="", bday = "12", bmonth = "December", byear = "5", aday ="13", amonth = "April", ayear ="6", address_2 = "",
                               phone_2 = "", notes = ""))
    app.session.logout()