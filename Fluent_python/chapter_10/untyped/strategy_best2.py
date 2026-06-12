from collections import namedtuple

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


def fidelity_promo(order):
    """ 
    5% discount for customers with 1000 or more fidelity points  
    
    """  
    return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0   
    

def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0 
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1 
        return discount

def large_order_promo(order):
    """
    7% discount for orders with 10 or more distinct items
    """

    discount_items = {item.product for item in order.cart}
    if len(discount_items) >= 10:
        return order.total() * 0.7 
    
    return 0

promos = [globals()[name] for name in globals() 
          if name.endswith('_promo')
          and name != 'best_promo'
          ]

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


