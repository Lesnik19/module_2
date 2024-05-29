class Car:
    def __init__(self, model, color, build_year, car_number):
        print('Создан новый автомобиль')
        self.model = str(model)
        self.color = str(color)
        self.build_year = str(build_year)
        self.car_number = str(car_number)

    def drive(self):
        print('Автомобиль с номером', self.car_number, 'поехал')

    def print_file(self):
        file = open('passport.txt', 'w', encoding='utf8')
        file.write('Модель автомобиля: ' + self.model + '\n')
        file.write('Цвет автомобиля: ' + self.color + '\n')
        file.write('Год сборки автомобиля: ' + self.build_year + '\n')
        file.write('Номер автомобиля: ' + self.car_number + '\n')
        file.close()


model = input('Введите модель автомобиля: ')
color = input('Введите цвет автомобиля: ')
year = input('Введите год изготовления автомобиля: ')
number = input('Введите номер автомобиля: ')

car1 = Car(model, color, year, number)

car1.print_file()

# print(car1.color, car1.car_number)
#
# car1.drive()


