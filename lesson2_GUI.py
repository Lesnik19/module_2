import tkinter

window = tkinter.Tk()
window.title('Моё окно')
window.geometry('500x500')
window.resizable(height=False, width=False)

# сделать флаг России
canvas = tkinter.Canvas(window, width=500, height=500, background='green')
canvas.create_rectangle(50, 50, 450, 300, fill='red')

canvas.pack()
window.mainloop()
