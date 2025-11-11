import json

students = {
    "+998995637829": {
        'name': 'Ali',
        'phone': '+998995637829',
        'age': '20'
    },
    "+998902877767": {
        'name': 'Vali',
        'phone': '+998902877767',
        'age': '30'
    }
}

def w_n73(d:dict):
    with open('students.json', 'w') as f:
        json.dump(d, f, indent = 4 )

def r_n75():

    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
            return data
    except:
        print("Student data not found.")


def add_n73():
    data = r_n75()
    name = input("name:")
    phone = input("phone:")
    age = input("age:")
    s = {
        phone:{
            'name':name,
            "phone":phone,
            'age':age
        }
    }

    if data:
        print("====", data)
        data.update(s)
        print("====", data)
        w_n73(data)
    else:
        w_n73()

# add_n73()



# print(r_n75())



def student_manager():
    while True:
        kod = input("1. view students \t 2. add student \t 3. exit\n")
        if kod == "1":
            # print(r_n75(), "\n")
            d = r_n75()
            for k, v in d.items():
                print(f"id: {k}, name: {v['name']}, age: {v['age']}")
        elif kod == "2":
            add_n73()
        else:
            break

student_manager()

# try:
#     a = int(input("a ="))
#     print(1/a)
# except:
#     print("bad input")