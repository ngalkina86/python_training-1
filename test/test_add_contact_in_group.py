from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


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
        app.contact.create(Contact(firstname ="firstname",lastname = "lastname", address= "address", home = "home",
                                   mobile = "mobile", work = "work", phone_2 = "phone_2", email = "email", email2 = "email2",
                                   email3= "email3"))
        orm_contacts = db.get_contacts_not_in_group(group)
        contact = orm_contacts[0]

    app.contact.add_contact_in_group(contact.id,group.name)
    contacts_list = db.get_contacts_in_group(group)
    assert contact in contacts_list


    


