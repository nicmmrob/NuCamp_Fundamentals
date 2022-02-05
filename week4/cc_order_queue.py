class Queue:  # using python lists instead of node linked list
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:  # this creates the class for what the objects will be instantiated from
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    # this is a method the instances will use to take an order
    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops

        # if flavor in self.flavor and (self.scoops >= 1 and self.scoops <= 3):
        #     print("Order created!")

        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor.")

        elif scoops < 1 or scoops > 3:
            print("Choose between 1-3 scoops.")

        else:
            print("Order created!")

        order = {"customer": customer,
                 "flavor": flavor, "scoops": scoops}

        self.orders.enqueue(order)

    # this is a method the instances will use to show all the pending orders
    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for items in self.orders.items:
            print("Customer: ", items["customer"], " -- Flavor: ",
                  items["flavor"], " -- Scoops: ", items["scoops"])

    def next_order(self):  # this is a method the instances will use to show the remaining orders
        print("\nNext Order Up!:")
        next = self.orders.dequeue()
        print("Customer: ", next["customer"], " -- Flavor: ",
              next["flavor"], " -- Scoops: ", next["scoops"])


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
