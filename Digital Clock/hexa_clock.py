from tkinter import *
from time import strftime
from hexa2dec import dec2hexa

root = Tk()
root.title('Hexadecimal Clock')
root.geometry('600x150')
root.config(bg= 'black')

def hexa_time():

    hour = dec2hexa(int(strftime('%H')))
    minute = dec2hexa(int(strftime('%M')))
    second = dec2hexa(int(strftime('%S')))

    return f'{hour}:{minute}:{second}'

def hexa_date():

    year = dec2hexa(int(strftime('%Y')))
    month = dec2hexa(int(strftime('%m')))
    day = dec2hexa(int(strftime('%d')))

    day_name = strftime('%A')

    return f'{day_name}    {day}/{month}/{year}'

def time():
    timeFormat = hexa_time()
    clock.config(text= timeFormat)
    clock.after(1000, time)

    dateFormat = hexa_date()
    date.config(text= dateFormat)

date = Label(root, font= "Arial 15 bold", pady= 0, fg= "cyan", bg= "black")
date.pack(anchor= E)

clock = Label(root, font= "Arial 100 bold", pady= 0, fg= "cyan", bg= "black")
clock.pack(anchor= "center")

time()
mainloop()