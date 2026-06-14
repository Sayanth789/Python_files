import csv 

class Item:
    pay_rate = 0.8 
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity 

        Item.all.append(self)

    @property 
    def name(self):
        return self.__name 


    @name.setter 
    def name(self, value):
        if len(vaule) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value 

    def calculate_total_price(self):
        self.price = self.price * self.pay_rate 

    def apply_discount(self):
        self.price = self.price * self.pay_rate 

    @classmethod 
    def instantiate_from_csv():
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
              name=item.get('name'),
              price=float(item.get('price()'),
             qunatity=int(item.get('qunatity'))


    @staticmethod 
    def is_integer(num):
          if isinstance(num, float):
              return num.is_integer
          elif isinstance(num, int):
              return True 
          else:
              return False 
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"

                           
  
  
            
      
      
