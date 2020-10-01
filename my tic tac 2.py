from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")

p1=StringVar()
p2=StringVar()

def main():
	global bclick,flag
	bclick = True
	flag = 0

	#creating text boxes do that players can enter their names
	player1_name = Entry(tk, bd=5,textvariable=p1)
	player1_name.grid(row=1, column=1, columnspan=8)
	player2_name = Entry(tk, bd=5,textvariable=p2)
	player2_name.grid(row=2, column=1, columnspan=8)


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



	#check if the player names are netered or not
	def players():
		if player1_name.get()=="" or player2_name.get()=="":
			tkinter.messagebox.showerror(title="Tic-Tac-Toe", message="Enter the player name first.", )
			return False
		else:
			playera = player1_name.get() + " Wins!!"
			playerb = str(player2_name.get()) + " Wins!!"
			return True
	
	def refresh(button):
		player1_name.delete(0,'end')
		player2_name.delete(0,'end')
		for i in button:
			i['text'] = ' '
			i['bg'] = 'gray'
			i.configure(state=NORMAL)


	def btnClick(buttons):
		global bclick, flag
		if players():
			if buttons["text"] == " " and bclick == True:
				buttons["text"] = "X"
				buttons["bg"] = "purple"
				bclick = False
				checkForWin()
				flag += 1
			elif buttons["text"] == " " and bclick == False:
				buttons["text"] = "O"
				buttons["bg"] = "red"
				bclick = True
				checkForWin()
				flag += 1
			elif buttons['text']=='RESET':
				refresh([button1,button2,button3,button4,button5,button6,button7,button8,button9])
				bclick= True
				flag*=0
			else:
				tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

	def checkForWin():
		if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
			button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
			button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
			button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
			button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
			button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
			button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
			button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
			button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
			disableButton()
			tkinter.messagebox.showinfo("Tic-Tac-Toe",player1_name.get()+" Wins!!")
			
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
			button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
			disableButton()
			tkinter.messagebox.showinfo("Tic-Tac-Toe", player2_name.get()+" Wins!!")
			
	label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
	label.grid(row=1, column=0)


	label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
	label.grid(row=2, column=0)

	button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
	button1.grid(row=3, column=0, padx=7, pady=4)

	button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
	button2.grid(row=3, column=1, padx=7, pady=4)

	button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
	button3.grid(row=3, column=2, padx=7, pady=4)

	button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
	button4.grid(row=4, column=0, padx=7, pady=4)

	button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
	button5.grid(row=4, column=1, padx=7, pady=4)

	button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
	button6.grid(row=4, column=2, padx=7, pady=4)

	button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
	button7.grid(row=5, column=0, padx=7, pady=4)

	button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
	button8.grid(row=5, column=1, padx=7, pady=4)

	button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
	button9.grid(row=5, column=2, padx=7, pady=4)

	reset_but = Button(tk,text='RESET',font='Times 20 bold', bg='green', fg='white', height =0,width=7, command=lambda: btnClick(reset_but))
	reset_but.grid(row=6,columnspan=3,padx=7, pady=4)

	tk.mainloop()

if __name__=='__main__':
	main()
