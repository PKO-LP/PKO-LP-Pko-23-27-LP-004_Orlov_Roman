from tkinter import *
from tkinter import ttk

root = Tk()
root.title("primer3")
root.geometry("250x150")

btn = ttk.Button()
btn.pack()

btn["text"] = "slovo"

btnText = btn["text"]
print(btnText)

root.mainloop()