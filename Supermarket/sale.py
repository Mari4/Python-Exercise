
class Sale():
    def __init__(self, total):
        self.total = total


    def total_price(self):
        for item in Register.buy_products():
            total += item[0].price*item[1]
        return total

    def receipt(self):
        print( Register.buy_products[0])
