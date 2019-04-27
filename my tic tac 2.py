from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

bclick = True
flag = 0

def btnClick(buttons):
    global bclick, flag
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

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Winner is X !!!')

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
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Winner is O !!!!')


buttons = StringVar()

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=1, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=1, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=1, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=2, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=2, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=2, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=3, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=3, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=3, column=2)

tk.mainloop()
