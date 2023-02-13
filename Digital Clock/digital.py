from tkinter import *
from time import strftime

root = Tk()
root.title('Digital Clock')
root.config(bg= 'black')

def time():
    timeFormat = strftime('%H:%M:%S')
    clock.config(text= timeFormat)
    clock.after(1000, time)

    dateFormat = strftime('%A  %d/%m/%Y')
    date.config(text= dateFormat)

date = Label(root, font= "Arial 15 bold", pady= 0, fg= "cyan", bg= "black")
date.pack(anchor= E)

clock = Label(root, font= "Arial 100 bold", pady= 0, fg= "cyan", bg= "black")
clock.pack(anchor= "center")

time()
mainloop()