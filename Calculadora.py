from tkinter import *

def button_click(num):
    global entrystring

    entrystring = entrystring + str(num)
    entrylabel.set(entrystring)

def equal():
    global entrystring
    total = str(eval(entrystring))

    entrylabel.set(total)

    entrystring = total

def clear():
    global entrystring
    entrylabel.set("")
    entrystring = ""

def delete():
    global entrystring
    entrystring = entrystring[:-1]
    entrylabel.set(entrystring)

calcwindow = Tk()
calcwindow.title("Calculadora Max Pro")

entrystring = ""

entrylabel = StringVar()

label = Label(calcwindow, textvariable=entrylabel,bg="white",width=32, height=2, anchor="e", font=('Ariel',10),background="#d1cfd0", activebackground='#d1cfd0', fg='black')
label.pack()

frame = Frame(calcwindow)
frame.pack()

button1 = Button(frame, text=1, height=3,width=7, font=('Ariel',10), command= lambda: button_click(1), background="black", activebackground='black', fg='white')
button1.grid(row=0,column=0)

button2 = Button(frame, text=2, height=3,width=7, font=('Ariel',10),command= lambda: button_click(2),background="black", activebackground='black', fg='white')
button2.grid(row=0,column=1)

button3 = Button(frame, text=3, height=3,width=7, font=('Ariel',10),command= lambda: button_click(3),background="black", activebackground='black', fg='white')
button3.grid(row=0,column=2)

button4 = Button(frame, text=4, height=3,width=7, font=('Ariel',10),command= lambda: button_click(4),background="black", activebackground='black', fg='white')
button4.grid(row=1,column=0)

button5 = Button(frame, text=5, height=3,width=7, font=('Ariel',10),command= lambda: button_click(5),background="black", activebackground='black', fg='white')
button5.grid(row=1,column=1)

button6 = Button(frame, text=6, height=3,width=7, font=('Ariel',10),command= lambda: button_click(6),background="black", activebackground='black', fg='white')
button6.grid(row=1,column=2)

button7 = Button(frame, text=7, height=3,width=7, font=('Ariel',10),command= lambda: button_click(7),background="black", activebackground='black', fg='white')
button7.grid(row=2,column=0)

button8 = Button(frame, text=8, height=3,width=7, font=('Ariel',10),command= lambda: button_click(8),background="black", activebackground='black', fg='white')
button8.grid(row=2,column=1)

button9 = Button(frame, text=9, height=3,width=7, font=('Ariel',10),command= lambda: button_click(9),background="black", activebackground='black', fg='white')
button9.grid(row=2,column=2)

button0 = Button(frame, text=0, height=3,width=7, font=('Ariel',10),command= lambda: button_click(0),background="black", activebackground='black', fg='white')
button0.grid(row=3,column=0)

plus = Button(frame, text="+", height=3,width=7, font=('Ariel',10),command= lambda: button_click("+"),background="#f79c34", activebackground='#f79c34', fg='black')
plus.grid(row=0, column=3)

Minus= Button(frame, text="-", height=3,width=7, font=('Ariel',10),command= lambda: button_click("-"),background="#f79c34", activebackground='#f79c34', fg='black')
Minus.grid(row=1, column=3)

Multiply = Button(frame, text="*", height=3,width=7, font=('Ariel',10),command= lambda: button_click("*"),background="#f79c34", activebackground='#f79c34', fg='black')
Multiply.grid(row=2, column=3)

Devide = Button(frame, text="/", height=3,width=7, font=('Ariel',10),command= lambda: button_click("/"),background="#f79c34", activebackground='#f79c34', fg='black')
Devide.grid(row=3, column=3)

Decimal = Button(frame, text=".", height=3,width=7, font=('Ariel',10),command= lambda: button_click("."),background="#f79c34", activebackground='#f79c34', fg='black')
Decimal.grid(row=3, column=1)

Equal = Button(frame, text="=", height=3,width=7, font=('Ariel',10), command= lambda: equal(),background="#f79c34", activebackground='#f79c34', fg='black')
Equal.grid(row=3, column=2)

frame2 = Frame(calcwindow)
frame2.pack()

Delete = Button(frame2, text="Delete", height=3, width=15,font=('Ariel',10), command= lambda: delete(),padx=2,background="#d1cfd0", activebackground='#d1cfd0', fg='black')
Delete.grid(row=0, column=0)

Clear = Button(frame2, text="Clear", height=3, width=15, font=('Ariel',10), command= lambda: clear(),padx=2,background="#d1cfd0", activebackground='#d1cfd0', fg='black')
Clear.grid(row=0, column=1)

calcwindow.mainloop()