import re

students = {
    "username1": {
        'name': 'Ali',
        'phone': '+998995637829',
        'age': '20'
    },
    "username2": {
        'name': 'Vali',
        'phone': '+998902877767',
        'age': '30'
    }
}

rgex_username = "^[a-z0-9_-]{3,15}$"
# regex_name = "/^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžæÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/u"
# regex_age = r"/\s[0-1]{1}[0-9]{0,2}/"
regex_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"



print(students)

def view_students(d:dict):
    for k, v in d.items():

        print(f"id: {k}, name: {v['name']}, age: {v['age']}")


# view_students(students)

def is_unique(d:dict, username):
    a = True
    for k, v in d.items():
        if k == username:
            a = False
    return a

def take_username(d):
    username = input('username: ')
    u = False
    while not u:
        u = is_unique(d, username)
        for k, v in d.items():
            if k == username:
                print('username already taken!')
                username = input('Please, enter a unique username: ')

    return username

def take_name():
    name = input('name: ')
    if name != '' and not name.isnumeric():
        # print(name)
        return name
    else:
        print("Invalid name. Try again.")
        return take_name()

def take_phone():
    phone = input('phone: ')
    if re.match(regex_phone, phone):
        return phone
    else:
        print("Invalid phone. Try again.")
        return take_phone()

def take_age():
    age = input('age: ')
    if 200>int(age)>0:
        return age
    else:
        print("Invalid age. Try again.")
        return take_age()

def add_student(d:dict):
    username = take_username(d)
    if re.match(rgex_username, username):
        name = take_name()
        # print(name)
        phone = take_phone()
        age = take_age()
        d.update({
            username: {
                'name': name, 'phone': phone, 'age': age
            }
        }
        )
    else:
        print("This username is not valid!\nTry again.")
        add_student(d)


    print(d)

# add_student(students)

def update_data(d:dict):
    u = input('username: ')
    if u in d.keys():

        update = input(' \t Which data do you want to update?(1/2/3/4) \t 1. username \t 2. name \t 3. phone \t 4. age \t 5. Back\n')
        if update == '1':
            username = take_username()

            d.update({username:d[u]})
            d.pop(u)
        elif update == '2':
            print("Enter updated name below")
            name = take_name()

            d[u]['name'] = name
        elif update == '3':
            print("Enter updated phone below")
            phone = take_phone()
            d[u]['phone'] = phone
        elif update == '4':
            print("Enter updated age below")
            age = take_age()
            d[u]['age'] = age
        elif update == '5':
            student_manager()
        else:
            "You can only enter numbers from 1 to 5."
    else:
        print("This username is not valid!\nTry again.")
        update_data(d)

# update_data(students)

def student_manager(d:dict):
    while True:
        kod = input("\n1. view students \t 2. add student \t 3. update data \t 4. break\n")

        if kod == '1':
            view_students(d)
        elif kod == '2':
            add_student(d)
        elif kod == '3':
            update_data(d)
        elif kod == '4':
            break
        else:
            print("Invalid option. Try again.")
            student_manager(d)

student_manager(students)