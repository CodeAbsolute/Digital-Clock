# from tkinter import *
import tkinter as tk
import time

clk = tk.Tk()
clk.title("My Clock")
clk.geometry("1350x700+0+0")
# width,height, x-axis, y-axis
clk.config(bg="#0C1E28")

def clock():

    hr = str(time.strftime("%H"))
    min = str(time.strftime("%M"))
    sec = str(time.strftime("%S"))
    print(hr, min, sec)

    if int(hr) > 12 and int(min)>0 : # to convert am to pm
        lb_dn.config(text="PM")
    if int(hr) > 12:
        hr = str(int(int(hr)-12))

    lb_hr.config(text=hr)
    lb_min.config(text=min)
    lb_sec.config(text=sec)

    lb_hr.after(200, clock) # to make clock update every sec




lb_hr = tk.Label(clk, text = "12", font = ("Times 20 bold", 75,"bold"), bg= "#087587", fg = "white")
lb_hr.place(x=350, y=200, width = 150, height = 150)

lb_hr_text = tk.Label(clk, text = "HOUR", font = ("Times 20 bold", 20,"bold"), bg= "#087587", fg = "white")
lb_hr_text.place(x=350, y=360, width = 150, height = 50)

lb_min = tk.Label(clk, text = "12", font = ("Times 20 bold", 75,"bold"), bg= "#008EA4", fg = "white")
lb_min.place(x=520, y=200, width = 150, height = 150)

lb_min_text = tk.Label(clk, text = "MINUTES", font = ("Times 20 bold", 20,"bold"), bg= "#008EA4", fg = "white")
lb_min_text.place(x=520, y=360, width = 150, height = 50)

lb_sec = tk.Label(clk, text = "12", font = ("Times 20 bold", 75,"bold"), bg= "#068488", fg = "white")
lb_sec.place(x=690, y=200, width = 150, height = 150)

lb_sec_text = tk.Label(clk, text = "SECONDS", font = ("Times 20 bold", 20,"bold"), bg= "#068488", fg = "white")
lb_sec_text.place(x=690, y=360, width = 150, height = 50)

lb_dn = tk.Label(clk, text = "AM", font = ("Times 20 bold", 70,"bold"), bg= "#9F0646", fg = "white")
lb_dn.place(x=860, y=200, width = 150, height = 150)

lb_dn_text = tk.Label(clk, text = "NOON", font = ("Times 20 bold", 20,"bold"), bg= "#9F0646", fg = "white")
lb_dn_text.place(x=860, y=360, width = 150, height = 50)

clock()

clk.mainloop()
