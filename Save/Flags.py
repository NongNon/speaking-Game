import tkinter as tk
import threading
import speech_recognition as sr
import random
from PIL import Image,ImageTk
import winsound


# save
ans_list={
        'flag1':['พม่า','เมียนมาร์'],
        'flag2':['ลาว'] ,
        'flag3':['มาเลเซีย'] ,
        'flag4':['กัมพูชา','เขมร'] ,
        'flag5':['ไทย'] ,
        'flag6':['เยอรมัน'] ,
        'flag7':['เกาหลีใต้'] ,
        'flag8':['แคนาดา','Canada'] ,
        'flag9':['จีน'],
        'flag10':['บราซิล']
    }

images={
    'flag1':Image.open("images\\flag1.png"),
    'flag2':Image.open("images\\flag2.png"),
    'flag3':Image.open("images\\flag3.png"),
    'flag4':Image.open("images\\flag4.png"),
    'flag5':Image.open("images\\flag5.png"),
    'flag6':Image.open("images\\flag6.png"),
    'flag7':Image.open("images\\flag7.png"),
    'flag8':Image.open("images\\flag8.png"),
    'flag9':Image.open("images\\flag9.png"),
    'flag10':Image.open("images\\flag10.png")
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
        self.answer=ans_list['flag1']
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
root.title("Let Say I")
root.iconbitmap('myicon.ico')
root.geometry("1200x800")
frame1=tk.Frame(root)

img=tk.PhotoImage(file='images\\flag.png')
last_color='-'
show_img=tk.Label(frame1,image=img,width=800,height=600)
show_img.pack(pady=20)

score=tk.Label(frame1,text='',font=("Courier", 44))
score.pack(pady=20)
frame1.pack()

frame1.after(100,update_gui)

root.mainloop()
