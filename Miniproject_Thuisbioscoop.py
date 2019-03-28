from tkinter import *
import tkinter as ob

if keuze == 3:
    overzicht_bezoekers_film_bekijken()
elif keuze == 4:
    film_kiezen_om_te_aanbieden()

def overzicht_bezoekers_film_bekijken():
    infile = open('codebezoekersinfofilm.txt', 'r')

    label['text'] = entry.get()

root = ob()

label = Label(master=root, text='De films die je aanbied', background='black', foreground='pink', font=('Century Gothic', 14, 'bold italic'), width=22, height=3)
label.pack()

button1 = Button(master=root, text='Film: Before I fall, Datum: time, Bezoekerscode: 8898', bg='light blue', command=clicked)
button1.pack(pady=10)

button2 = Button(master=root, text='Film: Irreplaceable you, Datum: time, Bezoekerscode: 6657', bg='pink', command=clicked)
button2.pack(pady=10)

button3 = Button(master=root, text='Film: Turn up Charlie, Datum: time, Bezoekerscode: 0987', bg='light blue',command=clicked)
button3.pack(pady=10)

button4 = Button(master=root, text="Film: Isn't it romantic, Datum: time, Bezoekerscode: 9876", bg='pink', command=clicked)
button4.pack(pady=10)

button5 = Button(master=root, text='Film: Bird box, Datum: time, Bezoekerscode: 9776', bg='light blue', command=clicked)
button5.pack(pady=10)

button6 = Button(master=root, text='Film: Mowgli, Datum: time, Bezoekerscode: 7554', bg='pink', command=clicked)
button6.pack(pady=10)

background_image = Tk(file='thuisbioscoop.png')
entry = Entry(master=root)
entry.pack(padx=10, pady=10)

def film_kiezen_om_te_aanbieden():
    infile = open('nietaangebodenfilms', 'r')



