from tkinter import *
from time import strftime
from dec2bin import dec2bin

root = Tk()
root.title('Binary Clock')

def bin_time():

    hour = dec2bin(int(strftime('%H')))
    minute = dec2bin(int(strftime('%M')))
    second = dec2bin(int(strftime('%S')))

    return f'{hour}:{minute}:{second}'

def time():
    timeFormat = bin_time()
    clock.config(text= timeFormat)
    clock.after(1000, time)

clock = Label(root, font= "Arial 70 bold", pady= 30, fg= "cyan", bg= "black")
clock.pack(anchor= "center")

time()
mainloop()