import json


def lets_read():
    try:
        with open("mahsulotlar.json", 'r')as f:
            return json.load(f)
    except:
        return False


def lets_write(d):
    with open("mahsulotlar.json", 'w') as f:
        json.dump(d, f, indent=4)


def lets_view(i):
    data = lets_read()
    print("\nLIST OF "+i.upper()+":\n")
    if data:
        for k,v in data.items():
            # print(f"{k}. {v}")
            j = 0
            if v['type'] == i:
                for k,v in v.items():
                    j += 1
                    print(f"{k.title()}: {v}")
                    if j == 5:
                        print("\n")
            elif i == "all":
                for k,v in v.items():
                    j += 1
                    print(f"{k.title()}: {v}", end="\t\t")
                    if j == 5:
                        print("")

    else:
        print("no items!")
    print()
# lets_view("all")


def add_items(i):
    data = lets_read()
    l = []
    if data:
        for k,v in data.items():
            if v['type'] == i:
                for j in v.keys():
                    if j != "title" and j != "type" and j != "price":
                        l.append(j)
        featues = list(set(l))
        # print(featues)
        id = input("ID: ")
        title = input("Title: ")
        price = input("Price: ")
        feature1 = input(f"{featues[0].title()}: ")
        feature2 = input(f"{featues[1].title()}: ")


        s = {
            id: {
                "title": title,
                "price": price,
                "type": i,
                featues[0]: feature1,
                featues[1]: feature2
            }
        }

        # print(s)
        data.update(s)
        lets_write(data)
    else:
        print("no items!")
    print()



# add_items('phones')

def update_items(i):
    data = lets_read()
    l = []
    if data:
        for k, v in data.items():
            if v['type'] == i:
                for j in v.keys():
                    if j != "title" and j != "type" and j != "price":
                        l.append(j)
        featues = list(set(l))
        id = input("Enter the id of item that you want to update: \n")
        print()
        if id in data.keys():

            ch = input(f"What do you want to change?\n1. title\n2. price\n3. id\n4. {featues[0]}\n5. {featues[1]}\n6. delete the item\n\n")
            if ch == "1":
                new_t = input("new title: ")
                data[id]["title"] = new_t
            elif ch == "2":
                new_p = input("new price: ")
                data[id]["price"] = new_p
            elif ch == "3":
                new_id = input("new id: ")
                data[id]["id"] = new_id
            elif ch == "4":
                feature0 = input(f"{featues[0]}: ")
                data[id][featues[0]] = feature0
            elif ch == "5":
                feature1 = input(f"{featues[1]}: ")
                data[id][featues[1]] = feature1
            elif ch == "6":
                data.pop(id)
            else:
                print("invalid input!")
                return

            lets_write(data)
        else:
            print("Couldn't find this id!\nTry again\n")
            return


    else:
        print("no items!")
    print()

# update_items("tvs")


def katalog(i):

    b = input(f"1. view list\n2. add item\n3. update\n4. back\n\n")
    if b == "1":
        lets_view(i)
    elif b == "2":
        add_items(i)
    elif b == "3":
        update_items(i)
    elif b == "4":
        return
    else:
        print("Please enter a valid option(1/2/3/4/5)\n")


def shop_m():

    while True:
        a = input("\n1. phones\n2. tvs\n3. laptops\n4. all\n5. exit\n\n")
        if a == "1":
            item = "phones"
            katalog(item)
        elif a == "2":
            item = 'tvs'
            katalog(item)
        elif a == "3":
            item = 'laptops'
            katalog(item)
        elif a == "4":
            item = 'all'
            lets_view(item)
        elif a == "5":
            break
        else:
            print("Please enter a valid option(1/2/3/4/5)\n")
            return


shop_m()

