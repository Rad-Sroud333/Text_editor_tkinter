import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser,filedialog
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename,askdirectory,askopenfile,askopenfiles,asksaveasfilename,asksaveasfile,askopenfilenames
from tkinter import font
import shutil
import os

win=tk.Tk()

win.geometry('1250x650')
win.title('BHAND EDITOR')

main_menu=tk.Menu(win)
win.config(menu=main_menu)

new=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\new.png")
save=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\open.png")
opens=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\save.png")
save_as=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\save_as.png")
exit=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\exit.png")

path=''
def new_func(event=None):
    text_editor.delete(1.0,tk.END)

def save_as_function(event=None):
  global path
  try:
    path=asksaveasfilename(defaultextension='*.txt',initialdir=os.getcwd(),title='Files',filetypes=[('Text Files','*.txt'),("all files","*.*")])
    with open(path,'w') as file:
              text=text_editor.get(1.0,tk.END)
              file.write(text)
  except:
      return

def save_func(event=None):
  global path
  try:
    if path:
        text1=text_editor.get(1.0,tk.END)
        with open(path,'w') as wf:
            wf.write(text1)
    else:
        path=asksaveasfilename(defaultextension='*.txt',initialdir=os.getcwd(),title='Files',filetypes=[('Text Files','*.txt'),("all files","*.*")])
        text2=text_editor.get(1.0,tk.END)
        with open(path,'w') as wf:
            wf.write(text2)
        path.close()
  except:
      return


def open_function(event=None):
    global  path
    path=askopenfilename(initialdir=os.getcwd(),title='Files',filetypes=[('Text Files','*.txt'),("all files","*.*")])
    try:
       with open(path, 'r') as file:
          text_editor.delete(1.0,tk.END)
          text_editor.insert(1.0,file.read())
    except FileNotFoundError:
        return
    except:
        return
    win.title(os.path.basename(path))

url=''
def Exit_func(event):
     global url,text_changed
     try:
         if text_changed:
             exit_msg=tmsg.askyesnocancel("Quit","Do U Wanna Save?")
             if exit_msg:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w')as f:
                         f.write(content)

                else:
                    url=asksaveasfilename(defaultextension='*.txt',initialdir=os.getcwd(),title='Files',filetypes=[('Text Files','*.txt'),("all files","*.*")])       
                    content1=text_editor.get(1.0,tk.END)
                    with open(url,'w') as f:
                        f.write(content1)
                    win.destroy()

             elif exit_msg is None:
                exit_msg.destroy()

             else:
                 win.destroy()

         else:
           win.destroy()
     except:
         return


file=tk.Menu(main_menu,tearoff=False)

file.add_command(label="New File",image=new,compound='left',accelerator='Ctrl+N',command=new_func)
file.add_command(label="Open File",image=opens,compound='left',accelerator='Ctrl+O',command=open_function)
file.add_separator()
file.add_command(label="Save",image=save,compound='left',accelerator='Ctrl+S',command=save_func)
file.add_command(label="Save As",image=save_as,compound='left',accelerator='Ctrl+Alt+S',command=save_as_function)
file.add_separator()
file.add_command(label="Exit",image=exit,compound='left',accelerator='Ctrl+Q',command=Exit_func)


main_menu.add_cascade(label='file',menu=file)

copy=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\copy.png")
cut=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\cut.png")
paste=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\paste.png")
clear=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\clear_all.png")
find=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\find.png")

def find_dialog(event=None):

  def find():
      find_var=find_entry.get()
      #text_editor.tag_remove('find_match','1.0',tk.END)
      start_pos='1.0'
      if start_pos:
           while 1:
                start_post=text_editor.search(find_var,start_pos,stopindex=tk.END)
                if not start_pos:break
                end_pos=f"{start_post}+{len(find_var)}c"
                text_editor.tag_add('find_match',start_post,end_pos)

                start_pos=end_pos

                text_editor.tag_configure('find_match',foreground='red',background='yellow')


  def replace():
      content=text_editor.get(1.0,tk.END)
      find_var=find_entry.get()
      replace_var=replace_entry.get()
      new_content= content.replace(find_var,replace_var)
      text_editor.delete(1.0,tk.END)
      text_editor.insert(1.0,new_content)

  find_win=tk.Toplevel()
  find_win.geometry('450x250+500+200')
  find_win.title('Find')
  find_win.resizable(0,0)

  find_label_frame=ttk.LabelFrame(find_win,text="Find/Replace",relief="sunken")
  find_label_frame.pack(pady=20)

  find_text_label=ttk.Label(find_label_frame,text='Find')
  find_text_label.grid(row=0,column=0,padx=4,pady=6,sticky='w')

  replace_text_label=ttk.Label(find_label_frame,text='Replace')
  replace_text_label.grid(row=1,column=0,padx=4,pady=4)

  find_entry=ttk.Entry(find_label_frame,width=20)
  find_entry.grid(row=0,column=1,padx=6,pady=6)

  replace_entry=ttk.Entry(find_label_frame,width=20)
  replace_entry.grid(row=1,column=1,padx=6,pady=6)

  find_button=ttk.Button(find_label_frame,text='Find',width=6,command=find)
  find_button.grid(row=2,column=0,padx=6,pady=6)

  Replace_button=ttk.Button(find_label_frame,text='Replace',width=8,command=replace)
  Replace_button.grid(row=2,column=1,padx=4,pady=6)


  find_win.mainloop()

