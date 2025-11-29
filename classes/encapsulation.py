class Student:
    def __init__(self, name, phone, seria_id, group_id):
        self.__name = name
        self.phone = phone
        self.__seria_id = seria_id
        self.group_id = group_id

    def get_serial_id(self):
        return self.__seria_id

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, new_name):
        if len(new_name) >= 3:
            self.__name = new_name
            print("Name changed!")
        else:
            print("Name is too short")

# class P(Student):
#     pass

# p1 = P("name", 74828392, 839, 273)
# p1.__seria_id          # Topmaydi
# p1.get_serial_id()     # Topadi

"""
Encapsulation - bu ob'ektning ichki ma'lumotlarini tashqaridan yashirish va 
ularga faqat maxsus metodlar orqali ruxsat berish.

3 xil access modifier bor:
1. Public     
2. Private    (__ - 2 ta pastki chiziqcha bilan)
3. Protected  (_ - 1 ta pastki chiziqcha bilan))

"""

st1 = Student("Aki", 378237, 7382739, 849392)
# print(st1.get_name())
# st1.set_name("A")
# print(st1.get_name())

print(st1.get_name)
st1.set_name = "Asi"
print(st1.get_name)

"""

"""