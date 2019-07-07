from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=3)
player1_name.grid(row=1, column=1)
player2_name = Entry(tk, textvariable=p2, bd=3)
player2_name.grid(row=2, column=1)

bclick = True
flag = 0

player1Score = 0;
player2Score = 0;

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def enableButton():
    button1.configure(state='normal')
    button2.configure(state='normal')
    button3.configure(state='normal')
    button4.configure(state='normal')
    button5.configure(state='normal')
    button6.configure(state='normal')
    button7.configure(state='normal')
    button8.configure(state='normal')
    button9.configure(state='normal')
    



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def startGame():
    global playerb, pa, labelscore1, labelscore2, labelname1, labelname2, buttonRestart
    playerb = p2.get() + " Wins!"
    pa = p1.get() + " Wins!"
    enableButton();
    p2label = p2.get()
    p1label = p1.get()
    labelname1 = Label( tk, text=p1label + ":", font='Times 20 bold', fg='black', height=1)
    labelname1.grid(row=6, column=0)
    labelname2 = Label( tk, text=p2label + ":", font='Times 20 bold', fg='black', height=1)
    labelname2.grid(row=7, column=0)
    labelscore1 = Label( tk, text='', font='Times 20 bold', fg='black', height=1)
    labelscore1.grid(row=6, column=1)
    labelscore2 = Label( tk, text='', font='Times 20 bold', fg='black', height=1)
    labelscore2.grid(row=7, column=1)
    buttonRestart.configure(state='normal')

def checkForWin():
    global player1Score, player2Score, labelscore1, labelscore2
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        player1Score = player1Score + 1
        labelscore1['text'] = player1Score

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        player2Score = player2Score + 1
        labelscore2['text'] = player2Score


def restartBoard():
    global bclick, flag
    enableButton();
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '
    bclick = True
    flag = 0

def resetBoard():
    global bclick, flag, labelscore1, labelscore2, player1_name, player2_name, labelname1, labelname2, player1Score, player2Score, buttonRestart
    disableButton()
    labelscore1['text'] = ''
    labelscore2['text'] = ''
    labelname1['text'] = ''
    labelname2['text'] = ''
    player1Score = 0
    player2Score = 0
    player1_name.delete(first=0, last=len(p1.get()))
    player2_name.delete(first=0, last=len(p2.get()))
    buttonRestart.configure(state=DISABLED)
    
    

buttons = StringVar()

label = Label( tk, text="Player 1:", font='Times 20 bold', fg='black', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Times 20 bold', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

buttonStart = Button(tk, text='Start', font='Times 20 bold', bg='cyan', fg='black', height=1, width=8, command=lambda: startGame() )
buttonStart.grid(row=1, column=2)

buttonRestart = Button(tk, text='Restart', font='Times 20 bold', bg='cyan', fg='black', height=1, width=8, command=lambda: restartBoard() )
buttonRestart.grid(row=2, column=2)

buttonReset = Button(tk, text='Reset', font='Times 20 bold', bg='red', fg='black', height=1, width=8, command=lambda: resetBoard() )
buttonReset.grid(row=8, column=1)

disableButton();
buttonRestart.configure(state=DISABLED)

tk.mainloop()
