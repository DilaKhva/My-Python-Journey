# from itertools import count
import re

class Car:
    def __init__(self, brand,model,year, availability, color, rent_price):
        self.brand = brand
        self.model = model
        self.year = year
        self.availability = availability
        self.color = color
        self.rent_price = int(rent_price)

car1 = Car("BMW", "M5", "2022", 1, "red", 1000)
car2 = Car("Malibu", "2", "2015", 1, "black", 500)
car3 = Car("Nexia", "3", "2016", 1, "white", 300)
car4 = Car("Gentra", "x2z", "2016", 1, "black", 450)
car5 = Car("Cobalt", "", "2018", 0, "blue", 300)

class Client:
    def __init__(self, name, phone, email, age, salary, user_id, user_password):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.salary = int(salary)
        self.user_id = user_id
        self.user_password = user_password
        self.balance = int(salary)
        self.rented_cars = []

    def get_rented_cars(self):
        print("-----------------------------------------------------")
        if self.rented_cars:
            count = 1
            for i in self.rented_cars:
                print(f"ID: {count}. {i.brand} {i.model} - {i.year} - {i.color} - {i.rent_price}$")
                count += 1
        else:
            print("No rented cars!")
        print("-----------------------------------------------------")

    def get_balance(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"My balance: {self.balance}$")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

cl1 = Client("Aki", "+193982387283", "aki@gmail.com", 21, "800", "00001", "Aki001")

class Admin:
    def __init__(self):
        self.admin_password = "admin"

    def add_car(self, rc: CarRent):
        brand = input("Enter car's brand: ")
        model = input("Enter car's model: ")
        year = input("Enter car's year: ")
        try:
            availability = int(input("Is it ready to be rented? (1 - Yes/0 - No): "))
        except ValueError:
            print("You had to enter an integer value! (1/0)")
        if availability == 1 or availability == 0:
            color = input("Enter car's color: ")
            rent_price = int(input("Enter car's rent price: "))
            car77 = Car(brand,model,year,availability,color,rent_price)
            rc.cars.append(car77)
            print("Successfully added!")
            print("-----------------------------------------------------------------")
        else:
            print("You can only enter 1 or 0!")

    def edit_car(self, rc: CarRent):
        rc.view_cars_info()
        car_index = int(input("\nEnter car ID: "))
        car88 = rc.cars[car_index-1]
        kod99 = input("What exactly do you want to change?\n1. Brand\n2. Model\n3. Year\n4. Color\n5. Rent Price\n6. Exit\n")
        if kod99 == "1":
            car88.brand = input("Enter the brand: ")
        elif kod99 == "2":
            car88.model = input("Enter the model: ")
        elif kod99 == "3":
            car88.year = input("Enter the year: ")
        elif kod99 == "4":
            car88.color = input("Enter the color: ")
        elif kod99 == "5":
            car88.rent_price = input("Enter the rent price: ")
        elif kod99 == "6":
            return
        else:
            print("Invalid option!")


    def view_rented_cars(self, cr: CarRent):
        print("-----------------------------------------------------")
        count = 1
        cr.rented_cars = []
        cr.available_cars = []
        for i in cr.cars:
            if not i.availability:
                print(f"ID: {count}. {i.brand} {i.model}")
                count += 1
                cr.rented_cars.append(i)
            else:
                cr.available_cars.append(i)
        print("-----------------------------------------------------")

