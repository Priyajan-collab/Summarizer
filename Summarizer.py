import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from NLTK import nltk_summarizer
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import tkinter
from tkinter import filedialog
#window banxa
main_screen=Tk()
main_screen.geometry("1200x720")
timestr=time.strftime('%Y%m%d-%H%M%S')
#style
style=ttk.Style(main_screen)
style.configure('lefttab.TNotebook', tabposition='wn') 


#get summary
def get_summary():
    Raw_text_taken=entry.get('1.0',tk.END)
    Final_text=nltk_summarizer(Raw_text_taken)
    print(Final_text)
    Processed_text="/n Summary{} ".format(Final_text)
    display_text.insert(tk.END,Processed_text)

def clear_text():
     entry.delete('1.0',END)

def clear_result():
    display_text.delete('1.0',END)

def save():
    Raw_text_taken=entry.get('1.0',tk.END)
    Final_text=nltk_summarizer(Raw_text_taken)
    file_name="summary"+timestr+'.txt'
    with open(file_name,'w') as f:
        f.write(Final_text)
    Processed_text="/nName of the file:  , /n Summary{} ".format(file_name,Final_text)
    display_text.insert(tk.END,Processed_text)

def get_url_summary():
    URL_id=str(URL.get('1.0',END))
    page=urlopen(URL_id)
    soup=BeautifulSoup(page,'lxml')
    fetched_text=''.join(map(lambda p:p.text,soup.find_all('p')))
    display_text2.insert( tk.END,fetched_text)
    

def get_summary2():
    Raw_text_taken=display_text2.get('1.0',tk.END)
    Final_text=nltk_summarizer(Raw_text_taken)
    print(Final_text)
    Processed_text="/n Summary{} ".format(Final_text)
    display_text3.insert(tk.END,Processed_text)


def save2():
    Raw_text_taken=display_text2.get('1.0',tk.END)
    Final_text=nltk_summarizer(Raw_text_taken)
    file_name="summary"+timestr+'.txt'
    with open(file_name,'w') as f:
        f.write(Final_text)
    Processed_text="/nName of the file:  , /n Summary{} ".format(file_name,Final_text)
    display_text.insert(tk.END,Processed_text)

def clear_text2():
     display_text2.delete('1.0',END)

def clear_result2():
    display_text3.delete('1.0',END)



#tab_controls
tab_controls=ttk.Notebook(main_screen,style='lefttab.TNotebook')
tab_1=ttk.Frame(tab_controls)
tab_2=ttk.Frame(tab_controls)
tab_3=ttk.Frame(tab_controls)

tab_controls.add(tab_1,text=f'{"Main page":^20}')
tab_controls.add(tab_2,text=f'{"URL":^20}')
tab_controls.add(tab_3,text=f' {"About me":^20}')
tab_controls.pack(expand=1,fill='both')

#labels
label_1=Label(tab_1,text='Enter your text to summarise',font=("ariel",15),fg='Blue')
label_1.grid(sticky="N",padx=320)
label_2=Label(tab_2,text="Enter your URl",font=('ariel',15),fg='Blue')
label_2.grid(sticky="N",padx=400)
label_3=Label(tab_3,text="Hi, My name is Priyajan Swongamikha and i somehow managed to make this app")
label_3.grid(row=0)

#entry tab
entry=ScrolledText(tab_1,height=20,width=120)
entry.grid(row=2,column=0,columnspan=20)
URL=Text(tab_2,height=2,width=50)
URL.grid(row=2,columnspan=5,padx=300)

#Buttons
Reset_buttons=Button(tab_1,text="Reset",font=('ariel',12),bg="green",fg='white',command=clear_text )
Summarise_button=Button(tab_1,text="Summarise",font=('ariel',12),bg="red",fg='white',command=get_summary)
Clear_Result=Button(tab_1,text="Clear Result",font=('ariel',15),bg='green',command=clear_result,fg='white')
save_button=Button(tab_1,text='Save',font=('ariel',15),fg='white',bg='blue',command=save)
Summarise_button2=Button(tab_2,text="Summarise",font=('ariel',12),bg="red",fg='white',command=get_summary2)
Clear_Result2=Button(tab_2,text="Clear Result",font=('ariel',15),bg='green',fg='white',command=clear_result2)
Reset_buttons2=Button(tab_2,text="Reset",font=('ariel',12),bg="green",fg='white' ,command=clear_text2)
save_button2=Button(tab_2,text='Save',font=('ariel',15),fg='white',bg='blue',command=save2)
fetch_button=Button(tab_2,text='Fetch URL',fg='Blue',bg='yellow',command=get_url_summary)


fetch_button.grid(row=2,sticky='E')
Reset_buttons.grid(sticky="E",row=6,column=19)
Reset_buttons2.grid(row=3,sticky='E')
Summarise_button.grid(sticky="N",row=6)
Clear_Result.grid(sticky="W",row=6)
save_button.grid(row=7,padx=120)
Summarise_button2.grid(row=3,padx=300)
Clear_Result2.grid(sticky="W",row=3)
save_button2.grid(row=6)

#display tab
display_text=ScrolledText(tab_1,height=20,width=120)
display_text.grid(row=8,columnspan=100)    

#URL display text
display_text2=ScrolledText(tab_2,height=15,width=120)
display_text2.grid(rows=4,columnspan=100)
display_text3=ScrolledText(tab_2,height=15,width=120)
display_text3.grid(rows=6,columnspan=100)






main_screen.mainloop()
