from product import Product
from register import Register
from sale import Sale

p0=Product('Washing Powder', 8)
p1=Product('Chocolate', 2)
p2=Product('Chineese veggy', 3)
p3=Product('Yoghurt', 1.5)
p4=Product('Butter', 2.25)


products =[p0,p1,p2,p3,p4]

register = Register(products)
register.buy_products()
sale = Sale(Register.buy_products())