edit=tk.Menu(main_menu,tearoff=False)

edit.add_command(label="Copy",image=copy,compound='left',accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Cut",image=cut,compound='left',accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Paste",image=paste,compound='left',accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v >"))
edit.add_separator()
edit.add_command(label="Clear All",image=clear,compound='left',accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))

edit.add_command(label="Find",image=find,compound='left',accelerator='Ctrl+F',command=find_dialog)

main_menu.add_cascade(label='Edit',menu=edit)

tool_bar1=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\tool_bar.png")
status_bar1=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\status_bar.png")

view=tk.Menu(main_menu,tearoff=False)

tool_bar_var=tk.BooleanVar()
tool_bar_var.set(True)
status_bar_var=tk.BooleanVar()
status_bar_var.set(True)
def tool_bar_func():
    global tool_bar_var
    var1=tool_bar_var.get()
    if var1 is False:
        tool_bar.pack_forget()
        #tool_bar_var=False

    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side='top',fill='x')
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)

def status_bar_func():
    global status_bar_var
    var2=status_bar_var.get()
    if var2 is False:
        status_bar.pack_forget()
    else:
        status_bar.pack(side='b',fill="x")


view.add_checkbutton(label="Tool Bar",variable=tool_bar_var,image=tool_bar1,compound='left',command=tool_bar_func)
view.add_checkbutton(label="Status Bar",variable=status_bar_var,image=status_bar1,compound='left',command=status_bar_func)

main_menu.add_cascade(label="View",menu=view)


light=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\light_default.png")
light_plus=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\light_plus.png")
night_blue=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\night_blue.png")
red=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\red.png")
dark=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\dark.png")
monokai=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\monokai.png")

colour_theme={
             'Light':('#0000000','#ffffff'),
             'Light_Plus':('#474747','#e0e0e0'),
             'Dark':('#c4c4c4','#2d2d2d'),
             'Red':('#2d2d2d','#ffe8e8'),
             'Monokai':('#d3b774','#474747'),
             'Night_Blue':('#ededed','#6b9dc2'),
              }

colour_icon=(light,light_plus,dark,red,monokai,night_blue)

background_colour=tk.Menu(main_menu,tearoff=False)
theme_choice=tk.StringVar()

def theme_choice_func():
    var3=theme_choice.get()
    for i,j in colour_theme.items():
        fg,bg=j[0],j[1]
        if var3==i:
            text_editor.configure(fg=fg,background=bg)



count=0
for i in colour_theme:
        background_colour.add_radiobutton(label=i,image=colour_icon[count],compound='left',variable=theme_choice,command=theme_choice_func)
        count+=1

main_menu.add_cascade(label="Background Theme",menu=background_colour)

tool_bar=tk.Label(win)
tool_bar.pack(fill='x',side='top')


def file_folder_sorter():
  files_extensions={
                  'audio_extensions':('.mp3','.mp4a'),
                  'video_extensions':('.avi','.mp4'),
                   'documents_extensions':('.pdf','.png','.jpg','.csv','.py')
                  }
  folderpath=askdirectory()

  def file_finder(folderpath,files_extensions):

     return [file for file in os.listdir(folderpath) for extension in files_extensions if file.endswith(extension)]

  for key,value in files_extensions.items():
    folder_name=key.split('_')[0] +"files"
    folder_path=os.path.join(folderpath,folder_name)



    for item in  (file_finder(folderpath,value)):
      try:
        if os.path.isfile(item):
            if os.path.exists(folder_path):
                print("alread exist")
            else:
                os.mkdir(folder_path)

                item_path=os.path.join(folderpath,item)
                #item_newpath=os.path.join(folder_path,item)
                shutil.move(item_path,folder_path)

        else:
            print("files are mising from directory")



      except:
          return


file_sorter_image=tk.PhotoImage(file=r"C:\Users\91935\PycharmProjects\pythonProject9\file_folder_sorter1.png")
file_soter=tk.Button(tool_bar,image=file_sorter_image,command=file_folder_sorter)
file_soter.grid(row=0,column=21)

font_style_var=tk.StringVar()
font_tuples=tk.font.families()
font_box=ttk.Combobox(tool_bar,width=40,textvariable=font_style_var,state='readonly')
font_box.grid(row=0,column=0,padx=4,pady=4)

font_box['value']=font_tuples
font_box.current(font_tuples.index('Arial'))

font_size_var=tk.IntVar()

font_size=ttk.Combobox(tool_bar,width=12,textvariable=font_size_var,state='readonly')
font_size['values']=tuple(range(8,101))
font_size.current(8)
font_size.grid(row=0,column=3,padx=4,pady=4)


