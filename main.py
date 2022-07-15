import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('BHANDS_EDITOR')
#create label

name_label=ttk.Label(win,text='enter ur name: ')
name_label.grid(row=0,column=0,sticky=tk.W)


class_label=ttk.Label(win,text='enter ur class: ')
class_label.grid(row=1,column=0,sticky=tk.W)

email_address=ttk.Label(win,text='enter ur email address: ')
email_address.grid(row=2,column=0,sticky=tk.W)

sub_address=ttk.Label(win,text='enter ur subjects: ')
sub_address.grid(row=3,column=0,sticky=tk.W)

#entryboxes
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

class_var=tk.StringVar()
class_entrybox=ttk.Entry(win,width=16,textvariable=class_var)
class_entrybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_address_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_address_entrybox.grid(row=2,column=1)

#combobox
combobox_var=tk.StringVar()
combobox1=ttk.Combobox(win,width=13,textvariable=combobox_var,state='readonly')
combobox1['values']=('physics','maths','english')
combobox1.current(0)
combobox1.grid(row=3,column=1)

#radiobutton
radiobutton_var=tk.StringVar\
    ()
radiobutton=ttk.Radiobutton(win,text='student',value='student',variable=radiobutton_var)
radiobutton.grid(row=4,column=0)

radiobutton1=ttk.Radiobutton(win,text='teacher',value='teacher',variable=radiobutton_var)
radiobutton1.grid(row=4,column=1)

#checkbutton
checkbutton_var=tk.IntVar()
checkbutton=ttk.Checkbutton(win,text='please subscribe to my new channel for more updates',variable=checkbutton_var)
checkbutton.grid(row=5,columnspan=3)

def action():
    username=name_var.get()
    userclass=class_var.get()
    useremail=email_var.get()
    userradio_button=radiobutton_var.get()
    user_commbobox=combobox_var.get()
    user_checkbuttton=checkbutton_var.get()
    if user_checkbuttton==1:
        y='subscribed channel'
    else:
        y='not subscribed channel'

    with open('userinfo.txt','a') as  f :
        f.write(f"{username},{userclass},{useremail},{y},{user_commbobox},{userradio_button}")
    #print(f"{username},{userclass},{useremail},{y},{user_commbobox},{userradio_button}")

    email_address_entrybox.delete(0,tk.EN)

#buttons
button1=tk.Button(win,text='submit',command=action)
button1.grid(row=6,column=0)



win.mainloop()
""""""