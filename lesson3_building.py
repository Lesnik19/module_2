class Building:
    def __init__(self, color, height, flats, material, year):
        print('Здание построено')
        self.color = color
        self.height = height
        self.flats = flats
        self.material = material
        self.year = year

    def __del__(self):
        print('Здание снесено')

    def __str__(self):
        return f'Это здание {self.color} цвета. {self.height} м в высоту. В нём {self.flats} квартир'

    def __call__(self, *args, **kwargs):
        self.height += 8
        print('Здание стало выше, теперь его высота', self.height)


federation_tower = Building('blue', 374, 250, 'glass', 2017)
# del federation_tower
# print(federation_tower)

federation_tower()
federation_tower()
federation_tower()
