from floors import Floors
from passengers import Passengers




m=Passengers()
k=Floors()
#m.how_many_passengers()
#m.list_of_clients()
m.create_passengers()
k.list_of_floors()
m.who_goes_where()

b = Building(floor_amount = k.how_many_floors(), Passengers = m.who_goes_where())
