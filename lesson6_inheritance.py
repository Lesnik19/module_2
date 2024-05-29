class Human:
    def __init__(self, level, name):
        print('Персонаж создан')
        self.level = level
        self.name = name

    def run(self):
        print('Персонаж бежит!')

    def _jump(self):
        print('Персонаж прыгает!')

    def say_hello(self):
        print('Привет! Я - персонаж по имени', self.name)


class Warrior(Human):
    def __init__(self, level, name, strength_points):
        print('Воин создан')
        super().__init__(level, name)
        self.strength_points = strength_points

    def sword_attack(self):
        print('Воин атакует мечом!')

    def say_hello(self):
        print('Дарова! Я - воин по имени', self.name)


class Mage(Human):
    def spell_attack(self):
        print('Маг бросает заклинание!')


# warrior = Warrior()
# warrior.run()
# warrior._jump()
# warrior.sword_attack()
#
# mage = Mage()
# mage.run()
# mage._jump()
# mage.spell_attack()

human = Human(12, 'serega337')
human.say_hello()

warrior = Warrior(10, 'danila882', 450)
warrior.say_hello()
