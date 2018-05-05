# class Tuna:
#     def __init__(self):
#         print(Brlrbblblrlrlrlrlb)
#
#     def swim(self):
#         print("I am swimming")
#
# # Error, beacuse we didn't call the constructor - "init" method
# flipper = Tuna()
# flipper.swim()

class Enemy:
    def __init__(self, hp): # hp = health pool
        self.energy = hp

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()