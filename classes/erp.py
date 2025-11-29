import re
class Student:
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email
        self.regex_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        self.regex_email = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

    def display_info(self):
        print("--------------------------------------------------------")
        print(f"Name: {self.name}, Phone: {self.phone}, Age: {self.age}, Email: {self.email}")
        print("--------------------------------------------------------")

    def edit_info(self):
        change = input("What exactly do you want to edit?\n1. Name\n2. Phone\n3. Age\n4. Email\n")
        if change == "1":
            self.name = input("Enter a new name: ")
            print("Successfully edited!")
        elif change == "2":
            p = input("Enter a new phone: ")
            if re.match(self.regex_phone, p):
                self.phone = p
                print("Successfully edited!")
            else:
                print("Invalid Phone Number!")
        elif change == "3":
            self.age = input("Enter a new age: ")
            print("Successfully edited!")
        elif change == "4":
            e = input("Enter a new email: ")
            if re.match(self.regex_email, e):
                self.email = e
                print("Successfully edited!")
            else:
                print("Invalid Email!")
        else:
            return

class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []
        self.regex_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        self.regex_email = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

    def add_student(self):
        name = input("Enter a name: ")
        phone = input("Enter a phone: ")
        if re.match(self.regex_phone, phone):
            age = input("Enter a age: ")
            email = input("Enter a email: ")
            if re.match(self.regex_email, email):
                student = Student(name, phone, age, email)
                self.students.append(student)
            else:
                print("Invalid Email!")
        else:
            print("Invalid Phone Number!")

    def view_students(self):
        count = 0
        print("--------------------------------------------------------")
        if self.students:
            for s in self.students:
                count += 1
                print(f"{count}. Name: {s.name} age: {s.age}")
        else:
            print("No data found!")
        print("--------------------------------------------------------")

class OTM:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def add_group(self):
        title = input("Enter a title of group: ")
        profession = input("Enter a profession: ")
        group = Group(title, profession)
        self.groups.append(group)

    def view_groups(self):
        count = 0
        print("--------------------------------------------------------")
        if self.groups:
            for g in self.groups:
                count += 1
                print(f"{count}. Title: {g.title} Profession: {g.profession}")
        else:
            print("No data found!")
        print("--------------------------------------------------------")



class ERP:
    def __init__(self):
        self.title = "ERP"
        self.otms = []

    def add_otm(self):
        title = input("Enter a title of OTM: ")
        otm = OTM(title)
        self.otms.append(otm)

    def view_otms(self):
        count = 0
        print("--------------------------------------------------------")
        if self.otms:
            for otm in self.otms:
                count += 1
                print(f"{count}. Title: {otm.title}")
        else:
            print("No data found!")
        print("--------------------------------------------------------")

erp = ERP()

def student_manager(st:Student):
    kod = input("1. View detail info\n2. Edit student's info\n3. Exit\n")
    if kod == "1":
        st.display_info()
    elif kod == "2":
        st.edit_info()
    else:
        return


def group_manager(group: Group):
    while True:
        kod = input("1. Add student\n2. View students\n3. Student detail\n4. Exit\n")
        if kod == "1":
            group.add_student()
        elif kod == "2":
            group.view_students()
        elif kod == "3":
            group.view_students()
            # print("------------")
            try:
                index = int(input("Enter student id: "))
                st = group.students[index - 1]
                student_manager(st)
            except IndexError:
                print("--------------------------------------------------------")
                print("No data found!")
                print("--------------------------------------------------------")
        else:
            break

def otm_manager(otm: OTM):
    while True:
        kod = input("1. Add group\n2. View groups\n3. View groups in detail\n4. Exit\n")
        if kod == "1":
            otm.add_group()
        elif kod == "2":
            otm.view_groups()
        elif kod == "3":
            otm.view_groups()
            # print("------------")
            try:
                index = int(input("Enter group id: "))
                gr = otm.groups[index - 1]
                group_manager(gr)
            except IndexError:
                print("--------------------------------------------------------")
                print("No data found!")
                print("--------------------------------------------------------")
        else:
            break

def erp_manager(erp: ERP):
    while True:
        kod = input("1. Add OTM\n2. View OTMs\n3. View OTM in detail\n4. Exit\n")
        if kod == "1":
            erp.add_otm()
        elif kod == "2":
            erp.view_otms()
        elif kod == "3":
            erp.view_otms()
            # print("------------")
            try:
                index = int(input("Enter OTM id: "))
                otm = erp.otms[index-1]
                # print(otm)
                otm_manager(otm)
            except IndexError:
                print("--------------------------------------------------------")
                print("No data found!")
                print("--------------------------------------------------------")
        else:
            break

erp_manager(erp)