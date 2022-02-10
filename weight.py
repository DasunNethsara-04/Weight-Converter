#Imports
from tkinter import *
from tkinter import messagebox

#functions
def calc():
	try:
		weight = float(entry.get())
		global pounds, grams, ounces, mtons, pounds
		a = str(grams * weight)
		b = str(pounds * weight)
		c = str(ounces * weight)
		d = str(mtons * weight)

		grams_txt.set(a)
		pounds_txt.set(b)
		ounce_txt.set(c)
		mTons.set(d)
	except:
		messagebox.showerror("Alert", "Enter the weight in the input filed below")
		pass

def clear():
	entry.delete(0, END)
	grams_txt.set("")
	pounds_txt.set("")
	ounce_txt.set("")
	mTons.set("")
	messagebox.showinfo('Done', 'All fileds are clearing completed!')



#Main User Interface
root = Tk()
root.title("Weight Convertor")
root.geometry('650x300+250+300')
root.resizable(0, 0)
root.config(bg='white')

#variables
pounds = 2.2
grams = 1000
ounces = 35.27
mtons = 0.001
pounds_txt = StringVar()
grams_txt = StringVar()
ounce_txt = StringVar()
mTons = StringVar()


#UI Widgets
Label(root, text='Weight Convertor', fg='cyan', bg='black', font=('Calibri', 25)).pack(fill='x', side=TOP)
Label(root, text='Enter weight in kg:', font=('Times', 15), bg='white').place(x=5, y=80)

entry = Entry(root, font=('Times', 15, 'bold'), bd=2, relief='groove', justify='center')
entry.place(x=163, y=79)

Button(root, text='Calculate', font=('Calibri', 15), bg='cyan', relief='groove', bd=5, command=calc).place(x=430, y=73)
Button(root, text='Clear', font=('Calibri', 15), bg='cyan', relief='groove', width=8, bd=5, command=clear).place(x=540, y=73)

#indicate
Label(root, text='Grams:', font=('Times', 15), bg='white').place(x=5, y=170)
Label(root, text='Pounds:', font=('Times', 15), bg='white').place(x=5, y=200)
Label(root, text='Ounces:', font=('Times', 15), bg='white').place(x=5, y=230)
Label(root, text='M. Tons:', font=('Times', 15), bg='white').place(x=5, y=260)


#outputs
lbl1 = Label(root, textvariable=grams_txt, font=('Times', 15), bg='white', fg='red')
lbl1.place(x=100, y=170)
lbl2 = Label(root, textvariable=pounds_txt, font=('Times', 15), bg='white', fg='red')
lbl2.place(x=100, y=200)
lbl3 = Label(root, textvariable=ounce_txt, font=('Times', 15), bg='white', fg='red')
lbl3.place(x=100, y=230)
lbl4 = Label(root, textvariable=mTons, font=('Times', 15), bg='white', fg='red')
lbl4.place(x=100, y=260)

Label(root, text='Dasun Nethsara\n25.12.2021', bg='black', fg='white').pack(side=BOTTOM, fill=X)


root.mainloop()