bold_button_variable=tk.StringVar()
bold_button_img=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\bold.png")
bold_text_button=tk.Button(tool_bar,image=bold_button_img,textvariable=bold_button_variable)
bold_text_button.grid(row=0,column=5,padx=4,pady=4)

italic_button_variable=tk.StringVar()
italic_button_img=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\italic.png")
italic_text_button=tk.Button(tool_bar,image=italic_button_img,textvariable=italic_button_variable)
italic_text_button.grid(row=0,column=7,padx=4,pady=4)

underline_button_variable=tk.StringVar()
underline_button_img=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\underline.png")
underline_text_button=tk.Button(tool_bar,image=underline_button_img,textvariable=underline_button_variable)
underline_text_button.grid(row=0,column=9,padx=4,pady=4)

fontcolor_button_variable=tk.StringVar()
fontcolor_button_img=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\font_color.png")
fontcolor_text_button=tk.Button(tool_bar,image=fontcolor_button_img,textvariable=fontcolor_button_variable)
fontcolor_text_button.grid(row=0,column=11,padx=4,pady=4)

align_left_button_variable=tk.StringVar()
align_left_button_img=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\align_left.png")
align_left_text_button=tk.Button(tool_bar,image=align_left_button_img,textvariable=align_left_button_variable)
align_left_text_button.grid(row=0,column=15,padx=4,pady=4)

align_right_button_variable=tk.StringVar()
align_right_button_img=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\align_right.png")
align_right_button=tk.Button(tool_bar,image=align_right_button_img,textvariable=align_right_button_variable)
align_right_button.grid(row=0,column=17,padx=4,pady=4)

align_center_button_variable=tk.StringVar()
align_center_button_img=tk.PhotoImage(file=r"C:\Users\91935\Downloads\icons2\icons2\align_center.png")
align_center_text_button=tk.Button(tool_bar,image=align_center_button_img,textvariable=align_center_button_variable)
align_center_text_button.grid(row=0,column=19,padx=4,pady=4)


scroll_bar=tk.Scrollbar(win)
scroll_bar.pack(fill="y",side="right")
text_editor=tk.Text(win,yscrollcommand=scroll_bar.set)
#text_editor.pack(fill='both',expand=True)
text_editor.focus_set()
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar.config(command=text_editor.yview())

status_bar=tk.Label(win,text="Words and Characters_Count")
status_bar.pack(side='bottom',fill='x')



#current_font_family='Arial'
#current_font_size=25
text_editor.configure(font=('Arial',16))

def change_font_family(win):

  current_font_family=font_style_var.get()
  current_font_size=font_size_var.get()

  text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font_family)

def change_font_size(event=None):

  current_font_family=font_style_var.get()
  current_font_size=font_size_var.get()

  text_editor.configure(font=(current_font_family,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_font_size)

def change_bold(event=None):
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(font_style_var.get(),font_size_var.get(),'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(font_style_var.get(),font_size_var.get(),'normal'))
bold_text_button.configure(command=change_bold)

def change_italic(event=None):
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(font_style_var.get(),font_size_var.get(),'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(font_style_var.get(),font_size_var.get(),'roman'))
bold_text_button.configure(command=change_bold)

italic_text_button.configure(command=change_italic)


def change_underline(event=None):
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(font_style_var.get(),font_size_var.get(),'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(font_style_var.get(),font_size_var.get(),'normal'))
bold_text_button.configure(command=change_bold)

underline_text_button.configure(command=change_underline)

def change_font_colour():
    colour_choser_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=colour_choser_var[1])

fontcolor_text_button.configure(command=change_font_colour)


def align_line_left():
    text_cotent=text_editor.get(1.0,'end')
    text_editor.delete(1.0,tk.END)
    text_editor.tag_config('left',justify=tk.LEFT)

    text_editor.insert(tk.INSERT,text_cotent,'left')

align_left_text_button.configure(command=align_line_left)


def align_line_right():
    text_cotent=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_cotent,'right')

align_right_button.configure(command=align_line_right)

def align_line_center():
    text_cotent=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_cotent,'center')

align_center_text_button.configure(command=align_line_center)

text_changed=False
def change_status_bar(event=None):
    if text_editor.edit_modified():
       global text_changed
       text_changed=True
       word=len(text_editor.get(1.0,'end-1c').split())
       character=len(text_editor.get(1.0,'end-1c'))
       characters_without_space=len(text_editor.get(1.0,'end-1c').replace(' ',''))
       status_bar.config(text=f"Chracters : {character}  Characters Without Space : {characters_without_space}   Word : {word} ")
       text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',change_status_bar)

text_editor.pack(fill='both',expand=True)

win.bind(("<Control-n>",new_func))
win.bind(("<Control-o>",open_function))
win.bind(("<Control-s>",save_func))
win.bind(("<Control-Alt-s>",save_as_function))
win.bind(("<Control-q>",Exit_func))
win.bind(("<Control-f>",find_dialog))

win.mainloop()