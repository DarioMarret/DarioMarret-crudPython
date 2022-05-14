from flask import Blueprint, render_template, request, redirect, url_for
from model.contact import Contact
from controller.contact import setContact, deleteContact, updateContact

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)



@contacts.route("/new", methods=['POST'])
def new():
    form = request.form
    setContact(form)
    return redirect(url_for('contacts.index'))



@contacts.route("/update/<id>", methods=['POST', 'GET'])
def update(id):
    if request.method == "POST":
        form = request.form
        up = updateContact(id, form)
        if up:
            return redirect(url_for('contacts.index'))
        else:
            print(up)
    else:
        contacts = Contact.query.get(id)
        return render_template('update.html', contacts=contacts)





@contacts.route("/detele/<id>")
def delete(id):
    deleteContact(id)
    return redirect(url_for('contacts.index'))