class CarRent:
    def __init__(self):
        self.clients = [cl1]
        self.cars = [car1, car2, car3, car4, car5]
        self.user_ids = ["00001"]
        self.available_cars = []
        self.rented_cars = []

    def add_client(self):
        print("-----------------------------------------------------")
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        regex_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        regex_email = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        if re.match(regex_phone, phone):
            email = input("Enter your email: ")
            if re.match(regex_email, email):
                age = input("Enter your age: ")
                try:
                    salary = int(input("Enter your salary: "))
                except ValueError:
                    print("Salary must be an integer!\n")
                    return
                user_id = input("Enter your user ID: ")
                if user_id not in self.user_ids:
                    user_password = input("Create password: ")
                    cl = Client(name, phone, email, age, salary, user_id, user_password)
                    self.clients.append(cl)
                    self.user_ids.append(user_id)
                    print("Now you can sign in!")
                    print("-----------------------------------------------------")
                    self.sign_in()
                else:
                    print("This user id already exists!")
            else:
                print("Invalid email!\n")
                return
        else:
            print("Invalid phone number!\n")
            return

    def sign_in(self):
        u_id = input("Enter your user ID: ")
        for i in self.clients:
            if i.user_id == u_id:
                u_password = input("Enter your password: ")
                if u_password == i.user_password:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("You are logged in!")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    user_manager(self, i)
                else:
                    print("Wrong password!\n")
        if u_id not in self.user_ids:
            print("Invalid user ID!\n")

    def view_cars_info(self):
        print("-----------------------------------------------------")
        count = 1
        for i in self.cars:
            if i.availability:
                print(f"ID: {count}. {i.brand} {i.model} - {i.year} - {i.color} - {i.rent_price}$ - Ready for rent!")
            else:
                print(f"ID: {count}. {i.brand} {i.model} - {i.year} - {i.color} - {i.rent_price}$ - Already rented!")
            count += 1
        print("-----------------------------------------------------")

    def view_ready_cars(self):
        print("-----------------------------------------------------")
        count = 1
        self.available_cars = []
        self.rented_cars = []
        for i in self.cars:
            if i.availability:
                print(f"ID: {count}. {i.brand} {i.model} - {i.rent_price}$")
                count += 1
                self.available_cars.append(i)
            else:
                self.rented_cars.append(i)

        print("-----------------------------------------------------")

    def rent_car(self, client):
        self.view_ready_cars()
        chosen_car_id = int(input("Enter car ID that you want to rent: "))
        carx = self.available_cars[chosen_car_id-1]
        if int(client.balance) >= int(carx.rent_price):
            client.rented_cars.append(carx)
            self.rented_cars.append(carx)
            self.available_cars.remove(carx)
            client.balance -= int(carx.rent_price)
            for c in self.cars:
                if c == carx:
                    c.availability = 0
            print("Successfully rented!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("You don't have enough money!\n")

    def return_car(self, client):

        client.get_rented_cars()
        if client.rented_cars:
            try:
                car_id = int(input("Enter car ID that you want to return: "))
            except ValueError:
                print("Invalid car ID!\n")
                return
            car_y = client.rented_cars[car_id-1]
            client.rented_cars.remove(car_y)
            self.rented_cars.remove(car_y)
            self.available_cars.append(car_y)
            for c in self.cars:
                if c == car_y:
                    c.availability = 1
            print("Successfully returned!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")



def user_manager(cr: CarRent, client):
    while True:
        kod = input("1. View cars that are ready for rent\n2. All cars' info\n3. Rent a car\n4. Return a car\n5. View my rented cars\n6. View my balance\n7. Exit\n")
        if kod == "1":
            cr.view_ready_cars()
        elif kod == "2":
            cr.view_cars_info()
        elif kod == "3":
            cr.rent_car(client)
        elif kod == "4":
            cr.return_car(client)
        elif kod == "5":
            client.get_rented_cars()
        elif kod == "6":
            client.get_balance()
        elif kod == "7":
            break
        else:
            print("Invalid option!\n")

def admin_manager(cr: CarRent, adm):
    while True:
        kod3 = input(
            "1. Add car\n2. Edit car\n3. View all cars' information\n4. View cars - ready for rent\n5. View rented cars\n6. Exit\n")
        if kod3 == "1":
            adm.add_car(cr)
        elif kod3 == "2":
            adm.edit_car(cr)
        elif kod3 == "3":
            cr.view_cars_info()
        elif kod3 == "4":
            cr.view_ready_cars()
        elif kod3 == "5":
            adm.view_rented_cars(cr)
        elif kod3 == "6":
            break
        else:
            print("Invalid input")

def car_rent_manager():
    cr = CarRent()
    adm = Admin()
    while True:
        kod = input("1. User Page\n2. Admin Page\n3. Exit\n")
        if kod == "1":
            kod2 = input("1. Sign in\n2. Sign up\n3. Exit\n")
            if kod2 == "1":
                cr.sign_in()
            elif kod2 == "2":
                cr.add_client()
            elif kod2 == "3":
                break
            else:
                print("Invalid option!")

        elif kod == "2":
            password = input("Enter the password: ")
            if adm.admin_password == password:
                admin_manager(cr, adm)
            else:
                print("Wrong password!")

        elif kod == "3":
            break
        else:
            print("Invalid option!\n")


car_rent_manager()