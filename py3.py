import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Shree Ram')
label_name=['name','class','roll_no']
for i in range(len(label_name)):
    cur_label=i
    cur_label=tk.Label(win,text='Enter-'+label_name[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)
    print(cur_label)






win.mainloop()