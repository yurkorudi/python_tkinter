import tkinter as tk
import random

t = tk.Tk()



t.geometry('1000x700')

t.title('reth')

t.config(bg='black')

def bt_1():
    # t.config(bg='blue')
    # a['state'] = 'disable'
    x = random.randint(50,950)

    y = random.randint(50,650)
    tk.Button(t, text='', width=10, height=2, bg='white', fg='blue', command=bt_2).place(x=x, y=y)
    return x
    return y

def bt_2():
    tk.Button(t, text='', width=10, height=2, bg='black', fg='blue', command=bt_1).place(x=x, y=y)
    
    





a = tk.Button(t, text='', width=10, height=2, bg='white', fg='blue', command=bt_1).place(x=100, y=50)

#a.place(x, y)









t.mainloop()