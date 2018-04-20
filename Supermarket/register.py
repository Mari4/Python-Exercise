from product import Product
from dicount import Discount

class Register():
        def __init__(self, products):
            self.products = products

        def sell_products(self):
            self.shopping_cart = [(self.products[0],2),(self.products[1],1),(self.products[2],1),(self.products[3],2),(self.products[4],4) ]

        def total_price(self):
            total_price = 0.0
            for item in self.shopping_cart:
                total_price += item[0].price*item[1]
            return total_price

        # def apply_discounts(self, available_discounts):
        #     self.discounts = []
        #     for item in self.shopping_cart:
        #         for discount in available_discounts:
        #             if (discount.is_applicable(item)):
        #                 self.discounts.append(discount)
        #                 print(self.discounts)



        def print_receipt(self):
            total_price = 0.0
            for item in self.shopping_cart:
                print("%s | %.2f x %d | total: %.2f" % (item[0].name, item[0].price, item[1], item[0].price*item[1))
            print('total price: ' + str(total_price))

        






# if __name__ = '__main__'
#     register = Register()
#     print('hello')
