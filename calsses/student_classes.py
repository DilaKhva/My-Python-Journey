class Student:
    def __init__(self, name, phone, age):
        self.name = name
        self.phone = phone
        self.age = age

student1 = Student("Aki", "9087634567", 12)
student2 = Student("Asi", "6523895623", 16)
student3 = Student("Avi", "4893662582", 18)
baza = [student1, student2, student3]

def view_students(s:list):

    for student in s:
        print(f"Name: {student.name}\t Phone: {student.phone}\t Age: {student.age}\t ")

# view_students(baza)

def add_student():
    name = input("Name: ")
    phone = input("Phone: ")
    age = input("Age: ")
    student = Student(name, phone, age)
    baza.append(student)
    view_students(baza)

# add_student()
# view_students(baza)

def update_list():
    pass

def student_manager():
    while True:
        kod = input("\n1. view students\n2. add student\n3. change student\n4. exit\n")
        if kod == "1":
            view_students(baza)
        elif kod == "2":
            add_student()
        elif kod == "3":
            update_list()
        elif kod == "4":
            break
        else:
            print("Invalid option!")

student_manager()