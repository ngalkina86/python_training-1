from model.contact import Contact

def test_del_first_contact(app):
    if app.group.count() == 0:
        app.group.create(Contact(name="test"))
    app.contact.delete_first_contact()