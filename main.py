from tkinter import *
import random


win = Tk()
win.geometry("700x700+750+200")
win.resizable(False,False)
win.config(bg="#996646")


Pc = ["rock","papper","seassors","rock","papper","seassors"]
pcpoints = 0
playerpoints = 0

#მოთამაშის ხელები
playerRock = PhotoImage(file="imgs/playerrock.png")
playerPapper = PhotoImage(file="imgs/playerpapper.png")
playerSeassors = PhotoImage(file="imgs/playerseassors.png")


#კომპიუტერის ხელები
pcRock = PhotoImage(file="imgs/pcrock.png")
pcPapper = PhotoImage(file="imgs/pcpapper.png")
pcSeassors = PhotoImage(file="imgs/pcseassors.png")

#ქვედა ასარჩევი სურათები
rockImg = PhotoImage(file="imgs/rock.png")
papperImg = PhotoImage(file="imgs/papper.png")
seassorsImg = PhotoImage(file="imgs/seassors.png")

#რესტარტის სურათი
restartImg = PhotoImage(file="imgs/restartImg.png")

#ფუნქციები !!!!


def pickRock(event):
    canvaLeft = Canvas(LeftFrame, width=300, height=300, bg="lightyellow")
    canvaLeft.place(x=0,y=0)
    canvaLeft.create_image(150,150,image=playerRock)

    PcPick =random.choice(Pc)


    if PcPick=="rock":
        condition["text"]="Tie"
        condition.config(fg="white", bg="blue")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcRock)
    elif PcPick=="papper":
        global pcpoints
        pcpoints +=1
        PcScore["text"]=pcpoints
        condition["text"] = "Computer Wins!"
        condition.config(fg="black",bg="red")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcPapper)
    else:
        global playerpoints
        playerpoints += 1
        PlayerScore["text"]=playerpoints
        condition["text"] = f'{PlayerName["text"]} Wins!'
        condition.config(fg="white", bg="green")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcSeassors)




def pickPapper(event):
    canvaLeft = Canvas(LeftFrame, width=300, height=300, bg="lightyellow")
    canvaLeft.place(x=0,y=0)
    canvaLeft.create_image(150,150,image=playerPapper)

    PcPick = random.choice(Pc)

    if PcPick=="rock":
        global playerpoints
        playerpoints += 1
        PlayerScore["text"] = playerpoints
        condition["text"] = f'{PlayerName["text"]} Wins!'
        condition.config(fg="white", bg="green")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcRock)
    elif PcPick=="papper":
        condition["text"] = "Tie"
        condition.config(fg="white", bg="blue")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcPapper)
    else:
        global pcpoints
        pcpoints += 1
        PcScore["text"] = pcpoints
        condition["text"] = "Computer Wins!"
        condition.config(fg="black", bg="red")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcSeassors)




def pickSeassors(event):
    canvaLeft = Canvas(LeftFrame, width=300, height=300, bg="lightyellow")
    canvaLeft.place(x=0,y=0)
    canvaLeft.create_image(150,150,image=playerSeassors)

    PcPick =random.choice(Pc)


    if PcPick=="rock":
        global pcpoints
        pcpoints += 1
        PcScore["text"] = pcpoints
        condition["text"] = "Computer Wins!"
        condition.config(fg="black", bg="red")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcRock)
    elif PcPick=="papper":
        global playerpoints
        playerpoints += 1
        PlayerScore["text"] = playerpoints
        condition["text"] = f'{PlayerName["text"]} Wins!'
        condition.config(fg="white", bg="green")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcPapper)
    else:
        condition["text"] = "Tie"
        condition.config(fg="white", bg="blue")
        canvaRight = Canvas(RightFrame, width=300, height=300, bg="silver")
        canvaRight.place(x=0, y=0)
        canvaRight.create_image(150, 150, image=pcSeassors)



