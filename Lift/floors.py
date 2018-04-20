class Floors:

    def how_many_floors(self):
        self.floor_amount=input("How many floors the building has?")
        try:
            val = int(self.floor_amount)
        except ValueError:
            print("Please give a number!")
            self.floor_amount=input("How many floors the building has?")
        print("The building has "+ str(self.floor_amount) + " floors")
        return self.floor_amount

    def list_of_floors(self):
        floor = "f"
        list_of_floors = list("f"*int(self.how_many_floors()))
        print (list_of_floors)

#k=Floors()
# #n.how_many_floors()
# n.list_of_floors()
