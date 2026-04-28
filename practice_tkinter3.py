import tkinter as tk
root=tk.Tk()
root.geometry('500x500')
root.title('my app')
root.config(bg='white')

items =["Python","C++","Java","Javascript"]
combo_box=ttk.Combobox(root,values=items)
combo_box.pack()
combo_box.current(0) #default value

def print_choice():
    item=combo_box.get()  #getting a cursor input
    print(item)
btn_print_choice=tk.Button(root,text="Print choice",command=print_choice).pack()

root.mainloop()