#გამოძახებული ფანჯარა
def popupwin(event):
    top = Toplevel(win,bg="#8E5029")
    top.geometry("300x200+950+400")
    top.resizable(False,False)

    nameEntryLabel = Label(top, text="Enter Your Name!",font=("Bankghotic",20,"bold"),justify=CENTER,bg="#8E5029",fg="white")
    nameEntryLabel.pack(pady=30)
    nameEntry = Entry(top,width=30)
    nameEntry.pack()

    submit = Button(top,text="Submit",command=lambda :PlayerName.config(text=nameEntry.get()))
    submit.place(x=90,y=130)
    submit.bind("<Return>",lambda event:PlayerName.config(text=nameEntry.get()))
    submit.bind("<Button-1>", lambda event: PlayerName.config(text=nameEntry.get()))

    close = Button(top, text="Close", command=lambda:top.destroy())
    close.place(x=160,y=130)


#დარესტარტება

def restartFunc():
    global pcpoints
    global playerpoints
    playerpoints = 0
    pcpoints = 0

    PlayerScore["text"] = playerpoints
    PcScore["text"] = pcpoints

    LeftFrame.config(bg="#DEAC8C")
    RightFrame.config(bg="#DEAC8C")

    canvaLeft = Canvas(LeftFrame, width=300, height=300, bg="#DEAC8C")
    canvaLeft.place(x=0, y=0)

    canvaRight = Canvas(RightFrame, width=300, height=300, bg="#DEAC8C")
    canvaRight.place(x=0, y=0)

    condition.config(bg="#996646",text="")





PlayerScore =Label(win,text=playerpoints,font=("Bankghotic",15,"bold"),bg="#DEAC8C",width=10)
PlayerScore.place(x=80,y=65)


PcScore =Label(win,text=pcpoints,font=("Bankghotic",15,"bold"),bg="#DEAC8C",width=10)
PcScore.place(x=490,y=65)

condition = Label(win,text="",font=("Bankghotic",25,"bold"),bg="#996646")
condition.pack(fill=X)

#ეკრანები სადაც გამოჩნდება არჩეული

PlayerName = Label(win,text="Player",font=("Bankghotic",15,"bold"),bg="#996646")
PlayerName.place(x=100,y=110)
PlayerName.bind("<Button-1>",popupwin)

LeftFrame = Frame(win,bg="#DEAC8C",width=300,height=300)
LeftFrame.place(x=0,y=150)

PC = Label(win,text="PC",font=("Bankghotic",15,"bold"),bg="#996646")
PC.place(x=540,y=110)

RightFrame = Frame(win,bg="#DEAC8C",width=300,height=300)
RightFrame.place(x=400,y=150)

vs = Label(win,text="VS",font=("Bankghotic",20,"bold"),bg="#996646")
vs.pack(expand=TRUE)




restart = Button(win,image=restartImg,width=60,height=65,bg="#996646",activebackground="#8E5029",command=restartFunc)
restart.pack(pady=15)


#ქვედა ჩარჩო
BottomFrame = Frame(win,bg="#8E5029")
BottomFrame.pack(side=BOTTOM,fill=X)


#ასარჩევი ღილაკები
rock = Button(BottomFrame,image=rockImg,width=140,height=125,bg="#F3A97A",activebackground="#8E5029")
rock.pack(side=LEFT,padx=40,pady=10)
rock.bind("<Button-1>",pickRock)


papper = Button(BottomFrame,image=papperImg,width=140,height=125,bg="#F3A97A",activebackground="#8E5029")
papper.pack(side=LEFT,padx=40,pady=10)
papper.bind("<Button-1>",pickPapper)


seassors = Button(BottomFrame,image=seassorsImg,width=140,height=125,bg="#F3A97A",activebackground="#8E5029")
seassors.pack(side=LEFT,padx=40,pady=10)
seassors.bind("<Button-1>",pickSeassors)






win.mainloop()