import speech_recognition as sr
import threading
import time
import winsound

from Configy import Command,Sound
from Model import Modely

class ControlSet(threading.Thread):
    def run(self):
        self.Gui_port=GuiConfig();
        CCU=Control_Core(self.Gui_port);
        CCU.run();

    def get_conect(self):
        return self.Gui_port

    # def status(self):
    #     print(self.Gui_port.Gui_speech)
    #     print(self.Gui_port.GuiConfig_Menu)
    #     print(self.Gui_port.GuiConfig_Game)
    #     print(self.Gui_port.GuiConfig_End)

class GuiConfig():
    def __init__(self):
        self.Gui_speech=""
        self.reset_menuconfig()
        self.reset_gameconfig()
        self.reset_endconfig()

    def reset_menuconfig(self):
        self.GuiConfig_Menu={
            'quit':False,
            'go':False,
            'change_hl':False,
            'selec_mode':0,
            # 1 = color
            # 2 = advance
            # 3 = animal
            # 4 = flag
        }

    def reset_gameconfig(self):
        self.GuiConfig_Game={
            'quit':False,
            'change_image':False,
            'end':False,
            'score':0,
            'image':None,
        }

    def reset_endconfig(self):
        self.GuiConfig_End={
            'again':False,
            'menu':False,
            'score':0
        }

class Control_Core():
    def __init__(self,Gui_port):
        self.r= sr.Recognizer();
        self.ToGui= Gui_port
        self.Model=Modely()

    def run(self):
        self.Command_set=1
            # 1=menu
            # 2=game
            # 3=end
        ################################################################
        def get_input():
            self.ToGui.Gui_speech="..."
            while True:
                with sr.Microphone() as source:
                    audio = self.r.listen(source,phrase_time_limit=3)
                try:
                    speech= self.r.recognize_google(audio, None,'th')
                    break
                except:
                    pass
            speech = speech.lower()
            self.ToGui.Gui_speech=speech
            time.sleep(1)
            return speech

        def Gui_selec(mode_id):
            play_sound(Sound.sound_fx['select'])
            self.ToGui.GuiConfig_Menu['selec_mode']=mode_id
            self.ToGui.GuiConfig_Menu["change_hl"]=True

        def Next_problem():
            self.ToGui.GuiConfig_Game['score']=self.Model.out_score()
            try:
                self.Model.Next_problem();
                self.ToGui.GuiConfig_Game['image']=self.Model.out_img()
                self.ToGui.GuiConfig_Game['change_image']=True
            except:
                self.ToGui.reset_endconfig();
                self.ToGui.GuiConfig_End['score']=self.Model.out_score();
                self.Command_set=3
                self.ToGui.GuiConfig_Game['end']=True;
        def play_sound(sound):
            winsound.PlaySound(sound, winsound.SND_ALIAS | winsound.SND_ASYNC)
        ################################################################

        while True:
            speech=get_input()

            if(self.Command_set==1):
                if any(word in speech for word in Command.Menu['colorM']):
                    Gui_selec(1)
                    continue
                if any(word in speech for word in Command.Menu['advanceM']):
                    Gui_selec(2)
                    continue
                if any(word in speech for word in Command.Menu['animalM']):
                    Gui_selec(3)
                    continue
                if any(word in speech for word in Command.Menu['flagM']):
                    Gui_selec(4)
                    continue

                if any(word in speech for word in Command.Menu['go']):
                    if (self.ToGui.GuiConfig_Menu['selec_mode']==0):
                        self.ToGui.Gui_speech="Error!"
                        time.sleep(1)
                        continue
                    else:
                        self.Command_set=2;
                        self.ToGui.reset_gameconfig();
                        self.Model.setmode(self.ToGui.GuiConfig_Menu['selec_mode'])
                        self.Model.set_model()
                        self.ToGui.GuiConfig_Menu['go']=True
                        continue

                if any(word in speech for word in Command.Menu['exit']):
                    self.ToGui.GuiConfig_Menu["quit"]=True
                    return

            if(self.Command_set==2):
                if self.Model.begin:

                    if self.Model.check_ans(speech):
                        play_sound(Sound.sound_fx['correct'])
                        Next_problem();
                        continue

                    if any(word in speech for word in Command.Game['next']):
                        Next_problem();
                        continue

                else:
                    if any(word in speech for word in Command.Game['start']):
                        self.ToGui.GuiConfig_Game['image']=self.Model.out_img()
                        self.ToGui.GuiConfig_Game['score']=self.Model.out_score()
                        self.ToGui.GuiConfig_Game['change_image']=True
                        self.Model.begin=True;
                        continue

                if any(word in speech for word in Command.Game['exit']):
                    self.ToGui.reset_menuconfig();
                    self.Command_set=1;
                    self.ToGui.GuiConfig_Game["quit"]=True
                    continue

            if(self.Command_set==3):
                if any(word in speech for word in Command.EndGame['menu']):
                    self.ToGui.reset_menuconfig();
                    self.Command_set=1;
                    self.ToGui.GuiConfig_End["menu"]=True
                    continue

                if any(word in speech for word in Command.EndGame['again']):
                    self.ToGui.reset_gameconfig();
                    self.Model.set_model()
                    self.Command_set=2;
                    self.ToGui.GuiConfig_End["again"]=True
                    continue

# if __name__=='__main__':
#     a=ControlSet();
#     a.start();
#     while True:
#         input()
#         a.status()
