from model.contact import ContactUpd, Contact
from random import randrange


def test_edit_some_contact_in_details_osx(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test_edit_contact"))
    old_contacts = app.contact.get_contact_upd_list()
    contact = ContactUpd(firstname_upd="Nickolay Edit Upd", middlename_upd="Igorevich Edit Upd",
                         lastname_upd="Efimov Edit Upd", nickname_upd="kolya Edit Upd", title_upd="Title Edit Upd",
                         company_upd="Company Edit Upd",
                         photo_upd="/Users/nikolayefimov/Downloads/pictures pycharm/testpicture3.jpeg",
                         address_upd="Address Edit Upd", home_phone_upd="HomePhone Edit Upd",
                         work_phone_upd="MobilePhone Edit Upd", mobile_phone_upd="WorkPhone Edit Upd",
                         fax_number_upd="FaxNumber Edit Upd", email_upd="updeditemail1@mail.ru",
                         email2_upd="updeditemail2@mail.ru", email3_upd="updeditemail3@mail.ru",
                         homepage_upd="updedithomepage.ru", birth_day_upd="22", birth_month_upd="April",
                         birth_year_upd="2005", anniversary_day_upd="21", anniversary_month_upd="May",
                         anniversary_year_upd="2007", address2_upd="address Edit Upd",
                         phone_number_2_upd="HomeAddress Edit Upd", notes_upd="Notes Edit Upd")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_in_details_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_upd_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactUpd.id_or_max) == sorted(new_contacts, key=ContactUpd.id_or_max)