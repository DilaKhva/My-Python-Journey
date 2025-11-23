class Product:
    def __init__(self, title, price, year):
        self.title = title
        self.price = price
        self.year = year
        self.type = ''

class Shop:
    def __init__(self, title, phone):
        self.title = title
        self.phone = phone
        self.baza = []

    def add_drink(self):
        title = input("Title: ")
        price = input("Price: ")
        year = input("Year: ")
        product = Product(title, price, year)
        product.type = "drink"
        self.baza.append(product)


    def add_food(self):
        title = input("Title: ")
        price = input("Price: ")
        year = input("Year: ")
        product = Product(title, price, year)
        product.type = "food"
        self.baza.append(product)

    def view_products(self):
        for product in self.baza:
            print(f"Title: {product.title}, Price: {product.price}, Type: {product.type}")
        print(self.baza)


    def view_drinks(self):
        for product in self.baza:
            if product.type == "drink":
                print(f"Title: {product.title}, Price: {product.price}, Type: {product.type}")

    def view_food(self):
        for product in self.baza:
            if product.type == "food":
                print(f"Title: {product.title}, Price: {product.price}, Type: {product.type}")

    def delete_product(self):
        deleted_product = input("Enter the title of product that you want to delete: ")
        titles = []
        for product in self.baza:
            titles.append(product.title)
            if deleted_product == product.title:
                self.baza.remove(product)
                print("Successfully deleted!")
        if title_for_edit not in titles:
            print("Invalid title!")

    def edit_product(self):
        title_for_edit = input("Enter the title of product that you want to edit: ")
        titles = []
        for product in self.baza:
            titles.append(product.title)
            if product.title == title_for_edit:
                for_edit = input(f"What exactly do you want to edit: 1. Title. 2. Price. 3. Year\n")
                if for_edit == "1":
                    new_title = input("Enter a new title: ")
                    product.title = new_title
                    print("Successfully edited!")
                elif for_edit == "2":
                    new_price = input("Enter a new price: ")
                    product.price = new_price
                    print("Successfully edited!")
                elif for_edit == "3":
                    new_year = input("Enter a new year: ")
                    product.year = new_year
                    print("Successfully edited!")
                else:
                    print("Invalid option!")
        if title_for_edit not in titles:
            print("Invalid title!")



shop1 = Shop("BeeShop", "2837472739")
# print(shop1.baza)

def shop_manager(sh1):
    while True:
        kod = input("\n1. Add drinks\n2. Add foods\n3. View all products\n4. View only food\n5. View only drinks\n6. Delete product\n7. Update product\n8. Exit\n")
        if kod == "1":
            sh1.add_drink()
        elif kod == "2":
            sh1.add_food()
        elif kod == "3":
            sh1.view_products()
        elif kod == "4":
            sh1.view_food()
        elif kod == "5":
            sh1.view_drinks()
        elif kod == "6":
            sh1.delete_product()
        elif kod == "7":
            sh1.edit_product()
        elif kod == "8":
            break
        else:
            print("Invalid option!")

shop_manager(shop1)