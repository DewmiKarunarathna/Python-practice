import tkinter as tk
#messsage box
from tkinter import messagebox
root=tk.Tk()
root.geometry("500x500")
root.config(bg="white")

def show_message():
    messagebox.showerror("Title","This is my message") #there are several types of messageboxes

btn_show=tk.Button(root,text="Show message",command=show_message).pack()

root.mainloop()
