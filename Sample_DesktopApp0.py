from tkinter import *
root = Tk()			# create a tkinter window
root.geometry('300x200')

label = Label(root, text ="Hello World !").pack()
btn = Button(root, text = 'Click me !', bd = '5',command = root.destroy)
btn.pack(side='bottom')
root.title("Inventory Tool")
root.mainloop()
