import tkinter as tk                #
from PIL import Image,ImageTk       # import module

from Configy import Gui_Image

class Main(tk.Tk):
    def __init__(self,con):
        tk.Tk.__init__(self);
        self.conny=con              # เพื่อ เก็บ obj ที่ใช้ติดต่อ
        self._frame = None          # เพื่อ เก็บ obj_Frame ที่แสดงผลอยู่
        self.go_menu()              # สั่งให้ไปmenu
        #self.switch_frame(EndGame)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self);
        if self._frame is not None:
            self._frame.destroy();
        self._frame = new_frame;
        self._frame.place(x=0,y=0);

    def go_menu(self):
        self.switch_frame(Menu) # เปลี่ยน frame เป็น menu
        self.update_menu()      # ให้วนลูปใน update เพื่อโต้ตอบกับ Controll

    def update_menu(self):
        self._frame.Show_Speech.config(text=self.conny.Gui_speech)
        if (self.conny.GuiConfig_Menu['quit']==True):
            self.quit();
            return
        if (self.conny.GuiConfig_Menu['go']==True):
            self.go_game();
            return

        if (self.conny.GuiConfig_Menu['change_hl']==True):
            self.up_menu_highlight();
            self.conny.GuiConfig_Menu['change_hl']=False

        self._frame.after(100,self.update_menu)

    def up_menu_highlight(self):
        x=self.conny.GuiConfig_Menu['selec_mode']
        if(x==1):
            self._frame.Color_mode.config(bg="#00B0FF")
            self._frame.Advance_mode.config(bg="#fdd1d0")
            self._frame.Animal_mode.config(bg="#fdd1d0")
            self._frame.Flag_mode.config(bg="#fdd1d0")
            self.img_info=ImageTk.PhotoImage(Gui_Image.Menu['color_info']);
            self._frame.Show_Info.config(image=self.img_info)
        if(x==2):
            self._frame.Color_mode.config(bg="#fdd1d0")
            self._frame.Advance_mode.config(bg="#00B0FF")
            self._frame.Animal_mode.config(bg="#fdd1d0")
            self._frame.Flag_mode.config(bg="#fdd1d0")
            self.img_info=ImageTk.PhotoImage(Gui_Image.Menu['advance_info']);
            self._frame.Show_Info.config(image=self.img_info)
        if(x==3):
            self._frame.Color_mode.config(bg="#fdd1d0")
            self._frame.Advance_mode.config(bg="#fdd1d0")
            self._frame.Animal_mode.config(bg="#00B0FF")
            self._frame.Flag_mode.config(bg="#fdd1d0")
            self.img_info=ImageTk.PhotoImage(Gui_Image.Menu['animal_info']);
            self._frame.Show_Info.config(image=self.img_info)
        if(x==4):
            self._frame.Color_mode.config(bg="#fdd1d0")
            self._frame.Advance_mode.config(bg="#fdd1d0")
            self._frame.Animal_mode.config(bg="#fdd1d0")
            self._frame.Flag_mode.config(bg="#00B0FF")
            self.img_info=ImageTk.PhotoImage(Gui_Image.Menu['flag_info']);
            self._frame.Show_Info.config(image=self.img_info)

    def go_game(self):
        self.Number=1;
        self.switch_frame(Game)
        self.update_game()

    def update_game(self):
        self._frame.Show_Speech.config(text=self.conny.Gui_speech)
        if (self.conny.GuiConfig_Game['quit']==True):
            self.go_menu();
            return
        if (self.conny.GuiConfig_Game['change_image']==True):
            self._frame.Show_Number.config(text=str(self.Number))
            self._frame.Show_Score.config(text=str(self.conny.GuiConfig_Game['score']))
            self.game_image=ImageTk.PhotoImage((self.conny.GuiConfig_Game['image']).resize((720,540),Image.ANTIALIAS))
            self._frame.Show_image.config(image=self.game_image)
            self.conny.GuiConfig_Game['change_image']=False
            self.Number=self.Number+1;
        if (self.conny.GuiConfig_Game['end']==True):
            self.go_end();
            return
        self._frame.after(100,self.update_game)

    def go_end(self):
        self.switch_frame(EndGame)
        self._frame.Show_Score.config(text=str(self.conny.GuiConfig_End['score']))
        self.update_end()

    def update_end(self):
        self._frame.Show_Speech.config(text=self.conny.Gui_speech)
        if (self.conny.GuiConfig_End['menu']==True):
            self.go_menu();
            return
        if (self.conny.GuiConfig_End['again']==True):
            self.go_game();
            return
        self._frame.after(100,self.update_end)

class MyFrame(tk.Frame):
    def background1(self, master):
        tk.Frame.__init__(self, master,height=800,width=1200)
        self.bg_frame=ImageTk.PhotoImage((Gui_Image.AMain['background1']).resize((1200,800),Image.ANTIALIAS))
        tk.Label(self,image=self.bg_frame).place(relx=0.5,rely=0.5,anchor='c')

    def background2(self, master):
        tk.Frame.__init__(self, master,height=800,width=1200)
        self.bg_frame=ImageTk.PhotoImage((Gui_Image.AMain['background2']).resize((1200,800),Image.ANTIALIAS))
        tk.Label(self,image=self.bg_frame).place(relx=0.5,rely=0.5,anchor='c')

    def new_widget(self,w,h,x,y,bg_color="#fdd1d0"):
        frame=tk.Frame(self,bg=bg_color,height=h,width=w);

        L_config=tk.Label(frame,bg=bg_color)
        L_config.place(relx=0.5,rely=0.5,anchor='c');

        frame.place(x=x,y=y)
        return L_config;

