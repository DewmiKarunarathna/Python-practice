import tkinter as tk
#making tables
root=tk.Tk()
root.geometry('500x500')
root.title('my app')
root.config(bg='white')

table = ttk.Treeview(root,columns=("col1","col2","col3"),show='headings')
table.heading('col1',text='No')
table.heading('col2',text='Name')
table.heading('col3',text='School')

table.column('col1',width=20,anchor="center")
table.column('col2',width=100,anchor="center")
table.column('col3',width=150,anchor="center")
table.pack(fill=tk.BOTH, expand=True)
#making a sample dataset
data = [ (1,"Dewmi Karunarathna","Sirimavo Bandaranaike Vidyalaya"),
         (2,"Kalitha Karunarathna","Ananda College")]
for i in data:
    table.insert('','end',values=i)
root.mainloop()
