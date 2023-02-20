from tkinter import *
from tkinter.ttk import *
from calendar import *


def Ok_Button_Click():
    a = int(Monatseingabe.get())
    b = int(Jahreseingabe.get())

    kalender = month(b,a)

    Ausgabe.delete(0.0, END)
    Ausgabe.insert(INSERT, kalender)


FONT = ('Consolas', 9, 'bold')
Größe = '250x210'
Lila = 'purple'
Gold = 'gold'


Kalender = Tk()
Kalender.config(bg=Lila, padx=10, pady=10)
Kalender.title("Kalender")
Kalender.geometry(Größe)
Kalender.resizable(False, False)


Monatslabel = Label(Kalender, text='Monat', font=FONT, background=Lila, foreground=Gold)
Monatslabel.place(x=15, y=0)


Jahreslabel = Label(Kalender, text='Jahr', font=FONT, background=Lila, foreground=Gold)
Jahreslabel.place(x=115, y=0)


Monatseingabe = Spinbox(Kalender, values=(1,2,3,4,5,6,7,8,9,10,11,12), font=FONT, width=4)
Monatseingabe.place(x=60, y=0)


Jahreseingabe = Spinbox(Kalender, from_=1900, to=3000, font=FONT, width=4)
Jahreseingabe.place(x=155, y=0)

Ok_Button = Button(Kalender, text='   OK   ', command=Ok_Button_Click)
Ok_Button.place(x=75, y=30)


Ausgabe = Text(Kalender, font=FONT, width=24, height=8)
Ausgabe.place(x=30, y=70)


if __name__ == '__main__':
    mainloop()
