
import tkinter as tk

h=[]
def onKeyPress(event):
    h.append(event.char)
    print(h)
    return event.char

root = tk.Tk()
root.geometry('300x200')

text = tk.Text(root, background='white', foreground='black', font=('Comic Sans MS', 30))
text.pack()
root.bind('<KeyPress>', onKeyPress)

root.mainloop()
