import tkinter as tk
"""
root=tk.Tk()
root.geometry("500x500")
root.title("Canvas")

#create a canvas
canvas=tk.Canvas(root, width=400,heigh=300,bg="white")
canvas.pack()

root.mainloop()
"""
#___________________________________________________________________________
root=tk.Tk()
root.geometry("500x500")
root.title("my app")
#creating a frame
f1=tk.Frame(root,bg="green")
f1.place(relwidth=1,relheight=1)

f2=tk.Frame(root,bg="yellow")
f2.place(relwidth=1,relheight=1)

lbl1=tk.Label(f1,text="This is frame 1").pack()
lbl2=tk.Label(f2,text="This is frame 2").pack()

def shift(frame):
    frame.tkraise()
btn1=tk.Button(f1,text="Go to frame 2",command=lambda:shift(f2)).pack()
btn1=tk.Button(f2,text="Go to frame 1",command=lambda:shift(f1)).pack()

root.mainloop()
