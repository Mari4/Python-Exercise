from floors import Floors
import random



class Passengers:

    def how_many_passengers(self):
        passengers_amount=input("How many people is waiting for the lift?")
        try:
            val = int(passengers_amount)
        except ValueError:
            print("Please give a number!")
            passengers_amount=input("How many people is waiting for the lift?")
        print(str(passengers_amount)+" people is waiting for the lift!")
        return passengers_amount

    def create_passengers(self):
        person="p"
        passengers = "p"*int(self.how_many_passengers())
        self.list_of_passengers=list(passengers)
        print(self.list_of_passengers)
        return self.list_of_passengers

#
# class Passenger:
#
#     def __init__=(self,id,trip=(0,0)):
#         self.id = id
#         self.trip = trip

    def who_goes_where(self):
        self.travel_plans = {}
        k=Floors()
        max_floor = int(k.how_many_floors())
        for i,p in enumerate(self.list_of_passengers):
            p={}
            print(max_floor)
            get_in = random.randrange(0,max_floor)
            get_out= random.randrange(0,max_floor)
            print(get_in,get_out)
            p[i] = (get_in, get_out)
            self.travel_plans.update(p)
        print(self.travel_plans)
        return self.travel_plans
# #
# k=Floors()
#
# m=Passengers()
# #m.how_many_passengers()
# #m.list_of_clients()
# m.create_passengers()
# k.list_of_floors()
# m.who_goes_where()
