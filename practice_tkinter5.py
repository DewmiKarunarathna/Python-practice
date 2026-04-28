import tkinter as tk
#menu bars
root=tk.Tk()
root.geometry("500x500")
root.config(bg="white")

menu_bar=tk.Menu(root)

file_menu = tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New",command=lambda:print("New file"))
file_menu.add_command(label="Open",command=lambda:print("Open file"))
file_menu.add_command(label="Save",command=lambda:print("Save file"))
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

edit_menu =tk.Menu(menu_bar,tearoff=0)
edit_menu.add_command(label="Cut",command=lambda: print("Copy"))
edit_menu.add_command(label="Copy",command=lambda: print("Cut"))
edit_menu.add_command(label="Paste",command=lambda: print("Paste"))

menu_bar.add_cascade(label="File",menu=file_menu)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
root.config(menu=menu_bar)

root.mainloop()
