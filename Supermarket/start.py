from product import Product
from register import Register
from sale import Sale

p0=Product('Washing Powder', 8)
p1=Product('Chocolate', 2)
p2=Product('Chineese veggy', 3)
p3=Product('Yoghurt', 1.5)
p4=Product('Butter', 2.25)


products =[p0,p1,p2,p3,p4]


# d1=Discount()
# d2=Discount()
# d3=Discount()
#
# available_discounts = [d1,d2,d3]

register = Register(products, discounts)
register.sell_products()
register.apply_discounts(available_discounts)
register.print_receipt()
# sale = Sale(Register.buy_products())
