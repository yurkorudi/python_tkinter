import tkinter as tk
import time



tik = tk.Tk()

#tik.rowconfigure(4, {'minsize': 100})
tik.columnconfigure(4, {'minsize': 100})

tik.geometry('500x500')

tik.title('log player')

tik.config(bg = 'black')

    

nick = tk.Label(tik, text="enter your nick")
nick.grid(row=2 , column=2)
a1 = tk.Entry(tik)
a1.grid(row=3, column=2)


password = tk.Label(tik, text="enter password")
password.grid(row=4 , column=2)
a2 = tk.Entry(tik)
a2.grid(row=5, column=2)
    



def log_in():
    nick = a1.get()
    password = a2.get()
    print(nick , password)
    # f = open(r'F:/python 2020/tkinter/accounts.txt')
    # f_ = f.readlines()
    # f.close()
    return nick
    return password



def reg():
    canvas.delete("all")






#tk.Label(tik, text="                  ").grid(row=2, column=4)


btn = tk.Button(tik, text='log in', width=10, height=2, bg='red', fg='blue', command = log_in())
btn.grid(row=2 , column=5)
btn.config(command=log_in)

btn_2 = tk.Button(tik, text='register', width=10, height=2, bg='green', fg='blue', command = reg())
btn_2.grid(row=5 , column=5)
btn_2.config(command=log_in)




tik.mainloop()













