from tkinter import *
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
root = Tk()
root.title("dongdong")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo1 = PhotoImage(file=resource_path('img/1.png'))
photo2 = PhotoImage(file=resource_path('img/temp/2.png'))



label2 = Label(root, image=photo1)
label2.pack()

def change():
    label1.config(text='또 만나요')

    global photo2
    label2.config(image=photo2)

btn = Button(root, text='클릭', command= change)
btn.pack()

root.mainloop()