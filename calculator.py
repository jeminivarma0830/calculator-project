from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

entry = Entry(root, width=20, font=('Arial', 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','C','=','+'
]

row = 1
col = 0

for button in buttons:
    if button == 'C':
        b = Button(root, text=button, padx=20, pady=20, command=clear)
    elif button == '=':
        b = Button(root, text=button, padx=20, pady=20, command=equal)
    else:
        b = Button(root, text=button, padx=20, pady=20, command=lambda b=button: click(b))

    b.grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
