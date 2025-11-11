import csv
#
# with open("students.csv", 'x') as f:
#     writer = csv.writer(f)

def add_student(data=None):
    if data:
        with open('students.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
    else:
        name = input("Enter name: ")
        age = input("Enter age: ")
        phone = input("Enter phone number: ")
        column = ["name", "age", "phone"]
        with open('students.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # writer.writerow(column)
            writer.writerows([[name, age, phone]])
        # print(writer)

# add_student()

def read_students():
    with open('students.csv', 'r') as f:
        reader = csv.reader(f)
        s = list(reader)
        # print(s)
        count = 0
        for i in s:
            # print(i)
            if count != 0:
                print(f"{count}. {i[0]} {i[1]} {i[2]}")
            else:
                print(f"id {i[0]} {i[1]} {i[2]}")
            count += 1

# read_students()


def update_students():
    with open('students.csv', 'r') as f:
        reader = csv.reader(f)
        s = list(reader)
    read_students()
    id = input("\nEnter student id: ")
    a = input("What do you want to update?\n1.name\n2.age\n3.phone\n")
    if a == "1":
        new_name = input("Enter new name: ")
        s[int(id)][0] = new_name
        add_student(s)
    elif a == "2":
        new_age = input("Enter new age: ")
        s[int(id)][1] = new_age
        add_student(s)
    elif a == "3":
        new_phone = input("Enter new phone number: ")
        s[int(id)][2] = new_phone
        add_student(s)
    else:
        print("Invalid input!")


update_students()