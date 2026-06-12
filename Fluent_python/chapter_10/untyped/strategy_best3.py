from collections import namedtuple
import inspect 
import promotions
 


Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price 

    def total(self):
        return self.price * self.quantity
    
class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart) 
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

        return self.__total 

    def due(self):
        if self.promotion is None:
            discount = 0 
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due {self.due():.2f}'



promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]

def best_promo(order):
    """ Select best discount available """
    return max(promo(order) for promo in promos)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0),
        ]

print(Order(joe, cart, fidelity_promo))

print(Order(ann, cart, fidelity_promo))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)
               ]
print(Order(joe, banana_cart, bulk_item_promo))

long_cart = [LineItem(str(item_code), 1, 1.0)
                   for item_code in range(10)]

print(Order(ann, long_cart, large_order_promo)
      )

print(Order(joe, long_cart, large_order_promo))

print(Order(joe, long_cart, best_promo))
print(Order(joe, long_cart, best_promo))
print(Order(ann, banana_cart, best_promo))


