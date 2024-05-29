from tkinter import *
from tkinter.ttk import Combobox


class My_combobox:
    def __init__(self, list, font, x, y, width):
        self.list = list
        self.font = font
        self.x = x
        self.y = y
        self.width = width

        self.combobox = Combobox(values=self.list, font=self.font, state='readonly')
        self.combobox.place(x=self.x, y=self.y, width=self.width)


class My_button:
    def __init__(self, text, font, x, y, width, command):
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.command = command

        self.button = Button(text=self.text, font=self.font, command=self.command)
        self.button.place(x=self.x, y=self.y, width=self.width)


class My_label:
    def __init__(self, text, font, x, y, color):
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.color = color

        self.label = Label(text=self.text, font=self.font, background=self.color)
        self.label.place(x=self.x, y=self.y)


class My_entry:
    def __init__(self, font, x, y, width):
        self.font = font
        self.x = x
        self.y = y
        self.width = width

        self.entry = Entry(font=self.font)
        self.entry.place(x=self.x, y=self.y, width=self.width)


class Window:
    def __init__(self):
        self.canvas = None
        self.window = Tk()
        self.width = 700
        self.height = 700
        self.color = '#0066CC'  # 0520CC 007dd1 0066CC

        self.window.geometry(f'{self.width}x{self.height}')
        self.window.title('Автосервис CAR-CARICH')
        self.window.resizable(height=False, width=False)

        self.create_canvas()
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.create_comboboxes()
        self.window.mainloop()

    def create_canvas(self):
        self.canvas = Canvas(
            self.window,
            width=self.width,
            height=self.height,
            background=self.color)

        self.canvas.pack()

    def create_labels(self):
        My_label('Автосервис CAR-CARICH', 'Arial20', 250, 50, color=self.color)

        My_label('Марка автомобиля: ', 'Arial16', 40, 150, color=self.color)
        My_label('Модель автомобиля: ', 'Arial16', 40, 200, color=self.color)
        My_label('Цвет: ', 'Arial16', 40, 250, color=self.color)
        My_label('Год производства: ', 'Arial16', 40, 300, color=self.color)
        My_label('Номер автомобиля: ', 'Arial16', 40, 350, color=self.color)
        My_label('Выберите услугу', 'Arial16', 500, 150, color=self.color)

    def create_entries(self):
        self.brand = My_entry(font='Arial 16', x=250, y=150, width=200)
        self.model = My_entry(font='Arial 16', x=250, y=200, width=200)
        self.car_color = My_entry(font='Arial 16', x=250, y=250, width=200)
        self.year = My_entry(font='Arial 16', x=250, y=300, width=200)
        self.number = My_entry(font='Arial 16', x=250, y=350, width=200)

    def create_buttons(self):
        My_button('Записать', font='Arial 16', x=500, y=500, width=100, command=self.record_information)

    def create_comboboxes(self):
        list = ['Замена детали',
                'Технический осмотр',
                'Покраска',
                'Ремонт детали',
                'Замена масла',
                'Замена шин',
                'Мойка']
        self.service = My_combobox(list=list, font='Arial 14', x=460, y=200, width=230)

    def record_information(self):
        print('Кнопка нажата')
        self.brand_value = self.brand.entry.get()
        self.model_value = self.model.entry.get()
        self.car_color_value = self.car_color.entry.get()
        self.year_value = self.year.entry.get()
        self.number_value = self.number.entry.get()

    def print_file(self):
        file = open('car_information.txt', 'w', encoding='utf8')
        file.write('Марка автомобиля: ' + self.brand_value + '\n')
        file.write('Модель автомобиля: ' + self.model_value + '\n')
        file.write('Цвет автомобиля: ' + self.car_color_value + '\n')
        file.write('Год сборки автомобиля: ' + self.year_value + '\n')
        file.write('Номер автомобиля: ' + self.number_value + '\n')
        file.close()


window = Window()
window.print_file()
