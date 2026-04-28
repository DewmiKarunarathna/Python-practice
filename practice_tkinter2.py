import tkinter as tk
root = tk.Tk()
root.geometry("500x500")
root.title("My app")
root.config(bg="white")

item=['Python','C++','Java','Javascript']
list_box=tk.Listbox(root)
list_box.pack()
#using a for loop to go through every element in my list
for i in item:
    list_box.insert(tk.END, i)
def print_selection():
    choice=list_box.curselection()
    print(item[choice[0]])

btn_print_selection=tk.Button(root, text="Print selection",command=print_selection).pack()
root.mainloop()
