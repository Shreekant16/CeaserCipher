alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from tkinter import *

window = Tk()
window.geometry("400x300")


def encode():
    text = text_e.get()
    shifts = int(shift_e.get())
    ans = ''
    for i in range(len(text)):
        position = alphabets.index(text[i])
        new_position = position + shifts
        new_letter = alphabets[new_position]
        ans += new_letter
    label = Label(text=f"{ans}")
    label.grid(column=1, row=5)


def decode():
    text = text_e.get()
    shifts = int(shift_e.get())
    ans = ''
    for i in text:
        position = alphabets.index(i)
        new_position = position - shifts
        ans += alphabets[new_position]
    label = Label(text=f"{ans}")
    label.grid(column=1, row=5)


def game():
    e = ede.get()
    if e == 'e':
        encode()
    elif e == 'd':
        decode()


def clears():
    text_e.delete(0, END)
    ede.delete(0, END)
    shift_e.delete(0, END)
    text_e.focus()


text = Label(text="Text : ")
text.grid(column=0, row=0)
text_e = Entry()
text_e.grid(column=1, row=0)

e_d = Label(text="E or D : ")
e_d.grid(column=0, row=1)
ede = Entry()
ede.grid(column=1, row=1)

shift = Label(text="Shifts : ")
shift.grid(column=0, row=2)
shift_e = Entry()
shift_e.grid(column=1, row=2)

button = Button(text="submit", command=game)
button.grid(column=1, row=4)

clear = Button(text="clear", command=clears)
clear.grid(column=2, row=4)

window.mainloop()
