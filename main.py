from tkinter import *


def calculate():
    n = int(input.get())
    res = n * 1.60934
    output_label.config(text= res)


# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

# Label
my_label = Label(text="Miles", font=("Arial", 10, "bold"))
is_equal_to = Label(text="is equal to", font=("Arial", 10, "bold"))
km = Label(text="Km", font=("Arial", 10, "bold"))
output_label = Label(text="0")
title_label = Label(text="Mile to Km Converter",font=("Arial", 10, "bold"))
output_label.grid(row=1,column=1)
my_label.grid(row=0, column=2)
is_equal_to.grid(row=1, column=0)
km.grid(row=1, column=2)
title_label.place(x=20,y=80)

# Entry
input = Entry(width=10)
input.grid(row=0, column=1)


window.mainloop()
