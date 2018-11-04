from model.group import Group
from random import randrange
import random

def test_modify_group_name(app,db,check_ui):
    #group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    id = group.id
    old_groups.remove(group)
    group = Group(id = id, name ="New group")
    old_groups.append(group)
    # group.id = old_groups[index].id
    app.group.modify_group_by_id(id,group)
    # app.group.modify_group_by_index(index,group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(),key = Group.id_or_max)


#def test_modify_group_header(app):
 #   old_groups = app.group.get_group_list()
  #  if app.group.count() == 0:
   #     app.group.create(Group(header="test"))
    #app.group.modify_first_group(Group(header ="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)