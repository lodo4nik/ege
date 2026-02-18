class Char:
    def __init__(self, hp, mana, x, y):
        self.hp = hp
        self.mana = mana
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y
        print(f"Персонаж перешел в {self.x}, {self.y}")

    def attack(self, target):
        print(f"Персонаж атакует {target}")

class Gnome(Char):
    def __init__(self, x, y):
        super().__init__(hp=150, mana=50, x=x, y=y)

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y
        print(f"Эльф перешел в {self.x}, {self.y}")

    def attack(self, target):
        print(f"Гном атакует {target}")


class Elf(Char):
    def __init__(self, x, y):
        super().__init__(hp=80, mana=200, x=x, y=y)

    def attack(self, target):
        print(f"Эльф атакует {target}")

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y
        print(f"Эльф перешел в {self.x}, {self.y}")

gnome = Gnome(0, 0)
elf = Elf(0, 0)
gnome.move(10, 13)
elf.move(30, 4)
elf.attack("малес")