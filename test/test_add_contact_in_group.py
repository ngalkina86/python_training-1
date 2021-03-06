from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group



db = ORMFixture(host="127.0.0.1", name="addressbook", user= "root",password = "")
def test_add_contact_in_group(app,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname ="firstname",lastname = "lastname", address= "address", home = "home",
                                   mobile = "mobile", work = "work", phone_2 = "phone_2", email = "email", email2 = "email2",
                                   email3= "email3"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group=None
    contact=None
    group_list=db.get_group_list()
    for index in range(len(group_list)):
        orm_contacts=db.get_contacts_not_in_group(group_list[index])
        group = group_list[index]
        if len(orm_contacts) > 0:
            contact = orm_contacts[0]
            break

    if contact is None:
        contact = db.get_contacts_in_group(group)[0]
        app.contact.remove_contact_from_group(contact.id, group.name)

    old_contacts_list = db.get_contacts_in_group(group)
    app.contact.add_contact_in_group(contact.id,group.name)
    new_contacts_list = db.get_contacts_in_group(group)
    assert len(new_contacts_list) == len(old_contacts_list) + 1
    assert contact in new_contacts_list





