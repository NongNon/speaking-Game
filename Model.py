import random

from Configy import Game_p


class Modely():
    def __init__(self):
        self.mode=0
        self.problem_set=[]

    def setmode(self,x):
        self.mode=x

    def set_model(self):
        if(self.mode==1):
            self.problem_set=random.sample(Game_p.colorM,10);
        if(self.mode==2):
            self.problem_set=random.sample(Game_p.advanceM,10);
        if(self.mode==3):
            self.problem_set=random.sample(Game_p.animalM,10);
        if(self.mode==4):
            self.problem_set=random.sample(Game_p.flagM,10);
        self.problem=self.problem_set.pop(0)
        self.score=0
        self.begin=False

    def check_ans(self,speech):
        if any(word in speech for word in self.problem['ans']):
            self.score=self.score+1
            return True;
        else:
            return False;

    def Next_problem(self):
        self.problem=self.problem_set.pop(0)

    def out_img(self):
        return self.problem['image']

    def out_score(self):
        return self.score


    #def out_ans(self):
    #    return self.problem['ans']
