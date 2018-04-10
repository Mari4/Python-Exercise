from product import Product

class Register():

        def __init__(self, products):
            self.products = products
            #self.amount = amount

        def buy_products(self):
            self.shopping_cart = [(self.products[0],2),(self.products[1],1),(self.products[2],1),(self.products[3],2),(self.products[4],4) ]
            print('hello')

# if __name__ = '__main__'
#     register = Register()
#     print('hello')
