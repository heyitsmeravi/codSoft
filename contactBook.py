def search(contactBook):
    name=input("Enter the name of the contact to search: ")
    if name not in contactBook:
        print(f"contact {name} doesn't exists! ")
    else:
        contactBook=contactBook[name]
        print(f"Name: {name}, Email: {contactBook['email']}, Number: {contactBook['number']}")
def add(contactBook):
    name=input("Enter the name of the contact: ")
    if name in contactBook:
        print(f"contact {name} already exists! ")
    else:
        email=input("Enter the email of the Contact: ")
        number=input("Enter the phone number: ")
        contactBook[name]={'email': email,'number':number }
        print("Contact created successfully!")
def delete(contactBook):
    name=input("Enter the name of the contact to delete: ")
    del contactBook[name]
    print(f"Contact {name} Deleted successfully! ")
def view(contactBook):
    name=input("Enter the name of the contact to view: ")
    if name in contactBook:
        contact=contactBook[name]
        print(f"Name:{name}, Email: {contact['email']}, Number: {contact['number']} ")
    else:
        print("Contact not found!!")
def update(contactBook):
    name=input("Enter the name of the contact to update: ")
    if name not in contactBook:
        print(f"contact {name} doesn't exists! ")
    else:
        email=input("Enter the email of the Contact to update: ")
        number=input("Enter the updated phone number: ")
        contactBook[name]={'email': email,'number':number }
        print(f"Contact {name} updated successfully!")
contactBook={}
exit=1
while(exit):
    print("Welcome to the ContactBook!")
    print("Choose what to do in ContactBook: (1. View, 2. Search, 3. Add, 4. Update, 5. Delete )")
    action=int(input())
    if action==1:
        view(contactBook)
    elif action==2:
        search(contactBook)
    elif action==3:
        add(contactBook)
    elif action==4:
        update(contactBook)
    elif action==5:
        delete(contactBook)
    else:
        print("Not a Valid Option!!")
    exit=int(input("Want to exit (0 to exit , 1 to continue): "))

