import tkinter as tk
import threading
import speech_recognition as sr
import random
from PIL import Image,ImageTk
import winsound


# save
ans_list={
        'Ele':['ช้าง'],
        'Leopard':['เสือดาว'] ,
        'Lion':['สิงโต'] ,
        'Owl':['นกฮูก'] ,
        'cat':['แมว'] ,
        'crocodile':['จระเข้'] ,
        'Kangaroo':['จิงโจ้'] ,
        'Duck':['เป็ด'] ,
        'Buffalo':['ควาย','กระบือ'],
        'Panda':['แพนด้า'],
        'Worm':['หนอน'],
        'koala':['โคอาล่า'],
        'Too':['เหี้ย','ตู่']
    }

images={
    'Too':Image.open("images\\Too.jpg"),
    'Panda':Image.open("images\\Panda.jpg"),
    'Worm':Image.open("images\\Worm.jpg"),
    'koala':Image.open("images\\koala.jpg"),
    'Ele':Image.open("images\\Ele.jpg"),
    'Leopard':Image.open("images\\Leopard.jpg"),
    'Lion':Image.open("images\\Lion.jpg"),
    'Owl':Image.open("images\\Owl.jpg"),
    'cat':Image.open("images\\cat.jpg"),
    'crocodile':Image.open("images\\crocodile.jpg"),
    'Kangaroo':Image.open("images\\Kangaroo.jpg"),
    'Duck':Image.open("images\\Duck.jpg"),
    'Buffalo':Image.open("images\\Buffalo.jpg")
    }
comm={
    'close':['ปิด','เลิกเล่น'],
    'next':['เปลี่ยน','ข้าม'],
    'start':['เริ่ม','เล่น','go','start']
}



### Speech Recognizer
class getvoice(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.point=0
        self.close=False
        self.next=True
        self.answer=ans_list['cat']
        self.begin=False
        self.fullscreen=False
    def run(self):
        r = sr.Recognizer()
        while True:
            while True:
                print('Say...')
                with sr.Microphone() as source:
                    audio = r.listen(source,phrase_time_limit=4)
                try:
                    print('Process...')
                    speech=r.recognize_google(audio, None,'th')
                    break
                except:
                    pass
            print(speech)
            for word in comm['start']:
                if word in speech:
                    self.begin=True
                    break
            if 'เต็มจอ' in speech:
                self.fullscreen=True
                continue
            for word in comm['next']:
                if word in speech :
                    self.next=True
                    break
            for word in self.answer:
                if word in speech:
                    self.next=True
                    self.point=self.point+1
                    break
            for word in comm['close']:
                if word in speech:
                    self.close=True
                    break
            if self.close:
                break

###update funtion
def update_gui():
    if(speech.close):
        root.destroy()
    if(speech.fullscreen):
        speech.fullscreen=False
        root.attributes('-fullscreen',True)
    if speech.begin:
        if(speech.next):
            speech.next=False
            update_img()
            update_score()
    frame1.after(100,update_gui)

def update_img():
    global img
    global last_color
    colors=list(images)
    if last_color in colors:
        colors.remove(last_color)
    key=random.choice(colors)
    last_color=key
    speech.answer=ans_list[key]
    img=ImageTk.PhotoImage(images[key])
    show_img.config(image=img)

def update_score():
    score.config(text=f'{speech.point}')

#winsound.PlaySound('test.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
###update gui
root=tk.Tk()

speech=getvoice()
speech.start()

#root.overrideredirect(1)
#root.attributes('-fullscreen',True)
root.title("Just Say !")
root.iconbitmap('myicon.ico')
root.geometry("1200x800")
frame1=tk.Frame(root)

img=tk.PhotoImage(file='animalmode.png')
last_color='-'
show_img=tk.Label(frame1,image=img,width=600,height=500)
show_img.pack(pady=20)

score=tk.Label(frame1,text='',font=("Courier", 44))
score.pack(pady=20)
frame1.pack()

frame1.after(100,update_gui)

root.mainloop()
