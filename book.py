from functools import total_ordering

@total_ordering
class Order:
    def __init__(self, quantity, price, priority, identity, buy = True):
        self.quantity = quantity
        self.price = price
        self.priority = priority
        self.identity = identity

    def is_sell(self):
        return not self.buy

    def __repr__(self):
        return "Order(%s, %s)" % (self.quantity, self.price)

    def __str__(self):
        return "%s @ %s" % (self.quantity, self.price)

    def __eq__(self, other):
        return other and self.quantity == other.quantity and self.price == other.price

    def __lt__(self, other):
        return other and self.price < other.price

    def is_priority(self, other):
        return other and self.priority < other.priority

class Book:
    def __init__(self, name):
        self.name = name
        self.buy_orders = []
        self.sell_orders = []
        self.executed_orders = []
        self.counter = 1

    def insert_order(self, quantity, price, buy = True): 
        if buy:
            priority = len(self.buy_orders) + 1
            identity = self.counter
            new_order = Order(quantity, price, priority, identity, buy)
            if len(self.buy_orders) == 0:
                self.buy_orders.append(new_order)
            else:
                for i in range(len(self.buy_orders)):
                    order_iter = self.buy_orders[i]
                    if new_order.price > order_iter.price:
                        self.buy_orders.insert(i, new_order)
                        break
                    elif i == len(self.buy_orders) - 1 :
                        self.buy_orders.append(new_order)
            print("---Insert BUY", new_order, "id=", new_order.identity, "on", self.name, '\n')

        else: # if the new order is a sell order
            priority = len(self.sell_orders) + 1
            identity = self.counter
            new_order = Order(quantity, price, priority, identity, buy)
            if len(self.sell_orders) == 0:
                self.sell_orders.append(new_order)
            else:
                for i in range(len(self.sell_orders)):
                    order_iter = self.sell_orders[i]
                    if new_order.price < order_iter.price:
                        self.sell_orders.insert(i, new_order)
                        break
                    elif i == len(self.sell_orders) - 1:
                        self.sell_orders.append(new_order)
            print("---Insert SELL", new_order, "id=", new_order.identity, "on", self.name, '\n')

        self.executed()
        print("Book on", self.name, '\n')
        for sell_order_iter in self.sell_orders:
            print("SELL", sell_order_iter, "id=", sell_order_iter.identity, '\n')
        for buy_order_iter in self.buy_orders:
            print("BUY", buy_order_iter, "id=", buy_order_iter.identity, '\n')
        print("------------------------", '\n')
        self.counter +=1


    def executed(self):
        while ((self.buy_orders != [] and self.sell_orders!= []) and (self.buy_orders[0] >= self.sell_orders[0])):
            if self.buy_orders[0].quantity < self.sell_orders[0].quantity:
                self.executed_orders.append([self.buy_orders[0].quantity, self.buy_orders[0].price])
                print("Execute", self.buy_orders[0].quantity, "at", self.buy_orders[0].price, "on", self.name, '\n')
                self.sell_orders[0].quantity = self.sell_orders[0].quantity - self.buy_orders[0].quantity 
                del self.buy_orders[0]

            elif self.buy_orders[0].quantity > self.sell_orders[0].quantity:
                self.executed_orders.append([self.sell_orders[0].quantity, self.buy_orders[0].price])
                print("Execute", self.sell_orders[0].quantity, "at", self.buy_orders[0].price, "on", self.name, '\n')
                self.buy_orders[0].quantity = self.buy_orders[0].quantity - self.sell_orders[0].quantity 
                del self.sell_orders[0]

            else:
                self.executed_orders.append([self.sell_orders[0].quantity, self.buy_orders[0].price])
                print("Execute", self.sell_orders[0].quantity, "at", self.buy_orders[0].price, "on", self.name, '\n')
                del self.sell_orders[0]
                del self.buy_orders[0]







