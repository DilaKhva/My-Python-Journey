import re

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

contact1 = Contact("Aki", "7363628", 'aki@gmail.com')
contact2 = Contact("Asi", "9472872", 'asi@gmail.com')
contact3 = Contact("Azi", "3728267", 'azi@gmail.com')
contact4 = Contact("Aoi", "9472683", 'aoi@gmail.com')
baza = [contact1, contact2, contact3, contact4]

regex_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
regex_email = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

def view_contact(s:list):
    for item in s:
        print(f"Name: {item.name}\t Phone: {item.phone}\t Email: {item.email}")
    # print("")

def add_contact(s:list):
    name = input("Name: ")
    phone = input("Phone: ")
    if re.match(regex_phone, phone):
        email = input("Email: ")
        if re.match(regex_email, email):
            contactx = Contact(name, phone, email)
            s.append(contactx)
        else:
            print("Invalid email!")
    else:
        print("Invalid phone number")

def delete_contact(s:list):
    id = input("which contact do you want to delete(enter a phone number): ")
    phone_nums = []
    for item in s:
        phone_nums.append(item.phone)
        if item.phone == id:
            s.remove(item)
            print("Successfully deleted!")

    if id not in phone_nums:
        print("There is no contact with that phone number!")

def edit_contact(s:list):
    id = input("Which contact do you want to edit(enter a phone number): ")
    phone_nums = []
    for item in s:
        phone_nums.append(item.phone)
        if item.phone == id:
            s.remove(item)
            add_contact(s)
            print("Successfully edited!")
    if id not in phone_nums:
        print("There is no contact with that phone number!")

def contact_manager(s:list):
    while True:
        kod = input("\n1. view contact\n2. add contact\n3. delete contact\n4. edit contact\n5.Exit\n")
        if kod == "1":
            view_contact(s)
        elif kod == "2":
            add_contact(s)
        elif kod == "3":
            delete_contact(s)
        elif kod == "4":
            edit_contact(s)
        elif kod == "5":
            break
        else:
            print("Invalid option!")

contact_manager(baza)
