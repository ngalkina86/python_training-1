from model.group import Group


def test_edit_group(app):
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Test group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

