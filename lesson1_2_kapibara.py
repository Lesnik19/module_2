class Capibara:
    # служебный метод
    def __init__(self, name, age, color):
        self.name = name  # свойства или атрибуты
        self.age = age
        self.color = color

    # пользовательский метод
    def eat(self):
        print('Ням, ням, ням. Мммм... какие вкусные мандарины')

    def swim(self):
        print('Буль, буль, буль')

    def sleep(self):
        print('Хррр... Вввв, Хррр... Вввв')


# объект или экземпляр класса
bora = Capibara('Боря', 3, 'коричневый')

print(bora.name, bora.age, bora.color)
