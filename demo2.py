from tkinter import *
win = Tk()

#add widgets

win.geometry("800x600+30+50")
win.title("My First GUI Application")

#label widgets

lbl1 = Label(win, text="My First GUI", fg="Black")
lbl1.place(x=370, y=50)

lbl2 = Label(win, text = "Student Profile Form", fg="Black")
lbl2.place(x=350, y=75)

lbl3 = Label(win, text = "Student Name:")
lbl3.place(x=220, y=120)
txtfld1 = Entry(win, text="Enter Name Here", bd=5)
txtfld1.place(x=420, y=120)

lbl4 = Label(win, text="Student Number:")
lbl4.place(x=220, y=150)
txtfld1 = Entry(win, text="Enter Number Here", bd=5)
txtfld1.place(x=420,y=150)

lbl4 = Label(win, text="Age:")
lbl4.place(x=220, y=180)
txtfld2 = Entry(win, text="Enter Age Here", bd=5)
txtfld2.place(x=420, y=180)

lbl6 = Label(win, text="Year Level:")
lbl6.place(x=220, y=260)
txtfld3 = Entry(win, text="Enter Year Level Here", bd=5)
txtfld3.place(x=420, y=260)

lbl7 = Label(win, text="Program:")
lbl7.place(x=220, y=290)
txtfld4 = Entry(win, text="Enter Program Here", bd=5)
txtfld4.place(x=420, y=290)

lbl8 = Label(win, text="Registration Adviser:")
lbl8.place(x=220, y=320)
txtfld4 = Entry(win, text="Enter Adviser Name Here", bd=5)
txtfld4.place(x=420, y=320)


#Add Radiobutton
def sel():
    selection = "You selected option" + str(var.get())
    Label.config(text=selection)
var = IntVar()
lbl5 = Label(win, text="Sex:")
lbl5.place(x=220, y=210)
d1 = Radiobutton(win,text="Male", variable=var, value=1, command = sel)
d1.place(x=420, y=210)
d2 = Radiobutton(win,text="Female", variable=var, value=2, command = sel)
d2.place(x=420, y=230)

#AddButton

btn1 = Button(win, text="Submit", fg="Blue", font=("Times New Roman", 15))
btn1.place(x=375, y=400)

lbl9 = Label(win, text="Form created by Joriz Nathaniel Angue, BSCPE 1-2")
lbl9.place(x=260, y=500)





win.mainloop()