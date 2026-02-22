from tkinter import *

# create window
window = Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# entry box
e = Entry(window, width=25)
e.place(x=20, y=20)

# global variables
first_number = 0
operation = ""

# function for numbers
def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))

# addition
def add():
    global first_number
    global operation
    operation = "add"
    first_number = int(e.get())
    e.delete(0, END)

# subtraction
def sub():
    global first_number
    global operation
    operation = "sub"
    first_number = int(e.get())
    e.delete(0, END)

# multiplication
def mul():
    global first_number
    global operation
    operation = "mul"
    first_number = int(e.get())
    e.delete(0, END)

# division
def div():
    global first_number
    global operation
    operation = "div"
    first_number = int(e.get())
    e.delete(0, END)

# equal button
def equal():
    second_number = int(e.get())
    e.delete(0, END)

    if operation == "add":
        result = first_number + second_number
        e.insert(0, result)

    elif operation == "sub":
        result = first_number - second_number
        e.insert(0, result)

    elif operation == "mul":
        result = first_number * second_number
        e.insert(0, result)

    elif operation == "div":
        if second_number != 0:
            result = first_number / second_number
            e.insert(0, result)
        else:
            e.insert(0, "Error")

# clear button
def clear():
    e.delete(0, END)


# buttons

# Number Buttons
b = Button(window, text='1', width=12, command=lambda: click(1))
b.place(x=10, y=60)

b = Button(window, text='2', width=12, command=lambda: click(2))
b.place(x=90, y=60)

b = Button(window, text='3', width=12, command=lambda: click(3))
b.place(x=170, y=60)

b = Button(window, text='4', width=12, command=lambda: click(4))
b.place(x=10, y=120)

b = Button(window, text='5', width=12, command=lambda: click(5))
b.place(x=90, y=120)

b = Button(window, text='6', width=12, command=lambda: click(6))
b.place(x=170, y=120)

b = Button(window, text='7', width=12, command=lambda: click(7))
b.place(x=10, y=180)

b = Button(window, text='8', width=12, command=lambda: click(8))
b.place(x=90, y=180)

b = Button(window, text='9', width=12, command=lambda: click(9))
b.place(x=170, y=180)

b = Button(window, text='0', width=12, command=lambda: click(0))
b.place(x=90, y=240)

# Operator Buttons
b = Button(window, text='+', width=12, command=add)
b.place(x=10, y=240)

b = Button(window, text='-', width=12, command=sub)
b.place(x=170, y=240)

b = Button(window, text='*', width=12, command=mul)
b.place(x=10, y=300)

b = Button(window, text='/', width=12, command=div)
b.place(x=170, y=300)

# Equal Button
b = Button(window, text='=', width=12, command=equal)
b.place(x=90, y=300)

# Clear Button
b = Button(window, text='Clear', width=12, command=clear)
b.place(x=90, y=350)

# run program
window.mainloop()
