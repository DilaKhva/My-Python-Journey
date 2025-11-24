class Product:
    def __init__(self, title, price, id):
        self.title = title
        self.price = price
        self.id = id


class Tv(Product):
    def __init__(self, title, price, id, size, smart):
        super().__init__(title, price, id)
        self.size = size
        self.smart = smart
        self.type = "tv"


class Phone(Product):
    def __init__(self, title, price, id, camera, storage):
        super().__init__(title, price, id)
        self.camera = camera
        self.storage = storage
        self.type = "phone"


class Laptop(Product):
    def __init__(self, title, price, id, RAM, CPU):
        super().__init__(title, price, id)
        self.RAM = RAM
        self.CPU = CPU
        self.type = "laptop"


class Shop():
    def __init__(self, name):
        self.name = name
        self.baza = []

    def add_tv(self):
        id = input("Enter a id: ")
        ids = []
        for i in self.baza:
            ids.append(i.id)
        if id not in ids:
            title = input("Enter a title: ")
            price = input("Enter a price: ")
            size = input("Enter a size: ")
            smart = input("Enter a smart(True or False): ")
            tv = Tv(title, price, id, size, smart)
            self.baza.append(tv)
            print("Successfully added!")
        else:
            print("Invalid id.")
            print("Please enter an unique id.\n")


    def add_laptop(self):
        id = input("Enter a id: ")
        ids = []
        for i in self.baza:
            ids.append(i.id)
        if id not in ids:
            title = input("Enter a title: ")
            price = input("Enter a price: ")
            RAM = input("Enter its RAM: ")
            CPU = input("Enter its CPU: ")
            lap = Laptop(title, price, id, RAM, CPU)
            self.baza.append(lap)
            print("Successfully added!")
        else:
            print("Invalid id.")
            print("Please enter an unique id.\n")

    def add_phone(self):
        id = input("Enter a id: ")
        ids = []
        for i in self.baza:
            ids.append(i.id)
        if id not in ids:
            title = input("Enter a title: ")
            price = input("Enter a price: ")
            cam = input("Camera: ")
            storage = input("Storage: ")
            phone = Phone(title, price, id, cam, storage)
            self.baza.append(phone)
            print("Successfully added!")
        else:
            print("Invalid id.")
            print("Please enter an unique id.\n")

    def view_phone(self):
        print("---------------------------------------------------------------------")
        if self.baza:
            for i in self.baza:

                if i.type == "phone":
                    print(f"ID: {i.id} - {i.title} - {i.price}$ - cam: {i.camera} - storage: {i.storage}")
        else:
            print("No data found!")
        print("---------------------------------------------------------------------")

    def view_tv(self):
        print("---------------------------------------------------------------------")
        if self.baza:
            for i in self.baza:
                if i.type == "tv":
                    print(f"ID: {i.id} - {i.title} - {i.price}$ - size: {i.size} - smart: {i.smart}")
        else:
            print("No data found!")
        print("---------------------------------------------------------------------")

    def view_laptop(self):
        print("---------------------------------------------------------------------")
        if self.baza:
            for i in self.baza:
                if i.type == "laptop":
                    print(f"ID: {i.id} - {i.title} - {i.price}$ - RAM: {i.RAM} - CPU: {i.CPU}")
        else:
            print("No data found!")
        print("---------------------------------------------------------------------")

    def edit_tv(self):
        id = input("Enter the id of tv you want to edit: ")
        ids = []
        for ik in self.baza:
            ids.append(ik.id)
        if id in ids:
            part = input("What exactly do you want to change? \n1. id\n2. title\n3. price\n4. size\n5. smart\n")
            if part == "1":
                new_id = input("Enter a new id: ")
                for i in self.baza:
                    if i.id == id:
                        i.id = new_id
                        print("Successfully changed!")
            elif part == "2":
                new_title = input("Enter a new title: ")
                for i in self.baza:
                    if i.id == id:
                        i.title = new_title
                        print("Successfully changed!")
            elif part == "3":
                new_price = input("Enter a new price: ")
                for i in self.baza:
                    if i.id == id:
                        i.price = new_price
                        print("Successfully changed!")
            elif part == "4":
                new_size = input("Enter a new size: ")
                for i in self.baza:
                    if i.id == id:
                        i.size = new_size
                        print("Successfully changed!")
            elif part == "5":
                new_smart = input("It is smart (True/False): ")
                for i in self.baza:
                    if i.id == id:
                        i.smart = new_smart
                        print("Successfully changed!")
            else:
                print("Invalid option!")

        else:
            print("Invalid id.")

    def edit_laptop(self):
        id = input("Enter the id of laptop you want to edit: ")
        ids = []
        for ik in self.baza:
            ids.append(ik.id)
        if id in ids:
            part = input("What exactly do you want to change? \n1. id\n2. title\n3. price\n4. ram\n5. cpu\n")
            if part == "1":
                new_id = input("Enter a new id: ")
                for i in self.baza:
                    if i.id == id:
                        i.id = new_id
                        print("Successfully changed!")
            elif part == "2":
                new_title = input("Enter a new title: ")
                for i in self.baza:
                    if i.id == id:
                        i.title = new_title
                        print("Successfully changed!")
            elif part == "3":
                new_price = input("Enter a new price: ")
                for i in self.baza:
                    if i.id == id:
                        i.price = new_price
                        print("Successfully changed!")
            elif part == "4":
                new_ram = input("Enter a new ram: ")
                for i in self.baza:
                    if i.id == id:
                        i.ram = new_ram
                        print("Successfully changed!")
            elif part == "5":
                new_cpu = input("Enter a new cpu: ")
                for i in self.baza:
                    if i.id == id:
                        i.smart = new_cpu
                        print("Successfully changed!")
            else:
                print("Invalid option!")

        else:
            print("Invalid id.")

    def edit_phone(self):
        id = input("Enter the id of phone you want to edit: ")
        ids = []
        for ik in self.baza:
            ids.append(ik.id)
        if id in ids:
            part = input("What exactly do you want to change? \n1. id\n2. title\n3. price\n4. camera\n5. storage\n")
            if part == "1":
                new_id = input("Enter a new id: ")
                for i in self.baza:
                    if i.id == id:
                        i.id = new_id
                        print("Successfully changed!")
            elif part == "2":
                new_title = input("Enter a new title: ")
                for i in self.baza:
                    if i.id == id:
                        i.title = new_title
                        print("Successfully changed!")
            elif part == "3":
                new_price = input("Enter a new price: ")
                for i in self.baza:
                    if i.id == id:
                        i.price = new_price
                        print("Successfully changed!")
            elif part == "4":
                new_cam = input("Camera: ")
                for i in self.baza:
                    if i.id == id:
                        i.camera = new_cam
                        print("Successfully changed!")
            elif part == "5":
                new_storage = input("Storage: ")
                for i in self.baza:
                    if i.id == id:
                        i.storage = new_storage
                        print("Successfully changed!")
            else:
                print("Invalid option!")

        else:
            print("Invalid id.")

    def delete_tv(self):
        id = input("Enter the id of tv you want to delete: ")
        ids = []
        for ik in self.baza:
            ids.append(ik.id)
        if id in ids:
            for i in self.baza:
                if i.id == id:
                    self.baza.remove(i)
                    print("Successfully deleted!")
        else:
            print("Invalid id.")

    def delete_phone(self):
        id = input("Enter the id of phone you want to delete: ")
        ids = []
        for ik in self.baza:
            ids.append(ik.id)
        if id in ids:
            for i in self.baza:
                if i.id == id:
                    self.baza.remove(i)
                    print("Successfully deleted!")

        else:
            print("Invalid id.")

    def delete_laptop(self):
        id = input("Enter the id of laptop you want to delete: ")
        ids = []
        for ik in self.baza:
            ids.append(ik.id)
        if id in ids:
            for i in self.baza:
                if i.id == id:
                    self.baza.remove(i)
                    print("Successfully deleted!")
        else:
            print("Invalid id.")

    def view_all(self):
        print("---------------------------------------------------------------------")
        if self.baza:
            for i in self.baza:
                print(f"ID: {i.id} - {i.title} - {i.price}$ - type: {i.type}")
        else:
            print("No data found!")
        print("---------------------------------------------------------------------")


def shop_manager():
    sh = Shop("Market")
    while True:
        kod = input("1. Add TV\n2. Add Laptop\n3. Add Phone\n4. View all\n5. View Tv\n6. View Laptop\n7. View Phone\n8. Edit TV\n9. Edit Laptop\n10. Edit Phone\n11. Delete TV\n12. Delete Laptop\n13. Delete Phone\n14. Exit\n")
        if kod == "1":
            sh.add_tv()
        elif kod == "2":
            sh.add_laptop()
        elif kod == "3":
            sh.add_phone()
        elif kod == "4":
            sh.view_all()
        elif kod == "5":
            sh.view_tv()
        elif kod == "6":
            sh.view_laptop()
        elif kod == "7":
            sh.view_phone()
        elif kod == "8":
            sh.edit_tv()
        elif kod == "9":
            sh.edit_laptop()
        elif kod == "10":
            sh.edit_phone()
        elif kod == "11":
            sh.delete_tv()
        elif kod == "12":
            sh.delete_laptop()
        elif kod == "13":
            sh.delete_phone()
        elif kod == "14":
            break
        else:
            print("Invalid option!")

shop_manager()