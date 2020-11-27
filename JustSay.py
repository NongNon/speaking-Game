from Controll import ControlSet
from View import Main

if __name__ == '__main__':
    conny=ControlSet()
    conny.start()
    fiber=conny.get_conect()
    app=Main(fiber)

    app.title("Just say!")
    app.geometry("1200x800+80+10")
    app.mainloop()
