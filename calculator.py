#calculator.py
from tkinter import *
tk = Tk()
tk.title('CALCULATOR - adi')
number1=0
number2=0
ans = 0
sym = False
ans_f = Frame(tk, bg='white', height = 100)
ans_f.pack(side = TOP)


low_f = Frame(tk)
low_f.pack(side = BOTTOM)


symbol = '+'
values = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9': 9, '0':0}
def number(buttons):
	global number1
	global number2
	global sym
	global symbol
	global ans
	striing = ''

	if buttons['text'] != '^' and buttons['text'] != '=' and buttons['text'] != '/' and  buttons['text'] != '*' and buttons['text'] != '-' and buttons['text'] != '+': 
		if sym:
			number2 = number2*10 + values[buttons['text']]
			striing += buttons['text']
			display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
			display.pack()
		else:
			number1 = number1*10 + values[buttons['text']]
			striing += buttons['text']
			display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
			display.pack()
	elif buttons['text']!='=':
		symbol = buttons['text']
		striing += buttons['text']
		display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
		display.pack()
		sym = True
	else:
		if symbol=='+':
			ans = number1+number2
			display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
			display.pack()
		elif symbol=='-':
			ans = number1-number2
			display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
			display.pack()
		elif symbol=='*':
			ans = number1*number2
			display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
			display.pack()
		elif symbol=='/':
			ans = number1/number2
			display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
			display.pack()
		elif symbol=='^':
			ans = number1**number2
			display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
			display.pack()
		striing = str(ans)
		print(ans)
		display = Label(ans_f, text = striing, bg = 'white', font = 'monospace')
		display.pack()
	

buttons = StringVar()
button1 = Button(low_f, text= '1', height  =4, width = 4, command = lambda:number(button1))
button1.grid(row = 2, column = 0, sticky = S+N+E+W)
button2 = Button(low_f, text= '2', height  =4, width = 4, command = lambda:number(button2))
button2.grid(row = 2, column = 1, sticky = S+N+E+W)
button3 = Button(low_f, text= '3', height  =4, width = 4, command = lambda:number(button3))
button3.grid(row = 2, column = 2, sticky = S+N+E+W)
button4 = Button(low_f, text= '4', height  =4, width = 4, command = lambda:number(button4))
button4.grid(row = 3, column = 0, sticky = S+N+E+W)
button5 = Button(low_f, text= '5', height  =4, width = 4, command = lambda:number(button5))
button5.grid(row = 3, column = 1, sticky = S+N+E+W)
button6 = Button(low_f, text= '6', height  =4, width = 4, command = lambda:number(button6))
button6.grid(row = 3, column = 2, sticky = S+N+E+W)
button7 = Button(low_f, text= '7', height  =4, width = 4, command = lambda:number(button7))
button7.grid(row = 4, column = 0, sticky = S+N+E+W)
button8 = Button(low_f, text= '8', height  =4, width = 4, command = lambda:number(button8))
button8.grid(row = 4, column = 1, sticky = S+N+E+W)
button9 = Button(low_f, text= '9', height  =4, width = 4, command = lambda:number(button9))
button9.grid(row = 4, column = 2, sticky = S+N+E+W)
button0 = Button(low_f, text= '0', height  =4, width = 4, command = lambda:number(button0))
button0.grid(row = 1, column = 0, sticky = S+N+E+W)
buttoneq = Button(low_f, text= '=', height  =4, width = 4, command = lambda:number(buttoneq))
buttoneq.grid(row = 1, column = 1, sticky = S+N+E+W)
buttonp = Button(low_f, text= '+', height  =4, width = 4, command = lambda:number(buttonp))
buttonp.grid(row = 4, column = 3, sticky = S+N+E+W)
buttonS = Button(low_f, text= '-', height  =4, width = 4, command = lambda:number(buttonS))
buttonS.grid(row = 3, column = 3, sticky = S+N+E+W)
buttonm = Button(low_f, text= '*', height  =4, width = 4, command = lambda:number(buttonm))
buttonm.grid(row = 2, column = 3, sticky = S+N+E+W)
buttond = Button(low_f, text= '/', height  =4, width = 4, command = lambda:number(buttond))
buttond.grid(row = 1, column = 3, sticky = S+N+E+W)
buttonpow = Button(low_f, text= '^', height  =4, width = 4, command = lambda:number(buttonpow))
buttonpow.grid(row = 1, column = 2, sticky = S+N+E+W)

tk.mainloop()