class Menu(MyFrame):
    def __init__(self, master):
        MyFrame.background1(self, master)

        tk.Frame(self,bg="#ffd162",height=800,width=400).place(x=0,y=0)

        self.Show_Info=self.new_widget(w=380,h=420,x=10,y=10)
        self.img_info=ImageTk.PhotoImage(Gui_Image.Menu['start_info']);
        self.Show_Info.config(image=self.img_info)

        #tk.Frame(self,bg="#FCFC66",height=190,width=380).place(height=190,width=380)

        self.Show_Speech=self.new_widget(w=380,h=140,x=10,y=640,bg_color="#fcaf38")
        self.Show_Speech.config(text='dadasda',font=("Times New Roman", 36))

        Show_How=self.new_widget(h=190,w=380,x=10,y=440)
        self.img_How=ImageTk.PhotoImage(Gui_Image.Menu['Howto']);
        Show_How.config(image=self.img_How)


        self.img_color=ImageTk.PhotoImage(Gui_Image.Menu['colorM']);
        self.img_advance=ImageTk.PhotoImage(Gui_Image.Menu['advanceM']);
        self.img_animal=ImageTk.PhotoImage(Gui_Image.Menu['animalM']);
        self.img_flag=ImageTk.PhotoImage(Gui_Image.Menu['flagM']);

        self.Color_mode=self.new_card(self.img_color)
        self.Color_mode.place(x=440,y=40)

        self.Advance_mode=self.new_card(self.img_advance)
        self.Advance_mode.place(x=840,y=40)

        self.Animal_mode=self.new_card(self.img_animal)
        self.Animal_mode.place(x=440,y=440)

        self.Flag_mode=self.new_card(self.img_flag)
        self.Flag_mode.place(x=840,y=440)


    def new_card(self,picture):
        frame=tk.Frame(self,bg="#fdd1d0",height=320,width=320);
        tk.Label(frame,image=picture).place(relx=0.5,rely=0.5,anchor='c');
        return frame;


class Game(MyFrame):
    def __init__(self,master):
        MyFrame.background1(self, master)

        self.Show_image=self.new_widget(w=720,h=540,x=240,y=50)
        self.img_begin=ImageTk.PhotoImage(Gui_Image.Game['start'])
        self.Show_image.config(image=self.img_begin)

        self.Show_Number=self.new_widget(w=120,h=100,x=60,y=50)
        self.Show_Number.config(text='',font=("Courier", 84))

        score=self.new_widget(w=120,h=50,x=1050,y=20)
        score.configure(text='คะแนน',font=("Courier", 34))

        self.Show_Score=self.new_widget(w=120,h=60,x=1050,y=70)
        self.Show_Score.config(text='00',font=("Courier", 60))

        self.Show_Speech=self.new_widget(w=900,h=90,x=150,y=650,bg_color="#FFFFFF")
        self.Show_Speech.config(text='abcavsdadad',font=("Times New Roman", 36))

        Show_Status=self.new_widget(w=90,h=90,x=1050,y=650)
        self.img_mic=ImageTk.PhotoImage(Gui_Image.Game['status_mic'])
        Show_Status.config(image=self.img_mic)

class EndGame(MyFrame):
    def __init__(self,master):
        MyFrame.background2(self, master)

        sframe=self.new_widget(w=720,h=540,x=240,y=50)
        self.img_f=ImageTk.PhotoImage((Gui_Image.AMain['background1']).resize((720,540),Image.ANTIALIAS))
        sframe.configure(image=self.img_f)

        self.Show_Score=self.new_widget(w=600,h=270,x=300,y=70) #c5a3a2
        self.Show_Score.config(text="99",font=("Times New Roman", 270))

        Home_sign=self.new_widget(w=200,h=40,x=350,y=350)
        Home_sign.config(text="กลับหน้าหลัก",font=("Times New Roman bold", 16))
        Home_symbol=self.new_widget(w=200,h=160,x=350,y=390)
        self.img_menusym=ImageTk.PhotoImage(Gui_Image.End['menu'])
        Home_symbol.config(image=self.img_menusym)

        Again_sign=self.new_widget(w=200,h=40,x=650,y=350)
        Again_sign.config(text="ลองอีกครั้ง",font=("Times New Roman bold", 16))
        Again_symbol=self.new_widget(w=200,h=160,x=650,y=390)
        self.img_againsym=ImageTk.PhotoImage(Gui_Image.End['again'])
        Again_symbol.config(image=self.img_againsym)

        self.Show_Speech=self.new_widget(w=600,h=90,x=300,y=600,bg_color="#FFFFFF")
        self.Show_Speech.config(text='abcavsdadad',font=("Times New Roman", 36))

# if __name__ == '__main__':
#
#    app=Main("conny")
#
#    app.title("PDsdsadsasd")
#    app.geometry("1200x800+80+10")
#    app.mainloop()
