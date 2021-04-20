import os
def clearterminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class board:
    
    def __init__(self):
        self.round = 0
        self.size = 8
        self.player1 = player(1)
        self.player2 = player(2)
        self.empt = " - "
        self.arr = []

    def set_size(self,i):
        self.size = int(i)

    def empty(self):
        for i in range (self.size):
            new = []
            for j in range (self.size):
                new.append (self.empt)
            self.arr.append(new)   
    def set_empt(self,c):
        self.empt = " "+c+" "

    def kill(self,i,j):
        self.arr[j-1][i-1] = self.empt

    def add (self,p,ist,jst):
        i = int(ist)
        j = int(jst)
        if (p == 1):
            self.arr[j-1][i-1]= self.player1.playercharacter
        elif (p == 2):
            self.arr[j-1][i-1]= self.player2.playercharacter
    def initialize(self):
        for i in range (self.size):
            self.add(self.player1.turn,i,1)
            self.add(self.player2.turn,i,self.size)
    def play(self,i):
        if (i == 1):
            self.player1.play(self)
        elif(i == 2):
            self.player2.play(self)

            
    def prnt(self):
        
        print (" -------------------------------  "+self.player1.name)
        x = 1
        y = 1
        w = " "
        for i in range (self.size):
            w = w + " " +str(x)+ " "
            x = x+1
        print(w)
            
        
        for i in range (self.size):
            word = str(y)
            
            for j in range (self.size):
                word = word + self.arr[i][j]
            
            print(word+str(y))
            
            y = y+1
        w = " "
        x = 1
        for i in range (self.size):
            w = w + " " +str(x)+ " "
            x = x+1
        print(w)
        print (" -------------------------------  "+self.player2.name)
        

class player:
    def __init__(self,t):
        if (t == 1):

            self.playercharacter = " O "
        elif(t == 2):
            self.playercharacter = " 0 "
        self.name = "Player"+str(t)
        self.turn = t
        self.status = False
    def set_player_character(self,c):
        self.playercharacter = " "+c+" "
    
    def move(self,b,i1s, j1s, i2s, j2s):
        i1 = int(i1s)
        j1 = int(j1s)
        j2 = int(j2s)
        i2 = int(i2s)
        if ((i2<i1-1 or i2>i1+1) or (j2<j1-1 or j2>j1+1)or (b.arr[j1-1][i1-1] != self.playercharacter )or(b.arr[j2-1][i2-1] != b.empt )or (i1 < 1 or i2 < 1 or j1 <1 or j2 <1 or i1 < 1 or i2 < 1 or j1 >b.size or i1 >b.size or i2 >b.size or j1 >b.size or j2 >b.size or i1 >b.size or i2 >b.size or j1 >b.size )):
            return "err"
        else :
            b.kill(int(i1),int(j1))
            b.add(self.turn,str(i2),str(j2))
            if (j2 == 1 and self.turn == 2 ) or (j2 == b.size and self.turn == 1):
                self.status = True
    check = True
    def play(self,b):
        clearterminal()
        if (self.check ):
            b.round = b.round + 1
        print("        Round : " + str(b.round) +'\n')
       
        b.prnt()
        print ("\n\n     ___ "+self.name + " ___")
        i1, j1 = input("     Select Piece: ").split()
        i2, j2 = input("    Set Destination: ").split()
        if (self.move(b,i1,j1,i2,j2) == "err"):
            
            self.check = False
            self.play(b)
        else: 
            self.check = True
        
             
            
    def win(self,b):
        clearterminal()
        print(self.name + " Is The WINNER !!!!!")
        b.prnt()
        print("Total rounds : "+ str(b.round))

        

def ask_name(p):

    p.name = input("Give Player Name: ")


    
        
clearterminal()
print("         Welcome !!!")

b = board()
b.empty()
b.initialize()
branch = input("Use Default Settings? (Y / N): ")
if branch == "N"or branch == "n"or branch == "Ν" or branch == "ν"  :
    name1 = input("Give Player 1 name :")
    name2 = input("Give Player 2 name :")
    b.player1.name = name1
    b.player2.name = name2
    branch2 = input("Use Custom Settings? (Y / N): ")
    if branch2 == "Y" or branch2 == "y"or branch2 == "Υ" or branch2 == "υ":
        c1 = input("Give "+ b.player1.name+"'s character: (don't use -): ")
        c2 = input("Give "+ b.player2.name+"'s character: (don't use -): ")
        b.player1.set_player_character(c1)
        b.player2.set_player_character(c2)
        branch3 = input ("Use Advanced Settings? (Y / N): ")
        if branch3 == "Y" or branch3 == "y"or branch3 == "Υ" or branch3 == "υ":
            size = input("Give chessboard size (default 8 ) :")
            b.set_size(size)
            c = input("Give blank space character (default - ):")
            b.set_empt(c)





clearterminal()
print ("Round : "+str(b.round))
while(True):
    b.play(1)
    if (b.player1.status == True):
        b.player1.win(b)
        break

    b.play(2)
    
    if (b.player2.status == True):
        b.player.win(b)
        break


