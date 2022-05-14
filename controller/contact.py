from model.contact import Contact
from util.db import db

def setContact(form):
    fullname = form["fullname"]
    email = form["email"]
    phone = form["phone"]
    new_contact = Contact(fullname, email, phone)
    db.session.add(new_contact)
    db.session.commit()

def deleteContact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

def updateContact(id, form):
    try:
        contact = Contact.query.get(id)
        contact.fullname = form["fullname"]
        contact.email = form["email"]
        contact.phone = form["phone"]
        db.session.commit()
        return True 
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        return ValueError