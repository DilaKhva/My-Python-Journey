class Products:
    def __init__(self, title, price, expiration_date, type, email, phone):
        self.title = title
        self.price = price
        self.exp_date = expiration_date
        self.type = type
        self.email = email
        self.phone = phone

product1 = Products("Tomato", "10000", "28.11.2026", 'oziq-ovqat', 'gg@gmail.com', "426382632")
product2 = Products("Potato", "15000", "29.11.2026", 'oziq-ovqat', 'gg@gmail.com', "426382632")
product3 = Products("Cucumber", "10000", "27.11.2026", 'oziq-ovqat', 'gg@gmail.com', "426382632")

baza = [product1, product2, product3]

def view_product(s:list):
    for item in s:
        print(f"Title: {item.title}\t Price: {item.price}\t Expiration Date: {item.exp_date}")

# view_product(baza)

def add_product(s:list):
    title = input("Title: ")
    price = input("Price: ")
    exp_date = input("Expiration Date: ")
    type = input("Type: ")
    email = input("Email: ")
    phone = input("Phone: ")
    product = Products(title, price, exp_date, type, email, phone)
    s.append(product)

def product_manager(s:list):
    while True:
        kod = input("\n1. View products\n2. Add product\n3. Exit\n")
        if kod == "1":
            view_product(s)
        elif kod == "2":
            add_product(s)
        elif kod == "3":
            break
        else:
            print("Invalid option!")

product_manager(baza)