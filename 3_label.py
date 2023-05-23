from tkinter import *

from PIL import Image, ImageTk
import os
import sys
import requests
import datetime

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

# temp_img = Image.open(resource_path('img/1.png'))
temp_img = Image.open(resource_path('img/1.png'))
resized_temp_img = temp_img.resize((20, 20), Image.ANTIALIAS)

# photo1 = PhotoImage(file=resource_path('img/1.png'))
photo1 = ImageTk.PhotoImage(resized_temp_img)
# photo1.config(width=20, height=20)
photo2 = PhotoImage(file=resource_path('img/2.png'))      
# 그냥 path를 적어줘야하는데... 후..



label2 = Label(root, image=photo1)
label2.pack()

def change():
    label1.config(text='또 만나요')

    global photo2
    label2.config(image=photo2)

btn = Button(root, text='클릭', command= change)
btn.pack()

OWNER = 'envsensorapp'
REPO = 'test_app'

API_SERVER_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"
# access_token = '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'
MY_API_KEY = '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'


# def firmware_update():
#     res = requests.get(f"{API_SERVER_URL}/releases/latest", auth=(OWNER, MY_API_KEY))  # 
#     if res.status_code != 200:
#         print(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"), "업데이트 체크 실패")
#     print(res.json())

# update_btn = Button(root, text='업데이트', command= firmware_update)
# update_btn.pack()




root.mainloop()

