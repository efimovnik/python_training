from model.contact import Contact
import random
from time import sleep


def test_del_some_contact_in_details(app, db, check_ui):
    if db.get_contacts_count() == 0:
        app.contact.create(Contact(middlename="test_edit_contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_in_details_by_id(contact.id)
    sleep(1)  # db did not have time to get information about the remote contact
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

