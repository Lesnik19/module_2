from tkinter import *

window = Tk()
window.title('Рисовалка')
window.geometry('1500x800')
window.resizable(height=False, width=False)

canvas = Canvas(window, width=1500, height=800, background='#f0d524')
canvas.create_line(150, 250, 650, 100, fill='red', width=4)
canvas.create_rectangle(50, 50, 150, 150, fill='black', outline='red', width=4, activefill='blue')
canvas.create_oval(50, 350, 200, 450)
canvas.create_polygon(200, 100, 325, 100, 350, 150, 325, 200)
canvas.create_text(400, 400, text='Привет', font='Arial 20')
img = PhotoImage(file='Шайлушай.png')
canvas.create_image( 500, 100, image=img, anchor=NW)

canvas.pack()
window.mainloop()
