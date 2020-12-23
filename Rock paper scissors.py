import tkinter as tk
import random

w=tk.Tk()
w.title('Rock-Paper-Scissor')
w.geometry('320x400')

def fscore():                                                                   #function to get max score from user.
    global sc
    sc=scoreentry.get()

def result(uc,cc):                                                              #function to check result of round    

    def playagain():
        greet.grid(row=1)
        scoreentry.grid(row=2)
        b1.grid(row=3,column=1)
        b2.grid(row=3,column=2)
        b3.grid(row=3,column=3)
        b4.grid(column=1,row=2)
        printtext.delete('1.0',tk.END)
        b6.grid_forget()
        scoreentry.delete(0,tk.END)
        global us
        global cs
        us=0
        cs=0

    global us
    global cs
    sr=''
    if uc==cc:
        print('Tie')
        p='Tie'
    elif (uc=='rock' and cc=='scissor') or (uc=='paper' and cc=='scissor') or (uc=='scissor' and cc=='paper'):
        p='You win'
        print('You win')
        us+=1
        if str(us)==sc:
            greet.grid_forget()
            scoreentry.grid_forget()
            b1.grid_forget()
            b2.grid_forget()
            b3.grid_forget()
            b4.grid_forget()
            sr='User reached the max points first.\nUSER WINS\n'
            b5=tk.Button(f3,text='Exit Game',command=exit)
            b5.grid(row=14)
            b6=tk.Button(f3,text='Play Again',command=playagain)
            b6.grid(row=13)

    else:
        p='Computer wins'
        print('Computer wins')
        cs+=1
        if str(cs)==sc:
            greet.grid_forget()
            scoreentry.grid_forget()
            b1.grid_forget()
            b2.grid_forget()
            b3.grid_forget()
            b4.grid_forget()
            sr='Computer reached the max points first.\nCOMPUTER WINS\nBetter luck next time...\n'
            b5=tk.Button(f3,text='Exit Game',command=exit)
            b5.grid(row=14)
            b6=tk.Button(f3,text='Play Again',command=playagain)
            b6.grid(row=13)

    a="Your choice: {uc} \nComputer's choice: {cc} \n\n{p} \n\nYour score: {us} \nComputer's score: {cs}\n\n\n{sr}".format(p=p,uc=uc,cc=cc,us=us,cs=cs,sr=sr)
    printtext.delete('1.0',tk.END)
    printtext.insert('1.0',a)

def rock():                                                                     #Function if user chooses 'rock'
    global uc
    uc='rock'
    global cc
    cc=comp_choice()
    result(uc,cc)

def paper():                                                                    #Function if user chooses 'paper'
    global uc
    uc='paper'
    global cc
    cc=comp_choice()
    result(uc,cc)

def scissor():                                                                  #Function if user chooses 'scissor'
    global uc
    uc='scissor'
    global cc
    cc=comp_choice()
    result(uc,cc)

def comp_choice():                                                              #function to get random computer choice
    a=['rock','paper','scissor']
    return random.choice(a)


f1=tk.Frame(w)
f1.grid()
f2=tk.Frame(w)
f2.grid()
f3=tk.Frame(w)
f3.grid()

greet=tk.Label(f1,text='Welcome\nEnter max score for the game: ')
greet.grid(row=1)
scoreentry=tk.Entry(f1,width=20)
scoreentry.grid(row=2)

sc=0
uc=''                                                                           #user's choice
us=0                                                                            #user's score
cc=''                                                                           #computer's choice
cs=0                                                                            #computer's score

# creating buttons for gui
b1=tk.Button(f2,text='     Rock    ',bg='grey',command=rock)
b2=tk.Button(f2,text='    Paper    ',bg='yellow',command=paper)
b3=tk.Button(f2,text='   Scissor   ',bg='orange',command=scissor)
b4=tk.Button(f1,text='Ok',command=fscore)
b1.grid(row=4,column=1)
b2.grid(row=4,column=2)
b3.grid(row=4,column=3)
b4.grid(column=1,row=2)
printtext=tk.Text(f3,bg='black',fg='yellow',height=15,width=40)
printtext.grid(row=6)

w.mainloop()