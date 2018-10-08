from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="firstname"))
    app.contact.modify_first_contact(Contact(firstname ="New firstname"))

def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="middlename"))
    app.contact.modify_first_contact(Contact(middlename="New middlename"))