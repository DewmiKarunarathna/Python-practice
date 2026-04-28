import tkinter as tk  #built in library, no need to import
root = tk.Tk()
root.geometry('500x500')
root.title('my app')
root.config(bg='white')
root.resizable(width=True, height=True)

#these won't work without them packed
lbl_email = tk.Label(root, text='Email')
lbl_password = tk.Label(root, text='Password')
txtbox_email = tk.Entry(root)
txtb_password = tk.Entry(root)


lbl_email.pack()
txtbox_email.pack()
lbl_password.pack()
txtb_password.pack()
def login():
    email = str(txtbox_email.get())
    password = str(txtb_password.get())
    if email=='Admin@gmail.com'and password=='admin':
        print('Logging succesful!')
    else:
        print('Logging failed')
btn_login = tk.Button(root, text='Login', command=login)
btn_login.pack()
root.mainloop()  #we need this to run the gui
