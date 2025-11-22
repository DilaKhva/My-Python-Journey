import json
import re

data = {
      "1234567891234567": {
            "balans": 23456,
            "parol": "user1",
            "karta egasi": "aesrtg etrfwd",
            "tel raqami": None,
            "sms": False
    }
}

"""I used regex only for password and phone"""
reg_password = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
reg_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

"""THis function is for reading our json file, if in file we have no data then it returns False"""
def read_k():
    with open("kartalar.json", 'r') as f:
        try:
            d = json.load(f)
            return d
        except:
            return False

"""I used cards variable to avoid using read_k() function many times during the process of coding"""
cards = read_k()
# print(cards)

"""add_data() function takes d param and adds d to our json file"""
def add_data(d):
    with open("kartalar.json", "w") as f:
        json.dump(d, f, indent=4)

# add_data(data)

"""
 check_card() function checks the user card and password. If the data is appropriate the process will go on, 
 if not then it defenitely gives some chances to try again.
"""
def check_card(c):
    if c:
        karta_num = input("Karta raqam kiriting: ")
        if karta_num in c:
            chances = 3
            while chances > 0:
                karta_pass = input("Parolni kiriting: ")
                chances -= 1
                if karta_pass == c[karta_num]["parol"]:
                    return karta_num
                else:
                    if chances != 0:
                        print("Parol hato, qaytadan urinib ko'ring.")
                    else:
                        print("Urinishingiz soni tugadi.")

            else:
                print("Karta bloklandi!")
        else:
            print("Bunday karta raqami mavjud emas!")
            return False
    else:
        print("Bankomatda sozlash ishlari amalga oshirilmoqda...")


""" 
Manager function is our main function and I think it has far more code than it supposed to have, it has a 
catalog part which includes viewing the balanse, adding/takin money to/from balanse, changing the password,
turning on/off sms service. And all heppens inside of manager function. ( Actually we could create other 
functions and just call them inside manager() for more clean code, but okay, let it be for now.. )
"""
def manager(c):

    karta_raq = check_card(c)
    if karta_raq:
        while True:
            xizmat = input("\n1. Balansni ko'rish\n2. Balansga pul qo'shish\n3. Balansdan pul yechish\n4. Parolni o'zgartirish\n5. SMS xizmatini yoqish\n6. SMS xizmatini o'chirish\n7. Exit\n")
            if xizmat == "1":

                print(f"\nSizning balansingiz: {c[karta_raq]['balans']} so'm.")

            elif xizmat == "2":
                try:
                    qoshma = int(input("\nQancha pul qo'shmoqchisiz? "))
                    one_percent = qoshma * 0.01
                    summ = (qoshma-one_percent) + int(c[karta_raq]['balans'])
                    c[karta_raq]["balans"] = summ
                    add_data(c)
                    print(f"Balansingiz: {summ} so'm bo'ldi.\n")
                except:
                    print("Noto'g'ri ma'lumot kiritdingiz!\n")
            elif xizmat == "3":
                try:
                    ayirma = int(input("\nQancha pul yechib olmoqchisiz? "))
                    one_percent = ayirma * 0.01
                    left = int(c[karta_raq]['balans'])-ayirma-one_percent
                    if left >= 0:
                        c[karta_raq]["balans"] = left
                        add_data(c)
                        print(f"Balansingizda {left} so'm qoldi.\n")
                    else:
                        print("Yetarli mablag' mavjud emas!")
                except:
                    print("Noto'g'ri ma'lumot kiritdingiz!\n")
            elif xizmat == "4":

                new_pass = input("Yangi parolni kiriting: ")
                if re.match(reg_password, new_pass):
                    c[karta_raq]["parol"] = new_pass
                    add_data(c)
                    print("Jarayon muvaffaqiyatli amalga oshirildi!\n")
                else:
                    print("Bu parol qoidalarga to'gri kelmaydi!\nBo'lishi shart:\n- Kamida 8 ta belgi\n- Bitta kotta harf\n- Bitta kichkina harf\n- 1 ta maxsus belgi(@#$%&)\n")
            elif xizmat == "5":
                phone = input("Tel raqam kiriting: ")
                if re.match(reg_phone, phone):
                    c[karta_raq]["tel raqami"] = phone
                    c[karta_raq]["sms"] = True
                    add_data(c)
                    print("Jarayon muvaffaqiyatli amalga oshirildi!\n")
                else:
                    print("Noto'g'ri ma'lumot kiritdingiz!\n")
            elif xizmat == "6":
                c[karta_raq]["tel raqami"] = None
                c[karta_raq]["sms"] = False
                print("Jarayon muvaffaqiyatli amalga oshirildi!")
            elif xizmat == "7":
                break
            else:
                print("\nFaqat 1/2/3/4/5/6/7 kiritish mumkin!\n")
    else:
        if c == False:
            return
        else:
            manager(c)
manager(cards)