import re

regex_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
regex_email = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init(self):
        self.baza = baza


    def view_contact(self, s:list):
        for item in s:
            print(f"Name: {item.name}\t Phone: {item.phone}\t Email: {item.email}")
        # print("")

    def add_contact(self, s:list):
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

    def delete_contact(self, s:list):
        id = input("which contact do you want to delete(enter a phone number): ")
        phone_nums = []
        for item in s:
            phone_nums.append(item.phone)
            if item.phone == id:
                s.remove(item)
                print("Successfully deleted!")

        if id not in phone_nums:
            print("There is no contact with that phone number!")

    def edit_contact(self, s:list):
        id = input("Which contact do you want to edit(enter a phone number): ")
        phone_nums = []
        for item in s:
            phone_nums.append(item.phone)
            if item.phone == id:
                # s.remove(item)
                # self.add_contact(s)
                elem = input("what exactly do you want to change? 1. Name. 2. Phone. 3. Email.\n")
                if elem == '1':
                    item.name = input("What is the new name? ")
                    print("Successfully edited!")
                elif elem == '2':
                    item.phone = input("What is the new phone number? ")
                    print("Successfully edited!")
                elif elem == '3':
                    item.email = input("What is the new email? ")
                    print("Successfully edited!")
                else:
                    print("Invalid option!")

        if id not in phone_nums:
            print("There is no contact with that phone number!")

def contact_manager(s:list):
    while True:
        kod = input("\n1. view contact\n2. add contact\n3. delete contact\n4. edit contact\n5.Exit\n")
        if kod == "1":
            cm = ContactManager()
            cm.view_contact(s)
        elif kod == "2":
            cm = ContactManager()
            cm.add_contact(s)
        elif kod == "3":
            cm = ContactManager()
            cm.delete_contact(s)
        elif kod == "4":
            cm = ContactManager()
            cm.edit_contact(s)
        elif kod == "5":
            break
        else:
            print("Invalid option!")

contact1 = Contact("Aki", "7363628", 'aki@gmail.com')
contact2 = Contact("Asi", "9472872", 'asi@gmail.com')
contact3 = Contact("Azi", "3728267", 'azi@gmail.com')
contact4 = Contact("Aoi", "9472683", 'aoi@gmail.com')
contact5 = Contact("Ali", "4674564", "ali@gmail.com")
baza = [contact1, contact2, contact3, contact4, contact5]
sms_list = []
sms_id = 1

class smsManager:
    def __init__(self, sms_list:list, sms_id):
        self.sms_list = sms_list
        self.sms_id = sms_id

    def send_sms(self, s:list):
        phone_list = []
        phone_num = input("Enter phone number that you want to send sms: ")
        for item in s:
            phone_list.append(item.phone)
            if item.phone == phone_num:
                print(f"This phone number belongs to {item.name}")
                message = input("Enter your message: ")
                a = f"ID: {self.sms_id}\t To: {item.name}\t Message: {message}"
        if phone_num not in phone_list:
            print("There is no such number in your contact")
            message = input("Enter your message: ")
            a = f"ID: {self.sms_id}\t To: {phone_num}\t Message: {message}"
        self.sms_id += 1
        self.sms_list.append(a)
        return self.sms_list, self.sms_id
        # print(self.sms_list)


    def view_sms(self, sms_list:list):
        # print(self.sms_list)
        for i in sms_list:
            print(i)

    def del_sms(self, s:list):
        sms_id_for_del = input("Enter sms ID that you want to delete: ")
        for i in self.sms_list:
            result = re.search(r'ID:\s*(\d+)', i)
            if sms_id_for_del==result.group(1):
                print("Successfully deleted!")
                return self.sms_list.remove(i)


def sms_manager(s, sms_list:list, sms_id):

    kod = input("1. Send sms\n2. View sms\n3. Delete sms\n4. Exit\n")
    sm = smsManager(sms_list, sms_id)
    if kod == "1":
        sms_list, sms_id = sm.send_sms(s)
        return sms_id
    elif kod == "2":
        sms_list = sm.view_sms(sms_list)
        return sms_id
    elif kod == "3":
        sms_list = sm.del_sms(s)
        return sms_id
    elif kod == "4":
        return sms_id
    else:
        print("Invalid option!")
        return sms_id



def manager(s, sms_l):
    global sms_id
    while True:
        kod = input("1. Contact manager\n2. SMS manager\n3. Exit\n")
        if kod == "1":
            contact_manager(s)
        elif kod == "2":
            sms_id = sms_manager(s, sms_l, sms_id)
        elif kod == "3":
            break
        else:
            print("Invalid option!")

manager(baza, sms_list)