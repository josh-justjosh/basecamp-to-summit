#!/usr/bin/env python
import tkinter as tk
import time
import datetime
from PIL import ImageTk, Image
import keyboard
import requests

def now():
    return datetime.datetime.now().astimezone()

scriptstart = now()

file="Logs/"+now().date().isoformat()+" "+now().time().isoformat()[0:8].replace(':','-')+".log"

def pw(*text):
    pout = str(now()) + " "
    #with open(file,"a") as f:
    #    f.write(str(now())+" ")
    for t in text:
        t=str(t)
    #       f.write(t+" ")
        pout += t + " "
    #  f.write("\n")
    print(pout)

pw("Script Start")

def alivetime():
    global scriptstart
    delta = now() - scriptstart
    days = delta.days
    hours = int(delta.seconds / 3600)
    minutes = int(delta.seconds / 60) - (hours * 60)
    seconds = delta.seconds - (hours * 3600) - (minutes * 60)
    days = str(days)
    hours = "0" + str(hours)
    minutes = "0" + str(minutes)
    seconds = "0" + str(seconds)
    out = days+":"+hours[-2:]+":"+minutes[-2:]+":"+seconds[-2:]
    return "Uptime: "+out

climbing = "Climbing Logo.png"
phantom = "Phantom Media Logo - white.png"

completedclimbs = 0
climbstogo = 681 - completedclimbs
requests.get("https://sequematic.com/variable-change/2293/85A7210D14/Climbing/="+str(completedclimbs))

my_w = tk.Tk()
climbs = tk.Label(my_w, text=str(completedclimbs),bg="black",fg="white",font=("Arial", 200,  'bold'))
climbs.place(relx=0.3, rely=0.3, anchor='center')
climbslbl = tk.Label(my_w, text="Climbs\nComplete",bg="black",fg="white",font=("Arial", 50,  'bold'))
climbslbl.place(relx=0.3, rely=0.5, anchor='center')
ctg = tk.Label(my_w, text=str(climbstogo),bg="black",fg="white",font=("Arial", 200,  'bold'))
ctg.place(relx=0.7, rely=0.3, anchor='center')
ctglbl = tk.Label(my_w, text="Climbs\nto Go",bg="black",fg="white",font=("Arial", 50,  'bold'))
ctglbl.place(relx=0.7, rely=0.5, anchor='center')
meters = tk.Label(my_w, text=str(round(completedclimbs*12.9939207048)),bg="black",fg="white",font=("Arial", 150,  'bold'))
meters.place(relx=0.3, rely=0.75, anchor='center')
meterslbl = tk.Label(my_w, text="Meters\nClimbed",bg="black",fg="white",font=("Arial", 40,  'bold'))
meterslbl.place(relx=0.3, rely=0.9, anchor='center')
mtg = tk.Label(my_w, text=str(round(climbstogo*12.9939207048,1)),bg="black",fg="white",font=("Arial", 150,  'bold'))
mtg.place(relx=0.7, rely=0.75, anchor='center')
mtglbl = tk.Label(my_w, text="Meters\nLeft",bg="black",fg="white",font=("Arial", 40,  'bold'))
mtglbl.place(relx=0.7, rely=0.9, anchor='center')
title = tk.Label(my_w, text="Basecamp to Summit",bg="black",fg="white",font=("Arial", 50, 'bold'))
title.place(relx=0.5, rely=0.05, anchor='center')
alive = tk.Label(my_w, text=alivetime(),bg="black",fg="white",font=("Arial", 5,  'bold'))
alive.place(relx=1, rely=1, anchor='se')

image1 = Image.open(climbing).resize((250, 250))
test = ImageTk.PhotoImage(image1)

climbinglogo = tk.Label(image=test)
climbinglogo.image = test
climbinglogo.configure(bg='black')
climbinglogo.place(relx=0.1, rely=0.15, anchor='center')

image2 = Image.open(phantom).resize((250, 250))
test = ImageTk.PhotoImage(image2)

phantomlogo = tk.Label(image=test)
phantomlogo.image = test
phantomlogo.configure(bg='black')
phantomlogo.place(relx=0.9, rely=0.15, anchor='center')

width,height=875,875 # set the variables 
c_width,c_height=width-5,height-5 # canvas width height
d=str(width)+"x"+str(height)+"+3840+0"
my_w.geometry(d)
my_w.configure(bg='black')
my_w.title("Basecamp to Summit")
sw,sh = my_w.winfo_screenwidth(),my_w.winfo_screenheight()
#pw("screen1:",sw,sh)
w,h = 1600,900 
my_w.geometry('%sx%s+%s+%s'%(w,h,int(sw),0))

def increase():
    global completedclimbs
    global climbstogo
    completedclimbs += 1
    climbstogo = 681 - completedclimbs
    climbs.configure(text=str(completedclimbs))
    ctg.configure(text=str(climbstogo))
    meters.configure(text=str(round(completedclimbs*12.9939207048)))
    mtg.configure(text=str(round(climbstogo*12.9939207048,1)))
    requests.get("https://sequematic.com/variable-change/2293/85A7210D14/Climbing/="+str(completedclimbs))
    pw(completedclimbs,climbstogo)

def decrease():
    global completedclimbs
    global climbstogo
    completedclimbs -= 1
    climbstogo += 1
    climbs.configure(text=str(completedclimbs))
    ctg.configure(text=str(climbstogo))
    meters.configure(text=str(round(completedclimbs*12.9939207048)))
    mtg.configure(text=str(round(climbstogo*12.9939207048,1)))
    pw(completedclimbs,climbstogo)

def loop():
    alive.config(text=alivetime())
    if keyboard.is_pressed("b"):
        increase()
        time.sleep(1)
    elif keyboard.is_pressed("ctrl+left"):
        decrease()
        time.sleep(1)
    title.after(1,loop)

my_w.attributes("-fullscreen", True)
loop()
my_w.mainloop()

