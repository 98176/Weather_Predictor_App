#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import time
from datetime import datetime
import requests




def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6e24fd7575d4d7a6daf799893afd5e31").json()
    e_wthr.config(text=data["weather"][0]["main"])
    e_wdsc.config(text=data["weather"][0]["description"])
    e_temp.config(text=str(int(data["main"]["temp"]-273.15))+ "°C")
    e_mntp.config(text=data["main"]["temp_min"])
    e_mxtp.config(text=data["main"]["temp_max"])
    e_prs.config(text=data["main"]["pressure"])
    e_wind.config(text=str(int(data['wind']['speed']))+"kmph")
    e_hmdt.config(text=f"{data['main']['humidity']}%")
    e_sunr.config(text=datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")+" AM")
    e_sunt.config(text=datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")+" PM")
    
    
    


win=Tk()
win.title("Weather Predictor")
win.config(bg="blue")
win.geometry("500x500")
win.resizable(width=False,height=False)


city_name=StringVar()

lbl_name=Label(win,text="Weather App",font=('Angsana New',40,'bold'),bg="blue",fg="white")
lbl_name.pack()


dt=time.strftime("%H:%M:%S")
e_date=Label(win,text=f"{dt}",font=('calibri',13),bg='blue',fg='white') # set date on window
e_date.place(relx=.4,rely=.4)


list_state=['----select----','Andhra Pradesh',
'Arunachal Pradesh',
'Assam',
'Bihar',
'Chhattisgarh',
'Goa',
'Gujarat',
'Haryana',
'Himachal Pradesh',
'Jharkhand',
'Karnataka',
'Kerala',
'Madhya Pradesh',
'Maharashtra',
'Manipur',
'Meghalaya',
'Mizoram',
'Nagaland',
'Odisha',
'Punjab',
'Rajasthan',
'Sikkim',
'Tamil Nadu',
'Telangana',
'Tripura',
'Uttar Pradesh',
'Uttarakhand',
'West Bengal']

com=ttk.Combobox(win,text="Weather App",values=list_state,font=("Calibri",20),textvariable=city_name)
com.place(x=95,y=65)


lbl_wthr=Label(win,text="Weather Climate :",font=('Angsana New',15),bg="blue",fg="white")
lbl_wthr.place(relx=.1,rely=.55)

e_wthr=Label(win,text="",font=('Calibri',15),bg='blue',fg='white',bd=0)
e_wthr.place(relx=.50,rely=.55)

lbl_wdsc=Label(win,text="Weather Description :",font=('Angsana New',15),bg="blue",fg="white")
lbl_wdsc.place(relx=.10,rely=.60)

e_wdsc=Label(win,text="",font=('Calibri',15),bg='blue',fg='white',bd=0)
e_wdsc.place(relx=.50,rely=.61)

lbl_temp=Label(win,text="Temperature :",font=('Angsana New',15),bg="blue",fg="white")
lbl_temp.place(relx=.10,rely=.65)

e_temp=Label(win,text="",font=('Calibri',15),bg='blue',fg='white',bd=0)
e_temp.place(relx=.50,rely=.67)

lbl_mntp=Label(win,text="Min Temp :",font=('Angsana New',15),bg="blue",fg="white")
lbl_mntp.place(relx=.10,rely=.70)

e_mntp=Label(win,text="",font=('Calibri',15),bg='blue',fg='white',bd=0)
e_mntp.place(relx=.50,rely=.73)

lbl_mxtp=Label(win,text="Max Temp :",font=('Angsana New',15),bg="blue",fg="white")
lbl_mxtp.place(relx=.10,rely=.75)

e_mxtp=Label(win,text="",font=('Calibri',15),bg='blue',fg='white',bd=0)
e_mxtp.place(relx=.50,rely=.79)

lbl_prs=Label(win,text="Pressure :",font=('Angsana New',15),bg="blue",fg="white")
lbl_prs.place(relx=.10,rely=.80)

e_prs=Label(win,text="",font=('Calibri',15),bg='blue',fg='white',bd=0)
e_prs.place(relx=.50,rely=.85)

e_wind=Label(win,text="",font=('Calibri',15),bg='blue',fg='white',bd=0)
e_wind.place(relx=.8,rely=.40)

e_hmdt=Label(win,text="",font=('Calibri',15),bg='blue',fg='white',bd=0)
e_hmdt.place(relx=.8,rely=.45)


e_sunr=Label(win,text="",font=('Calibri',10),bg='blue',fg='white',bd=0)
e_sunr.place(relx=0,rely=.4)

e_sunt=Label(win,text="",font=('Calibri',10),bg='blue',fg='white',bd=0)
e_sunt.place(relx=0,rely=.43)


btn_done=Button(win,text="Done",font=("Calibri",15,"bold"),bd=5,command=data_get)
btn_done.place(x=220,y=120)






win.mainloop()


# In[ ]:




