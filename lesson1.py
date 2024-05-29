class Cat:
    # конструктор класса
    def __init__(self, name, color, weight):
        print('Создали нового', color, 'котика', name)
        self.name = name
        self.color = color
        self.weight = weight

    def sey_meow(self):
        print('МЯЯЯЯУ!')

    def sey_eat(self):
        print('Жрааааать')

    def introduce(self):
        print('Меня зовут', self.name + ', мой окрас:', self.color)

    def gain_weight(self):
        self.weight += 0.1

    def lose_weight(self):
        self.weight -= 0.1


name = input('Введите имя котика: ')
color = input('Введите имя котика: ')
weight = float(input('Введите имя котика: '))

cat1 = Cat(name, color, weight)  # запускается метод __init__

cat1.introduce()
