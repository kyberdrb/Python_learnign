class Enemy:
    # everything indented after "class" declaration belongs to that class

    life = 3

    def attack(self):   # self refers to the class itself
        print("ouch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()

enemy1.checkLife()
enemy2.checkLife()