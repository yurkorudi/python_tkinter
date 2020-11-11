from tkinter import *
import time

t = Tk()
s = 0
t.geometry('500x500')
a = 0
lab = Label(t, text='clicks -')

lab.pack()
repeat = False
lab2 = Label(t, text='time = ')

lab2.pack()
t.config(bg='black')


    

def start():
    global s
    b_c['state'] = 'normal'
    b_s['state'] = 'disable'
    
    
    if s < 10:
        global a
        repeat = False
        s = s + 1
        t.after(1000, start)
        lab2.config(text='time = ' + str(s))
    else:
        repeat = True
        lab2.config(text='in 10 seconds you did' + str(s) + 'clicks')
        time.sleep(3)
        lab2.config(text='')
        lab.config(text='')
        b_c['state'] = 'disable'
        b_s['state'] = 'normal'
        a = 0
        s = 0
        
        
        return a
        return s

        
def click():
    global a
    a = a + 1
    lab.config(text='clicks - ' + str(a))
    


    return a

    
b_c = Button(t, text='cick', width=10, height=2, bg='white', fg='blue', command=click)
  
b_c['state']='disable'
b_c.pack()

b_s = Button(t, text='start', width=10, height=2, bg='white', fg='blue', command=start)

b_s.pack()



t.mainloop()
