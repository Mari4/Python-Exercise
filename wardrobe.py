class Wardrobe:

    def __init__(self, material=["wood", "carbon", "glass"], name='', status= 'close'):
        self.material = material
        self.name = name
        self.status = status

    def open(self):
        '''
        Function checks the status of the wardrobe.
        If it's broken it can't do anything
        If the wardrobe is closed it can open itself.
        It confirm the action with the print
        '''
        if self.status == "broken":
            print("I can't do anything. The wardbrode is broken")
        else:
            self.status = "open"
            print("The wardrobe is "+ self.status)

    def close(self):
        '''
        Function checks the status of the wardrobe.
        If the wardrobe is open it can close itself.
        If it's not open it checks if it's broken.
        If it's not neither broke or open it informs it has to be open first.
        It confirm the action with the print.
        '''
        if self.status == "open":
            self.status = "close"
            print("The wardrobe is "+ self.status)
        elif self.status == "broken":
            print("I can't do anything. The wardbrode is broken")
        else:
            print("The wardrobe was not open!")

    def get_in(self):
        '''
        Function checks the status of the wardrobe.
        If it's broken it can't do anything
        If the wardrobe is not broken someone can get in to wardrobe.
        It confirm the action with the print.
        '''

        if self.status == "broken":
            print("I can't do anything. The wardbrode is broken")
        else:
            self.status = "someone in"
            print(self.status)

    def get_out(self):
        '''
        Function checks the status of the wardrobe.
        If there is someone in the wardrobe, then he can get out.
        If nobody is in it checks if it's broken.
        If it's not neither broke or someone in it informs nobody in.
        It confirm the action with the print.
        '''

        if self.status == "someone in":
            self.status = "someone out"
            print(self.status)
        elif self.status == "broken":
            print("I can't do anything. The wardbrode is broken")
        else:
            print("Nobody in the wordrobe!")

    def kick(self):
        '''
        If you kick the wardrobe it checks what material it's made of.
        Depends on material it can break or not.
        If it can break it changes status to broken, so not other action can be executed.
        '''

        for i in self.material:
            if self.material == 'wood' or self.material =='glass':
                print("The wardrobe is broken!")
                self.status = "broken"
                break
            elif self.material == 'carbon':
                print("Don't kick me! It's rude!")
                break
            else:
                print("I don't know what I'm made of but kicking is rude!")


# w = Wardrobe("metal","closet")
# w.kick()
# w.open()
# w.close()
# w.get_in()
# w.get_out()
