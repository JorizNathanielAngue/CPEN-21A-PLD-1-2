from tkinter import *
win = Tk()
#Hello po Maam, hindi ko po kasi ma-connect ang PyCharm ko sa Github, kaya dinownload ko na lang po ang files tapos manualk na in-upload sa Github. Sana okay lang po, thank you.
class MyWin:

    def __init__(self, win):
        self.lbl0 = Label(win, text="My First Standard Calculator")
        self.lbl0.place(x=230, y=80)

        self.lbl1 = Label(win, text="First Number:")
        self.lbl1.place(x=180, y=140)
        self.txt1 = Entry(win, bd=3)
        self.txt1.place(x=300, y=140)

        self.lbl2 = Label(win, text="Second Number:")
        self.lbl2.place(x=180, y=180)
        self.txt2 = Entry(win, bd=2)
        self.txt2.place(x=300, y=180)

        self.btn1 = Button(win, text="Addition", command=self.addition)
        self.btn1.place(x=225, y=250)
        self.btn2 = Button(win, text="Subtraction", command=self.subtraction)
        self.btn2.place(x=320, y=250)
        self.btn3 = Button(win, text="Multiplication", command=self.multiplication)
        self.btn3.place(x=210, y=300)
        self.btn4 = Button(win, text="Division", command=self.division)
        self.btn4.place(x=330, y=300)

        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=200, y=400)
        self.txt3 = Entry(win, bd=2)
        self.txt3.place(x=240, y=400)

        self.lbl4 = Label(win, text="This calculator was created by Joriz Nathaniel Angue, BSCPE 1-2")
        self.lbl4.place(x=130, y=500)

    def addition(self):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1+num2
        self.txt3.insert(END,str(result))

    def subtraction(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def multiplication(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 =int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def division(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1/num2
        self.txt3.insert(END, str(result))

mywin=MyWin(win)
win.geometry("600x600+20+20")
win.title("Standard Calculator")

win.mainloop()
