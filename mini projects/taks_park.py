import re
from datetime import date

class Car:
    def __init__(self, brand, model, year, seria):
        self.brand = brand
        self.model = model
        self.year = year
        self.seria = seria
        self.is_in_use = False


car1 = Car("BMW", "M5", "2022", "88871")
car2 = Car("Mercedes-Benz", "C300", "2019", "28947")
car3 = Car("Toyota Camry", "", "2021", "29472")
car4 = Car("Audi", "A6", "2020", "52846")
car5 = Car("Tesla Mode", "3", "2023", "73923")


class User:
    def __init__(self, name, phone, seria, age):
        self.name = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.is_active = False


class Order:
    def __init__(self, user_id, car_id, date_start, date_end, order_id):
        self.user_id = user_id
        self.car_id = car_id
        self.date_start = date_start
        self.date_end = date_end
        self.order_id = order_id
        self.is_active = True


class Park:
    def __init__(self, title):
        self.cars = [car1, car2, car3, car4, car5]
        self.users = []
        self.orders = []
        self.title = title

    def view_cars(self):
        print("____________________________________________________")
        if self.cars:
            count = 0
            for car in self.cars:
                count += 1
                print(f"{count}. {car.brand} {car.model} - {car.year}")
        else:
            print("No cars")
        print("____________________________________________________")

    def add_car(self):
        c_brand = input("Enter car's brand: ")
        c_model = input("Enter car's model: ")
        try:
            c_year = int(input("Enter car's year: "))
        except ValueError:
            print("Invalid year!\n")
            return
        c_seria = input("Enter car's seria: ")
        c_series = []
        for car in self.cars:
            c_series.append(car.seria)
        if c_seria not in c_series:
            car = Car(c_brand, c_model, c_year, c_seria)
            self.cars.append(car)
            print("Car added\n")
        else:
            print("Car seria already exists!\n")
            return

    def view_available_cars(self):
        not_rented_cars = []
        print("____________________________________________________")
        if self.cars:
            count = 0
            for car in self.cars:
                if car.is_in_use == False:
                    not_rented_cars.append(car)
                    count += 1
                    print(f"ID: {count}. {car.brand} {car.model} - {car.year}")
            print("____________________________________________________")
            return not_rented_cars
        else:
            print("No cars")
        print("____________________________________________________")

    def rent_car(self):
        re_date = r"(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})"
        available_cars = self.view_available_cars()
        try:
            index = int(input(f"Enter car's id: (1-{len(available_cars)})\n"))
        except ValueError:
            print(f"Invalid id! You had to enter 1-{len(available_cars)}\n")
            return
        car_id = available_cars[index-1].seria
        usr_id = input("Enter user's id: ")
        u_ids = []
        for j in self.users:
            u_ids.append(j.seria)
        if usr_id in u_ids:
            d_start = input("Enter start date: ")
            d_end = input("Enter end date: ")
            if not re.match(re_date, d_start) or not re.match(re_date, d_end):
                print("Invalid date!\n")
                return
            ord_id = input("Create order's seria number: ")
            ord_ids = []
            for ord in self.orders:
                ord_ids.append(ord.order_id)
            if ord_id in ord_ids:
                print("Order with this seria number already exists!\n")
                return
            order = Order(usr_id, car_id, d_start, d_end, ord_id)
            self.orders.append(order)
            available_cars[index - 1].is_in_use = True
            for user in self.users:
                if user.seria == usr_id:
                    user.is_active = True
            print("Car rented successfully!\n")
        else:
            print("User does not exist!\n")
            return

    def return_car(self):
        today = date.today()
        ord_id = input("Enter your order's seria number: ")
        for ord in self.orders:
            if str(ord.order_id) == ord_id:
                day, month, year = map(int, ord.date_end.split("."))
                given_date = date(year, month, day)
                if given_date >= today:
                    print("Returned on time!.")
                    print("Car returned successfully!\n")
                else:
                    print("Deadline was missed!")
                    print("Penalty is waiting for you...")
                    print("Car returned.\n")
                ord.is_active = False
                for u in self.users:
                    if u.seria == ord.user_id:
                        u.is_active = False
                for c in self.cars:
                    if c.seria == ord.car_id:
                        c.is_in_use = False


    def edit_car(self):
        c_id = input("Enter car's seria number that you want to edit: ")
        p = input("What exactly do you want to change?\n1. Brand\n2. Model\n3. Year\n4. Seria\n")
        car_ids = []
        for c in self.cars:
            car_ids.append(c.seria)
        for c in self.cars:
            if c.seria == c_id:
                if p == "1":
                    c.brand = input("Enter brand: ")
                    print("Edited!\n")
                elif p == "2":
                    c.model = input("Enter model: ")
                    print("Edited!\n")
                elif p == "3":
                    # c.year = input("Enter year: ")
                    try:
                        c.year = int(input("Enter car's year: "))
                        print("Edited!\n")
                    except ValueError:
                        print("Invalid year!\n")
                        return
                elif p == "4":
                    c_id = input("Enter car's seria: ")
                    if c_id not in car_ids:
                        c.seria = c_id
                        print("Edited!\n")
                    else:
                        print("Car with this seria number already exists!\n")
                        return

    def del_car(self):
        x = input("Enter car's seria number that you want to delete: ")
        for c in self.cars:
            if c.seria == x:
                self.cars.remove(c)
                print("Car deleted!\n")

    def add_user(self):
        u_name = input("Enter user's name: ")
        u_phone = input("Enter user's phone number: ")
        re_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        if not re.match(re_phone, u_phone):
            print("Invalid phone number!\n")
            return
        try:
            u_age = int(input("Enter user's age: "))
        except ValueError:
            print("Invalid age!\n")
            return
        u_seria = input("Enter user's seria: ")
        u_series = []
        for user in self.users:
            u_series.append(user.seria)
        if u_seria not in u_series:
            user_x = User(u_name, u_phone, u_seria, u_age)
            self.users.append(user_x)
            print("User added\n")
        else:
            print("User already exists!\n")
            return

    def view_users(self):
        print("____________________________________________________")
        if self.users:
            count = 0
            for user in self.users:
                count += 1
                print(f"{count}. {user.name} - {user.phone} - {user.age} - {user.seria}")
        else:
            print("No users")
        print("____________________________________________________")

    def view_active_users(self):
        print("____________________________________________________")
        if self.users:
            count = 0
            for user in self.users:
                if user.is_active:
                    count += 1
                    print(f"{count}. {user.name} - {user.phone} - {user.age}")
        else:
            print("No users")
        print("____________________________________________________")

    def edit_user(self):
        re_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        y = input("Enter user's seria number that you want to edit: ")
        u_ids = []
        for u in self.users:
            u_ids.append(u.seria)
        for usr in self.users:
            if usr.seria == y:
                x = input("What exactly do you want to change?\n1. Name\n2. Phone\n3. Seria\n4. Age\n")
                if x == "1":
                    usr.name = input("Enter name: ")
                    print("Edited!\n")
                elif x == "2":
                    usr_phone = input("Enter phone number: ")
                    if not re.match(re_phone, usr_phone):
                        print("Invalid phone number!\n")
                        return
                    else:
                        usr.phone = usr_phone
                        print("Edited!\n")
                elif x == "3":
                    usr_seria = input("Enter seria number: ")
                    if usr_seria not in u_ids:
                        usr.seria = usr_seria
                        print("Edited!\n")
                    else:
                        print("Seria already exists!\n")
                        return
                elif x == "4":
                    usr.age = input("Enter age: ")
                    print("Edited!\n")
                else:
                    print("Invalid option!\n")
                    return
            else:
                print("This seria number does not exist!\n")


    def del_user(self):
        usr_id = input("Enter user's seria number that you want to delete: ")
        for u in self.users:
            if u.seria == usr_id:
                self.users.remove(u)
                print("User deleted\n")



    def view_active_orders(self):
        print("____________________________________________________")
        if self.orders:
            count = 0
            for order in self.orders:
                if order.is_active:
                    count += 1
                    print(f"{count}. User ID: {order.user_id}, Car ID: {order.car_id}, Date: {order.date_start} - {order.date_end}")
        else:
            print("No orders")
        print("____________________________________________________")

    def view_orders(self):
        print("____________________________________________________")
        if self.orders:
            count = 0
            for order in self.orders:
                count += 1
                print(f"{count}. User ID: {order.user_id}, Car ID: {order.car_id}, Date: {order.date_start} - {order.date_end}")
        else:
            print("No orders")
        print("____________________________________________________")



def park_manager(p:Park):
    while True:
        kod = input("1. View all Cars\n2. View cars - ready to be rent\n3. View all Users\n4. View active users\n5. View all orders\n6. View active orders\n7. Add car\n8. Add user\n9. Edit car\n10. Edit user\n11. Delete car\n12. Delete user\n13. Rent car\n14. Return car\n15. Exit\n")
        if kod == "1":
            p.view_cars()
        elif kod == "2":
            p.view_available_cars()
        elif kod == "3":
            p.view_users()
        elif kod == "4":
            p.view_active_users()
        elif kod == "5":
            p.view_orders()
        elif kod == "6":
            p.view_active_orders()
        elif kod == "7":
            p.add_car()
        elif kod == "8":
            p.add_user()
        elif kod == "9":
            p.edit_car()
        elif kod == "10":
            p.edit_user()
        elif kod == "11":
            p.del_car()
        elif kod == "12":
            p.del_user()
        elif kod == "13":
            p.rent_car()
        elif kod == "14":
            p.return_car()
        elif kod == "15":
            break
        else:
            print("Invalid option!\n")

prk = Park("GGpark")
park_manager(prk)