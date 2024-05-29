from abc import ABC, abstractmethod


class Shape(ABC):  # это абстрактный класс
    @abstractmethod  # декоратор
    def get_area(self):
        print('Расчёт площади фигуры')


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print('Создан прямоугольник')

    def get_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, width):
        self.width = width
        print('Создан квадрат')

    def get_area(self):
        return self.width ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        print('Круг создан')

    def get_area(self):
        return 3.14 * self.radius ** 2


rect1 = Rectangle(5, 4)
sq1 = Square(5)
ci1 = Circle(5)

shapes = [rect1, sq1, ci1]

# for shape in shapes:
#     if isinstance(shape, Rectangle):
#         print(shape.get_rect_area())
#     elif isinstance(shape, Square):
#         print(shape.get_square_area())
#     elif isinstance(shape, Circle):
#         print(shape.get_circle_area())

for shape in shapes:
    print(shape.get_area())

# полиморфизм - это возможность работы с совершенно
# разными объектами единым образов
