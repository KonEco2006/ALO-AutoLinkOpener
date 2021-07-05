import schedule        
import time
import webbrowser
import clock
import plan
import apscheduler
import sched
import day
import datetime
import calendar
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image

  

    
root = Tk()
root.title("ALO(AutoLinkOpener)")
root.geometry("800x600")
root.iconbitmap(r"icon.ico")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

def _on_mousewheel(event):
    my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
my_canvas.bind_all("<MouseWheel>", _on_mousewheel)

def open1():
    global my_img
    top1 = Toplevel()
    top1.title('ALO(AutoLinkOpener)-Instructions')
    top1.iconbitmap(r'icon.ico')
    
    my_img = ImageTk.PhotoImage(Image.open(r'ALO(AutoLinkOpener)-Instructions.png'))
    my_label1 = Label(top1, image=my_img).pack()
    btn2 = Button(top1, text="Close Instructions", command=top1.destroy, bg="WHITE", cursor="hand2").pack()


btn = Button(second_frame, text="Instructions", command=open1, bg="WHITE", cursor="hand2").pack()

   



label=Label(second_frame, text= "Insert the link1:", font=("Calibri", 12), fg ='blue')
label.pack()
link1= Entry(second_frame, width=100)
link1.pack()
label=Label(second_frame, text= "Insert the day you want to open the link1:", font=("Calibri", 12), fg ='orange')
label.pack()
day1= Entry(second_frame)
day1.pack()
label=Label(second_frame, text= "Insert the time you want to open the link1:", font=("Calibri", 12), fg ='red')
label.pack()
time1= Entry(second_frame)
time1.pack()
label=Label(second_frame, text= "Insert the link2:", font=("Calibri", 12), fg ='blue')
label.pack()
link2= Entry(second_frame, width=100)
link2.pack()
label=Label(second_frame, text= "Insert the day you want to open the link2:", font=("Calibri", 12), fg ='orange')
label.pack()
day2= Entry(second_frame)
day2.pack()
label=Label(second_frame, text= "Insert the time you want to open the link2:", font=("Calibri", 12), fg ='red')
label.pack()
time2= Entry(second_frame)
time2.pack()
label=Label(second_frame, text= "Insert the link3:", font=("Calibri", 12), fg ='blue')
label.pack()
link3= Entry(second_frame, width=100)
link3.pack()
label=Label(second_frame, text= "Insert the day you want to open the link3:", font=("Calibri", 12), fg ='orange')
label.pack()
day3= Entry(second_frame)
day3.pack()
label=Label(second_frame, text= "Insert the time you want to open the link3:", font=("Calibri", 12), fg ='red')
label.pack()
time3= Entry(second_frame)
time3.pack()
label=Label(second_frame, text= "Insert the link4:", font=("Calibri", 12), fg ='blue')
label.pack()
link4= Entry(second_frame, width=100)
link4.pack()
label=Label(second_frame, text= "Insert the day you want to open the link4:", font=("Calibri", 12), fg ='orange')
label.pack()
day4= Entry(second_frame)
day4.pack()
label=Label(second_frame, text= "Insert the time you want to open the link4:", font=("Calibri", 12), fg ='red')
label.pack()
time4= Entry(second_frame)
time4.pack()
label=Label(second_frame, text= "Insert the link5:", font=("Calibri", 12), fg ='blue')
label.pack()
link5= Entry(second_frame, width=100)
link5.pack()
label=Label(second_frame, text= "Insert the day you want to open the link5:", font=("Calibri", 12), fg ='orange')
label.pack()
day5= Entry(second_frame)
day5.pack()
label=Label(second_frame, text= "Insert the time you want to open the link5:", font=("Calibri", 12), fg ='red')
label.pack()
time5= Entry(second_frame)
time5.pack()
label=Label(second_frame, text= "Insert the link6:", font=("Calibri", 12), fg ='blue')
label.pack()
link6= Entry(second_frame, width=100)
link6.pack()
label=Label(second_frame, text= "Insert the day you want to open the link6:", font=("Calibri", 12), fg ='orange')
label.pack()
day6= Entry(second_frame)
day6.pack()
label=Label(second_frame, text= "Insert the time you want to open the link6:", font=("Calibri", 12), fg ='red')
label.pack()
time6= Entry(second_frame)
time6.pack()
label=Label(second_frame, text= "Insert the link7:", font=("Calibri", 12), fg ='blue')
label.pack()
link7= Entry(second_frame, width=100)
link7.pack()
label=Label(second_frame, text= "Insert the day you want to open the link7:", font=("Calibri", 12), fg ='orange')
label.pack()
day7= Entry(second_frame)
day7.pack()
label=Label(second_frame, text= "Insert the time you want to open the link7:", font=("Calibri", 12), fg ='red')
label.pack()
time7= Entry(second_frame)
time7.pack()
label=Label(second_frame, text= "Insert the link8:", font=("Calibri", 12), fg ='blue')
label.pack()
link8= Entry(second_frame, width=100)
link8.pack()
label=Label(second_frame, text= "Insert the day you want to open the link8:", font=("Calibri", 12), fg ='orange')
label.pack()
day8= Entry(second_frame)
day8.pack()
label=Label(second_frame, text= "Insert the time you want to open the link8:", font=("Calibri", 12), fg ='red')
label.pack()
time8= Entry(second_frame)
time8.pack()
label=Label(second_frame, text= "Insert the link9:", font=("Calibri", 12), fg ='blue')
label.pack()
link9= Entry(second_frame, width=100)
link9.pack()
label=Label(second_frame, text= "Insert the day you want to open the link9:", font=("Calibri", 12), fg ='orange')
label.pack()
day9= Entry(second_frame)
day9.pack()
label=Label(second_frame, text= "Insert the time you want to open the link9:", font=("Calibri", 12), fg ='red')
label.pack()
time9= Entry(second_frame)
time9.pack()
label=Label(second_frame, text= "Insert the link10:", font=("Calibri", 12), fg ='blue')
label.pack()
link10= Entry(second_frame, width=100)
link10.pack()
label=Label(second_frame, text= "Insert the day you want to open the link10:", font=("Calibri", 12), fg ='orange')
label.pack()
day10= Entry(second_frame)
day10.pack()
label=Label(second_frame, text= "Insert the time you want to open the link10:", font=("Calibri", 12), fg ='red')
label.pack()
time10= Entry(second_frame)
time10.pack()
label=Label(second_frame, text= "Insert the link11:", font=("Calibri", 12), fg ='blue')
label.pack()
link11= Entry(second_frame, width=100)
link11.pack()
label=Label(second_frame, text= "Insert the day you want to open the link11:", font=("Calibri", 12), fg ='orange')
label.pack()
day11= Entry(second_frame)
day11.pack()
label=Label(second_frame, text= "Insert the time you want to open the link11:", font=("Calibri", 12), fg ='red')
label.pack()
time11= Entry(second_frame)
time11.pack()
label=Label(second_frame, text= "Insert the link12:", font=("Calibri", 12), fg ='blue')
label.pack()
link12= Entry(second_frame, width=100)
link12.pack()
label=Label(second_frame, text= "Insert the day you want to open the link12:", font=("Calibri", 12), fg ='orange')
label.pack()
day12= Entry(second_frame)
day12.pack()
label=Label(second_frame, text= "Insert the time you want to open the link12:", font=("Calibri", 12), fg ='red')
label.pack()
time12= Entry(second_frame)
time12.pack()
label=Label(second_frame, text= "Insert the link13:", font=("Calibri", 12), fg ='blue')
label.pack()
link13= Entry(second_frame, width=100)
link13.pack()
label=Label(second_frame, text= "Insert the day you want to open the link13:", font=("Calibri", 12), fg ='orange')
label.pack()
day13= Entry(second_frame)
day13.pack()
label=Label(second_frame, text= "Insert the time you want to open the link13:", font=("Calibri", 12), fg ='red')
label.pack()
time13= Entry(second_frame)
time13.pack()
label=Label(second_frame, text= "Insert the link14:", font=("Calibri", 12), fg ='blue')
label.pack()
link14= Entry(second_frame, width=100)
link14.pack()
label=Label(second_frame, text= "Insert the day you want to open the link14:", font=("Calibri", 12), fg ='orange')
label.pack()
day14= Entry(second_frame)
day14.pack()
label=Label(second_frame, text= "Insert the time you want to open the link14:", font=("Calibri", 12), fg ='red')
label.pack()
time14= Entry(second_frame)
time14.pack()
label=Label(second_frame, text= "Insert the link15:", font=("Calibri", 12), fg ='blue')
label.pack()
link15= Entry(second_frame, width=100)
link15.pack()
label=Label(second_frame, text= "Insert the day you want to open the link15:", font=("Calibri", 12), fg ='orange')
label.pack()
day15= Entry(second_frame)
day15.pack()
label=Label(second_frame, text= "Insert the time you want to open the link15:", font=("Calibri", 12), fg ='red')
label.pack()
time15= Entry(second_frame)
time15.pack()
label=Label(second_frame, text= "Insert the link16:", font=("Calibri", 12), fg ='blue')
label.pack()
link16= Entry(second_frame, width=100)
link16.pack()
label=Label(second_frame, text= "Insert the day you want to open the link16:", font=("Calibri", 12), fg ='orange')
label.pack()
day16= Entry(second_frame)
day16.pack()
label=Label(second_frame, text= "Insert the time you want to open the link16:", font=("Calibri", 12), fg ='red')
label.pack()
time16= Entry(second_frame)
time16.pack()
label=Label(second_frame, text= "Insert the link17:", font=("Calibri", 12), fg ='blue')
label.pack()
link17= Entry(second_frame, width=100)
link17.pack()
label=Label(second_frame, text= "Insert the day you want to open the link17:", font=("Calibri", 12), fg ='orange')
label.pack()
day17= Entry(second_frame)
day17.pack()
label=Label(second_frame, text= "Insert the time you want to open the link17:", font=("Calibri", 12), fg ='red')
label.pack()
time17= Entry(second_frame)
time17.pack()
label=Label(second_frame, text= "Insert the link18:", font=("Calibri", 12), fg ='blue')
label.pack()
link18= Entry(second_frame, width=100)
link18.pack()
label=Label(second_frame, text= "Insert the day you want to open the link18:", font=("Calibri", 12), fg ='orange')
label.pack()
day18= Entry(second_frame)
day18.pack()
label=Label(second_frame, text= "Insert the time you want to open the link18:", font=("Calibri", 12), fg ='red')
label.pack()
time18= Entry(second_frame)
time18.pack()
label=Label(second_frame, text= "Insert the link19:", font=("Calibri", 12), fg ='blue')
label.pack()
link19= Entry(second_frame, width=100)
link19.pack()
label=Label(second_frame, text= "Insert the day you want to open the link19:", font=("Calibri", 12), fg ='orange')
label.pack()
day19= Entry(second_frame)
day19.pack()
label=Label(second_frame, text= "Insert the time you want to open the link19:", font=("Calibri", 12), fg ='red')
label.pack()
time19= Entry(second_frame)
time19.pack()
label=Label(second_frame, text= "Insert the link20:", font=("Calibri", 12), fg ='blue')
label.pack()
link20= Entry(second_frame, width=100)
link20.pack()
label=Label(second_frame, text= "Insert the day you want to open the link20:", font=("Calibri", 12), fg ='orange')
label.pack()
day20= Entry(second_frame)
day20.pack()
label=Label(second_frame, text= "Insert the time you want to open the link20:", font=("Calibri", 12), fg ='red')
label.pack()
time20= Entry(second_frame)
time20.pack()
label=Label(second_frame, text= "Insert the link21:", font=("Calibri", 12), fg ='blue')
label.pack()
link21= Entry(second_frame, width=100)
link21.pack()
label=Label(second_frame, text= "Insert the day you want to open the link21:", font=("Calibri", 12), fg ='orange')
label.pack()
day21= Entry(second_frame)
day21.pack()
label=Label(second_frame, text= "Insert the time you want to open the link21:", font=("Calibri", 12), fg ='red')
label.pack()
time21= Entry(second_frame)
time21.pack()
label=Label(second_frame, text= "Insert the link22:", font=("Calibri", 12), fg ='blue')
label.pack()
link22= Entry(second_frame, width=100)
link22.pack()
label=Label(second_frame, text= "Insert the day you want to open the link22:", font=("Calibri", 12), fg ='orange')
label.pack()
day22= Entry(second_frame)
day22.pack()
label=Label(second_frame, text= "Insert the time you want to open the link22:", font=("Calibri", 12), fg ='red')
label.pack()
time22= Entry(second_frame)
time22.pack()
label=Label(second_frame, text= "Insert the link23:", font=("Calibri", 12), fg ='blue')
label.pack()
link23= Entry(second_frame, width=100)
link23.pack()
label=Label(second_frame, text= "Insert the day you want to open the link23:", font=("Calibri", 12), fg ='orange')
label.pack()
day23= Entry(second_frame)
day23.pack()
label=Label(second_frame, text= "Insert the time you want to open the link23:", font=("Calibri", 12), fg ='red')
label.pack()
time23= Entry(second_frame)
time23.pack()
label=Label(second_frame, text= "Insert the link24:", font=("Calibri", 12), fg ='blue')
label.pack()
link24= Entry(second_frame, width=100)
link24.pack()
label=Label(second_frame, text= "Insert the day you want to open the link24:", font=("Calibri", 12), fg ='orange')
label.pack()
day24= Entry(second_frame)
day24.pack()
label=Label(second_frame, text= "Insert the time you want to open the link24:", font=("Calibri", 12), fg ='red')
label.pack()
time24= Entry(second_frame)
time24.pack()
label=Label(second_frame, text= "Insert the link25:", font=("Calibri", 12), fg ='blue')
label.pack()
link25= Entry(second_frame, width=100)
link25.pack()
label=Label(second_frame, text= "Insert the day you want to open the link25:", font=("Calibri", 12), fg ='orange')
label.pack()
day25= Entry(second_frame)
day25.pack()
label=Label(second_frame, text= "Insert the time you want to open the link25:", font=("Calibri", 12), fg ='red')
label.pack()
time25= Entry(second_frame)
time25.pack()
label=Label(second_frame, text= "Insert the link26:", font=("Calibri", 12), fg ='blue')
label.pack()
link26= Entry(second_frame, width=100)
link26.pack()
label=Label(second_frame, text= "Insert the day you want to open the link26:", font=("Calibri", 12), fg ='orange')
label.pack()
day26= Entry(second_frame)
day26.pack()
label=Label(second_frame, text= "Insert the time you want to open the link26:", font=("Calibri", 12), fg ='red')
label.pack()
time26= Entry(second_frame)
time26.pack()
label=Label(second_frame, text= "Insert the link27:", font=("Calibri", 12), fg ='blue')
label.pack()
link27= Entry(second_frame, width=100)
link27.pack()
label=Label(second_frame, text= "Insert the day you want to open the link27:", font=("Calibri", 12), fg ='orange')
label.pack()
day27= Entry(second_frame)
day27.pack()
label=Label(second_frame, text= "Insert the time you want to open the link27:", font=("Calibri", 12), fg ='red')
label.pack()
time27= Entry(second_frame)
time27.pack()
label=Label(second_frame, text= "Insert the link28:", font=("Calibri", 12), fg ='blue')
label.pack()
link28= Entry(second_frame, width=100)
link28.pack()
label=Label(second_frame, text= "Insert the day you want to open the link28:", font=("Calibri", 12), fg ='orange')
label.pack()
day28= Entry(second_frame)
day28.pack()
label=Label(second_frame, text= "Insert the time you want to open the link28:", font=("Calibri", 12), fg ='red')
label.pack()
time28= Entry(second_frame)
time28.pack()
label=Label(second_frame, text= "Insert the link29:", font=("Calibri", 12), fg ='blue')
label.pack()
link29= Entry(second_frame, width=100)
link29.pack()
label=Label(second_frame, text= "Insert the day you want to open the link29:", font=("Calibri", 12), fg ='orange')
label.pack()
day29= Entry(second_frame)
day29.pack()
label=Label(second_frame, text= "Insert the time you want to open the link29:", font=("Calibri", 12), fg ='red')
label.pack()
time29= Entry(second_frame)
time29.pack()
label=Label(second_frame, text= "Insert the link30:", font=("Calibri", 12), fg ='blue')
label.pack()
link30= Entry(second_frame, width=100)
link30.pack()
label=Label(second_frame, text= "Insert the day you want to open the link30:", font=("Calibri", 12), fg ='orange')
label.pack()
day30= Entry(second_frame)
day30.pack()
label=Label(second_frame, text= "Insert the time you want to open the link30:", font=("Calibri", 12), fg ='red')
label.pack()
time30= Entry(second_frame)
time30.pack()
label=Label(second_frame, text= "Insert the link31:", font=("Calibri", 12), fg ='blue')
label.pack()
link31= Entry(second_frame, width=100)
link31.pack()
label=Label(second_frame, text= "Insert the day you want to open the link31:", font=("Calibri", 12), fg ='orange')
label.pack()
day31= Entry(second_frame)
day31.pack()
label=Label(second_frame, text= "Insert the time you want to open the link31:", font=("Calibri", 12), fg ='red')
label.pack()
time31= Entry(second_frame)
time31.pack()
label=Label(second_frame, text= "Insert the link32:", font=("Calibri", 12), fg ='blue')
label.pack()
link32= Entry(second_frame, width=100)
link32.pack()
label=Label(second_frame, text= "Insert the day you want to open the link32:", font=("Calibri", 12), fg ='orange')
label.pack()
day32= Entry(second_frame)
day32.pack()
label=Label(second_frame, text= "Insert the time you want to open the link32:", font=("Calibri", 12), fg ='red')
label.pack()
time32= Entry(second_frame)
time32.pack()
label=Label(second_frame, text= "Insert the link33:", font=("Calibri", 12), fg ='blue')
label.pack()
link33= Entry(second_frame, width=100)
link33.pack()
label=Label(second_frame, text= "Insert the day you want to open the link33:", font=("Calibri", 12), fg ='orange')
label.pack()
day33= Entry(second_frame)
day33.pack()
label=Label(second_frame, text= "Insert the time you want to open the link33:", font=("Calibri", 12), fg ='red')
label.pack()
time33= Entry(second_frame)
time33.pack()
label=Label(second_frame, text= "Insert the link34:", font=("Calibri", 12), fg ='blue')
label.pack()
link34= Entry(second_frame, width=100)
link34.pack()
label=Label(second_frame, text= "Insert the day you want to open the link34:", font=("Calibri", 12), fg ='orange')
label.pack()
day34= Entry(second_frame)
day34.pack()
label=Label(second_frame, text= "Insert the time you want to open the link34:", font=("Calibri", 12), fg ='red')
label.pack()
time34= Entry(second_frame)
time34.pack()
label=Label(second_frame, text= "Insert the link35:", font=("Calibri", 12), fg ='blue')
label.pack()
link35= Entry(second_frame, width=100)
link35.pack()
label=Label(second_frame, text= "Insert the day you want to open the link35:", font=("Calibri", 12), fg ='orange')
label.pack()
day35= Entry(second_frame)
day35.pack()
label=Label(second_frame, text= "Insert the time you want to open the link35:", font=("Calibri", 12), fg ='red')
label.pack()
time35= Entry(second_frame)
time35.pack()
label=Label(second_frame, text= "Insert the link36:", font=("Calibri", 12), fg ='blue')
label.pack()
link36= Entry(second_frame, width=100)
link36.pack()
label=Label(second_frame, text= "Insert the day you want to open the link36:", font=("Calibri", 12), fg ='orange')
label.pack()
day36= Entry(second_frame)
day36.pack()
label=Label(second_frame, text= "Insert the time you want to open the link36:", font=("Calibri", 12), fg ='red')
label.pack()
time36= Entry(second_frame)
time36.pack()
label=Label(second_frame, text= "Insert the link37:", font=("Calibri", 12), fg ='blue')
label.pack()
link37= Entry(second_frame, width=100)
link37.pack()
label=Label(second_frame, text= "Insert the day you want to open the link37:", font=("Calibri", 12), fg ='orange')
label.pack()
day37= Entry(second_frame)
day37.pack()
label=Label(second_frame, text= "Insert the time you want to open the link37:", font=("Calibri", 12), fg ='red')
label.pack()
time37= Entry(second_frame)
time37.pack()
label=Label(second_frame, text= "Insert the link38:", font=("Calibri", 12), fg ='blue')
label.pack()
link38= Entry(second_frame, width=100)
link38.pack()
label=Label(second_frame, text= "Insert the day you want to open the link38:", font=("Calibri", 12), fg ='orange')
label.pack()
day38= Entry(second_frame)
day38.pack()
label=Label(second_frame, text= "Insert the time you want to open the link38:", font=("Calibri", 12), fg ='red')
label.pack()
time38= Entry(second_frame)
time38.pack()
label=Label(second_frame, text= "Insert the link39:", font=("Calibri", 12), fg ='blue')
label.pack()
link39= Entry(second_frame, width=100)
link39.pack()
label=Label(second_frame, text= "Insert the day you want to open the link39:", font=("Calibri", 12), fg ='orange')
label.pack()
day39= Entry(second_frame)
day39.pack()
label=Label(second_frame, text= "Insert the time you want to open the link39:", font=("Calibri", 12), fg ='red')
label.pack()
time39= Entry(second_frame)
time39.pack()
label=Label(second_frame, text= "Insert the link40:", font=("Calibri", 12), fg ='blue')
label.pack()
link40= Entry(second_frame, width=100)
link40.pack()
label=Label(second_frame, text= "Insert the day you want to open the link40:", font=("Calibri", 12), fg ='orange')
label.pack()
day40= Entry(second_frame)
day40.pack()
label=Label(second_frame, text= "Insert the time you want to open the link40:", font=("Calibri", 12), fg ='red')
label.pack()
time40= Entry(second_frame)
time40.pack()
label=Label(second_frame, text= "Insert the link41:", font=("Calibri", 12), fg ='blue')
label.pack()
link41= Entry(second_frame, width=100)
link41.pack()
label=Label(second_frame, text= "Insert the day you want to open the link41:", font=("Calibri", 12), fg ='orange')
label.pack()
day41= Entry(second_frame)
day41.pack()
label=Label(second_frame, text= "Insert the time you want to open the link41:", font=("Calibri", 12), fg ='red')
label.pack()
time41= Entry(second_frame)
time41.pack()
label=Label(second_frame, text= "Insert the link42:", font=("Calibri", 12), fg ='blue')
label.pack()
link42= Entry(second_frame, width=100)
link42.pack()
label=Label(second_frame, text= "Insert the day you want to open the link42:", font=("Calibri", 12), fg ='orange')
label.pack()
day42= Entry(second_frame)
day42.pack()
label=Label(second_frame, text= "Insert the time you want to open the link42:", font=("Calibri", 12), fg ='red')
label.pack()
time42= Entry(second_frame)
time42.pack()
label=Label(second_frame, text= "Insert the link43:", font=("Calibri", 12), fg ='blue')
label.pack()
link43= Entry(second_frame, width=100)
link43.pack()
label=Label(second_frame, text= "Insert the day you want to open the link43:", font=("Calibri", 12), fg ='orange')
label.pack()
day43= Entry(second_frame)
day43.pack()
label=Label(second_frame, text= "Insert the time you want to open the link43:", font=("Calibri", 12), fg ='red')
label.pack()
time43= Entry(second_frame)
time43.pack()
label=Label(second_frame, text= "Insert the link44:", font=("Calibri", 12), fg ='blue')
label.pack()
link44= Entry(second_frame, width=100)
link44.pack()
label=Label(second_frame, text= "Insert the day you want to open the link44:", font=("Calibri", 12), fg ='orange')
label.pack()
day44= Entry(second_frame)
day44.pack()
label=Label(second_frame, text= "Insert the time you want to open the link44:", font=("Calibri", 12), fg ='red')
label.pack()
time44= Entry(second_frame)
time44.pack()
label=Label(second_frame, text= "Insert the link45:", font=("Calibri", 12), fg ='blue')
label.pack()
link45= Entry(second_frame, width=100)
link45.pack()
label=Label(second_frame, text= "Insert the day you want to open the link45:", font=("Calibri", 12), fg ='orange')
label.pack()
day45= Entry(second_frame)
day45.pack()
label=Label(second_frame, text= "Insert the time you want to open the link45:", font=("Calibri", 12), fg ='red')
label.pack()
time45= Entry(second_frame)
time45.pack()
label=Label(second_frame, text= "Insert the link46:", font=("Calibri", 12), fg ='blue')
label.pack()
link46= Entry(second_frame, width=100)
link46.pack()
label=Label(second_frame, text= "Insert the day you want to open the link46:", font=("Calibri", 12), fg ='orange')
label.pack()
day46= Entry(second_frame)
day46.pack()
label=Label(second_frame, text= "Insert the time you want to open the link46:", font=("Calibri", 12), fg ='red')
label.pack()
time46= Entry(second_frame)
time46.pack()
label=Label(second_frame, text= "Insert the link47:", font=("Calibri", 12), fg ='blue')
label.pack()
link47= Entry(second_frame, width=100)
link47.pack()
label=Label(second_frame, text= "Insert the day you want to open the link47:", font=("Calibri", 12), fg ='orange')
label.pack()
day47= Entry(second_frame)
day47.pack()
label=Label(second_frame, text= "Insert the time you want to open the link47:", font=("Calibri", 12), fg ='red')
label.pack()
time47= Entry(second_frame)
time47.pack()
label=Label(second_frame, text= "Insert the link48:", font=("Calibri", 12), fg ='blue')
label.pack()
link48= Entry(second_frame, width=100)
link48.pack()
label=Label(second_frame, text= "Insert the day you want to open the link48:", font=("Calibri", 12), fg ='orange')
label.pack()
day48= Entry(second_frame)
day48.pack()
label=Label(second_frame, text= "Insert the time you want to open the link48:", font=("Calibri", 12), fg ='red')
label.pack()
time48= Entry(second_frame)
time48.pack()
label=Label(second_frame, text= "Insert the link49:", font=("Calibri", 12), fg ='blue')
label.pack()
link49= Entry(second_frame, width=100)
link49.pack()
label=Label(second_frame, text= "Insert the day you want to open the link49:", font=("Calibri", 12), fg ='orange')
label.pack()
day49= Entry(second_frame)
day49.pack()
label=Label(second_frame, text= "Insert the time you want to open the link49:", font=("Calibri", 12), fg ='red')
label.pack()
time49= Entry(second_frame)
time49.pack()
label=Label(second_frame, text= "Insert the link50:", font=("Calibri", 12), fg ='blue')
label.pack()
link50= Entry(second_frame, width=100)
link50.pack()
label=Label(second_frame, text= "Insert the day you want to open the link50:", font=("Calibri", 12), fg ='orange')
label.pack()
day50= Entry(second_frame)
day50.pack()
label=Label(second_frame, text= "Insert the time you want to open the link50:", font=("Calibri", 12), fg ='red')
label.pack()
time50= Entry(second_frame)
time50.pack()
label=Label(second_frame, text= "Insert the link51:", font=("Calibri", 12), fg ='blue')
label.pack()
link51= Entry(second_frame, width=100)
link51.pack()
label=Label(second_frame, text= "Insert the day you want to open the link51:", font=("Calibri", 12), fg ='orange')
label.pack()
day51= Entry(second_frame)
day51.pack()
label=Label(second_frame, text= "Insert the time you want to open the link51:", font=("Calibri", 12), fg ='red')
label.pack()
time51= Entry(second_frame)
time51.pack()
label=Label(second_frame, text= "Insert the link52:", font=("Calibri", 12), fg ='blue')
label.pack()
link52= Entry(second_frame, width=100)
link52.pack()
label=Label(second_frame, text= "Insert the day you want to open the link52:", font=("Calibri", 12), fg ='orange')
label.pack()
day52= Entry(second_frame)
day52.pack()
label=Label(second_frame, text= "Insert the time you want to open the link52:", font=("Calibri", 12), fg ='red')
label.pack()
time52= Entry(second_frame)
time52.pack()
label=Label(second_frame, text= "Insert the link53:", font=("Calibri", 12), fg ='blue')
label.pack()
link53= Entry(second_frame, width=100)
link53.pack()
label=Label(second_frame, text= "Insert the day you want to open the link53:", font=("Calibri", 12), fg ='orange')
label.pack()
day53= Entry(second_frame)
day53.pack()
label=Label(second_frame, text= "Insert the time you want to open the link53:", font=("Calibri", 12), fg ='red')
label.pack()
time53= Entry(second_frame)
time53.pack()
label=Label(second_frame, text= "Insert the link54:", font=("Calibri", 12), fg ='blue')
label.pack()
link54= Entry(second_frame, width=100)
link54.pack()
label=Label(second_frame, text= "Insert the day you want to open the link54:", font=("Calibri", 12), fg ='orange')
label.pack()
day54= Entry(second_frame)
day54.pack()
label=Label(second_frame, text= "Insert the time you want to open the link54:", font=("Calibri", 12), fg ='red')
label.pack()
time54= Entry(second_frame)
time54.pack()
label=Label(second_frame, text= "Insert the link55:", font=("Calibri", 12), fg ='blue')
label.pack()
link55= Entry(second_frame, width=100)
link55.pack()
label=Label(second_frame, text= "Insert the day you want to open the link55:", font=("Calibri", 12), fg ='orange')
label.pack()
day55= Entry(second_frame)
day55.pack()
label=Label(second_frame, text= "Insert the time you want to open the link55:", font=("Calibri", 12), fg ='red')
label.pack()
time55= Entry(second_frame)
time55.pack()
label=Label(second_frame, text= "Insert the link56:", font=("Calibri", 12), fg ='blue')
label.pack()
link56= Entry(second_frame, width=100)
link56.pack()
label=Label(second_frame, text= "Insert the day you want to open the link56:", font=("Calibri", 12), fg ='orange')
label.pack()
day56= Entry(second_frame)
day56.pack()
label=Label(second_frame, text= "Insert the time you want to open the link56:", font=("Calibri", 12), fg ='red')
label.pack()
time56= Entry(second_frame)
time56.pack()
label=Label(second_frame, text= "Insert the link57:", font=("Calibri", 12), fg ='blue')
label.pack()
link57= Entry(second_frame, width=100)
link57.pack()
label=Label(second_frame, text= "Insert the day you want to open the link57:", font=("Calibri", 12), fg ='orange')
label.pack()
day57= Entry(second_frame)
day57.pack()
label=Label(second_frame, text= "Insert the time you want to open the link57:", font=("Calibri", 12), fg ='red')
label.pack()
time57= Entry(second_frame)
time57.pack()
label=Label(second_frame, text= "Insert the link58:", font=("Calibri", 12), fg ='blue')
label.pack()
link58= Entry(second_frame, width=100)
link58.pack()
label=Label(second_frame, text= "Insert the day you want to open the link58:", font=("Calibri", 12), fg ='orange')
label.pack()
day58= Entry(second_frame)
day58.pack()
label=Label(second_frame, text= "Insert the time you want to open the link58:", font=("Calibri", 12), fg ='red')
label.pack()
time58= Entry(second_frame)
time58.pack()
label=Label(second_frame, text= "Insert the link59:", font=("Calibri", 12), fg ='blue')
label.pack()
link59= Entry(second_frame, width=100)
link59.pack()
label=Label(second_frame, text= "Insert the day you want to open the link59:", font=("Calibri", 12), fg ='orange')
label.pack()
day59= Entry(second_frame)
day59.pack()
label=Label(second_frame, text= "Insert the time you want to open the link59:", font=("Calibri", 12), fg ='red')
label.pack()
time59= Entry(second_frame)
time59.pack()
label=Label(second_frame, text= "Insert the link60:", font=("Calibri", 12), fg ='blue')
label.pack()
link60= Entry(second_frame, width=100)
link60.pack()
label=Label(second_frame, text= "Insert the day you want to open the link60:", font=("Calibri", 12), fg ='orange')
label.pack()
day60= Entry(second_frame)
day60.pack()
label=Label(second_frame, text= "Insert the time you want to open the link60:", font=("Calibri", 12), fg ='red')
label.pack()
time60= Entry(second_frame)
time60.pack()
label=Label(second_frame, text= "Insert the link61:", font=("Calibri", 12), fg ='blue')
label.pack()
link61= Entry(second_frame, width=100)
link61.pack()
label=Label(second_frame, text= "Insert the day you want to open the link61:", font=("Calibri", 12), fg ='orange')
label.pack()
day61= Entry(second_frame)
day61.pack()
label=Label(second_frame, text= "Insert the time you want to open the link61:", font=("Calibri", 12), fg ='red')
label.pack()
time61= Entry(second_frame)
time61.pack()
label=Label(second_frame, text= "Insert the link62:", font=("Calibri", 12), fg ='blue')
label.pack()
link62= Entry(second_frame, width=100)
link62.pack()
label=Label(second_frame, text= "Insert the day you want to open the link62:", font=("Calibri", 12), fg ='orange')
label.pack()
day62= Entry(second_frame)
day62.pack()
label=Label(second_frame, text= "Insert the time you want to open the link62:", font=("Calibri", 12), fg ='red')
label.pack()
time62= Entry(second_frame)
time62.pack()
label=Label(second_frame, text= "Insert the link63:", font=("Calibri", 12), fg ='blue')
label.pack()
link63= Entry(second_frame, width=100)
link63.pack()
label=Label(second_frame, text= "Insert the day you want to open the link63:", font=("Calibri", 12), fg ='orange')
label.pack()
day63= Entry(second_frame)
day63.pack()
label=Label(second_frame, text= "Insert the time you want to open the link63:", font=("Calibri", 12), fg ='red')
label.pack()
time63= Entry(second_frame)
time63.pack()
label=Label(second_frame, text= "Insert the link64:", font=("Calibri", 12), fg ='blue')
label.pack()
link64= Entry(second_frame, width=100)
link64.pack()
label=Label(second_frame, text= "Insert the day you want to open the link64:", font=("Calibri", 12), fg ='orange')
label.pack()
day64= Entry(second_frame)
day64.pack()
label=Label(second_frame, text= "Insert the time you want to open the link64:", font=("Calibri", 12), fg ='red')
label.pack()
time64= Entry(second_frame)
time64.pack()
label=Label(second_frame, text= "Insert the link65:", font=("Calibri", 12), fg ='blue')
label.pack()
link65= Entry(second_frame, width=100)
link65.pack()
label=Label(second_frame, text= "Insert the day you want to open the link65:", font=("Calibri", 12), fg ='orange')
label.pack()
day65= Entry(second_frame)
day65.pack()
label=Label(second_frame, text= "Insert the time you want to open the link65:", font=("Calibri", 12), fg ='red')
label.pack()
time65= Entry(second_frame)
time65.pack()
label=Label(second_frame, text= "Insert the link66:", font=("Calibri", 12), fg ='blue')
label.pack()
link66= Entry(second_frame, width=100)
link66.pack()
label=Label(second_frame, text= "Insert the day you want to open the link66:", font=("Calibri", 12), fg ='orange')
label.pack()
day66= Entry(second_frame)
day66.pack()
label=Label(second_frame, text= "Insert the time you want to open the link66:", font=("Calibri", 12), fg ='red')
label.pack()
time66= Entry(second_frame)
time66.pack()
label=Label(second_frame, text= "Insert the link67:", font=("Calibri", 12), fg ='blue')
label.pack()
link67= Entry(second_frame, width=100)
link67.pack()
label=Label(second_frame, text= "Insert the day you want to open the link67:", font=("Calibri", 12), fg ='orange')
label.pack()
day67= Entry(second_frame)
day67.pack()
label=Label(second_frame, text= "Insert the time you want to open the link67:", font=("Calibri", 12), fg ='red')
label.pack()
time67= Entry(second_frame)
time67.pack()
label=Label(second_frame, text= "Insert the link68:", font=("Calibri", 12), fg ='blue')
label.pack()
link68= Entry(second_frame, width=100)
link68.pack()
label=Label(second_frame, text= "Insert the day you want to open the link68:", font=("Calibri", 12), fg ='orange')
label.pack()
day68= Entry(second_frame)
day68.pack()
label=Label(second_frame, text= "Insert the time you want to open the link68:", font=("Calibri", 12), fg ='red')
label.pack()
time68= Entry(second_frame)
time68.pack()
label=Label(second_frame, text= "Insert the link69:", font=("Calibri", 12), fg ='blue')
label.pack()
link69= Entry(second_frame, width=100)
link69.pack()
label=Label(second_frame, text= "Insert the day you want to open the link69:", font=("Calibri", 12), fg ='orange')
label.pack()
day69= Entry(second_frame)
day69.pack()
label=Label(second_frame, text= "Insert the time you want to open the link69:", font=("Calibri", 12), fg ='red')
label.pack()
time69= Entry(second_frame)
time69.pack()
label=Label(second_frame, text= "Insert the link70:", font=("Calibri", 12), fg ='blue')
label.pack()
link70= Entry(second_frame, width=100)
link70.pack()
label=Label(second_frame, text= "Insert the day you want to open the link70:", font=("Calibri", 12), fg ='orange')
label.pack()
day70= Entry(second_frame)
day70.pack()
label=Label(second_frame, text= "Insert the time you want to open the link70:", font=("Calibri", 12), fg ='red')
label.pack()
time70= Entry(second_frame)
time70.pack()
label=Label(second_frame, text= "Insert the link71:", font=("Calibri", 12), fg ='blue')
label.pack()
link71= Entry(second_frame, width=100)
link71.pack()
label=Label(second_frame, text= "Insert the day you want to open the link71:", font=("Calibri", 12), fg ='orange')
label.pack()
day71= Entry(second_frame)
day71.pack()
label=Label(second_frame, text= "Insert the time you want to open the link71:", font=("Calibri", 12), fg ='red')
label.pack()
time71= Entry(second_frame)
time71.pack()
label=Label(second_frame, text= "Insert the link72:", font=("Calibri", 12), fg ='blue')
label.pack()
link72= Entry(second_frame, width=100)
link72.pack()
label=Label(second_frame, text= "Insert the day you want to open the link72:", font=("Calibri", 12), fg ='orange')
label.pack()
day72= Entry(second_frame)
day72.pack()
label=Label(second_frame, text= "Insert the time you want to open the link72:", font=("Calibri", 12), fg ='red')
label.pack()
time72= Entry(second_frame)
time72.pack()
label=Label(second_frame, text= "Insert the link73:", font=("Calibri", 12), fg ='blue')
label.pack()
link73= Entry(second_frame, width=100)
link73.pack()
label=Label(second_frame, text= "Insert the day you want to open the link73:", font=("Calibri", 12), fg ='orange')
label.pack()
day73= Entry(second_frame)
day73.pack()
label=Label(second_frame, text= "Insert the time you want to open the link73:", font=("Calibri", 12), fg ='red')
label.pack()
time73= Entry(second_frame)
time73.pack()
label=Label(second_frame, text= "Insert the link74:", font=("Calibri", 12), fg ='blue')
label.pack()
link74= Entry(second_frame, width=100)
link74.pack()
label=Label(second_frame, text= "Insert the day you want to open the link74:", font=("Calibri", 12), fg ='orange')
label.pack()
day74= Entry(second_frame)
day74.pack()
label=Label(second_frame, text= "Insert the time you want to open the link74:", font=("Calibri", 12), fg ='red')
label.pack()
time74= Entry(second_frame)
time74.pack()
label=Label(second_frame, text= "Insert the link75:", font=("Calibri", 12), fg ='blue')
label.pack()
link75= Entry(second_frame, width=100)
link75.pack()
label=Label(second_frame, text= "Insert the day you want to open the link75:", font=("Calibri", 12), fg ='orange')
label.pack()
day75= Entry(second_frame)
day75.pack()
label=Label(second_frame, text= "Insert the time you want to open the link75:", font=("Calibri", 12), fg ='red')
label.pack()
time75= Entry(second_frame)
time75.pack()
label=Label(second_frame, text= "Insert the link76:", font=("Calibri", 12), fg ='blue')
label.pack()
link76= Entry(second_frame, width=100)
link76.pack()
label=Label(second_frame, text= "Insert the day you want to open the link76:", font=("Calibri", 12), fg ='orange')
label.pack()
day76= Entry(second_frame)
day76.pack()
label=Label(second_frame, text= "Insert the time you want to open the link76:", font=("Calibri", 12), fg ='red')
label.pack()
time76= Entry(second_frame)
time76.pack()
label=Label(second_frame, text= "Insert the link77:", font=("Calibri", 12), fg ='blue')
label.pack()
link77= Entry(second_frame, width=100)
link77.pack()
label=Label(second_frame, text= "Insert the day you want to open the link77:", font=("Calibri", 12), fg ='orange')
label.pack()
day77= Entry(second_frame)
day77.pack()
label=Label(second_frame, text= "Insert the time you want to open the link77:", font=("Calibri", 12), fg ='red')
label.pack()
time77= Entry(second_frame)
time77.pack()
label=Label(second_frame, text= "Insert the link78:", font=("Calibri", 12), fg ='blue')
label.pack()
link78= Entry(second_frame, width=100)
link78.pack()
label=Label(second_frame, text= "Insert the day you want to open the link78:", font=("Calibri", 12), fg ='orange')
label.pack()
day78= Entry(second_frame)
day78.pack()
label=Label(second_frame, text= "Insert the time you want to open the link78:", font=("Calibri", 12), fg ='red')
label.pack()
time78= Entry(second_frame)
time78.pack()
label=Label(second_frame, text= "Insert the link79:", font=("Calibri", 12), fg ='blue')
label.pack()
link79= Entry(second_frame, width=100)
link79.pack()
label=Label(second_frame, text= "Insert the day you want to open the link79:", font=("Calibri", 12), fg ='orange')
label.pack()
day79= Entry(second_frame)
day79.pack()
label=Label(second_frame, text= "Insert the time you want to open the link79:", font=("Calibri", 12), fg ='red')
label.pack()
time79= Entry(second_frame)
time79.pack()
label=Label(second_frame, text= "Insert the link80:", font=("Calibri", 12), fg ='blue')
label.pack()
link80= Entry(second_frame, width=100)
link80.pack()
label=Label(second_frame, text= "Insert the day you want to open the link80:", font=("Calibri", 12), fg ='orange')
label.pack()
day80= Entry(second_frame)
day80.pack()
label=Label(second_frame, text= "Insert the time you want to open the link80:", font=("Calibri", 12), fg ='red')
label.pack()
time80= Entry(second_frame)
time80.pack()
label=Label(second_frame, text= "Insert the link81:", font=("Calibri", 12), fg ='blue')
label.pack()
link81= Entry(second_frame, width=100)
link81.pack()
label=Label(second_frame, text= "Insert the day you want to open the link81:", font=("Calibri", 12), fg ='orange')
label.pack()
day81= Entry(second_frame)
day81.pack()
label=Label(second_frame, text= "Insert the time you want to open the link81:", font=("Calibri", 12), fg ='red')
label.pack()
time81= Entry(second_frame)
time81.pack()
label=Label(second_frame, text= "Insert the link82:", font=("Calibri", 12), fg ='blue')
label.pack()
link82= Entry(second_frame, width=100)
link82.pack()
label=Label(second_frame, text= "Insert the day you want to open the link82:", font=("Calibri", 12), fg ='orange')
label.pack()
day82= Entry(second_frame)
day82.pack()
label=Label(second_frame, text= "Insert the time you want to open the link82:", font=("Calibri", 12), fg ='red')
label.pack()
time82= Entry(second_frame)
time82.pack()
label=Label(second_frame, text= "Insert the link83:", font=("Calibri", 12), fg ='blue')
label.pack()
link83= Entry(second_frame, width=100)
link83.pack()
label=Label(second_frame, text= "Insert the day you want to open the link83:", font=("Calibri", 12), fg ='orange')
label.pack()
day83= Entry(second_frame)
day83.pack()
label=Label(second_frame, text= "Insert the time you want to open the link83:", font=("Calibri", 12), fg ='red')
label.pack()
time83= Entry(second_frame)
time83.pack()
label=Label(second_frame, text= "Insert the link84:", font=("Calibri", 12), fg ='blue')
label.pack()
link84= Entry(second_frame, width=100)
link84.pack()
label=Label(second_frame, text= "Insert the day you want to open the link84:", font=("Calibri", 12), fg ='orange')
label.pack()
day84= Entry(second_frame)
day84.pack()
label=Label(second_frame, text= "Insert the time you want to open the link84:", font=("Calibri", 12), fg ='red')
label.pack()
time84= Entry(second_frame)
time84.pack()
label=Label(second_frame, text= "Insert the link85:", font=("Calibri", 12), fg ='blue')
label.pack()
link85= Entry(second_frame, width=100)
link85.pack()
label=Label(second_frame, text= "Insert the day you want to open the link85:", font=("Calibri", 12), fg ='orange')
label.pack()
day85= Entry(second_frame)
day85.pack()
label=Label(second_frame, text= "Insert the time you want to open the link85:", font=("Calibri", 12), fg ='red')
label.pack()
time85= Entry(second_frame)
time85.pack()
label=Label(second_frame, text= "Insert the link86:", font=("Calibri", 12), fg ='blue')
label.pack()
link86= Entry(second_frame, width=100)
link86.pack()
label=Label(second_frame, text= "Insert the day you want to open the link86:", font=("Calibri", 12), fg ='orange')
label.pack()
day86= Entry(second_frame)
day86.pack()
label=Label(second_frame, text= "Insert the time you want to open the link86:", font=("Calibri", 12), fg ='red')
label.pack()
time86= Entry(second_frame)
time86.pack()
label=Label(second_frame, text= "Insert the link87:", font=("Calibri", 12), fg ='blue')
label.pack()
link87= Entry(second_frame, width=100)
link87.pack()
label=Label(second_frame, text= "Insert the day you want to open the link87:", font=("Calibri", 12), fg ='orange')
label.pack()
day87= Entry(second_frame)
day87.pack()
label=Label(second_frame, text= "Insert the time you want to open the link87:", font=("Calibri", 12), fg ='red')
label.pack()
time87= Entry(second_frame)
time87.pack()
label=Label(second_frame, text= "Insert the link88:", font=("Calibri", 12), fg ='blue')
label.pack()
link88= Entry(second_frame, width=100)
link88.pack()
label=Label(second_frame, text= "Insert the day you want to open the link88:", font=("Calibri", 12), fg ='orange')
label.pack()
day88= Entry(second_frame)
day88.pack()
label=Label(second_frame, text= "Insert the time you want to open the link88:", font=("Calibri", 12), fg ='red')
label.pack()
time88= Entry(second_frame)
time88.pack()
label=Label(second_frame, text= "Insert the link89:", font=("Calibri", 12), fg ='blue')
label.pack()
link89= Entry(second_frame, width=100)
link89.pack()
label=Label(second_frame, text= "Insert the day you want to open the link89:", font=("Calibri", 12), fg ='orange')
label.pack()
day89= Entry(second_frame)
day89.pack()
label=Label(second_frame, text= "Insert the time you want to open the link89:", font=("Calibri", 12), fg ='red')
label.pack()
time89= Entry(second_frame)
time89.pack()
label=Label(second_frame, text= "Insert the link90:", font=("Calibri", 12), fg ='blue')
label.pack()
link90= Entry(second_frame, width=100)
link90.pack()
label=Label(second_frame, text= "Insert the day you want to open the link90:", font=("Calibri", 12), fg ='orange')
label.pack()
day90= Entry(second_frame)
day90.pack()
label=Label(second_frame, text= "Insert the time you want to open the link90:", font=("Calibri", 12), fg ='red')
label.pack()
time90= Entry(second_frame)
time90.pack()
label=Label(second_frame, text= "Insert the link91:", font=("Calibri", 12), fg ='blue')
label.pack()
link91= Entry(second_frame, width=100)
link91.pack()
label=Label(second_frame, text= "Insert the day you want to open the link91:", font=("Calibri", 12), fg ='orange')
label.pack()
day91= Entry(second_frame)
day91.pack()
label=Label(second_frame, text= "Insert the time you want to open the link91:", font=("Calibri", 12), fg ='red')
label.pack()
time91= Entry(second_frame)
time91.pack()
label=Label(second_frame, text= "Insert the link92:", font=("Calibri", 12), fg ='blue')
label.pack()
link92= Entry(second_frame, width=100)
link92.pack()
label=Label(second_frame, text= "Insert the day you want to open the link92:", font=("Calibri", 12), fg ='orange')
label.pack()
day92= Entry(second_frame)
day92.pack()
label=Label(second_frame, text= "Insert the time you want to open the link92:", font=("Calibri", 12), fg ='red')
label.pack()
time92= Entry(second_frame)
time92.pack()
label=Label(second_frame, text= "Insert the link93:", font=("Calibri", 12), fg ='blue')
label.pack()
link93= Entry(second_frame, width=100)
link93.pack()
label=Label(second_frame, text= "Insert the day you want to open the link93:", font=("Calibri", 12), fg ='orange')
label.pack()
day93= Entry(second_frame)
day93.pack()
label=Label(second_frame, text= "Insert the time you want to open the link93:", font=("Calibri", 12), fg ='red')
label.pack()
time93= Entry(second_frame)
time93.pack()
label=Label(second_frame, text= "Insert the link94:", font=("Calibri", 12), fg ='blue')
label.pack()
link94= Entry(second_frame, width=100)
link94.pack()
label=Label(second_frame, text= "Insert the day you want to open the link94:", font=("Calibri", 12), fg ='orange')
label.pack()
day94= Entry(second_frame)
day94.pack()
label=Label(second_frame, text= "Insert the time you want to open the link94:", font=("Calibri", 12), fg ='red')
label.pack()
time94= Entry(second_frame)
time94.pack()
label=Label(second_frame, text= "Insert the link95:", font=("Calibri", 12), fg ='blue')
label.pack()
link95= Entry(second_frame, width=100)
link95.pack()
label=Label(second_frame, text= "Insert the day you want to open the link95:", font=("Calibri", 12), fg ='orange')
label.pack()
day95= Entry(second_frame)
day95.pack()
label=Label(second_frame, text= "Insert the time you want to open the link95:", font=("Calibri", 12), fg ='red')
label.pack()
time95= Entry(second_frame)
time95.pack()
label=Label(second_frame, text= "Insert the link96:", font=("Calibri", 12), fg ='blue')
label.pack()
link96= Entry(second_frame, width=100)
link96.pack()
label=Label(second_frame, text= "Insert the day you want to open the link96:", font=("Calibri", 12), fg ='orange')
label.pack()
day96= Entry(second_frame)
day96.pack()
label=Label(second_frame, text= "Insert the time you want to open the link96:", font=("Calibri", 12), fg ='red')
label.pack()
time96= Entry(second_frame)
time96.pack()
label=Label(second_frame, text= "Insert the link97:", font=("Calibri", 12), fg ='blue')
label.pack()
link97= Entry(second_frame, width=100)
link97.pack()
label=Label(second_frame, text= "Insert the day you want to open the link97:", font=("Calibri", 12), fg ='orange')
label.pack()
day97= Entry(second_frame)
day97.pack()
label=Label(second_frame, text= "Insert the time you want to open the link97:", font=("Calibri", 12), fg ='red')
label.pack()
time97= Entry(second_frame)
time97.pack()
label=Label(second_frame, text= "Insert the link98:", font=("Calibri", 12), fg ='blue')
label.pack()
link98= Entry(second_frame, width=100)
link98.pack()
label=Label(second_frame, text= "Insert the day you want to open the link98:", font=("Calibri", 12), fg ='orange')
label.pack()
day98= Entry(second_frame)
day98.pack()
label=Label(second_frame, text= "Insert the time you want to open the link98:", font=("Calibri", 12), fg ='red')
label.pack()
time98= Entry(second_frame)
time98.pack()
label=Label(second_frame, text= "Insert the link99:", font=("Calibri", 12), fg ='blue')
label.pack()
link99= Entry(second_frame, width=100)
link99.pack()
label=Label(second_frame, text= "Insert the day you want to open the link99:", font=("Calibri", 12), fg ='orange')
label.pack()
day99= Entry(second_frame)
day99.pack()
label=Label(second_frame, text= "Insert the time you want to open the link99:", font=("Calibri", 12), fg ='red')
label.pack()
time99= Entry(second_frame)
time99.pack()
label=Label(second_frame, text= "Insert the link100:", font=("Calibri", 12), fg ='blue')
label.pack()
link100= Entry(second_frame, width=100)
link100.pack()
label=Label(second_frame, text= "Insert the day you want to open the link100:", font=("Calibri", 12), fg ='orange')
label.pack()
day100= Entry(second_frame)
day100.pack()
label=Label(second_frame, text= "Insert the time you want to open the link100:", font=("Calibri", 12), fg ='red')
label.pack()
time100= Entry(second_frame)
time100.pack()
label=Label(second_frame, text= "Insert the link101:", font=("Calibri", 12), fg ='blue')
label.pack()
link101= Entry(second_frame, width=100)
link101.pack()
label=Label(second_frame, text= "Insert the day you want to open the link101:", font=("Calibri", 12), fg ='orange')
label.pack()
day101= Entry(second_frame)
day101.pack()
label=Label(second_frame, text= "Insert the time you want to open the link101:", font=("Calibri", 12), fg ='red')
label.pack()
time101= Entry(second_frame)
time101.pack()
label=Label(second_frame, text= "Insert the link102:", font=("Calibri", 12), fg ='blue')
label.pack()
link102= Entry(second_frame, width=100)
link102.pack()
label=Label(second_frame, text= "Insert the day you want to open the link102:", font=("Calibri", 12), fg ='orange')
label.pack()
day102= Entry(second_frame)
day102.pack()
label=Label(second_frame, text= "Insert the time you want to open the link102:", font=("Calibri", 12), fg ='red')
label.pack()
time102= Entry(second_frame)
time102.pack()
label=Label(second_frame, text= "Insert the link103:", font=("Calibri", 12), fg ='blue')
label.pack()
link103= Entry(second_frame, width=100)
link103.pack()
label=Label(second_frame, text= "Insert the day you want to open the link103:", font=("Calibri", 12), fg ='orange')
label.pack()
day103= Entry(second_frame)
day103.pack()
label=Label(second_frame, text= "Insert the time you want to open the link103:", font=("Calibri", 12), fg ='red')
label.pack()
time103= Entry(second_frame)
time103.pack()
label=Label(second_frame, text= "Insert the link104:", font=("Calibri", 12), fg ='blue')
label.pack()
link104= Entry(second_frame, width=100)
link104.pack()
label=Label(second_frame, text= "Insert the day you want to open the link104:", font=("Calibri", 12), fg ='orange')
label.pack()
day104= Entry(second_frame)
day104.pack()
label=Label(second_frame, text= "Insert the time you want to open the link104:", font=("Calibri", 12), fg ='red')
label.pack()
time104= Entry(second_frame)
time104.pack()
label=Label(second_frame, text= "Insert the link105:", font=("Calibri", 12), fg ='blue')
label.pack()
link105= Entry(second_frame, width=100)
link105.pack()
label=Label(second_frame, text= "Insert the day you want to open the link105:", font=("Calibri", 12), fg ='orange')
label.pack()
day105= Entry(second_frame)
day105.pack()
label=Label(second_frame, text= "Insert the time you want to open the link105:", font=("Calibri", 12), fg ='red')
label.pack()
time105= Entry(second_frame)
time105.pack()
label=Label(second_frame, text= "Insert the link106:", font=("Calibri", 12), fg ='blue')
label.pack()
link106= Entry(second_frame, width=100)
link106.pack()
label=Label(second_frame, text= "Insert the day you want to open the link106:", font=("Calibri", 12), fg ='orange')
label.pack()
day106= Entry(second_frame)
day106.pack()
label=Label(second_frame, text= "Insert the time you want to open the link106:", font=("Calibri", 12), fg ='red')
label.pack()
time106= Entry(second_frame)
time106.pack()
label=Label(second_frame, text= "Insert the link107:", font=("Calibri", 12), fg ='blue')
label.pack()
link107= Entry(second_frame, width=100)
link107.pack()
label=Label(second_frame, text= "Insert the day you want to open the link107:", font=("Calibri", 12), fg ='orange')
label.pack()
day107= Entry(second_frame)
day107.pack()
label=Label(second_frame, text= "Insert the time you want to open the link107:", font=("Calibri", 12), fg ='red')
label.pack()
time107= Entry(second_frame)
time107.pack()
label=Label(second_frame, text= "Insert the link108:", font=("Calibri", 12), fg ='blue')
label.pack()
link108= Entry(second_frame, width=100)
link108.pack()
label=Label(second_frame, text= "Insert the day you want to open the link108:", font=("Calibri", 12), fg ='orange')
label.pack()
day108= Entry(second_frame)
day108.pack()
label=Label(second_frame, text= "Insert the time you want to open the link108:", font=("Calibri", 12), fg ='red')
label.pack()
time108= Entry(second_frame)
time108.pack()
label=Label(second_frame, text= "Insert the link109:", font=("Calibri", 12), fg ='blue')
label.pack()
link109= Entry(second_frame, width=100)
link109.pack()
label=Label(second_frame, text= "Insert the day you want to open the link109:", font=("Calibri", 12), fg ='orange')
label.pack()
day109= Entry(second_frame)
day109.pack()
label=Label(second_frame, text= "Insert the time you want to open the link109:", font=("Calibri", 12), fg ='red')
label.pack()
time109= Entry(second_frame)
time109.pack()
label=Label(second_frame, text= "Insert the link110:", font=("Calibri", 12), fg ='blue')
label.pack()
link110= Entry(second_frame, width=100)
link110.pack()
label=Label(second_frame, text= "Insert the day you want to open the link110:", font=("Calibri", 12), fg ='orange')
label.pack()
day110= Entry(second_frame)
day110.pack()
label=Label(second_frame, text= "Insert the time you want to open the link110:", font=("Calibri", 12), fg ='red')
label.pack()
time110= Entry(second_frame)
time110.pack()
label=Label(second_frame, text= "Insert the link111:", font=("Calibri", 12), fg ='blue')
label.pack()
link111= Entry(second_frame, width=100)
link111.pack()
label=Label(second_frame, text= "Insert the day you want to open the link111:", font=("Calibri", 12), fg ='orange')
label.pack()
day111= Entry(second_frame)
day111.pack()
label=Label(second_frame, text= "Insert the time you want to open the link111:", font=("Calibri", 12), fg ='red')
label.pack()
time111= Entry(second_frame)
time111.pack()
label=Label(second_frame, text= "Insert the link112:", font=("Calibri", 12), fg ='blue')
label.pack()
link112= Entry(second_frame, width=100)
link112.pack()
label=Label(second_frame, text= "Insert the day you want to open the link112:", font=("Calibri", 12), fg ='orange')
label.pack()
day112= Entry(second_frame)
day112.pack()
label=Label(second_frame, text= "Insert the time you want to open the link112:", font=("Calibri", 12), fg ='red')
label.pack()
time112= Entry(second_frame)
time112.pack()
label=Label(second_frame, text= "Insert the link113:", font=("Calibri", 12), fg ='blue')
label.pack()
link113= Entry(second_frame, width=100)
link113.pack()
label=Label(second_frame, text= "Insert the day you want to open the link113:", font=("Calibri", 12), fg ='orange')
label.pack()
day113= Entry(second_frame)
day113.pack()
label=Label(second_frame, text= "Insert the time you want to open the link113:", font=("Calibri", 12), fg ='red')
label.pack()
time113= Entry(second_frame)
time113.pack()
label=Label(second_frame, text= "Insert the link114:", font=("Calibri", 12), fg ='blue')
label.pack()
link114= Entry(second_frame, width=100)
link114.pack()
label=Label(second_frame, text= "Insert the day you want to open the link114:", font=("Calibri", 12), fg ='orange')
label.pack()
day114= Entry(second_frame)
day114.pack()
label=Label(second_frame, text= "Insert the time you want to open the link114:", font=("Calibri", 12), fg ='red')
label.pack()
time114= Entry(second_frame)
time114.pack()
label=Label(second_frame, text= "Insert the link115:", font=("Calibri", 12), fg ='blue')
label.pack()
link115= Entry(second_frame, width=100)
link115.pack()
label=Label(second_frame, text= "Insert the day you want to open the link115:", font=("Calibri", 12), fg ='orange')
label.pack()
day115= Entry(second_frame)
day115.pack()
label=Label(second_frame, text= "Insert the time you want to open the link115:", font=("Calibri", 12), fg ='red')
label.pack()
time115= Entry(second_frame)
time115.pack()
label=Label(second_frame, text= "Insert the link116:", font=("Calibri", 12), fg ='blue')
label.pack()
link116= Entry(second_frame, width=100)
link116.pack()
label=Label(second_frame, text= "Insert the day you want to open the link116:", font=("Calibri", 12), fg ='orange')
label.pack()
day116= Entry(second_frame)
day116.pack()
label=Label(second_frame, text= "Insert the time you want to open the link116:", font=("Calibri", 12), fg ='red')
label.pack()
time116= Entry(second_frame)
time116.pack()
label=Label(second_frame, text= "Insert the link117:", font=("Calibri", 12), fg ='blue')
label.pack()
link117= Entry(second_frame, width=100)
link117.pack()
label=Label(second_frame, text= "Insert the day you want to open the link117:", font=("Calibri", 12), fg ='orange')
label.pack()
day117= Entry(second_frame)
day117.pack()
label=Label(second_frame, text= "Insert the time you want to open the link117:", font=("Calibri", 12), fg ='red')
label.pack()
time117= Entry(second_frame)
time117.pack()
label=Label(second_frame, text= "Insert the link118:", font=("Calibri", 12), fg ='blue')
label.pack()
link118= Entry(second_frame, width=100)
link118.pack()
label=Label(second_frame, text= "Insert the day you want to open the link118:", font=("Calibri", 12), fg ='orange')
label.pack()
day118= Entry(second_frame)
day118.pack()
label=Label(second_frame, text= "Insert the time you want to open the link118:", font=("Calibri", 12), fg ='red')
label.pack()
time118= Entry(second_frame)
time118.pack()
label=Label(second_frame, text= "Insert the link119:", font=("Calibri", 12), fg ='blue')
label.pack()
link119= Entry(second_frame, width=100)
link119.pack()
label=Label(second_frame, text= "Insert the day you want to open the link119:", font=("Calibri", 12), fg ='orange')
label.pack()
day119= Entry(second_frame)
day119.pack()
label=Label(second_frame, text= "Insert the time you want to open the link119:", font=("Calibri", 12), fg ='red')
label.pack()
time119= Entry(second_frame)
time119.pack()
label=Label(second_frame, text= "Insert the link120:", font=("Calibri", 12), fg ='blue')
label.pack()
link120= Entry(second_frame, width=100)
link120.pack()
label=Label(second_frame, text= "Insert the day you want to open the link120:", font=("Calibri", 12), fg ='orange')
label.pack()
day120= Entry(second_frame)
day120.pack()
label=Label(second_frame, text= "Insert the time you want to open the link120:", font=("Calibri", 12), fg ='red')
label.pack()
time120= Entry(second_frame)
time120.pack()
label=Label(second_frame, text= "Insert the link121:", font=("Calibri", 12), fg ='blue')
label.pack()
link121= Entry(second_frame, width=100)
link121.pack()
label=Label(second_frame, text= "Insert the day you want to open the link121:", font=("Calibri", 12), fg ='orange')
label.pack()
day121= Entry(second_frame)
day121.pack()
label=Label(second_frame, text= "Insert the time you want to open the link121:", font=("Calibri", 12), fg ='red')
label.pack()
time121= Entry(second_frame)
time121.pack()
label=Label(second_frame, text= "Insert the link122:", font=("Calibri", 12), fg ='blue')
label.pack()
link122= Entry(second_frame, width=100)
link122.pack()
label=Label(second_frame, text= "Insert the day you want to open the link122:", font=("Calibri", 12), fg ='orange')
label.pack()
day122= Entry(second_frame)
day122.pack()
label=Label(second_frame, text= "Insert the time you want to open the link122:", font=("Calibri", 12), fg ='red')
label.pack()
time122= Entry(second_frame)
time122.pack()
label=Label(second_frame, text= "Insert the link123:", font=("Calibri", 12), fg ='blue')
label.pack()
link123= Entry(second_frame, width=100)
link123.pack()
label=Label(second_frame, text= "Insert the day you want to open the link123:", font=("Calibri", 12), fg ='orange')
label.pack()
day123= Entry(second_frame)
day123.pack()
label=Label(second_frame, text= "Insert the time you want to open the link123:", font=("Calibri", 12), fg ='red')
label.pack()
time123= Entry(second_frame)
time123.pack()
label=Label(second_frame, text= "Insert the link124:", font=("Calibri", 12), fg ='blue')
label.pack()
link124= Entry(second_frame, width=100)
link124.pack()
label=Label(second_frame, text= "Insert the day you want to open the link124:", font=("Calibri", 12), fg ='orange')
label.pack()
day124= Entry(second_frame)
day124.pack()
label=Label(second_frame, text= "Insert the time you want to open the link124:", font=("Calibri", 12), fg ='red')
label.pack()
time124= Entry(second_frame)
time124.pack()
label=Label(second_frame, text= "Insert the link125:", font=("Calibri", 12), fg ='blue')
label.pack()
link125= Entry(second_frame, width=100)
link125.pack()
label=Label(second_frame, text= "Insert the day you want to open the link125:", font=("Calibri", 12), fg ='orange')
label.pack()
day125= Entry(second_frame)
day125.pack()
label=Label(second_frame, text= "Insert the time you want to open the link125:", font=("Calibri", 12), fg ='red')
label.pack()
time125= Entry(second_frame)
time125.pack()
label=Label(second_frame, text= "Insert the link126:", font=("Calibri", 12), fg ='blue')
label.pack()
link126= Entry(second_frame, width=100)
link126.pack()
label=Label(second_frame, text= "Insert the day you want to open the link126:", font=("Calibri", 12), fg ='orange')
label.pack()
day126= Entry(second_frame)
day126.pack()
label=Label(second_frame, text= "Insert the time you want to open the link126:", font=("Calibri", 12), fg ='red')
label.pack()
time126= Entry(second_frame)
time126.pack()
label=Label(second_frame, text= "Insert the link127:", font=("Calibri", 12), fg ='blue')
label.pack()
link127= Entry(second_frame, width=100)
link127.pack()
label=Label(second_frame, text= "Insert the day you want to open the link127:", font=("Calibri", 12), fg ='orange')
label.pack()
day127= Entry(second_frame)
day127.pack()
label=Label(second_frame, text= "Insert the time you want to open the link127:", font=("Calibri", 12), fg ='red')
label.pack()
time127= Entry(second_frame)
time127.pack()
label=Label(second_frame, text= "Insert the link128:", font=("Calibri", 12), fg ='blue')
label.pack()
link128= Entry(second_frame, width=100)
link128.pack()
label=Label(second_frame, text= "Insert the day you want to open the link128:", font=("Calibri", 12), fg ='orange')
label.pack()
day128= Entry(second_frame)
day128.pack()
label=Label(second_frame, text= "Insert the time you want to open the link128:", font=("Calibri", 12), fg ='red')
label.pack()
time128= Entry(second_frame)
time128.pack()
label=Label(second_frame, text= "Insert the link129:", font=("Calibri", 12), fg ='blue')
label.pack()
link129= Entry(second_frame, width=100)
link129.pack()
label=Label(second_frame, text= "Insert the day you want to open the link129:", font=("Calibri", 12), fg ='orange')
label.pack()
day129= Entry(second_frame)
day129.pack()
label=Label(second_frame, text= "Insert the time you want to open the link129:", font=("Calibri", 12), fg ='red')
label.pack()
time129= Entry(second_frame)
time129.pack()
label=Label(second_frame, text= "Insert the link130:", font=("Calibri", 12), fg ='blue')
label.pack()
link130= Entry(second_frame, width=100)
link130.pack()
label=Label(second_frame, text= "Insert the day you want to open the link130:", font=("Calibri", 12), fg ='orange')
label.pack()
day130= Entry(second_frame)
day130.pack()
label=Label(second_frame, text= "Insert the time you want to open the link130:", font=("Calibri", 12), fg ='red')
label.pack()
time130= Entry(second_frame)
time130.pack()
label=Label(second_frame, text= "Insert the link131:", font=("Calibri", 12), fg ='blue')
label.pack()
link131= Entry(second_frame, width=100)
link131.pack()
label=Label(second_frame, text= "Insert the day you want to open the link131:", font=("Calibri", 12), fg ='orange')
label.pack()
day131= Entry(second_frame)
day131.pack()
label=Label(second_frame, text= "Insert the time you want to open the link131:", font=("Calibri", 12), fg ='red')
label.pack()
time131= Entry(second_frame)
time131.pack()
label=Label(second_frame, text= "Insert the link132:", font=("Calibri", 12), fg ='blue')
label.pack()
link132= Entry(second_frame, width=100)
link132.pack()
label=Label(second_frame, text= "Insert the day you want to open the link132:", font=("Calibri", 12), fg ='orange')
label.pack()
day132= Entry(second_frame)
day132.pack()
label=Label(second_frame, text= "Insert the time you want to open the link132:", font=("Calibri", 12), fg ='red')
label.pack()
time132= Entry(second_frame)
time132.pack()
label=Label(second_frame, text= "Insert the link133:", font=("Calibri", 12), fg ='blue')
label.pack()
link133= Entry(second_frame, width=100)
link133.pack()
label=Label(second_frame, text= "Insert the day you want to open the link133:", font=("Calibri", 12), fg ='orange')
label.pack()
day133= Entry(second_frame)
day133.pack()
label=Label(second_frame, text= "Insert the time you want to open the link133:", font=("Calibri", 12), fg ='red')
label.pack()
time133= Entry(second_frame)
time133.pack()
label=Label(second_frame, text= "Insert the link134:", font=("Calibri", 12), fg ='blue')
label.pack()
link134= Entry(second_frame, width=100)
link134.pack()
label=Label(second_frame, text= "Insert the day you want to open the link134:", font=("Calibri", 12), fg ='orange')
label.pack()
day134= Entry(second_frame)
day134.pack()
label=Label(second_frame, text= "Insert the time you want to open the link134:", font=("Calibri", 12), fg ='red')
label.pack()
time134= Entry(second_frame)
time134.pack()
label=Label(second_frame, text= "Insert the link135:", font=("Calibri", 12), fg ='blue')
label.pack()
link135= Entry(second_frame, width=100)
link135.pack()
label=Label(second_frame, text= "Insert the day you want to open the link135:", font=("Calibri", 12), fg ='orange')
label.pack()
day135= Entry(second_frame)
day135.pack()
label=Label(second_frame, text= "Insert the time you want to open the link135:", font=("Calibri", 12), fg ='red')
label.pack()
time135= Entry(second_frame)
time135.pack()
label=Label(second_frame, text= "Insert the link136:", font=("Calibri", 12), fg ='blue')
label.pack()
link136= Entry(second_frame, width=100)
link136.pack()
label=Label(second_frame, text= "Insert the day you want to open the link136:", font=("Calibri", 12), fg ='orange')
label.pack()
day136= Entry(second_frame)
day136.pack()
label=Label(second_frame, text= "Insert the time you want to open the link136:", font=("Calibri", 12), fg ='red')
label.pack()
time136= Entry(second_frame)
time136.pack()
label=Label(second_frame, text= "Insert the link137:", font=("Calibri", 12), fg ='blue')
label.pack()
link137= Entry(second_frame, width=100)
link137.pack()
label=Label(second_frame, text= "Insert the day you want to open the link137:", font=("Calibri", 12), fg ='orange')
label.pack()
day137= Entry(second_frame)
day137.pack()
label=Label(second_frame, text= "Insert the time you want to open the link137:", font=("Calibri", 12), fg ='red')
label.pack()
time137= Entry(second_frame)
time137.pack()
label=Label(second_frame, text= "Insert the link138:", font=("Calibri", 12), fg ='blue')
label.pack()
link138= Entry(second_frame, width=100)
link138.pack()
label=Label(second_frame, text= "Insert the day you want to open the link138:", font=("Calibri", 12), fg ='orange')
label.pack()
day138= Entry(second_frame)
day138.pack()
label=Label(second_frame, text= "Insert the time you want to open the link138:", font=("Calibri", 12), fg ='red')
label.pack()
time138= Entry(second_frame)
time138.pack()
label=Label(second_frame, text= "Insert the link139:", font=("Calibri", 12), fg ='blue')
label.pack()
link139= Entry(second_frame, width=100)
link139.pack()
label=Label(second_frame, text= "Insert the day you want to open the link139:", font=("Calibri", 12), fg ='orange')
label.pack()
day139= Entry(second_frame)
day139.pack()
label=Label(second_frame, text= "Insert the time you want to open the link139:", font=("Calibri", 12), fg ='red')
label.pack()
time139= Entry(second_frame)
time139.pack()
label=Label(second_frame, text= "Insert the link140:", font=("Calibri", 12), fg ='blue')
label.pack()
link140= Entry(second_frame, width=100)
link140.pack()
label=Label(second_frame, text= "Insert the day you want to open the link140:", font=("Calibri", 12), fg ='orange')
label.pack()
day140= Entry(second_frame)
day140.pack()
label=Label(second_frame, text= "Insert the time you want to open the link140:", font=("Calibri", 12), fg ='red')
label.pack()
time140= Entry(second_frame)
time140.pack()
label=Label(second_frame, text= "Insert the link141:", font=("Calibri", 12), fg ='blue')
label.pack()
link141= Entry(second_frame, width=100)
link141.pack()
label=Label(second_frame, text= "Insert the day you want to open the link141:", font=("Calibri", 12), fg ='orange')
label.pack()
day141= Entry(second_frame)
day141.pack()
label=Label(second_frame, text= "Insert the time you want to open the link141:", font=("Calibri", 12), fg ='red')
label.pack()
time141= Entry(second_frame)
time141.pack()
label=Label(second_frame, text= "Insert the link142:", font=("Calibri", 12), fg ='blue')
label.pack()
link142= Entry(second_frame, width=100)
link142.pack()
label=Label(second_frame, text= "Insert the day you want to open the link142:", font=("Calibri", 12), fg ='orange')
label.pack()
day142= Entry(second_frame)
day142.pack()
label=Label(second_frame, text= "Insert the time you want to open the link142:", font=("Calibri", 12), fg ='red')
label.pack()
time142= Entry(second_frame)
time142.pack()
label=Label(second_frame, text= "Insert the link143:", font=("Calibri", 12), fg ='blue')
label.pack()
link143= Entry(second_frame, width=100)
link143.pack()
label=Label(second_frame, text= "Insert the day you want to open the link143:", font=("Calibri", 12), fg ='orange')
label.pack()
day143= Entry(second_frame)
day143.pack()
label=Label(second_frame, text= "Insert the time you want to open the link143:", font=("Calibri", 12), fg ='red')
label.pack()
time143= Entry(second_frame)
time143.pack()
label=Label(second_frame, text= "Insert the link144:", font=("Calibri", 12), fg ='blue')
label.pack()
link144= Entry(second_frame, width=100)
link144.pack()
label=Label(second_frame, text= "Insert the day you want to open the link144:", font=("Calibri", 12), fg ='orange')
label.pack()
day144= Entry(second_frame)
day144.pack()
label=Label(second_frame, text= "Insert the time you want to open the link144:", font=("Calibri", 12), fg ='red')
label.pack()
time144= Entry(second_frame)
time144.pack()
label=Label(second_frame, text= "Insert the link145:", font=("Calibri", 12), fg ='blue')
label.pack()
link145= Entry(second_frame, width=100)
link145.pack()
label=Label(second_frame, text= "Insert the day you want to open the link145:", font=("Calibri", 12), fg ='orange')
label.pack()
day145= Entry(second_frame)
day145.pack()
label=Label(second_frame, text= "Insert the time you want to open the link145:", font=("Calibri", 12), fg ='red')
label.pack()
time145= Entry(second_frame)
time145.pack()
label=Label(second_frame, text= "Insert the link146:", font=("Calibri", 12), fg ='blue')
label.pack()
link146= Entry(second_frame, width=100)
link146.pack()
label=Label(second_frame, text= "Insert the day you want to open the link146:", font=("Calibri", 12), fg ='orange')
label.pack()
day146= Entry(second_frame)
day146.pack()
label=Label(second_frame, text= "Insert the time you want to open the link146:", font=("Calibri", 12), fg ='red')
label.pack()
time146= Entry(second_frame)
time146.pack()
label=Label(second_frame, text= "Insert the link147:", font=("Calibri", 12), fg ='blue')
label.pack()
link147= Entry(second_frame, width=100)
link147.pack()
label=Label(second_frame, text= "Insert the day you want to open the link147:", font=("Calibri", 12), fg ='orange')
label.pack()
day147= Entry(second_frame)
day147.pack()
label=Label(second_frame, text= "Insert the time you want to open the link147:", font=("Calibri", 12), fg ='red')
label.pack()
time147= Entry(second_frame)
time147.pack()
label=Label(second_frame, text= "Insert the link148:", font=("Calibri", 12), fg ='blue')
label.pack()
link148= Entry(second_frame, width=100)
link148.pack()
label=Label(second_frame, text= "Insert the day you want to open the link148:", font=("Calibri", 12), fg ='orange')
label.pack()
day148= Entry(second_frame)
day148.pack()
label=Label(second_frame, text= "Insert the time you want to open the link148:", font=("Calibri", 12), fg ='red')
label.pack()
time148= Entry(second_frame)
time148.pack()
label=Label(second_frame, text= "Insert the link149:", font=("Calibri", 12), fg ='blue')
label.pack()
link149= Entry(second_frame, width=100)
link149.pack()
label=Label(second_frame, text= "Insert the day you want to open the link149:", font=("Calibri", 12), fg ='orange')
label.pack()
day149= Entry(second_frame)
day149.pack()
label=Label(second_frame, text= "Insert the time you want to open the link149:", font=("Calibri", 12), fg ='red')
label.pack()
time149= Entry(second_frame)
time149.pack()
label=Label(second_frame, text= "Insert the link150:", font=("Calibri", 12), fg ='blue')
label.pack()
link150= Entry(second_frame, width=100)
link150.pack()
label=Label(second_frame, text= "Insert the day you want to open the link150:", font=("Calibri", 12), fg ='orange')
label.pack()
day150= Entry(second_frame)
day150.pack()
label=Label(second_frame, text= "Insert the time you want to open the link150:", font=("Calibri", 12), fg ='red')
label.pack()
time150= Entry(second_frame)
time150.pack()
label=Label(second_frame, text= "Insert the link151:", font=("Calibri", 12), fg ='blue')
label.pack()
link151= Entry(second_frame, width=100)
link151.pack()
label=Label(second_frame, text= "Insert the day you want to open the link151:", font=("Calibri", 12), fg ='orange')
label.pack()
day151= Entry(second_frame)
day151.pack()
label=Label(second_frame, text= "Insert the time you want to open the link151:", font=("Calibri", 12), fg ='red')
label.pack()
time151= Entry(second_frame)
time151.pack()
label=Label(second_frame, text= "Insert the link152:", font=("Calibri", 12), fg ='blue')
label.pack()
link152= Entry(second_frame, width=100)
link152.pack()
label=Label(second_frame, text= "Insert the day you want to open the link152:", font=("Calibri", 12), fg ='orange')
label.pack()
day152= Entry(second_frame)
day152.pack()
label=Label(second_frame, text= "Insert the time you want to open the link152:", font=("Calibri", 12), fg ='red')
label.pack()
time152= Entry(second_frame)
time152.pack()
label=Label(second_frame, text= "Insert the link153:", font=("Calibri", 12), fg ='blue')
label.pack()
link153= Entry(second_frame, width=100)
link153.pack()
label=Label(second_frame, text= "Insert the day you want to open the link153:", font=("Calibri", 12), fg ='orange')
label.pack()
day153= Entry(second_frame)
day153.pack()
label=Label(second_frame, text= "Insert the time you want to open the link153:", font=("Calibri", 12), fg ='red')
label.pack()
time153= Entry(second_frame)
time153.pack()
label=Label(second_frame, text= "Insert the link154:", font=("Calibri", 12), fg ='blue')
label.pack()
link154= Entry(second_frame, width=100)
link154.pack()
label=Label(second_frame, text= "Insert the day you want to open the link154:", font=("Calibri", 12), fg ='orange')
label.pack()
day154= Entry(second_frame)
day154.pack()
label=Label(second_frame, text= "Insert the time you want to open the link154:", font=("Calibri", 12), fg ='red')
label.pack()
time154= Entry(second_frame)
time154.pack()
label=Label(second_frame, text= "Insert the link155:", font=("Calibri", 12), fg ='blue')
label.pack()
link155= Entry(second_frame, width=100)
link155.pack()
label=Label(second_frame, text= "Insert the day you want to open the link155:", font=("Calibri", 12), fg ='orange')
label.pack()
day155= Entry(second_frame)
day155.pack()
label=Label(second_frame, text= "Insert the time you want to open the link155:", font=("Calibri", 12), fg ='red')
label.pack()
time155= Entry(second_frame)
time155.pack()
label=Label(second_frame, text= "Insert the link156:", font=("Calibri", 12), fg ='blue')
label.pack()
link156= Entry(second_frame, width=100)
link156.pack()
label=Label(second_frame, text= "Insert the day you want to open the link156:", font=("Calibri", 12), fg ='orange')
label.pack()
day156= Entry(second_frame)
day156.pack()
label=Label(second_frame, text= "Insert the time you want to open the link156:", font=("Calibri", 12), fg ='red')
label.pack()
time156= Entry(second_frame)
time156.pack()
label=Label(second_frame, text= "Insert the link157:", font=("Calibri", 12), fg ='blue')
label.pack()
link157= Entry(second_frame, width=100)
link157.pack()
label=Label(second_frame, text= "Insert the day you want to open the link157:", font=("Calibri", 12), fg ='orange')
label.pack()
day157= Entry(second_frame)
day157.pack()
label=Label(second_frame, text= "Insert the time you want to open the link157:", font=("Calibri", 12), fg ='red')
label.pack()
time157= Entry(second_frame)
time157.pack()
label=Label(second_frame, text= "Insert the link158:", font=("Calibri", 12), fg ='blue')
label.pack()
link158= Entry(second_frame, width=100)
link158.pack()
label=Label(second_frame, text= "Insert the day you want to open the link158:", font=("Calibri", 12), fg ='orange')
label.pack()
day158= Entry(second_frame)
day158.pack()
label=Label(second_frame, text= "Insert the time you want to open the link158:", font=("Calibri", 12), fg ='red')
label.pack()
time158= Entry(second_frame)
time158.pack()
label=Label(second_frame, text= "Insert the link159:", font=("Calibri", 12), fg ='blue')
label.pack()
link159= Entry(second_frame, width=100)
link159.pack()
label=Label(second_frame, text= "Insert the day you want to open the link159:", font=("Calibri", 12), fg ='orange')
label.pack()
day159= Entry(second_frame)
day159.pack()
label=Label(second_frame, text= "Insert the time you want to open the link159:", font=("Calibri", 12), fg ='red')
label.pack()
time159= Entry(second_frame)
time159.pack()
label=Label(second_frame, text= "Insert the link160:", font=("Calibri", 12), fg ='blue')
label.pack()
link160= Entry(second_frame, width=100)
link160.pack()
label=Label(second_frame, text= "Insert the day you want to open the link160:", font=("Calibri", 12), fg ='orange')
label.pack()
day160= Entry(second_frame)
day160.pack()
label=Label(second_frame, text= "Insert the time you want to open the link160:", font=("Calibri", 12), fg ='red')
label.pack()
time160= Entry(second_frame)
time160.pack()
label=Label(second_frame, text= "Insert the link161:", font=("Calibri", 12), fg ='blue')
label.pack()
link161= Entry(second_frame, width=100)
link61.pack()
label=Label(second_frame, text= "Insert the day you want to open the link161:", font=("Calibri", 12), fg ='orange')
label.pack()
day161= Entry(second_frame)
day161.pack()
label=Label(second_frame, text= "Insert the time you want to open the link161:", font=("Calibri", 12), fg ='red')
label.pack()
time161= Entry(second_frame)
time161.pack()
label=Label(second_frame, text= "Insert the link162:", font=("Calibri", 12), fg ='blue')
label.pack()
link162= Entry(second_frame, width=100)
link162.pack()
label=Label(second_frame, text= "Insert the day you want to open the link162:", font=("Calibri", 12), fg ='orange')
label.pack()
day162= Entry(second_frame)
day162.pack()
label=Label(second_frame, text= "Insert the time you want to open the link162:", font=("Calibri", 12), fg ='red')
label.pack()
time162= Entry(second_frame)
time162.pack()
label=Label(second_frame, text= "Insert the link163:", font=("Calibri", 12), fg ='blue')
label.pack()
link163= Entry(second_frame, width=100)
link63.pack()
label=Label(second_frame, text= "Insert the day you want to open the link163:", font=("Calibri", 12), fg ='orange')
label.pack()
day163= Entry(second_frame)
day163.pack()
label=Label(second_frame, text= "Insert the time you want to open the link163:", font=("Calibri", 12), fg ='red')
label.pack()
time163= Entry(second_frame)
time163.pack()
label=Label(second_frame, text= "Insert the link164:", font=("Calibri", 12), fg ='blue')
label.pack()
link164= Entry(second_frame, width=100)
link164.pack()
label=Label(second_frame, text= "Insert the day you want to open the link164:", font=("Calibri", 12), fg ='orange')
label.pack()
day164= Entry(second_frame)
day164.pack()
label=Label(second_frame, text= "Insert the time you want to open the link164:", font=("Calibri", 12), fg ='red')
label.pack()
time164= Entry(second_frame)
time164.pack()
label=Label(second_frame, text= "Insert the link165:", font=("Calibri", 12), fg ='blue')
label.pack()
link165= Entry(second_frame, width=100)
link165.pack()
label=Label(second_frame, text= "Insert the day you want to open the link165:", font=("Calibri", 12), fg ='orange')
label.pack()
day165= Entry(second_frame)
day165.pack()
label=Label(second_frame, text= "Insert the time you want to open the link165:", font=("Calibri", 12), fg ='red')
label.pack()
time165= Entry(second_frame)
time165.pack()
label=Label(second_frame, text= "Insert the link166:", font=("Calibri", 12), fg ='blue')
label.pack()
link166= Entry(second_frame, width=100)
link166.pack()
label=Label(second_frame, text= "Insert the day you want to open the link166:", font=("Calibri", 12), fg ='orange')
label.pack()
day166= Entry(second_frame)
day166.pack()
label=Label(second_frame, text= "Insert the time you want to open the link166:", font=("Calibri", 12), fg ='red')
label.pack()
time166= Entry(second_frame)
time166.pack()
label=Label(second_frame, text= "Insert the link167:", font=("Calibri", 12), fg ='blue')
label.pack()
link167= Entry(second_frame, width=100)
link167.pack()
label=Label(second_frame, text= "Insert the day you want to open the link167:", font=("Calibri", 12), fg ='orange')
label.pack()
day167= Entry(second_frame)
day167.pack()
label=Label(second_frame, text= "Insert the time you want to open the link167:", font=("Calibri", 12), fg ='red')
label.pack()
time167= Entry(second_frame)
time167.pack()
label=Label(second_frame, text= "Insert the link168:", font=("Calibri", 12), fg ='blue')
label.pack()
link168= Entry(second_frame, width=100)
link168.pack()
label=Label(second_frame, text= "Insert the day you want to open the link168:", font=("Calibri", 12), fg ='orange')
label.pack()
day168= Entry(second_frame)
day168.pack()
label=Label(second_frame, text= "Insert the time you want to open the link168:", font=("Calibri", 12), fg ='red')
label.pack()
time168= Entry(second_frame)
time168.pack()
label=Label(second_frame, text= "Insert the link169:", font=("Calibri", 12), fg ='blue')
label.pack()
link169= Entry(second_frame, width=100)
link169.pack()
label=Label(second_frame, text= "Insert the day you want to open the link169:", font=("Calibri", 12), fg ='orange')
label.pack()
day169= Entry(second_frame)
day169.pack()
label=Label(second_frame, text= "Insert the time you want to open the link169:", font=("Calibri", 12), fg ='red')
label.pack()
time169= Entry(second_frame)
time169.pack()
label=Label(second_frame, text= "Insert the link170:", font=("Calibri", 12), fg ='blue')
label.pack()
link170= Entry(second_frame, width=100)
link170.pack()
label=Label(second_frame, text= "Insert the day you want to open the link170:", font=("Calibri", 12), fg ='orange')
label.pack()
day170= Entry(second_frame)
day170.pack()
label=Label(second_frame, text= "Insert the time you want to open the link170:", font=("Calibri", 12), fg ='red')
label.pack()
time170= Entry(second_frame)
time170.pack()
label=Label(second_frame, text= "Insert the link171:", font=("Calibri", 12), fg ='blue')
label.pack()
link171= Entry(second_frame, width=100)
link171.pack()
label=Label(second_frame, text= "Insert the day you want to open the link171:", font=("Calibri", 12), fg ='orange')
label.pack()
day171= Entry(second_frame)
day171.pack()
label=Label(second_frame, text= "Insert the time you want to open the link171:", font=("Calibri", 12), fg ='red')
label.pack()
time171= Entry(second_frame)
time171.pack()
label=Label(second_frame, text= "Insert the link172:", font=("Calibri", 12), fg ='blue')
label.pack()
link172= Entry(second_frame, width=100)
link172.pack()
label=Label(second_frame, text= "Insert the day you want to open the link172:", font=("Calibri", 12), fg ='orange')
label.pack()
day172= Entry(second_frame)
day172.pack()
label=Label(second_frame, text= "Insert the time you want to open the link172:", font=("Calibri", 12), fg ='red')
label.pack()
time172= Entry(second_frame)
time172.pack()
label=Label(second_frame, text= "Insert the link173:", font=("Calibri", 12), fg ='blue')
label.pack()
link173= Entry(second_frame, width=100)
link173.pack()
label=Label(second_frame, text= "Insert the day you want to open the link173:", font=("Calibri", 12), fg ='orange')
label.pack()
day173= Entry(second_frame)
day173.pack()
label=Label(second_frame, text= "Insert the time you want to open the link173:", font=("Calibri", 12), fg ='red')
label.pack()
time173= Entry(second_frame)
time173.pack()
label=Label(second_frame, text= "Insert the link174:", font=("Calibri", 12), fg ='blue')
label.pack()
link174= Entry(second_frame, width=100)
link174.pack()
label=Label(second_frame, text= "Insert the day you want to open the link174:", font=("Calibri", 12), fg ='orange')
label.pack()
day174= Entry(second_frame)
day174.pack()
label=Label(second_frame, text= "Insert the time you want to open the link174:", font=("Calibri", 12), fg ='red')
label.pack()
time174= Entry(second_frame)
time174.pack()
label=Label(second_frame, text= "Insert the link175:", font=("Calibri", 12), fg ='blue')
label.pack()
link175= Entry(second_frame, width=100)
link175.pack()
label=Label(second_frame, text= "Insert the day you want to open the link175:", font=("Calibri", 12), fg ='orange')
label.pack()
day175= Entry(second_frame)
day175.pack()
label=Label(second_frame, text= "Insert the time you want to open the link175:", font=("Calibri", 12), fg ='red')
label.pack()
time175= Entry(second_frame)
time175.pack()
label=Label(second_frame, text= "Insert the link176:", font=("Calibri", 12), fg ='blue')
label.pack()
link176= Entry(second_frame, width=100)
link176.pack()
label=Label(second_frame, text= "Insert the day you want to open the link176:", font=("Calibri", 12), fg ='orange')
label.pack()
day176= Entry(second_frame)
day176.pack()
label=Label(second_frame, text= "Insert the time you want to open the link176:", font=("Calibri", 12), fg ='red')
label.pack()
time176= Entry(second_frame)
time176.pack()
label=Label(second_frame, text= "Insert the link177:", font=("Calibri", 12), fg ='blue')
label.pack()
link177= Entry(second_frame, width=100)
link177.pack()
label=Label(second_frame, text= "Insert the day you want to open the link177:", font=("Calibri", 12), fg ='orange')
label.pack()
day177= Entry(second_frame)
day177.pack()
label=Label(second_frame, text= "Insert the time you want to open the link177:", font=("Calibri", 12), fg ='red')
label.pack()
time177= Entry(second_frame)
time177.pack()
label=Label(second_frame, text= "Insert the link178:", font=("Calibri", 12), fg ='blue')
label.pack()
link178= Entry(second_frame, width=100)
link178.pack()
label=Label(second_frame, text= "Insert the day you want to open the link178:", font=("Calibri", 12), fg ='orange')
label.pack()
day178= Entry(second_frame)
day178.pack()
label=Label(second_frame, text= "Insert the time you want to open the link178:", font=("Calibri", 12), fg ='red')
label.pack()
time178= Entry(second_frame)
time178.pack()
label=Label(second_frame, text= "Insert the link179:", font=("Calibri", 12), fg ='blue')
label.pack()
link179= Entry(second_frame, width=100)
link179.pack()
label=Label(second_frame, text= "Insert the day you want to open the link179:", font=("Calibri", 12), fg ='orange')
label.pack()
day179= Entry(second_frame)
day179.pack()
label=Label(second_frame, text= "Insert the time you want to open the link179:", font=("Calibri", 12), fg ='red')
label.pack()
time179= Entry(second_frame)
time179.pack()
label=Label(second_frame, text= "Insert the link180:", font=("Calibri", 12), fg ='blue')
label.pack()
link180= Entry(second_frame, width=100)
link180.pack()
label=Label(second_frame, text= "Insert the day you want to open the link180:", font=("Calibri", 12), fg ='orange')
label.pack()
day180= Entry(second_frame)
day180.pack()
label=Label(second_frame, text= "Insert the time you want to open the link180:", font=("Calibri", 12), fg ='red')
label.pack()
time180= Entry(second_frame)
time180.pack()
label=Label(second_frame, text= "Insert the link181:", font=("Calibri", 12), fg ='blue')
label.pack()
link181= Entry(second_frame, width=100)
link181.pack()
label=Label(second_frame, text= "Insert the day you want to open the link181:", font=("Calibri", 12), fg ='orange')
label.pack()
day181= Entry(second_frame)
day181.pack()
label=Label(second_frame, text= "Insert the time you want to open the link181:", font=("Calibri", 12), fg ='red')
label.pack()
time181= Entry(second_frame)
time181.pack()
label=Label(second_frame, text= "Insert the link182:", font=("Calibri", 12), fg ='blue')
label.pack()
link182= Entry(second_frame, width=100)
link182.pack()
label=Label(second_frame, text= "Insert the day you want to open the link182:", font=("Calibri", 12), fg ='orange')
label.pack()
day182= Entry(second_frame)
day182.pack()
label=Label(second_frame, text= "Insert the time you want to open the link182:", font=("Calibri", 12), fg ='red')
label.pack()
time182= Entry(second_frame)
time182.pack()
label=Label(second_frame, text= "Insert the link183:", font=("Calibri", 12), fg ='blue')
label.pack()
link183= Entry(second_frame, width=100)
link183.pack()
label=Label(second_frame, text= "Insert the day you want to open the link183:", font=("Calibri", 12), fg ='orange')
label.pack()
day183= Entry(second_frame)
day183.pack()
label=Label(second_frame, text= "Insert the time you want to open the link183:", font=("Calibri", 12), fg ='red')
label.pack()
time183= Entry(second_frame)
time183.pack()
label=Label(second_frame, text= "Insert the link184:", font=("Calibri", 12), fg ='blue')
label.pack()
link184= Entry(second_frame, width=100)
link184.pack()
label=Label(second_frame, text= "Insert the day you want to open the link184:", font=("Calibri", 12), fg ='orange')
label.pack()
day184= Entry(second_frame)
day184.pack()
label=Label(second_frame, text= "Insert the time you want to open the link184:", font=("Calibri", 12), fg ='red')
label.pack()
time184= Entry(second_frame)
time184.pack()
label=Label(second_frame, text= "Insert the link185:", font=("Calibri", 12), fg ='blue')
label.pack()
link185= Entry(second_frame, width=100)
link185.pack()
label=Label(second_frame, text= "Insert the day you want to open the link185:", font=("Calibri", 12), fg ='orange')
label.pack()
day185= Entry(second_frame)
day185.pack()
label=Label(second_frame, text= "Insert the time you want to open the link185:", font=("Calibri", 12), fg ='red')
label.pack()
time185= Entry(second_frame)
time185.pack()
label=Label(second_frame, text= "Insert the link186:", font=("Calibri", 12), fg ='blue')
label.pack()
link186= Entry(second_frame, width=100)
link186.pack()
label=Label(second_frame, text= "Insert the day you want to open the link186:", font=("Calibri", 12), fg ='orange')
label.pack()
day186= Entry(second_frame)
day186.pack()
label=Label(second_frame, text= "Insert the time you want to open the link186:", font=("Calibri", 12), fg ='red')
label.pack()
time186= Entry(second_frame)
time186.pack()
label=Label(second_frame, text= "Insert the link187:", font=("Calibri", 12), fg ='blue')
label.pack()
link187= Entry(second_frame, width=100)
link187.pack()
label=Label(second_frame, text= "Insert the day you want to open the link187:", font=("Calibri", 12), fg ='orange')
label.pack()
day187= Entry(second_frame)
day187.pack()
label=Label(second_frame, text= "Insert the time you want to open the link187:", font=("Calibri", 12), fg ='red')
label.pack()
time187= Entry(second_frame)
time187.pack()
label=Label(second_frame, text= "Insert the link188:", font=("Calibri", 12), fg ='blue')
label.pack()
link188= Entry(second_frame, width=100)
link188.pack()
label=Label(second_frame, text= "Insert the day you want to open the link188:", font=("Calibri", 12), fg ='orange')
label.pack()
day188= Entry(second_frame)
day188.pack()
label=Label(second_frame, text= "Insert the time you want to open the link188:", font=("Calibri", 12), fg ='red')
label.pack()
time188= Entry(second_frame)
time188.pack()
label=Label(second_frame, text= "Insert the link189:", font=("Calibri", 12), fg ='blue')
label.pack()
link189= Entry(second_frame, width=100)
link189.pack()
label=Label(second_frame, text= "Insert the day you want to open the link189:", font=("Calibri", 12), fg ='orange')
label.pack()
day189= Entry(second_frame)
day189.pack()
label=Label(second_frame, text= "Insert the time you want to open the link189:", font=("Calibri", 12), fg ='red')
label.pack()
time189= Entry(second_frame)
time189.pack()
label=Label(second_frame, text= "Insert the link190:", font=("Calibri", 12), fg ='blue')
label.pack()
link190= Entry(second_frame, width=100)
link190.pack()
label=Label(second_frame, text= "Insert the day you want to open the link190:", font=("Calibri", 12), fg ='orange')
label.pack()
day190= Entry(second_frame)
day190.pack()
label=Label(second_frame, text= "Insert the time you want to open the link190:", font=("Calibri", 12), fg ='red')
label.pack()
time190= Entry(second_frame)
time190.pack()
label=Label(second_frame, text= "Insert the link191:", font=("Calibri", 12), fg ='blue')
label.pack()
link191= Entry(second_frame, width=100)
link191.pack()
label=Label(second_frame, text= "Insert the day you want to open the link191:", font=("Calibri", 12), fg ='orange')
label.pack()
day191= Entry(second_frame)
day191.pack()
label=Label(second_frame, text= "Insert the time you want to open the link191:", font=("Calibri", 12), fg ='red')
label.pack()
time191= Entry(second_frame)
time191.pack()
label=Label(second_frame, text= "Insert the link192:", font=("Calibri", 12), fg ='blue')
label.pack()
link192= Entry(second_frame, width=100)
link192.pack()
label=Label(second_frame, text= "Insert the day you want to open the link192:", font=("Calibri", 12), fg ='orange')
label.pack()
day192= Entry(second_frame)
day192.pack()
label=Label(second_frame, text= "Insert the time you want to open the link192:", font=("Calibri", 12), fg ='red')
label.pack()
time192= Entry(second_frame)
time192.pack()
label=Label(second_frame, text= "Insert the link193:", font=("Calibri", 12), fg ='blue')
label.pack()
link193= Entry(second_frame, width=100)
link193.pack()
label=Label(second_frame, text= "Insert the day you want to open the link193:", font=("Calibri", 12), fg ='orange')
label.pack()
day193= Entry(second_frame)
day193.pack()
label=Label(second_frame, text= "Insert the time you want to open the link193:", font=("Calibri", 12), fg ='red')
label.pack()
time193= Entry(second_frame)
time193.pack()
label=Label(second_frame, text= "Insert the link194:", font=("Calibri", 12), fg ='blue')
label.pack()
link194= Entry(second_frame, width=100)
link194.pack()
label=Label(second_frame, text= "Insert the day you want to open the link194:", font=("Calibri", 12), fg ='orange')
label.pack()
day194= Entry(second_frame)
day194.pack()
label=Label(second_frame, text= "Insert the time you want to open the link194:", font=("Calibri", 12), fg ='red')
label.pack()
time194= Entry(second_frame)
time194.pack()
label=Label(second_frame, text= "Insert the link195:", font=("Calibri", 12), fg ='blue')
label.pack()
link195= Entry(second_frame, width=100)
link195.pack()
label=Label(second_frame, text= "Insert the day you want to open the link195:", font=("Calibri", 12), fg ='orange')
label.pack()
day195= Entry(second_frame)
day195.pack()
label=Label(second_frame, text= "Insert the time you want to open the link195:", font=("Calibri", 12), fg ='red')
label.pack()
time195= Entry(second_frame)
time195.pack()
label=Label(second_frame, text= "Insert the link196:", font=("Calibri", 12), fg ='blue')
label.pack()
link196= Entry(second_frame, width=100)
link196.pack()
label=Label(second_frame, text= "Insert the day you want to open the link196:", font=("Calibri", 12), fg ='orange')
label.pack()
day196= Entry(second_frame)
day196.pack()
label=Label(second_frame, text= "Insert the time you want to open the link196:", font=("Calibri", 12), fg ='red')
label.pack()
time196= Entry(second_frame)
time196.pack()
label=Label(second_frame, text= "Insert the link197:", font=("Calibri", 12), fg ='blue')
label.pack()
link197= Entry(second_frame, width=100)
link197.pack()
label=Label(second_frame, text= "Insert the day you want to open the link197:", font=("Calibri", 12), fg ='orange')
label.pack()
day197= Entry(second_frame)
day197.pack()
label=Label(second_frame, text= "Insert the time you want to open the link197:", font=("Calibri", 12), fg ='red')
label.pack()
time197= Entry(second_frame)
time197.pack()
label=Label(second_frame, text= "Insert the link198:", font=("Calibri", 12), fg ='blue')
label.pack()
link198= Entry(second_frame, width=100)
link198.pack()
label=Label(second_frame, text= "Insert the day you want to open the link198:", font=("Calibri", 12), fg ='orange')
label.pack()
day198= Entry(second_frame)
day198.pack()
label=Label(second_frame, text= "Insert the time you want to open the link198:", font=("Calibri", 12), fg ='red')
label.pack()
time198= Entry(second_frame)
time198.pack()
label=Label(second_frame, text= "Insert the link199:", font=("Calibri", 12), fg ='blue')
label.pack()
link199= Entry(second_frame, width=100)
link199.pack()
label=Label(second_frame, text= "Insert the day you want to open the link199:", font=("Calibri", 12), fg ='orange')
label.pack()
day199= Entry(second_frame)
day199.pack()
label=Label(second_frame, text= "Insert the time you want to open the link199:", font=("Calibri", 12), fg ='red')
label.pack()
time199= Entry(second_frame)
time199.pack()
label=Label(second_frame, text= "Insert the link200:", font=("Calibri", 12), fg ='blue')
label.pack()
link200= Entry(second_frame, width=100)
link200.pack()
label=Label(second_frame, text= "Insert the day you want to open the link200:", font=("Calibri", 12), fg ='orange')
label.pack()
day200= Entry(second_frame)
day200.pack()
label=Label(second_frame, text= "Insert the time you want to open the link200:", font=("Calibri", 12), fg ='red')
label.pack()
time200= Entry(second_frame)
time200.pack()




def job1():
     webbrowser.open (link1.get())
     
def job2():
     webbrowser.open (link2.get())
     
def job3():
     webbrowser.open (link3.get())     

def job4():
     webbrowser.open (link4.get())
     
def job5():
     webbrowser.open (link5.get())

def job6():
     webbrowser.open (link6.get())

def job7():
     webbrowser.open (link7.get())

def job8():
     webbrowser.open (link8.get())
     
def job9():
     webbrowser.open (link9.get())

def job10():
     webbrowser.open (link10.get())

def job11():
     webbrowser.open (link11.get())
     
def job12():
     webbrowser.open (link12.get())
     
def job13():
     webbrowser.open (link13.get())     

def job14():
     webbrowser.open (link14.get())
     
def job15():
     webbrowser.open (link15.get())

def job16():
     webbrowser.open (link16.get())

def job17():
     webbrowser.open (link17.get())

def job18():
     webbrowser.open (link18.get())
     
def job19():
     webbrowser.open (link19.get())

def job20():
     webbrowser.open (link20.get())

def job21():
     webbrowser.open (link21.get())
     
def job22():
     webbrowser.open (link22.get())
     
def job23():
     webbrowser.open (link23.get())     

def job24():
     webbrowser.open (link24.get())
     
def job25():
     webbrowser.open (link25.get())

def job26():
     webbrowser.open (link26.get())

def job27():
     webbrowser.open (link27.get())

def job28():
     webbrowser.open (link28.get())
     
def job29():
     webbrowser.open (link29.get())

def job30():
     webbrowser.open (link30.get())

def job31():
     webbrowser.open (link31.get())
     
def job32():
     webbrowser.open (link32.get())
     
def job33():
     webbrowser.open (link33.get())     

def job34():
     webbrowser.open (link34.get())
     
def job35():
     webbrowser.open (link35.get())

def job36():
     webbrowser.open (link36.get())

def job37():
     webbrowser.open (link37.get())

def job38():
     webbrowser.open (link38.get())
     
def job39():
     webbrowser.open (link39.get())

def job40():
     webbrowser.open (link40.get())

def job41():
     webbrowser.open (link41.get())
     
def job42():
     webbrowser.open (link42.get())
     
def job43():
     webbrowser.open (link43.get())     

def job44():
     webbrowser.open (link44.get())
     
def job45():
     webbrowser.open (link45.get())

def job46():
     webbrowser.open (link46.get())

def job47():
     webbrowser.open (link47.get())

def job48():
     webbrowser.open (link48.get())
     
def job49():
     webbrowser.open (link49.get())

def job50():
     webbrowser.open (link50.get())

def job51():
     webbrowser.open (link51.get())
     
def job52():
     webbrowser.open (link52.get())
     
def job53():
     webbrowser.open (link53.get())     

def job54():
     webbrowser.open (link54.get())
     
def job55():
     webbrowser.open (link55.get())

def job56():
     webbrowser.open (link56.get())

def job57():
     webbrowser.open (link57.get())

def job58():
     webbrowser.open (link58.get())
     
def job59():
     webbrowser.open (link59.get())

def job60():
     webbrowser.open (link60.get())

def job61():
     webbrowser.open (link61.get())
     
def job62():
     webbrowser.open (link62.get())
     
def job63():
     webbrowser.open (link63.get())     

def job64():
     webbrowser.open (link64.get())
     
def job65():
     webbrowser.open (link65.get())

def job66():
     webbrowser.open (link66.get())

def job67():
     webbrowser.open (link67.get())

def job68():
     webbrowser.open (link68.get())
     
def job69():
     webbrowser.open (link69.get())

def job70():
     webbrowser.open (link70.get())

def job71():
     webbrowser.open (link71.get())
     
def job72():
     webbrowser.open (link72.get())
     
def job73():
     webbrowser.open (link73.get())     

def job74():
     webbrowser.open (link74.get())
     
def job75():
     webbrowser.open (link75.get())

def job76():
     webbrowser.open (link76.get())

def job77():
     webbrowser.open (link77.get())

def job78():
     webbrowser.open (link78.get())
     
def job79():
     webbrowser.open (link79.get())

def job80():
     webbrowser.open (link80.get())

def job81():
     webbrowser.open (link81.get())
     
def job82():
     webbrowser.open (link82.get())
     
def job83():
     webbrowser.open (link83.get())     

def job84():
     webbrowser.open (link84.get())
     
def job85():
     webbrowser.open (link85.get())

def job86():
     webbrowser.open (link86.get())

def job87():
     webbrowser.open (link87.get())

def job88():
     webbrowser.open (link88.get())
     
def job89():
     webbrowser.open (link89.get())

def job90():
     webbrowser.open (link90.get())

def job91():
     webbrowser.open (link91.get())
     
def job92():
     webbrowser.open (link92.get())
     
def job93():
     webbrowser.open (link93.get())     

def job94():
     webbrowser.open (link94.get())
     
def job95():
     webbrowser.open (link95.get())

def job96():
     webbrowser.open (link96.get())

def job97():
     webbrowser.open (link97.get())

def job98():
     webbrowser.open (link98.get())
     
def job99():
     webbrowser.open (link99.get())

def job100():
     webbrowser.open (link100.get())

def job101():
     webbrowser.open (link101.get())
     
def job102():
     webbrowser.open (link102.get())
     
def job103():
     webbrowser.open (link103.get())     

def job104():
     webbrowser.open (link104.get())
     
def job105():
     webbrowser.open (link105.get())

def job106():
     webbrowser.open (link106.get())

def job107():
     webbrowser.open (link107.get())

def job108():
     webbrowser.open (link108.get())
     
def job109():
     webbrowser.open (link109.get())

def job110():
     webbrowser.open (link110.get())

def job111():
     webbrowser.open (link111.get())
     
def job112():
     webbrowser.open (link112.get())
     
def job113():
     webbrowser.open (link113.get())     

def job114():
     webbrowser.open (link114.get())
     
def job115():
     webbrowser.open (link115.get())

def job116():
     webbrowser.open (link116.get())

def job117():
     webbrowser.open (link117.get())

def job118():
     webbrowser.open (link118.get())
     
def job119():
     webbrowser.open (link119.get())

def job120():
     webbrowser.open (link120.get())

def job121():
     webbrowser.open (link121.get())
     
def job122():
     webbrowser.open (link122.get())
     
def job123():
     webbrowser.open (link123.get())     

def job124():
     webbrowser.open (link124.get())
     
def job125():
     webbrowser.open (link125.get())

def job126():
     webbrowser.open (link126.get())

def job127():
     webbrowser.open (link127.get())

def job128():
     webbrowser.open (link128.get())
     
def job129():
     webbrowser.open (link129.get())

def job130():
     webbrowser.open (link130.get())

def job131():
     webbrowser.open (link131.get())
     
def job132():
     webbrowser.open (link132.get())
     
def job133():
     webbrowser.open (link133.get())     

def job134():
     webbrowser.open (link134.get())
     
def job135():
     webbrowser.open (link135.get())

def job136():
     webbrowser.open (link136.get())

def job137():
     webbrowser.open (link137.get())

def job138():
     webbrowser.open (link138.get())
     
def job139():
     webbrowser.open (link139.get())

def job140():
     webbrowser.open (link140.get())

def job141():
     webbrowser.open (link141.get())
     
def job142():
     webbrowser.open (link142.get())
     
def job143():
     webbrowser.open (link143.get())     

def job144():
     webbrowser.open (link144.get())
     
def job145():
     webbrowser.open (link145.get())

def job146():
     webbrowser.open (link146.get())

def job147():
     webbrowser.open (link147.get())

def job148():
     webbrowser.open (link148.get())
     
def job149():
     webbrowser.open (link149.get())

def job150():
     webbrowser.open (link150.get())

def job151():
     webbrowser.open (link151.get())
     
def job152():
     webbrowser.open (link152.get())
     
def job153():
     webbrowser.open (link153.get())     

def job154():
     webbrowser.open (link154.get())
     
def job155():
     webbrowser.open (link155.get())

def job156():
     webbrowser.open (link156.get())

def job157():
     webbrowser.open (link157.get())

def job158():
     webbrowser.open (link158.get())
     
def job159():
     webbrowser.open (link159.get())

def job160():
     webbrowser.open (link160.get())

def job161():
     webbrowser.open (link161.get())
     
def job162():
     webbrowser.open (link162.get())
     
def job163():
     webbrowser.open (link163.get())     

def job164():
     webbrowser.open (link164.get())
     
def job165():
     webbrowser.open (link165.get())

def job166():
     webbrowser.open (link166.get())

def job167():
     webbrowser.open (link167.get())

def job168():
     webbrowser.open (link168.get())
     
def job169():
     webbrowser.open (link169.get())

def job170():
     webbrowser.open (link170.get())

def job171():
     webbrowser.open (link171.get())
     
def job172():
     webbrowser.open (link172.get())
     
def job173():
     webbrowser.open (link173.get())     

def job174():
     webbrowser.open (link174.get())
     
def job175():
     webbrowser.open (link175.get())

def job176():
     webbrowser.open (link176.get())

def job177():
     webbrowser.open (link177.get())

def job178():
     webbrowser.open (link178.get())
     
def job179():
     webbrowser.open (link179.get())

def job180():
     webbrowser.open (link180.get())

def job181():
     webbrowser.open (link181.get())
     
def job182():
     webbrowser.open (link182.get())
     
def job183():
     webbrowser.open (link183.get())     

def job184():
     webbrowser.open (link184.get())
     
def job185():
     webbrowser.open (link185.get())

def job186():
     webbrowser.open (link186.get())

def job187():
     webbrowser.open (link187.get())

def job188():
     webbrowser.open (link188.get())
     
def job189():
     webbrowser.open (link189.get())

def job190():
     webbrowser.open (link190.get())

def job191():
     webbrowser.open (link191.get())
     
def job192():
     webbrowser.open (link192.get())
     
def job193():
     webbrowser.open (link193.get())     

def job194():
     webbrowser.open (link194.get())
     
def job195():
     webbrowser.open (link195.get())

def job196():
     webbrowser.open (link196.get())

def job197():
     webbrowser.open (link197.get())

def job198():
     webbrowser.open (link198.get())
     
def job199():
     webbrowser.open (link199.get())

def job200():
     webbrowser.open (link200.get())

def job409():
     
     if day181.get()=="1":
             schedule.every().monday.at(time181.get()).do(job181)
     elif day181.get()=="2":
             schedule.every().tuesday.at(time181.get()).do(job181)
     elif day181.get()=="3":
             schedule.every().wednesday.at(time181.get()).do(job181)
     elif day181.get()=="4":
             schedule.every().thursday.at(time181.get()).do(job181)
     elif day181.get()=="5":
             schedule.every().friday.at(time181.get()).do(job181)
     elif day181.get()=="6":
             schedule.every().saturday.at(time181.get()).do(job181)
     elif day181.get()=="7":
             schedule.every().sunday.at(time181.get()).do(job181)

     while True:
          schedule.run_pending()
          if day182.get()=="1":
                  schedule.every().monday.at(time182.get()).do(job182)
          elif day182.get()=="2":
                  schedule.every().tuesday.at(time182.get()).do(job182)
          elif day182.get()=="3":
                  schedule.every().wednesday.at(time182.get()).do(job182)
          elif day182.get()=="4":
                  schedule.every().thursday.at(time182.get()).do(job182)
          elif day182.get()=="5":
                  schedule.every().friday.at(time182.get()).do(job182)
          elif day182.get()=="6":
                  schedule.every().saturday.at(time182.get()).do(job182)
          elif day182.get()=="7":
                  schedule.every().sunday.at(time182.get()).do(job182)

          while True:
               schedule.run_pending()        
               if day183.get()=="1":
                       schedule.every().monday.at(time183.get()).do(job183)
               elif day183.get()=="2":
                       schedule.every().tuesday.at(time183.get()).do(job183)
               elif day183.get()=="3":
                       schedule.every().wednesday.at(time183.get()).do(job183)
               elif day183.get()=="4":
                       schedule.every().thursday.at(time183.get()).do(job183)
               elif day183.get()=="5":
                       schedule.every().friday.at(time183.get()).do(job183)
               elif day183.get()=="6":
                       schedule.every().saturday.at(time183.get()).do(job183)
               elif day183.get()=="7":
                       schedule.every().sunday.at(time183.get()).do(job183)

               while True:
                    schedule.run_pending()
                    if day184.get()=="1":
                            schedule.every().monday.at(time184.get()).do(job184)
                    elif day184.get()=="2":
                            schedule.every().tuesday.at(time184.get()).do(job184)
                    elif day184.get()=="3":
                            schedule.every().wednesday.at(time184.get()).do(job184)
                    elif day184.get()=="4":
                            schedule.every().thursday.at(time184.get()).do(job184)
                    elif day184.get()=="5":
                            schedule.every().friday.at(time184.get()).do(job184)
                    elif day184.get()=="6":
                            schedule.every().saturday.at(time184.get()).do(job184)
                    elif day184.get()=="7":
                            schedule.every().sunday.at(time184.get()).do(job184)

                    while True:
                         schedule.run_pending()
                         if day185.get()=="1":
                                 schedule.every().monday.at(time185.get()).do(job185)
                         elif day185.get()=="2":
                                 schedule.every().tuesday.at(time185.get()).do(job185)
                         elif day185.get()=="3":
                                 schedule.every().wednesday.at(time185.get()).do(job185)
                         elif day185.get()=="4":
                                 schedule.every().thursday.at(time185.get()).do(job185)
                         elif day185.get()=="5":
                                 schedule.every().friday.at(time185.get()).do(job185)
                         elif day185.get()=="6":
                                 schedule.every().saturday.at(time185.get()).do(job185)
                         elif day185.get()=="7":
                                 schedule.every().sunday.at(time185.get()).do(job185)

                         while True:
                              schedule.run_pending()
                              if day186.get()=="1":
                                      schedule.every().monday.at(time186.get()).do(job186)
                              elif day186.get()=="2":
                                      schedule.every().tuesday.at(time186.get()).do(job186)
                              elif day186.get()=="3":
                                      schedule.every().wednesday.at(time186.get()).do(job186)
                              elif day186.get()=="4":
                                      schedule.every().thursday.at(time186.get()).do(job186)
                              elif day186.get()=="5":
                                      schedule.every().friday.at(time186.get()).do(job186)
                              elif day186.get()=="6":
                                      schedule.every().saturday.at(time186.get()).do(job186)
                              elif day186.get()=="7":
                                      schedule.every().sunday.at(time186.get()).do(job186)

                              while True:
                                   schedule.run_pending()
                                   if day187.get()=="1":
                                           schedule.every().monday.at(time187.get()).do(job187)
                                   elif day187.get()=="2":
                                           schedule.every().tuesday.at(time187.get()).do(job187)
                                   elif day187.get()=="3":
                                           schedule.every().wednesday.at(time187.get()).do(job187)
                                   elif day187.get()=="4":
                                           schedule.every().thursday.at(time187.get()).do(job187)
                                   elif day187.get()=="5":
                                           schedule.every().friday.at(time187.get()).do(job187)
                                   elif day187.get()=="6":
                                           schedule.every().saturday.at(time187.get()).do(job187)
                                   elif day187.get()=="7":
                                           schedule.every().sunday.at(time187.get()).do(job187)

                                   while True:
                                        schedule.run_pending()
                                        if day188.get()=="1":
                                                schedule.every().monday.at(time188.get()).do(job188)
                                        elif day188.get()=="2":
                                                schedule.every().tuesday.at(time188.get()).do(job188)
                                        elif day188.get()=="3":
                                                schedule.every().wednesday.at(time188.get()).do(job188)
                                        elif day188.get()=="4":
                                                schedule.every().thursday.at(time188.get()).do(job188)
                                        elif day188.get()=="5":
                                                schedule.every().friday.at(time188.get()).do(job188)
                                        elif day188.get()=="6":
                                                schedule.every().saturday.at(time188.get()).do(job188)
                                        elif day188.get()=="7":
                                                schedule.every().sunday.at(time188.get()).do(job188)

                                        while True:
                                             schedule.run_pending()
                                             if day189.get()=="1":
                                                     schedule.every().monday.at(time189.get()).do(job189)
                                             elif day189.get()=="2":
                                                     schedule.every().tuesday.at(time189.get()).do(job189)
                                             elif day189.get()=="3":
                                                     schedule.every().wednesday.at(time189.get()).do(job189)
                                             elif day189.get()=="4":
                                                     schedule.every().thursday.at(time189.get()).do(job189)
                                             elif day189.get()=="5":
                                                     schedule.every().friday.at(time189.get()).do(job189)
                                             elif day189.get()=="6":
                                                     schedule.every().saturday.at(time189.get()).do(job189)
                                             elif day189.get()=="7":
                                                     schedule.every().sunday.at(time189.get()).do(job189)

                                             while True:
                                                  schedule.run_pending()
                                                  if day190.get()=="1":
                                                          schedule.every().monday.at(time190.get()).do(job190)
                                                  elif day190.get()=="2":
                                                          schedule.every().tuesday.at(time190.get()).do(job190)
                                                  elif day190.get()=="3":
                                                          schedule.every().wednesday.at(time190.get()).do(job190)
                                                  elif day190.get()=="4":
                                                          schedule.every().thursday.at(time190.get()).do(job190)
                                                  elif day190.get()=="5":
                                                          schedule.every().friday.at(time190.get()).do(job190)
                                                  elif day190.get()=="6":
                                                          schedule.every().saturday.at(time190.get()).do(job190)
                                                  elif day190.get()=="7":
                                                          schedule.every().sunday.at(time190.get()).do(job190)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day191.get()=="1":
                                                               schedule.every().monday.at(time191.get()).do(job191)
                                                       elif day191.get()=="2":
                                                               schedule.every().tuesday.at(time191.get()).do(job191)
                                                       elif day191.get()=="3":
                                                               schedule.every().wednesday.at(time191.get()).do(job191)
                                                       elif day191.get()=="4":
                                                               schedule.every().thursday.at(time191.get()).do(job191)
                                                       elif day191.get()=="5":
                                                               schedule.every().friday.at(time191.get()).do(job191)
                                                       elif day191.get()=="6":
                                                               schedule.every().saturday.at(time191.get()).do(job191)
                                                       elif day191.get()=="7":
                                                               schedule.every().sunday.at(time191.get()).do(job191)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day192.get()=="1":
                                                                    schedule.every().monday.at(time192.get()).do(job192)
                                                            elif day192.get()=="2":
                                                                    schedule.every().tuesday.at(time192.get()).do(job192)
                                                            elif day192.get()=="3":
                                                                    schedule.every().wednesday.at(time192.get()).do(job192)
                                                            elif day192.get()=="4":
                                                                    schedule.every().thursday.at(time192.get()).do(job192)
                                                            elif day192.get()=="5":
                                                                    schedule.every().friday.at(time192.get()).do(job192)
                                                            elif day192.get()=="6":
                                                                    schedule.every().saturday.at(time192.get()).do(job192)
                                                            elif day192.get()=="7":
                                                                    schedule.every().sunday.at(time192.get()).do(job192)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day193.get()=="1":
                                                                         schedule.every().monday.at(time193.get()).do(job193)
                                                                 elif day193.get()=="2":
                                                                         schedule.every().tuesday.at(time193.get()).do(job193)
                                                                 elif day193.get()=="3":
                                                                         schedule.every().wednesday.at(time193.get()).do(job193)
                                                                 elif day193.get()=="4":
                                                                         schedule.every().thursday.at(time193.get()).do(job193)
                                                                 elif day193.get()=="5":
                                                                         schedule.every().friday.at(time193.get()).do(job193)
                                                                 elif day193.get()=="6":
                                                                         schedule.every().saturday.at(time193.get()).do(job193)
                                                                 elif day193.get()=="7":
                                                                         schedule.every().sunday.at(time193.get()).do(job193)

                                                                 while True:
                                                                      schedule.run_pending()
                                                                      if day194.get()=="1":
                                                                              schedule.every().monday.at(time194.get()).do(job194)
                                                                      elif day194.get()=="2":
                                                                              schedule.every().tuesday.at(time194.get()).do(job194)
                                                                      elif day194.get()=="3":
                                                                              schedule.every().wednesday.at(time194.get()).do(job194)
                                                                      elif day194.get()=="4":
                                                                              schedule.every().thursday.at(time194.get()).do(job194)
                                                                      elif day194.get()=="5":
                                                                              schedule.every().friday.at(time194.get()).do(job194)
                                                                      elif day194.get()=="6":
                                                                              schedule.every().saturday.at(time194.get()).do(job194)
                                                                      elif day194.get()=="7":
                                                                              schedule.every().sunday.at(time194.get()).do(job194)

                                                                      while True:
                                                                           schedule.run_pending()        
                                                                           if day195.get()=="1":
                                                                                   schedule.every().monday.at(time195.get()).do(job195)
                                                                           elif day195.get()=="2":
                                                                                   schedule.every().tuesday.at(time195.get()).do(job195)
                                                                           elif day195.get()=="3":
                                                                                   schedule.every().wednesday.at(time195.get()).do(job195)
                                                                           elif day195.get()=="4":
                                                                                   schedule.every().thursday.at(time195.get()).do(job195)
                                                                           elif day195.get()=="5":
                                                                                   schedule.every().friday.at(time195.get()).do(job195)
                                                                           elif day195.get()=="6":
                                                                                   schedule.every().saturday.at(time195.get()).do(job195)
                                                                           elif day195.get()=="7":
                                                                                   schedule.every().sunday.at(time195.get()).do(job195)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day196.get()=="1":
                                                                                        schedule.every().monday.at(time196.get()).do(job196)
                                                                                elif day196.get()=="2":
                                                                                        schedule.every().tuesday.at(time196.get()).do(job196)
                                                                                elif day196.get()=="3":
                                                                                        schedule.every().wednesday.at(time196.get()).do(job196)
                                                                                elif day196.get()=="4":
                                                                                        schedule.every().thursday.at(time196.get()).do(job196)
                                                                                elif day196.get()=="5":
                                                                                        schedule.every().friday.at(time196.get()).do(job196)
                                                                                elif day196.get()=="6":
                                                                                        schedule.every().saturday.at(time196.get()).do(job196)
                                                                                elif day196.get()=="7":
                                                                                        schedule.every().sunday.at(time196.get()).do(job196)

                                                                                while True:
                                                                                     schedule.run_pending()        
                                                                                     if day197.get()=="1":
                                                                                             schedule.every().monday.at(time197.get()).do(job197)
                                                                                     elif day197.get()=="2":
                                                                                             schedule.every().tuesday.at(time197.get()).do(job197)
                                                                                     elif day197.get()=="3":
                                                                                             schedule.every().wednesday.at(time197.get()).do(job197)
                                                                                     elif day197.get()=="4":
                                                                                             schedule.every().thursday.at(time197.get()).do(job197)
                                                                                     elif day197.get()=="5":
                                                                                             schedule.every().friday.at(time197.get()).do(job197)
                                                                                     elif day197.get()=="6":
                                                                                             schedule.every().saturday.at(time197.get()).do(job197)
                                                                                     elif day197.get()=="7":
                                                                                             schedule.every().sunday.at(time197.get()).do(job197)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day198.get()=="1":
                                                                                                  schedule.every().monday.at(time198.get()).do(job198)
                                                                                          elif day198.get()=="2":
                                                                                                  schedule.every().tuesday.at(time198.get()).do(job198)
                                                                                          elif day198.get()=="3":
                                                                                                  schedule.every().wednesday.at(time198.get()).do(job198)
                                                                                          elif day198.get()=="4":
                                                                                                  schedule.every().thursday.at(time198.get()).do(job198)
                                                                                          elif day198.get()=="5":
                                                                                                  schedule.every().friday.at(time198.get()).do(job198)
                                                                                          elif day198.get()=="6":
                                                                                                  schedule.every().saturday.at(time198.get()).do(job198)
                                                                                          elif day198.get()=="7":
                                                                                                  schedule.every().sunday.at(time198.get()).do(job198)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day199.get()=="1":
                                                                                                       schedule.every().monday.at(time199.get()).do(job199)
                                                                                               elif day199.get()=="2":
                                                                                                       schedule.every().tuesday.at(time199.get()).do(job199)
                                                                                               elif day199.get()=="3":
                                                                                                       schedule.every().wednesday.at(time199.get()).do(job199)
                                                                                               elif day199.get()=="4":
                                                                                                       schedule.every().thursday.at(time199.get()).do(job199)
                                                                                               elif day199.get()=="5":
                                                                                                       schedule.every().friday.at(time199.get()).do(job199)
                                                                                               elif day199.get()=="6":
                                                                                                       schedule.every().saturday.at(time199.get()).do(job199)
                                                                                               elif day199.get()=="7":
                                                                                                       schedule.every().sunday.at(time199.get()).do(job199)

                                                                                               while True:
                                                                                                    schedule.run_pending()        
                                                                                                    if day200.get()=="1":
                                                                                                            schedule.every().monday.at(time200.get()).do(job200)
                                                                                                    elif day200.get()=="2":
                                                                                                            schedule.every().tuesday.at(time200.get()).do(job200)
                                                                                                    elif day200.get()=="3":
                                                                                                            schedule.every().wednesday.at(time200.get()).do(job200)
                                                                                                    elif day200.get()=="4":
                                                                                                            schedule.every().thursday.at(time200.get()).do(job200)
                                                                                                    elif day200.get()=="5":
                                                                                                            schedule.every().friday.at(time200.get()).do(job200)
                                                                                                    elif day200.get()=="6":
                                                                                                            schedule.every().saturday.at(time200.get()).do(job200)
                                                                                                    elif day200.get()=="7":
                                                                                                            schedule.every().sunday.at(time200.get()).do(job200)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         







def job408():
     
     if day161.get()=="1":
             schedule.every().monday.at(time161.get()).do(job161)
     elif day161.get()=="2":
             schedule.every().tuesday.at(time161.get()).do(job161)
     elif day161.get()=="3":
             schedule.every().wednesday.at(time161.get()).do(job161)
     elif day161.get()=="4":
             schedule.every().thursday.at(time161.get()).do(job161)
     elif day161.get()=="5":
             schedule.every().friday.at(time161.get()).do(job161)
     elif day161.get()=="6":
             schedule.every().saturday.at(time161.get()).do(job161)
     elif day161.get()=="7":
             schedule.every().sunday.at(time161.get()).do(job161)

     while True:
          schedule.run_pending()
          if day162.get()=="1":
                  schedule.every().monday.at(time162.get()).do(job162)
          elif day162.get()=="2":
                  schedule.every().tuesday.at(time162.get()).do(job162)
          elif day162.get()=="3":
                  schedule.every().wednesday.at(time162.get()).do(job162)
          elif day162.get()=="4":
                  schedule.every().thursday.at(time162.get()).do(job162)
          elif day162.get()=="5":
                  schedule.every().friday.at(time162.get()).do(job162)
          elif day162.get()=="6":
                  schedule.every().saturday.at(time162.get()).do(job162)
          elif day162.get()=="7":
                  schedule.every().sunday.at(time162.get()).do(job162)

          while True:
               schedule.run_pending()
               if day163.get()=="1":
                       schedule.every().monday.at(time163.get()).do(job163)
               elif day163.get()=="2":
                       schedule.every().tuesday.at(time163.get()).do(job163)
               elif day163.get()=="3":
                       schedule.every().wednesday.at(time163.get()).do(job163)
               elif day163.get()=="4":
                       schedule.every().thursday.at(time163.get()).do(job163)
               elif day163.get()=="5":
                       schedule.every().friday.at(time163.get()).do(job163)
               elif day163.get()=="6":
                       schedule.every().saturday.at(time163.get()).do(job163)
               elif day163.get()=="7":
                       schedule.every().sunday.at(time163.get()).do(job163)

               while True:
                    schedule.run_pending()
                    if day164.get()=="1":
                            schedule.every().monday.at(time164.get()).do(job164)
                    elif day164.get()=="2":
                            schedule.every().tuesday.at(time164.get()).do(job164)
                    elif day164.get()=="3":
                            schedule.every().wednesday.at(time164.get()).do(job164)
                    elif day164.get()=="4":
                            schedule.every().thursday.at(time164.get()).do(job164)
                    elif day164.get()=="5":
                            schedule.every().friday.at(time164.get()).do(job164)
                    elif day164.get()=="6":
                            schedule.every().saturday.at(time164.get()).do(job164)
                    elif day164.get()=="7":
                            schedule.every().sunday.at(time164.get()).do(job164)

                    while True:
                         schedule.run_pending()
                         if day165.get()=="1":
                                 schedule.every().monday.at(time165.get()).do(job165)
                         elif day165.get()=="2":
                                 schedule.every().tuesday.at(time165.get()).do(job165)
                         elif day165.get()=="3":
                                 schedule.every().wednesday.at(time165.get()).do(job165)
                         elif day165.get()=="4":
                                 schedule.every().thursday.at(time165.get()).do(job165)
                         elif day165.get()=="5":
                                 schedule.every().friday.at(time165.get()).do(job165)
                         elif day165.get()=="6":
                                 schedule.every().saturday.at(time165.get()).do(job165)
                         elif day165.get()=="7":
                                 schedule.every().sunday.at(time165.get()).do(job165)

                         while True:
                              schedule.run_pending()
                              if day166.get()=="1":
                                      schedule.every().monday.at(time166.get()).do(job166)
                              elif day166.get()=="2":
                                      schedule.every().tuesday.at(time166.get()).do(job166)
                              elif day166.get()=="3":
                                      schedule.every().wednesday.at(time166.get()).do(job166)
                              elif day166.get()=="4":
                                      schedule.every().thursday.at(time166.get()).do(job166)
                              elif day166.get()=="5":
                                      schedule.every().friday.at(time166.get()).do(job166)
                              elif day166.get()=="6":
                                      schedule.every().saturday.at(time166.get()).do(job166)
                              elif day166.get()=="7":
                                      schedule.every().sunday.at(time166.get()).do(job166)

                              while True:
                                   schedule.run_pending()
                                   if day167.get()=="1":
                                           schedule.every().monday.at(time167.get()).do(job167)
                                   elif day167.get()=="2":
                                           schedule.every().tuesday.at(time167.get()).do(job167)
                                   elif day167.get()=="3":
                                           schedule.every().wednesday.at(time167.get()).do(job167)
                                   elif day167.get()=="4":
                                           schedule.every().thursday.at(time167.get()).do(job167)
                                   elif day167.get()=="5":
                                           schedule.every().friday.at(time167.get()).do(job167)
                                   elif day167.get()=="6":
                                           schedule.every().saturday.at(time167.get()).do(job167)
                                   elif day167.get()=="7":
                                           schedule.every().sunday.at(time167.get()).do(job167)

                                   while True:
                                        schedule.run_pending()
                                        if day168.get()=="1":
                                                schedule.every().monday.at(time168.get()).do(job168)
                                        elif day168.get()=="2":
                                                schedule.every().tuesday.at(time168.get()).do(job168)
                                        elif day168.get()=="3":
                                                schedule.every().wednesday.at(time168.get()).do(job168)
                                        elif day168.get()=="4":
                                                schedule.every().thursday.at(time168.get()).do(job168)
                                        elif day168.get()=="5":
                                                schedule.every().friday.at(time168.get()).do(job168)
                                        elif day168.get()=="6":
                                                schedule.every().saturday.at(time168.get()).do(job168)
                                        elif day168.get()=="7":
                                                schedule.every().sunday.at(time168.get()).do(job168)

                                        while True:
                                             schedule.run_pending()
                                             if day169.get()=="1":
                                                     schedule.every().monday.at(time169.get()).do(job169)
                                             elif day169.get()=="2":
                                                     schedule.every().tuesday.at(time169.get()).do(job169)
                                             elif day169.get()=="3":
                                                     schedule.every().wednesday.at(time169.get()).do(job169)
                                             elif day169.get()=="4":
                                                     schedule.every().thursday.at(time169.get()).do(job169)
                                             elif day169.get()=="5":
                                                     schedule.every().friday.at(time169.get()).do(job169)
                                             elif day169.get()=="6":
                                                     schedule.every().saturday.at(time169.get()).do(job169)
                                             elif day169.get()=="7":
                                                     schedule.every().sunday.at(time169.get()).do(job169)

                                             while True:
                                                  schedule.run_pending()
                                                  if day170.get()=="1":
                                                          schedule.every().monday.at(time170.get()).do(job170)
                                                  elif day170.get()=="2":
                                                          schedule.every().tuesday.at(time170.get()).do(job170)
                                                  elif day170.get()=="3":
                                                          schedule.every().wednesday.at(time170.get()).do(job170)
                                                  elif day170.get()=="4":
                                                          schedule.every().thursday.at(time170.get()).do(job170)
                                                  elif day170.get()=="5":
                                                          schedule.every().friday.at(time170.get()).do(job170)
                                                  elif day170.get()=="6":
                                                          schedule.every().saturday.at(time170.get()).do(job170)
                                                  elif day170.get()=="7":
                                                          schedule.every().sunday.at(time170.get()).do(job170)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day171.get()=="1":
                                                               schedule.every().monday.at(time171.get()).do(job171)
                                                       elif day171.get()=="2":
                                                               schedule.every().tuesday.at(time171.get()).do(job171)
                                                       elif day171.get()=="3":
                                                               schedule.every().wednesday.at(time171.get()).do(job171)
                                                       elif day171.get()=="4":
                                                               schedule.every().thursday.at(time171.get()).do(job171)
                                                       elif day171.get()=="5":
                                                               schedule.every().friday.at(time171.get()).do(job171)
                                                       elif day171.get()=="6":
                                                               schedule.every().saturday.at(time171.get()).do(job171)
                                                       elif day171.get()=="7":
                                                               schedule.every().sunday.at(time171.get()).do(job171)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day172.get()=="1":
                                                                    schedule.every().monday.at(time172.get()).do(job172)
                                                            elif day172.get()=="2":
                                                                    schedule.every().tuesday.at(time172.get()).do(job172)
                                                            elif day172.get()=="3":
                                                                    schedule.every().wednesday.at(time172.get()).do(job172)
                                                            elif day172.get()=="4":
                                                                    schedule.every().thursday.at(time172.get()).do(job172)
                                                            elif day172.get()=="5":
                                                                    schedule.every().friday.at(time172.get()).do(job172)
                                                            elif day172.get()=="6":
                                                                    schedule.every().saturday.at(time172.get()).do(job172)
                                                            elif day172.get()=="7":
                                                                    schedule.every().sunday.at(time172.get()).do(job172)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day173.get()=="1":
                                                                         schedule.every().monday.at(time173.get()).do(job173)
                                                                 elif day173.get()=="2":
                                                                         schedule.every().tuesday.at(time173.get()).do(job173)
                                                                 elif day173.get()=="3":
                                                                         schedule.every().wednesday.at(time173.get()).do(job173)
                                                                 elif day173.get()=="4":
                                                                         schedule.every().thursday.at(time173.get()).do(job173)
                                                                 elif day173.get()=="5":
                                                                         schedule.every().friday.at(time173.get()).do(job173)
                                                                 elif day173.get()=="6":
                                                                         schedule.every().saturday.at(time173.get()).do(job173)
                                                                 elif day173.get()=="7":
                                                                         schedule.every().sunday.at(time173.get()).do(job173)

                                                                 while True:
                                                                      schedule.run_pending()
                                                                      if day174.get()=="1":
                                                                              schedule.every().monday.at(time174.get()).do(job174)
                                                                      elif day174.get()=="2":
                                                                              schedule.every().tuesday.at(time174.get()).do(job174)
                                                                      elif day174.get()=="3":
                                                                              schedule.every().wednesday.at(time174.get()).do(job174)
                                                                      elif day174.get()=="4":
                                                                              schedule.every().thursday.at(time174.get()).do(job174)
                                                                      elif day174.get()=="5":
                                                                              schedule.every().friday.at(time174.get()).do(job174)
                                                                      elif day174.get()=="6":
                                                                              schedule.every().saturday.at(time174.get()).do(job174)
                                                                      elif day174.get()=="7":
                                                                              schedule.every().sunday.at(time174.get()).do(job174)

                                                                      while True:
                                                                           schedule.run_pending()
                                                                           if day175.get()=="1":
                                                                                   schedule.every().monday.at(time175.get()).do(job175)
                                                                           elif day175.get()=="2":
                                                                                   schedule.every().tuesday.at(time175.get()).do(job175)
                                                                           elif day175.get()=="3":
                                                                                   schedule.every().wednesday.at(time175.get()).do(job175)
                                                                           elif day175.get()=="4":
                                                                                   schedule.every().thursday.at(time175.get()).do(job175)
                                                                           elif day175.get()=="5":
                                                                                   schedule.every().friday.at(time175.get()).do(job175)
                                                                           elif day175.get()=="6":
                                                                                   schedule.every().saturday.at(time175.get()).do(job175)
                                                                           elif day175.get()=="7":
                                                                                   schedule.every().sunday.at(time175.get()).do(job175)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day176.get()=="1":
                                                                                        schedule.every().monday.at(time176.get()).do(job176)
                                                                                elif day176.get()=="2":
                                                                                        schedule.every().tuesday.at(time176.get()).do(job176)
                                                                                elif day176.get()=="3":
                                                                                        schedule.every().wednesday.at(time176.get()).do(job176)
                                                                                elif day176.get()=="4":
                                                                                        schedule.every().thursday.at(time176.get()).do(job176)
                                                                                elif day176.get()=="5":
                                                                                        schedule.every().friday.at(time176.get()).do(job176)
                                                                                elif day176.get()=="6":
                                                                                        schedule.every().saturday.at(time176.get()).do(job176)
                                                                                elif day176.get()=="7":
                                                                                        schedule.every().sunday.at(time176.get()).do(job176)

                                                                                while True:
                                                                                     schedule.run_pending()
                                                                                     if day177.get()=="1":
                                                                                             schedule.every().monday.at(time177.get()).do(job177)
                                                                                     elif day177.get()=="2":
                                                                                             schedule.every().tuesday.at(time177.get()).do(job177)
                                                                                     elif day177.get()=="3":
                                                                                             schedule.every().wednesday.at(time177.get()).do(job177)
                                                                                     elif day177.get()=="4":
                                                                                             schedule.every().thursday.at(time177.get()).do(job177)
                                                                                     elif day177.get()=="5":
                                                                                             schedule.every().friday.at(time177.get()).do(job177)
                                                                                     elif day177.get()=="6":
                                                                                             schedule.every().saturday.at(time177.get()).do(job177)
                                                                                     elif day177.get()=="7":
                                                                                             schedule.every().sunday.at(time177.get()).do(job177)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day178.get()=="1":
                                                                                                  schedule.every().monday.at(time178.get()).do(job178)
                                                                                          elif day178.get()=="2":
                                                                                                  schedule.every().tuesday.at(time178.get()).do(job178)
                                                                                          elif day178.get()=="3":
                                                                                                  schedule.every().wednesday.at(time178.get()).do(job178)
                                                                                          elif day178.get()=="4":
                                                                                                  schedule.every().thursday.at(time178.get()).do(job178)
                                                                                          elif day178.get()=="5":
                                                                                                  schedule.every().friday.at(time178.get()).do(job178)
                                                                                          elif day178.get()=="6":
                                                                                                  schedule.every().saturday.at(time178.get()).do(job178)
                                                                                          elif day178.get()=="7":
                                                                                                  schedule.every().sunday.at(time178.get()).do(job178)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day179.get()=="1":
                                                                                                       schedule.every().monday.at(time179.get()).do(job179)
                                                                                               elif day179.get()=="2":
                                                                                                       schedule.every().tuesday.at(time179.get()).do(job179)
                                                                                               elif day179.get()=="3":
                                                                                                       schedule.every().wednesday.at(time179.get()).do(job179)
                                                                                               elif day179.get()=="4":
                                                                                                       schedule.every().thursday.at(time179.get()).do(job179)
                                                                                               elif day179.get()=="5":
                                                                                                       schedule.every().friday.at(time179.get()).do(job179)
                                                                                               elif day179.get()=="6":
                                                                                                       schedule.every().saturday.at(time179.get()).do(job179)
                                                                                               elif day179.get()=="7":
                                                                                                       schedule.every().sunday.at(time179.get()).do(job179)

                                                                                               while True:
                                                                                                    schedule.run_pending()
                                                                                                    if day180.get()=="1":
                                                                                                            schedule.every().monday.at(time180.get()).do(job180)
                                                                                                    elif day180.get()=="2":
                                                                                                            schedule.every().tuesday.at(time180.get()).do(job180)
                                                                                                    elif day180.get()=="3":
                                                                                                            schedule.every().wednesday.at(time180.get()).do(job180)
                                                                                                    elif day180.get()=="4":
                                                                                                            schedule.every().thursday.at(time180.get()).do(job180)
                                                                                                    elif day180.get()=="5":
                                                                                                            schedule.every().friday.at(time180.get()).do(job180)
                                                                                                    elif day180.get()=="6":
                                                                                                            schedule.every().saturday.at(time180.get()).do(job180)
                                                                                                    elif day180.get()=="7":
                                                                                                            schedule.every().sunday.at(time180.get()).do(job180)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         (job409())




def job407():
     
     if day141.get()=="1":
             schedule.every().monday.at(time141.get()).do(job141)
     elif day141.get()=="2":
             schedule.every().tuesday.at(time141.get()).do(job141)
     elif day141.get()=="3":
             schedule.every().wednesday.at(time141.get()).do(job141)
     elif day141.get()=="4":
             schedule.every().thursday.at(time141.get()).do(job141)
     elif day141.get()=="5":
             schedule.every().friday.at(time141.get()).do(job141)
     elif day141.get()=="6":
             schedule.every().saturday.at(time141.get()).do(job141)
     elif day141.get()=="7":
             schedule.every().sunday.at(time141.get()).do(job141)

     while True:
          schedule.run_pending()
          if day142.get()=="1":
                  schedule.every().monday.at(time142.get()).do(job142)
          elif day142.get()=="2":
                  schedule.every().tuesday.at(time142.get()).do(job142)
          elif day142.get()=="3":
                  schedule.every().wednesday.at(time142.get()).do(job142)
          elif day142.get()=="4":
                  schedule.every().thursday.at(time142.get()).do(job142)
          elif day142.get()=="5":
                  schedule.every().friday.at(time142.get()).do(job142)
          elif day142.get()=="6":
                  schedule.every().saturday.at(time142.get()).do(job142)
          elif day142.get()=="7":
                  schedule.every().sunday.at(time142.get()).do(job142)

          while True:
               schedule.run_pending()
               if day143.get()=="1":
                       schedule.every().monday.at(time143.get()).do(job143)
               elif day143.get()=="2":
                       schedule.every().tuesday.at(time143.get()).do(job143)
               elif day143.get()=="3":
                       schedule.every().wednesday.at(time143.get()).do(job143)
               elif day143.get()=="4":
                       schedule.every().thursday.at(time143.get()).do(job143)
               elif day143.get()=="5":
                       schedule.every().friday.at(time143.get()).do(job143)
               elif day143.get()=="6":
                       schedule.every().saturday.at(time143.get()).do(job143)
               elif day143.get()=="7":
                       schedule.every().sunday.at(time143.get()).do(job143)

               while True:
                    schedule.run_pending()
                    if day144.get()=="1":
                            schedule.every().monday.at(time144.get()).do(job144)
                    elif day144.get()=="2":
                            schedule.every().tuesday.at(time144.get()).do(job144)
                    elif day144.get()=="3":
                            schedule.every().wednesday.at(time144.get()).do(job144)
                    elif day144.get()=="4":
                            schedule.every().thursday.at(time144.get()).do(job144)
                    elif day144.get()=="5":
                            schedule.every().friday.at(time144.get()).do(job144)
                    elif day144.get()=="6":
                            schedule.every().saturday.at(time144.get()).do(job144)
                    elif day144.get()=="7":
                            schedule.every().sunday.at(time144.get()).do(job144)

                    while True:
                         schedule.run_pending()        
                         if day145.get()=="1":
                                 schedule.every().monday.at(time145.get()).do(job145)
                         elif day145.get()=="2":
                                 schedule.every().tuesday.at(time145.get()).do(job145)
                         elif day145.get()=="3":
                                 schedule.every().wednesday.at(time145.get()).do(job145)
                         elif day145.get()=="4":
                                 schedule.every().thursday.at(time145.get()).do(job145)
                         elif day145.get()=="5":
                                 schedule.every().friday.at(time145.get()).do(job145)
                         elif day145.get()=="6":
                                 schedule.every().saturday.at(time145.get()).do(job145)
                         elif day145.get()=="7":
                                 schedule.every().sunday.at(time145.get()).do(job145)

                         while True:
                              schedule.run_pending()
                              if day146.get()=="1":
                                      schedule.every().monday.at(time146.get()).do(job146)
                              elif day146.get()=="2":
                                      schedule.every().tuesday.at(time146.get()).do(job146)
                              elif day146.get()=="3":
                                      schedule.every().wednesday.at(time146.get()).do(job146)
                              elif day146.get()=="4":
                                      schedule.every().thursday.at(time146.get()).do(job146)
                              elif day146.get()=="5":
                                      schedule.every().friday.at(time146.get()).do(job146)
                              elif day146.get()=="6":
                                      schedule.every().saturday.at(time146.get()).do(job146)
                              elif day146.get()=="7":
                                      schedule.every().sunday.at(time146.get()).do(job146)

                              while True:
                                   schedule.run_pending()
                                   if day147.get()=="1":
                                           schedule.every().monday.at(time147.get()).do(job147)
                                   elif day147.get()=="2":
                                           schedule.every().tuesday.at(time147.get()).do(job147)
                                   elif day147.get()=="3":
                                           schedule.every().wednesday.at(time147.get()).do(job147)
                                   elif day147.get()=="4":
                                           schedule.every().thursday.at(time147.get()).do(job147)
                                   elif day147.get()=="5":
                                           schedule.every().friday.at(time147.get()).do(job147)
                                   elif day147.get()=="6":
                                           schedule.every().saturday.at(time147.get()).do(job147)
                                   elif day147.get()=="7":
                                           schedule.every().sunday.at(time147.get()).do(job147)

                                   while True:
                                        schedule.run_pending()
                                        if day148.get()=="1":
                                                schedule.every().monday.at(time148.get()).do(job148)
                                        elif day148.get()=="2":
                                                schedule.every().tuesday.at(time148.get()).do(job148)
                                        elif day148.get()=="3":
                                                schedule.every().wednesday.at(time148.get()).do(job148)
                                        elif day148.get()=="4":
                                                schedule.every().thursday.at(time148.get()).do(job148)
                                        elif day148.get()=="5":
                                                schedule.every().friday.at(time148.get()).do(job148)
                                        elif day148.get()=="6":
                                                schedule.every().saturday.at(time148.get()).do(job148)
                                        elif day148.get()=="7":
                                                schedule.every().sunday.at(time148.get()).do(job148)

                                        while True:
                                             schedule.run_pending()
                                             if day149.get()=="1":
                                                     schedule.every().monday.at(time149.get()).do(job149)
                                             elif day149.get()=="2":
                                                     schedule.every().tuesday.at(time149.get()).do(job149)
                                             elif day149.get()=="3":
                                                     schedule.every().wednesday.at(time149.get()).do(job149)
                                             elif day149.get()=="4":
                                                     schedule.every().thursday.at(time149.get()).do(job149)
                                             elif day149.get()=="5":
                                                     schedule.every().friday.at(time149.get()).do(job149)
                                             elif day149.get()=="6":
                                                     schedule.every().saturday.at(time149.get()).do(job149)
                                             elif day149.get()=="7":
                                                     schedule.every().sunday.at(time149.get()).do(job149)

                                             while True:
                                                  schedule.run_pending()
                                                  if day150.get()=="1":
                                                          schedule.every().monday.at(time150.get()).do(job150)
                                                  elif day150.get()=="2":
                                                          schedule.every().tuesday.at(time150.get()).do(job150)
                                                  elif day150.get()=="3":
                                                          schedule.every().wednesday.at(time150.get()).do(job150)
                                                  elif day150.get()=="4":
                                                          schedule.every().thursday.at(time150.get()).do(job150)
                                                  elif day150.get()=="5":
                                                          schedule.every().friday.at(time150.get()).do(job150)
                                                  elif day150.get()=="6":
                                                          schedule.every().saturday.at(time150.get()).do(job150)
                                                  elif day150.get()=="7":
                                                          schedule.every().sunday.at(time150.get()).do(job150)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day151.get()=="1":
                                                               schedule.every().monday.at(time151.get()).do(job151)
                                                       elif day151.get()=="2":
                                                               schedule.every().tuesday.at(time151.get()).do(job151)
                                                       elif day151.get()=="3":
                                                               schedule.every().wednesday.at(time151.get()).do(job151)
                                                       elif day151.get()=="4":
                                                               schedule.every().thursday.at(time151.get()).do(job151)
                                                       elif day151.get()=="5":
                                                               schedule.every().friday.at(time151.get()).do(job151)
                                                       elif day151.get()=="6":
                                                               schedule.every().saturday.at(time151.get()).do(job151)
                                                       elif day151.get()=="7":
                                                               schedule.every().sunday.at(time151.get()).do(job151)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day152.get()=="1":
                                                                    schedule.every().monday.at(time152.get()).do(job152)
                                                            elif day152.get()=="2":
                                                                    schedule.every().tuesday.at(time152.get()).do(job152)
                                                            elif day152.get()=="3":
                                                                    schedule.every().wednesday.at(time152.get()).do(job152)
                                                            elif day152.get()=="4":
                                                                    schedule.every().thursday.at(time152.get()).do(job152)
                                                            elif day152.get()=="5":
                                                                    schedule.every().friday.at(time152.get()).do(job152)
                                                            elif day152.get()=="6":
                                                                    schedule.every().saturday.at(time152.get()).do(job152)
                                                            elif day152.get()=="7":
                                                                    schedule.every().sunday.at(time152.get()).do(job152)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day153.get()=="1":
                                                                         schedule.every().monday.at(time153.get()).do(job153)
                                                                 elif day153.get()=="2":
                                                                         schedule.every().tuesday.at(time153.get()).do(job153)
                                                                 elif day153.get()=="3":
                                                                         schedule.every().wednesday.at(time153.get()).do(job153)
                                                                 elif day153.get()=="4":
                                                                         schedule.every().thursday.at(time153.get()).do(job153)
                                                                 elif day153.get()=="5":
                                                                         schedule.every().friday.at(time153.get()).do(job153)
                                                                 elif day153.get()=="6":
                                                                         schedule.every().saturday.at(time153.get()).do(job153)
                                                                 elif day153.get()=="7":
                                                                         schedule.every().sunday.at(time153.get()).do(job153)

                                                                 while True:
                                                                      schedule.run_pending()
                                                                      if day154.get()=="1":
                                                                              schedule.every().monday.at(time154.get()).do(job154)
                                                                      elif day154.get()=="2":
                                                                              schedule.every().tuesday.at(time154.get()).do(job154)
                                                                      elif day154.get()=="3":
                                                                              schedule.every().wednesday.at(time154.get()).do(job154)
                                                                      elif day154.get()=="4":
                                                                              schedule.every().thursday.at(time154.get()).do(job154)
                                                                      elif day154.get()=="5":
                                                                              schedule.every().friday.at(time154.get()).do(job154)
                                                                      elif day154.get()=="6":
                                                                              schedule.every().saturday.at(time154.get()).do(job154)
                                                                      elif day154.get()=="7":
                                                                              schedule.every().sunday.at(time154.get()).do(job154)

                                                                      while True:
                                                                           schedule.run_pending()
                                                                           if day155.get()=="1":
                                                                                   schedule.every().monday.at(time155.get()).do(job155)
                                                                           elif day155.get()=="2":
                                                                                   schedule.every().tuesday.at(time155.get()).do(job155)
                                                                           elif day155.get()=="3":
                                                                                   schedule.every().wednesday.at(time155.get()).do(job155)
                                                                           elif day155.get()=="4":
                                                                                   schedule.every().thursday.at(time155.get()).do(job155)
                                                                           elif day155.get()=="5":
                                                                                   schedule.every().friday.at(time155.get()).do(job155)
                                                                           elif day155.get()=="6":
                                                                                   schedule.every().saturday.at(time155.get()).do(job155)
                                                                           elif day155.get()=="7":
                                                                                   schedule.every().sunday.at(time155.get()).do(job155)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day156.get()=="1":
                                                                                        schedule.every().monday.at(time156.get()).do(job156)
                                                                                elif day156.get()=="2":
                                                                                        schedule.every().tuesday.at(time156.get()).do(job156)
                                                                                elif day156.get()=="3":
                                                                                        schedule.every().wednesday.at(time156.get()).do(job156)
                                                                                elif day156.get()=="4":
                                                                                        schedule.every().thursday.at(time156.get()).do(job156)
                                                                                elif day156.get()=="5":
                                                                                        schedule.every().friday.at(time156.get()).do(job156)
                                                                                elif day156.get()=="6":
                                                                                        schedule.every().saturday.at(time156.get()).do(job156)
                                                                                elif day156.get()=="7":
                                                                                        schedule.every().sunday.at(time156.get()).do(job156)

                                                                                while True:
                                                                                     schedule.run_pending()
                                                                                     if day157.get()=="1":
                                                                                             schedule.every().monday.at(time157.get()).do(job157)
                                                                                     elif day157.get()=="2":
                                                                                             schedule.every().tuesday.at(time157.get()).do(job157)
                                                                                     elif day157.get()=="3":
                                                                                             schedule.every().wednesday.at(time157.get()).do(job157)
                                                                                     elif day157.get()=="4":
                                                                                             schedule.every().thursday.at(time157.get()).do(job157)
                                                                                     elif day157.get()=="5":
                                                                                             schedule.every().friday.at(time157.get()).do(job157)
                                                                                     elif day157.get()=="6":
                                                                                             schedule.every().saturday.at(time157.get()).do(job157)
                                                                                     elif day157.get()=="7":
                                                                                             schedule.every().sunday.at(time157.get()).do(job157)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day158.get()=="1":
                                                                                                  schedule.every().monday.at(time158.get()).do(job158)
                                                                                          elif day158.get()=="2":
                                                                                                  schedule.every().tuesday.at(time158.get()).do(job158)
                                                                                          elif day158.get()=="3":
                                                                                                  schedule.every().wednesday.at(time158.get()).do(job158)
                                                                                          elif day158.get()=="4":
                                                                                                  schedule.every().thursday.at(time158.get()).do(job158)
                                                                                          elif day158.get()=="5":
                                                                                                  schedule.every().friday.at(time158.get()).do(job158)
                                                                                          elif day158.get()=="6":
                                                                                                  schedule.every().saturday.at(time158.get()).do(job158)
                                                                                          elif day158.get()=="7":
                                                                                                  schedule.every().sunday.at(time158.get()).do(job158)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day159.get()=="1":
                                                                                                       schedule.every().monday.at(time159.get()).do(job159)
                                                                                               elif day159.get()=="2":
                                                                                                       schedule.every().tuesday.at(time159.get()).do(job159)
                                                                                               elif day159.get()=="3":
                                                                                                       schedule.every().wednesday.at(time159.get()).do(job159)
                                                                                               elif day159.get()=="4":
                                                                                                       schedule.every().thursday.at(time159.get()).do(job159)
                                                                                               elif day159.get()=="5":
                                                                                                       schedule.every().friday.at(time159.get()).do(job159)
                                                                                               elif day159.get()=="6":
                                                                                                       schedule.every().saturday.at(time159.get()).do(job159)
                                                                                               elif day159.get()=="7":
                                                                                                       schedule.every().sunday.at(time159.get()).do(job159)

                                                                                               while True:
                                                                                                    schedule.run_pending()
                                                                                                    if day160.get()=="1":
                                                                                                            schedule.every().monday.at(time160.get()).do(job160)
                                                                                                    elif day160.get()=="2":
                                                                                                            schedule.every().tuesday.at(time160.get()).do(job160)
                                                                                                    elif day160.get()=="3":
                                                                                                            schedule.every().wednesday.at(time160.get()).do(job160)
                                                                                                    elif day160.get()=="4":
                                                                                                            schedule.every().thursday.at(time160.get()).do(job160)
                                                                                                    elif day160.get()=="5":
                                                                                                            schedule.every().friday.at(time160.get()).do(job160)
                                                                                                    elif day160.get()=="6":
                                                                                                            schedule.every().saturday.at(time160.get()).do(job160)
                                                                                                    elif day160.get()=="7":
                                                                                                            schedule.every().sunday.at(time160.get()).do(job160)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         (job408())





def job406():
     
     if day121.get()=="1":
             schedule.every().monday.at(time121.get()).do(job121)
     elif day121.get()=="2":
             schedule.every().tuesday.at(time121.get()).do(job121)
     elif day121.get()=="3":
             schedule.every().wednesday.at(time121.get()).do(job121)
     elif day121.get()=="4":
             schedule.every().thursday.at(time121.get()).do(job121)
     elif day121.get()=="5":
             schedule.every().friday.at(time121.get()).do(job121)
     elif day121.get()=="6":
             schedule.every().saturday.at(time121.get()).do(job121)
     elif day121.get()=="7":
             schedule.every().sunday.at(time121.get()).do(job121)

     while True:
          schedule.run_pending()
          if day122.get()=="1":
                  schedule.every().monday.at(time122.get()).do(job122)
          elif day122.get()=="2":
                  schedule.every().tuesday.at(time122.get()).do(job122)
          elif day122.get()=="3":
                  schedule.every().wednesday.at(time122.get()).do(job122)
          elif day122.get()=="4":
                  schedule.every().thursday.at(time122.get()).do(job122)
          elif day122.get()=="5":
                  schedule.every().friday.at(time122.get()).do(job122)
          elif day122.get()=="6":
                  schedule.every().saturday.at(time122.get()).do(job122)
          elif day122.get()=="7":
                  schedule.every().sunday.at(time122.get()).do(job122)

          while True:
               schedule.run_pending()
               if day123.get()=="1":
                       schedule.every().monday.at(time123.get()).do(job123)
               elif day123.get()=="2":
                       schedule.every().tuesday.at(time123.get()).do(job123)
               elif day123.get()=="3":
                       schedule.every().wednesday.at(time123.get()).do(job123)
               elif day123.get()=="4":
                       schedule.every().thursday.at(time123.get()).do(job123)
               elif day123.get()=="5":
                       schedule.every().friday.at(time123.get()).do(job123)
               elif day123.get()=="6":
                       schedule.every().saturday.at(time123.get()).do(job123)
               elif day123.get()=="7":
                       schedule.every().sunday.at(time123.get()).do(job123)

               while True:
                    schedule.run_pending()
                    if day124.get()=="1":
                            schedule.every().monday.at(time124.get()).do(job124)
                    elif day124.get()=="2":
                            schedule.every().tuesday.at(time124.get()).do(job124)
                    elif day124.get()=="3":
                            schedule.every().wednesday.at(time124.get()).do(job124)
                    elif day124.get()=="4":
                            schedule.every().thursday.at(time124.get()).do(job124)
                    elif day124.get()=="5":
                            schedule.every().friday.at(time124.get()).do(job124)
                    elif day124.get()=="6":
                            schedule.every().saturday.at(time124.get()).do(job124)
                    elif day124.get()=="7":
                            schedule.every().sunday.at(time124.get()).do(job124)

                    while True:
                         schedule.run_pending()
                         if day125.get()=="1":
                                 schedule.every().monday.at(time125.get()).do(job125)
                         elif day125.get()=="2":
                                 schedule.every().tuesday.at(time125.get()).do(job125)
                         elif day125.get()=="3":
                                 schedule.every().wednesday.at(time125.get()).do(job125)
                         elif day125.get()=="4":
                                 schedule.every().thursday.at(time125.get()).do(job125)
                         elif day125.get()=="5":
                                 schedule.every().friday.at(time125.get()).do(job125)
                         elif day125.get()=="6":
                                 schedule.every().saturday.at(time125.get()).do(job125)
                         elif day125.get()=="7":
                                 schedule.every().sunday.at(time125.get()).do(job125)

                         while True:
                              schedule.run_pending()        
                              if day126.get()=="1":
                                      schedule.every().monday.at(time126.get()).do(job126)
                              elif day126.get()=="2":
                                      schedule.every().tuesday.at(time126.get()).do(job126)
                              elif day126.get()=="3":
                                      schedule.every().wednesday.at(time126.get()).do(job126)
                              elif day126.get()=="4":
                                      schedule.every().thursday.at(time126.get()).do(job126)
                              elif day126.get()=="5":
                                      schedule.every().friday.at(time126.get()).do(job126)
                              elif day126.get()=="6":
                                      schedule.every().saturday.at(time126.get()).do(job126)
                              elif day126.get()=="7":
                                      schedule.every().sunday.at(time126.get()).do(job126)

                              while True:
                                   schedule.run_pending()
                                   if day127.get()=="1":
                                           schedule.every().monday.at(time127.get()).do(job127)
                                   elif day127.get()=="2":
                                           schedule.every().tuesday.at(time127.get()).do(job127)
                                   elif day127.get()=="3":
                                           schedule.every().wednesday.at(time127.get()).do(job127)
                                   elif day127.get()=="4":
                                           schedule.every().thursday.at(time127.get()).do(job127)
                                   elif day127.get()=="5":
                                           schedule.every().friday.at(time127.get()).do(job127)
                                   elif day127.get()=="6":
                                           schedule.every().saturday.at(time127.get()).do(job127)
                                   elif day127.get()=="7":
                                           schedule.every().sunday.at(time127.get()).do(job127)

                                   while True:
                                        schedule.run_pending()
                                        if day128.get()=="1":
                                                schedule.every().monday.at(time128.get()).do(job128)
                                        elif day128.get()=="2":
                                                schedule.every().tuesday.at(time128.get()).do(job128)
                                        elif day128.get()=="3":
                                                schedule.every().wednesday.at(time128.get()).do(job128)
                                        elif day128.get()=="4":
                                                schedule.every().thursday.at(time128.get()).do(job128)
                                        elif day128.get()=="5":
                                                schedule.every().friday.at(time128.get()).do(job128)
                                        elif day128.get()=="6":
                                                schedule.every().saturday.at(time128.get()).do(job128)
                                        elif day128.get()=="7":
                                                schedule.every().sunday.at(time128.get()).do(job128)

                                        while True:
                                             schedule.run_pending()
                                             if day129.get()=="1":
                                                     schedule.every().monday.at(time129.get()).do(job129)
                                             elif day129.get()=="2":
                                                     schedule.every().tuesday.at(time129.get()).do(job129)
                                             elif day129.get()=="3":
                                                     schedule.every().wednesday.at(time129.get()).do(job129)
                                             elif day129.get()=="4":
                                                     schedule.every().thursday.at(time129.get()).do(job129)
                                             elif day129.get()=="5":
                                                     schedule.every().friday.at(time129.get()).do(job129)
                                             elif day129.get()=="6":
                                                     schedule.every().saturday.at(time129.get()).do(job129)
                                             elif day129.get()=="7":
                                                     schedule.every().sunday.at(time129.get()).do(job129)

                                             while True:
                                                  schedule.run_pending()
                                                  if day130.get()=="1":
                                                          schedule.every().monday.at(time130.get()).do(job130)
                                                  elif day130.get()=="2":
                                                          schedule.every().tuesday.at(time130.get()).do(job130)
                                                  elif day130.get()=="3":
                                                          schedule.every().wednesday.at(time130.get()).do(job130)
                                                  elif day130.get()=="4":
                                                          schedule.every().thursday.at(time130.get()).do(job130)
                                                  elif day130.get()=="5":
                                                          schedule.every().friday.at(time130.get()).do(job130)
                                                  elif day130.get()=="6":
                                                          schedule.every().saturday.at(time130.get()).do(job130)
                                                  elif day130.get()=="7":
                                                          schedule.every().sunday.at(time130.get()).do(job130)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day131.get()=="1":
                                                               schedule.every().monday.at(time131.get()).do(job131)
                                                       elif day131.get()=="2":
                                                               schedule.every().tuesday.at(time131.get()).do(job131)
                                                       elif day131.get()=="3":
                                                               schedule.every().wednesday.at(time131.get()).do(job131)
                                                       elif day131.get()=="4":
                                                               schedule.every().thursday.at(time131.get()).do(job131)
                                                       elif day131.get()=="5":
                                                               schedule.every().friday.at(time131.get()).do(job131)
                                                       elif day131.get()=="6":
                                                               schedule.every().saturday.at(time131.get()).do(job131)
                                                       elif day131.get()=="7":
                                                               schedule.every().sunday.at(time131.get()).do(job131)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day132.get()=="1":
                                                                    schedule.every().monday.at(time132.get()).do(job132)
                                                            elif day132.get()=="2":
                                                                    schedule.every().tuesday.at(time132.get()).do(job132)
                                                            elif day132.get()=="3":
                                                                    schedule.every().wednesday.at(time132.get()).do(job132)
                                                            elif day132.get()=="4":
                                                                    schedule.every().thursday.at(time132.get()).do(job132)
                                                            elif day132.get()=="5":
                                                                    schedule.every().friday.at(time132.get()).do(job132)
                                                            elif day132.get()=="6":
                                                                    schedule.every().saturday.at(time132.get()).do(job132)
                                                            elif day132.get()=="7":
                                                                    schedule.every().sunday.at(time132.get()).do(job132)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day133.get()=="1":
                                                                         schedule.every().monday.at(time133.get()).do(job133)
                                                                 elif day133.get()=="2":
                                                                         schedule.every().tuesday.at(time133.get()).do(job133)
                                                                 elif day133.get()=="3":
                                                                         schedule.every().wednesday.at(time133.get()).do(job133)
                                                                 elif day133.get()=="4":
                                                                         schedule.every().thursday.at(time133.get()).do(job133)
                                                                 elif day133.get()=="5":
                                                                         schedule.every().friday.at(time133.get()).do(job133)
                                                                 elif day133.get()=="6":
                                                                         schedule.every().saturday.at(time133.get()).do(job133)
                                                                 elif day133.get()=="7":
                                                                         schedule.every().sunday.at(time133.get()).do(job133)

                                                                 while True:
                                                                      schedule.run_pending()
                                                                      if day134.get()=="1":
                                                                              schedule.every().monday.at(time134.get()).do(job134)
                                                                      elif day134.get()=="2":
                                                                              schedule.every().tuesday.at(time134.get()).do(job134)
                                                                      elif day134.get()=="3":
                                                                              schedule.every().wednesday.at(time134.get()).do(job134)
                                                                      elif day134.get()=="4":
                                                                              schedule.every().thursday.at(time134.get()).do(job134)
                                                                      elif day134.get()=="5":
                                                                              schedule.every().friday.at(time134.get()).do(job134)
                                                                      elif day134.get()=="6":
                                                                              schedule.every().saturday.at(time134.get()).do(job134)
                                                                      elif day134.get()=="7":
                                                                              schedule.every().sunday.at(time134.get()).do(job134)

                                                                      while True:
                                                                           schedule.run_pending()
                                                                           if day135.get()=="1":
                                                                                   schedule.every().monday.at(time135.get()).do(job135)
                                                                           elif day135.get()=="2":
                                                                                   schedule.every().tuesday.at(time135.get()).do(job135)
                                                                           elif day135.get()=="3":
                                                                                   schedule.every().wednesday.at(time135.get()).do(job135)
                                                                           elif day135.get()=="4":
                                                                                   schedule.every().thursday.at(time135.get()).do(job135)
                                                                           elif day135.get()=="5":
                                                                                   schedule.every().friday.at(time135.get()).do(job135)
                                                                           elif day135.get()=="6":
                                                                                   schedule.every().saturday.at(time135.get()).do(job135)
                                                                           elif day135.get()=="7":
                                                                                   schedule.every().sunday.at(time135.get()).do(job135)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day136.get()=="1":
                                                                                        schedule.every().monday.at(time136.get()).do(job136)
                                                                                elif day136.get()=="2":
                                                                                        schedule.every().tuesday.at(time136.get()).do(job136)
                                                                                elif day136.get()=="3":
                                                                                        schedule.every().wednesday.at(time136.get()).do(job136)
                                                                                elif day136.get()=="4":
                                                                                        schedule.every().thursday.at(time136.get()).do(job136)
                                                                                elif day136.get()=="5":
                                                                                        schedule.every().friday.at(time136.get()).do(job136)
                                                                                elif day136.get()=="6":
                                                                                        schedule.every().saturday.at(time136.get()).do(job136)
                                                                                elif day136.get()=="7":
                                                                                        schedule.every().sunday.at(time136.get()).do(job136)

                                                                                while True:
                                                                                     schedule.run_pending()
                                                                                     if day137.get()=="1":
                                                                                             schedule.every().monday.at(time137.get()).do(job137)
                                                                                     elif day137.get()=="2":
                                                                                             schedule.every().tuesday.at(time137.get()).do(job137)
                                                                                     elif day137.get()=="3":
                                                                                             schedule.every().wednesday.at(time137.get()).do(job137)
                                                                                     elif day137.get()=="4":
                                                                                             schedule.every().thursday.at(time137.get()).do(job137)
                                                                                     elif day137.get()=="5":
                                                                                             schedule.every().friday.at(time137.get()).do(job137)
                                                                                     elif day137.get()=="6":
                                                                                             schedule.every().saturday.at(time137.get()).do(job137)
                                                                                     elif day137.get()=="7":
                                                                                             schedule.every().sunday.at(time137.get()).do(job137)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day138.get()=="1":
                                                                                                  schedule.every().monday.at(time138.get()).do(job138)
                                                                                          elif day138.get()=="2":
                                                                                                  schedule.every().tuesday.at(time138.get()).do(job138)
                                                                                          elif day138.get()=="3":
                                                                                                  schedule.every().wednesday.at(time138.get()).do(job138)
                                                                                          elif day138.get()=="4":
                                                                                                  schedule.every().thursday.at(time138.get()).do(job138)
                                                                                          elif day138.get()=="5":
                                                                                                  schedule.every().friday.at(time138.get()).do(job138)
                                                                                          elif day138.get()=="6":
                                                                                                  schedule.every().saturday.at(time138.get()).do(job138)
                                                                                          elif day138.get()=="7":
                                                                                                  schedule.every().sunday.at(time138.get()).do(job138)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day139.get()=="1":
                                                                                                       schedule.every().monday.at(time139.get()).do(job139)
                                                                                               elif day139.get()=="2":
                                                                                                       schedule.every().tuesday.at(time139.get()).do(job139)
                                                                                               elif day139.get()=="3":
                                                                                                       schedule.every().wednesday.at(time139.get()).do(job139)
                                                                                               elif day139.get()=="4":
                                                                                                       schedule.every().thursday.at(time139.get()).do(job139)
                                                                                               elif day139.get()=="5":
                                                                                                       schedule.every().friday.at(time139.get()).do(job139)
                                                                                               elif day139.get()=="6":
                                                                                                       schedule.every().saturday.at(time139.get()).do(job139)
                                                                                               elif day139.get()=="7":
                                                                                                       schedule.every().sunday.at(time139.get()).do(job139)

                                                                                               while True:
                                                                                                    schedule.run_pending()
                                                                                                    if day140.get()=="1":
                                                                                                            schedule.every().monday.at(time140.get()).do(job140)
                                                                                                    elif day140.get()=="2":
                                                                                                            schedule.every().tuesday.at(time140.get()).do(job140)
                                                                                                    elif day140.get()=="3":
                                                                                                            schedule.every().wednesday.at(time140.get()).do(job140)
                                                                                                    elif day140.get()=="4":
                                                                                                            schedule.every().thursday.at(time140.get()).do(job140)
                                                                                                    elif day140.get()=="5":
                                                                                                            schedule.every().friday.at(time140.get()).do(job140)
                                                                                                    elif day140.get()=="6":
                                                                                                            schedule.every().saturday.at(time140.get()).do(job140)
                                                                                                    elif day140.get()=="7":
                                                                                                            schedule.every().sunday.at(time140.get()).do(job140)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         (job407())





def job405():
     
     if day101.get()=="1":
             schedule.every().monday.at(time101.get()).do(job101)
     elif day101.get()=="2":
             schedule.every().tuesday.at(time101.get()).do(job101)
     elif day101.get()=="3":
             schedule.every().wednesday.at(time101.get()).do(job101)
     elif day101.get()=="4":
             schedule.every().thursday.at(time101.get()).do(job101)
     elif day101.get()=="5":
             schedule.every().friday.at(time101.get()).do(job101)
     elif day101.get()=="6":
             schedule.every().saturday.at(time101.get()).do(job101)
     elif day101.get()=="7":
             schedule.every().sunday.at(time101.get()).do(job101)

     while True:
          schedule.run_pending()
          if day102.get()=="1":
                  schedule.every().monday.at(time102.get()).do(job102)
          elif day102.get()=="2":
                  schedule.every().tuesday.at(time102.get()).do(job102)
          elif day102.get()=="3":
                  schedule.every().wednesday.at(time102.get()).do(job102)
          elif day102.get()=="4":
                  schedule.every().thursday.at(time102.get()).do(job102)
          elif day102.get()=="5":
                  schedule.every().friday.at(time102.get()).do(job102)
          elif day102.get()=="6":
                  schedule.every().saturday.at(time102.get()).do(job102)
          elif day102.get()=="7":
                  schedule.every().sunday.at(time102.get()).do(job102)

          while True:
               schedule.run_pending()
               if day103.get()=="1":
                       schedule.every().monday.at(time103.get()).do(job103)
               elif day103.get()=="2":
                       schedule.every().tuesday.at(time103.get()).do(job103)
               elif day103.get()=="3":
                       schedule.every().wednesday.at(time103.get()).do(job103)
               elif day103.get()=="4":
                       schedule.every().thursday.at(time103.get()).do(job103)
               elif day103.get()=="5":
                       schedule.every().friday.at(time103.get()).do(job103)
               elif day103.get()=="6":
                       schedule.every().saturday.at(time103.get()).do(job103)
               elif day103.get()=="7":
                       schedule.every().sunday.at(time103.get()).do(job103)

               while True:
                    schedule.run_pending()
                    if day104.get()=="1":
                            schedule.every().monday.at(time104.get()).do(job104)
                    elif day104.get()=="2":
                            schedule.every().tuesday.at(time104.get()).do(job104)
                    elif day104.get()=="3":
                            schedule.every().wednesday.at(time104.get()).do(job104)
                    elif day104.get()=="4":
                            schedule.every().thursday.at(time104.get()).do(job104)
                    elif day104.get()=="5":
                            schedule.every().friday.at(time104.get()).do(job104)
                    elif day104.get()=="6":
                            schedule.every().saturday.at(time104.get()).do(job104)
                    elif day104.get()=="7":
                            schedule.every().sunday.at(time104.get()).do(job104)

                    while True:
                         schedule.run_pending()
                         if day105.get()=="1":
                                 schedule.every().monday.at(time105.get()).do(job105)
                         elif day105.get()=="2":
                                 schedule.every().tuesday.at(time105.get()).do(job105)
                         elif day105.get()=="3":
                                 schedule.every().wednesday.at(time105.get()).do(job105)
                         elif day105.get()=="4":
                                 schedule.every().thursday.at(time105.get()).do(job105)
                         elif day105.get()=="5":
                                 schedule.every().friday.at(time105.get()).do(job105)
                         elif day105.get()=="6":
                                 schedule.every().saturday.at(time105.get()).do(job105)
                         elif day105.get()=="7":
                                 schedule.every().sunday.at(time105.get()).do(job105)

                         while True:
                              schedule.run_pending()
                              if day106.get()=="1":
                                      schedule.every().monday.at(time106.get()).do(job106)
                              elif day106.get()=="2":
                                      schedule.every().tuesday.at(time106.get()).do(job106)
                              elif day106.get()=="3":
                                      schedule.every().wednesday.at(time106.get()).do(job106)
                              elif day106.get()=="4":
                                      schedule.every().thursday.at(time106.get()).do(job106)
                              elif day106.get()=="5":
                                      schedule.every().friday.at(time106.get()).do(job106)
                              elif day106.get()=="6":
                                      schedule.every().saturday.at(time106.get()).do(job106)
                              elif day106.get()=="7":
                                      schedule.every().sunday.at(time106.get()).do(job106)

                              while True:
                                   schedule.run_pending()
                                   if day107.get()=="1":
                                           schedule.every().monday.at(time107.get()).do(job107)
                                   elif day107.get()=="2":
                                           schedule.every().tuesday.at(time107.get()).do(job107)
                                   elif day107.get()=="3":
                                           schedule.every().wednesday.at(time107.get()).do(job107)
                                   elif day107.get()=="4":
                                           schedule.every().thursday.at(time107.get()).do(job107)
                                   elif day107.get()=="5":
                                           schedule.every().friday.at(time107.get()).do(job107)
                                   elif day107.get()=="6":
                                           schedule.every().saturday.at(time107.get()).do(job107)
                                   elif day107.get()=="7":
                                           schedule.every().sunday.at(time107.get()).do(job107)

                                   while True:
                                        schedule.run_pending()
                                        if day108.get()=="1":
                                                schedule.every().monday.at(time108.get()).do(job108)
                                        elif day108.get()=="2":
                                                schedule.every().tuesday.at(time108.get()).do(job108)
                                        elif day108.get()=="3":
                                                schedule.every().wednesday.at(time108.get()).do(job108)
                                        elif day108.get()=="4":
                                                schedule.every().thursday.at(time108.get()).do(job108)
                                        elif day108.get()=="5":
                                                schedule.every().friday.at(time108.get()).do(job108)
                                        elif day108.get()=="6":
                                                schedule.every().saturday.at(time108.get()).do(job108)
                                        elif day108.get()=="7":
                                                schedule.every().sunday.at(time108.get()).do(job108)

                                        while True:
                                             schedule.run_pending()
                                             if day109.get()=="1":
                                                     schedule.every().monday.at(time109.get()).do(job109)
                                             elif day109.get()=="2":
                                                     schedule.every().tuesday.at(time109.get()).do(job109)
                                             elif day109.get()=="3":
                                                     schedule.every().wednesday.at(time109.get()).do(job109)
                                             elif day109.get()=="4":
                                                     schedule.every().thursday.at(time109.get()).do(job109)
                                             elif day109.get()=="5":
                                                     schedule.every().friday.at(time109.get()).do(job109)
                                             elif day109.get()=="6":
                                                     schedule.every().saturday.at(time109.get()).do(job109)
                                             elif day109.get()=="7":
                                                     schedule.every().sunday.at(time109.get()).do(job109)

                                             while True:
                                                  schedule.run_pending()
                                                  if day110.get()=="1":
                                                          schedule.every().monday.at(time110.get()).do(job110)
                                                  elif day110.get()=="2":
                                                          schedule.every().tuesday.at(time110.get()).do(job110)
                                                  elif day110.get()=="3":
                                                          schedule.every().wednesday.at(time110.get()).do(job110)
                                                  elif day110.get()=="4":
                                                          schedule.every().thursday.at(time110.get()).do(job110)
                                                  elif day110.get()=="5":
                                                          schedule.every().friday.at(time110.get()).do(job110)
                                                  elif day110.get()=="6":
                                                          schedule.every().saturday.at(time110.get()).do(job110)
                                                  elif day110.get()=="7":
                                                          schedule.every().sunday.at(time110.get()).do(job110)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day111.get()=="1":
                                                               schedule.every().monday.at(time111.get()).do(job111)
                                                       elif day111.get()=="2":
                                                               schedule.every().tuesday.at(time111.get()).do(job111)
                                                       elif day111.get()=="3":
                                                               schedule.every().wednesday.at(time111.get()).do(job111)
                                                       elif day111.get()=="4":
                                                               schedule.every().thursday.at(time111.get()).do(job111)
                                                       elif day111.get()=="5":
                                                               schedule.every().friday.at(time111.get()).do(job111)
                                                       elif day111.get()=="6":
                                                               schedule.every().saturday.at(time111.get()).do(job111)
                                                       elif day111.get()=="7":
                                                               schedule.every().sunday.at(time111.get()).do(job111)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day112.get()=="1":
                                                                    schedule.every().monday.at(time112.get()).do(job112)
                                                            elif day112.get()=="2":
                                                                    schedule.every().tuesday.at(time112.get()).do(job112)
                                                            elif day112.get()=="3":
                                                                    schedule.every().wednesday.at(time112.get()).do(job112)
                                                            elif day112.get()=="4":
                                                                    schedule.every().thursday.at(time112.get()).do(job112)
                                                            elif day112.get()=="5":
                                                                    schedule.every().friday.at(time112.get()).do(job112)
                                                            elif day112.get()=="6":
                                                                    schedule.every().saturday.at(time112.get()).do(job112)
                                                            elif day112.get()=="7":
                                                                    schedule.every().sunday.at(time112.get()).do(job112)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day113.get()=="1":
                                                                         schedule.every().monday.at(time113.get()).do(job113)
                                                                 elif day113.get()=="2":
                                                                         schedule.every().tuesday.at(time113.get()).do(job113)
                                                                 elif day113.get()=="3":
                                                                         schedule.every().wednesday.at(time113.get()).do(job113)
                                                                 elif day113.get()=="4":
                                                                         schedule.every().thursday.at(time113.get()).do(job113)
                                                                 elif day113.get()=="5":
                                                                         schedule.every().friday.at(time113.get()).do(job113)
                                                                 elif day113.get()=="6":
                                                                         schedule.every().saturday.at(time113.get()).do(job113)
                                                                 elif day113.get()=="7":
                                                                         schedule.every().sunday.at(time113.get()).do(job113)

                                                                 while True:
                                                                      schedule.run_pending()        
                                                                      if day114.get()=="1":
                                                                              schedule.every().monday.at(time114.get()).do(job114)
                                                                      elif day114.get()=="2":
                                                                              schedule.every().tuesday.at(time114.get()).do(job114)
                                                                      elif day114.get()=="3":
                                                                              schedule.every().wednesday.at(time114.get()).do(job114)
                                                                      elif day114.get()=="4":
                                                                              schedule.every().thursday.at(time114.get()).do(job114)
                                                                      elif day114.get()=="5":
                                                                              schedule.every().friday.at(time114.get()).do(job114)
                                                                      elif day114.get()=="6":
                                                                              schedule.every().saturday.at(time114.get()).do(job114)
                                                                      elif day114.get()=="7":
                                                                              schedule.every().sunday.at(time114.get()).do(job114)

                                                                      while True:
                                                                           schedule.run_pending()
                                                                           if day115.get()=="1":
                                                                                   schedule.every().monday.at(time115.get()).do(job115)
                                                                           elif day115.get()=="2":
                                                                                   schedule.every().tuesday.at(time115.get()).do(job115)
                                                                           elif day115.get()=="3":
                                                                                   schedule.every().wednesday.at(time115.get()).do(job115)
                                                                           elif day115.get()=="4":
                                                                                   schedule.every().thursday.at(time115.get()).do(job115)
                                                                           elif day115.get()=="5":
                                                                                   schedule.every().friday.at(time115.get()).do(job115)
                                                                           elif day115.get()=="6":
                                                                                   schedule.every().saturday.at(time115.get()).do(job115)
                                                                           elif day115.get()=="7":
                                                                                   schedule.every().sunday.at(time115.get()).do(job115)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day116.get()=="1":
                                                                                        schedule.every().monday.at(time116.get()).do(job116)
                                                                                elif day116.get()=="2":
                                                                                        schedule.every().tuesday.at(time116.get()).do(job116)
                                                                                elif day116.get()=="3":
                                                                                        schedule.every().wednesday.at(time116.get()).do(job116)
                                                                                elif day116.get()=="4":
                                                                                        schedule.every().thursday.at(time116.get()).do(job116)
                                                                                elif day116.get()=="5":
                                                                                        schedule.every().friday.at(time116.get()).do(job116)
                                                                                elif day116.get()=="6":
                                                                                        schedule.every().saturday.at(time116.get()).do(job116)
                                                                                elif day116.get()=="7":
                                                                                        schedule.every().sunday.at(time116.get()).do(job116)

                                                                                while True:
                                                                                     schedule.run_pending()
                                                                                     if day117.get()=="1":
                                                                                             schedule.every().monday.at(time117.get()).do(job117)
                                                                                     elif day117.get()=="2":
                                                                                             schedule.every().tuesday.at(time117.get()).do(job117)
                                                                                     elif day117.get()=="3":
                                                                                             schedule.every().wednesday.at(time117.get()).do(job117)
                                                                                     elif day117.get()=="4":
                                                                                             schedule.every().thursday.at(time117.get()).do(job117)
                                                                                     elif day117.get()=="5":
                                                                                             schedule.every().friday.at(time117.get()).do(job117)
                                                                                     elif day117.get()=="6":
                                                                                             schedule.every().saturday.at(time117.get()).do(job117)
                                                                                     elif day117.get()=="7":
                                                                                             schedule.every().sunday.at(time117.get()).do(job117)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day118.get()=="1":
                                                                                                  schedule.every().monday.at(time118.get()).do(job118)
                                                                                          elif day118.get()=="2":
                                                                                                  schedule.every().tuesday.at(time118.get()).do(job118)
                                                                                          elif day118.get()=="3":
                                                                                                  schedule.every().wednesday.at(time118.get()).do(job118)
                                                                                          elif day118.get()=="4":
                                                                                                  schedule.every().thursday.at(time118.get()).do(job118)
                                                                                          elif day118.get()=="5":
                                                                                                  schedule.every().friday.at(time118.get()).do(job118)
                                                                                          elif day118.get()=="6":
                                                                                                  schedule.every().saturday.at(time118.get()).do(job118)
                                                                                          elif day118.get()=="7":
                                                                                                  schedule.every().sunday.at(time118.get()).do(job118)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day119.get()=="1":
                                                                                                       schedule.every().monday.at(time119.get()).do(job119)
                                                                                               elif day119.get()=="2":
                                                                                                       schedule.every().tuesday.at(time119.get()).do(job119)
                                                                                               elif day119.get()=="3":
                                                                                                       schedule.every().wednesday.at(time119.get()).do(job119)
                                                                                               elif day119.get()=="4":
                                                                                                       schedule.every().thursday.at(time119.get()).do(job119)
                                                                                               elif day119.get()=="5":
                                                                                                       schedule.every().friday.at(time119.get()).do(job119)
                                                                                               elif day119.get()=="6":
                                                                                                       schedule.every().saturday.at(time119.get()).do(job119)
                                                                                               elif day119.get()=="7":
                                                                                                       schedule.every().sunday.at(time119.get()).do(job119)

                                                                                               while True:
                                                                                                    schedule.run_pending()
                                                                                                    if day120.get()=="1":
                                                                                                            schedule.every().monday.at(time120.get()).do(job120)
                                                                                                    elif day120.get()=="2":
                                                                                                            schedule.every().tuesday.at(time120.get()).do(job120)
                                                                                                    elif day120.get()=="3":
                                                                                                            schedule.every().wednesday.at(time120.get()).do(job120)
                                                                                                    elif day120.get()=="4":
                                                                                                            schedule.every().thursday.at(time120.get()).do(job120)
                                                                                                    elif day120.get()=="5":
                                                                                                            schedule.every().friday.at(time120.get()).do(job120)
                                                                                                    elif day120.get()=="6":
                                                                                                            schedule.every().saturday.at(time120.get()).do(job120)
                                                                                                    elif day120.get()=="7":
                                                                                                            schedule.every().sunday.at(time120.get()).do(job120)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         (job406())




def job404():
     
     if day81.get()=="1":
             schedule.every().monday.at(time81.get()).do(job81)
     elif day81.get()=="2":
             schedule.every().tuesday.at(time81.get()).do(job81)                
     elif day81.get()=="3":
             schedule.every().wednesday.at(time81.get()).do(job81)
     elif day81.get()=="4":
             schedule.every().thursday.at(time81.get()).do(job81)
     elif day81.get()=="5":
             schedule.every().friday.at(time81.get()).do(job81)
     elif day81.get()=="6":
             schedule.every().saturday.at(time81.get()).do(job81)
     elif day81.get()=="7":
             schedule.every().sunday.at(time81.get()).do(job81)

     while True:
          schedule.run_pending()
          if day82.get()=="1":
                  schedule.every().monday.at(time82.get()).do(job82)
          elif day82.get()=="2":
                  schedule.every().tuesday.at(time82.get()).do(job82)
          elif day82.get()=="3":
                  schedule.every().wednesday.at(time82.get()).do(job82)
          elif day82.get()=="4":
                  schedule.every().thursday.at(time82.get()).do(job82)
          elif day82.get()=="5":
                  schedule.every().friday.at(time82.get()).do(job82)
          elif day82.get()=="6":
                  schedule.every().saturday.at(time82.get()).do(job82)
          elif day82.get()=="7":
                  schedule.every().sunday.at(time82.get()).do(job82)

          while True:
               schedule.run_pending()
               if day83.get()=="1":
                       schedule.every().monday.at(time83.get()).do(job83)
               elif day83.get()=="2":
                       schedule.every().tuesday.at(time83.get()).do(job83)
               elif day83.get()=="3":
                       schedule.every().wednesday.at(time83.get()).do(job83)
               elif day83.get()=="4":
                       schedule.every().thursday.at(time83.get()).do(job83)
               elif day83.get()=="5":
                       schedule.every().friday.at(time83.get()).do(job83)
               elif day83.get()=="6":
                       schedule.every().saturday.at(time83.get()).do(job83)
               elif day83.get()=="7":
                       schedule.every().sunday.at(time83.get()).do(job83)

               while True:
                    schedule.run_pending()
                    if day84.get()=="1":
                            schedule.every().monday.at(time84.get()).do(job84)
                    elif day84.get()=="2":
                            schedule.every().tuesday.at(time84.get()).do(job84)
                    elif day84.get()=="3":
                            schedule.every().wednesday.at(time84.get()).do(job84)
                    elif day84.get()=="4":
                            schedule.every().thursday.at(time84.get()).do(job84)
                    elif day84.get()=="5":
                            schedule.every().friday.at(time84.get()).do(job84)
                    elif day84.get()=="6":
                            schedule.every().saturday.at(time84.get()).do(job84)
                    elif day84.get()=="7":
                            schedule.every().sunday.at(time84.get()).do(job84)

                    while True:
                         schedule.run_pending()
                         if day85.get()=="1":
                                 schedule.every().monday.at(time85.get()).do(job85)
                         elif day85.get()=="2":
                                 schedule.every().tuesday.at(time85.get()).do(job85)
                         elif day85.get()=="3":
                                 schedule.every().wednesday.at(time85.get()).do(job85)
                         elif day85.get()=="4":
                                 schedule.every().thursday.at(time85.get()).do(job85)
                         elif day85.get()=="5":
                                 schedule.every().friday.at(time85.get()).do(job85)
                         elif day85.get()=="6":
                                 schedule.every().saturday.at(time85.get()).do(job85)
                         elif day85.get()=="7":
                                 schedule.every().sunday.at(time85.get()).do(job85)

                         while True:
                              schedule.run_pending()
                              if day86.get()=="1":
                                      schedule.every().monday.at(time86.get()).do(job86)
                              elif day86.get()=="2":
                                      schedule.every().tuesday.at(time86.get()).do(job86)
                              elif day86.get()=="3":
                                      schedule.every().wednesday.at(time86.get()).do(job86)
                              elif day86.get()=="4":
                                      schedule.every().thursday.at(time86.get()).do(job86)
                              elif day86.get()=="5":
                                      schedule.every().friday.at(time86.get()).do(job86)
                              elif day86.get()=="6":
                                      schedule.every().saturday.at(time86.get()).do(job86)
                              elif day86.get()=="7":
                                      schedule.every().sunday.at(time86.get()).do(job86)

                              while True:
                                   schedule.run_pending()
                                   if day87.get()=="1":
                                           schedule.every().monday.at(time87.get()).do(job87)
                                   elif day87.get()=="2":
                                           schedule.every().tuesday.at(time87.get()).do(job87)
                                   elif day87.get()=="3":
                                           schedule.every().wednesday.at(time87.get()).do(job87)
                                   elif day87.get()=="4":
                                           schedule.every().thursday.at(time87.get()).do(job87)
                                   elif day87.get()=="5":
                                           schedule.every().friday.at(time87.get()).do(job87)
                                   elif day87.get()=="6":
                                           schedule.every().saturday.at(time87.get()).do(job87)
                                   elif day87.get()=="7":
                                           schedule.every().sunday.at(time87.get()).do(job87)

                                   while True:
                                        schedule.run_pending()
                                        if day88.get()=="1":
                                                schedule.every().monday.at(time88.get()).do(job88)
                                        elif day88.get()=="2":
                                                schedule.every().tuesday.at(time88.get()).do(job88)
                                        elif day88.get()=="3":
                                                schedule.every().wednesday.at(time88.get()).do(job88)
                                        elif day88.get()=="4":
                                                schedule.every().thursday.at(time88.get()).do(job88)
                                        elif day88.get()=="5":
                                                schedule.every().friday.at(time88.get()).do(job88)
                                        elif day88.get()=="6":
                                                schedule.every().saturday.at(time88.get()).do(job88)
                                        elif day88.get()=="7":
                                                schedule.every().sunday.at(time88.get()).do(job88)

                                        while True:
                                             schedule.run_pending()
                                             if day89.get()=="1":
                                                     schedule.every().monday.at(time89.get()).do(job89)
                                             elif day89.get()=="2":
                                                     schedule.every().tuesday.at(time89.get()).do(job89)
                                             elif day89.get()=="3":
                                                     schedule.every().wednesday.at(time89.get()).do(job89)
                                             elif day89.get()=="4":
                                                     schedule.every().thursday.at(time89.get()).do(job89)
                                             elif day89.get()=="5":
                                                     schedule.every().friday.at(time89.get()).do(job89)
                                             elif day89.get()=="6":
                                                     schedule.every().saturday.at(time89.get()).do(job89)
                                             elif day89.get()=="7":
                                                     schedule.every().sunday.at(time89.get()).do(job89)

                                             while True:
                                                  schedule.run_pending()
                                                  if day90.get()=="1":
                                                          schedule.every().monday.at(time90.get()).do(job90)
                                                  elif day90.get()=="2":
                                                          schedule.every().tuesday.at(time90.get()).do(job90)
                                                  elif day90.get()=="3":
                                                          schedule.every().wednesday.at(time90.get()).do(job90)
                                                  elif day90.get()=="4":
                                                          schedule.every().thursday.at(time90.get()).do(job90)
                                                  elif day90.get()=="5":
                                                          schedule.every().friday.at(time90.get()).do(job90)
                                                  elif day90.get()=="6":
                                                          schedule.every().saturday.at(time90.get()).do(job90)
                                                  elif day90.get()=="7":
                                                          schedule.every().sunday.at(time90.get()).do(job90)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day91.get()=="1":
                                                               schedule.every().monday.at(time91.get()).do(job91)
                                                       elif day91.get()=="2":
                                                               schedule.every().tuesday.at(time91.get()).do(job91)
                                                       elif day91.get()=="3":
                                                               schedule.every().wednesday.at(time91.get()).do(job91)
                                                       elif day91.get()=="4":
                                                               schedule.every().thursday.at(time91.get()).do(job91)
                                                       elif day91.get()=="5":
                                                               schedule.every().friday.at(time91.get()).do(job91)
                                                       elif day91.get()=="6":
                                                               schedule.every().saturday.at(time91.get()).do(job91)
                                                       elif day91.get()=="7":
                                                               schedule.every().sunday.at(time91.get()).do(job91)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day92.get()=="1":
                                                                    schedule.every().monday.at(time92.get()).do(job92)
                                                            elif day92.get()=="2":
                                                                    schedule.every().tuesday.at(time92.get()).do(job92)
                                                            elif day92.get()=="3":
                                                                    schedule.every().wednesday.at(time92.get()).do(job92)
                                                            elif day92.get()=="4":
                                                                    schedule.every().thursday.at(time92.get()).do(job92)
                                                            elif day92.get()=="5":
                                                                    schedule.every().friday.at(time92.get()).do(job92)
                                                            elif day92.get()=="6":
                                                                    schedule.every().saturday.at(time92.get()).do(job92)
                                                            elif day92.get()=="7":
                                                                    schedule.every().sunday.at(time92.get()).do(job92)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day93.get()=="1":
                                                                         schedule.every().monday.at(time93.get()).do(job93)
                                                                 elif day93.get()=="2":
                                                                         schedule.every().tuesday.at(time93.get()).do(job93)
                                                                 elif day93.get()=="3":
                                                                         schedule.every().wednesday.at(time93.get()).do(job93)
                                                                 elif day93.get()=="4":
                                                                         schedule.every().thursday.at(time93.get()).do(job93)
                                                                 elif day93.get()=="5":
                                                                         schedule.every().friday.at(time93.get()).do(job93)
                                                                 elif day93.get()=="6":
                                                                         schedule.every().saturday.at(time93.get()).do(job93)
                                                                 elif day93.get()=="7":
                                                                         schedule.every().sunday.at(time93.get()).do(job93)

                                                                 while True:
                                                                      schedule.run_pending()
                                                                      if day94.get()=="1":
                                                                              schedule.every().monday.at(time94.get()).do(job94)
                                                                      elif day94.get()=="2":
                                                                              schedule.every().tuesday.at(time94.get()).do(job94)
                                                                      elif day94.get()=="3":
                                                                              schedule.every().wednesday.at(time94.get()).do(job94)
                                                                      elif day94.get()=="4":
                                                                              schedule.every().thursday.at(time94.get()).do(job94)
                                                                      elif day94.get()=="5":
                                                                              schedule.every().friday.at(time94.get()).do(job94)
                                                                      elif day94.get()=="6":
                                                                              schedule.every().saturday.at(time94.get()).do(job94)
                                                                      elif day94.get()=="7":
                                                                              schedule.every().sunday.at(time94.get()).do(job94)

                                                                      while True:
                                                                           schedule.run_pending()
                                                                           if day95.get()=="1":
                                                                                   schedule.every().monday.at(time95.get()).do(job95)
                                                                           elif day95.get()=="2":
                                                                                   schedule.every().tuesday.at(time95.get()).do(job95)
                                                                           elif day95.get()=="3":
                                                                                   schedule.every().wednesday.at(time95.get()).do(job95)
                                                                           elif day95.get()=="4":
                                                                                   schedule.every().thursday.at(time95.get()).do(job95)
                                                                           elif day95.get()=="5":
                                                                                   schedule.every().friday.at(time95.get()).do(job95)
                                                                           elif day95.get()=="6":
                                                                                   schedule.every().saturday.at(time95.get()).do(job95)
                                                                           elif day95.get()=="7":
                                                                                   schedule.every().sunday.at(time95.get()).do(job95)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day96.get()=="1":
                                                                                        schedule.every().monday.at(time96.get()).do(job96)
                                                                                elif day96.get()=="2":
                                                                                        schedule.every().tuesday.at(time96.get()).do(job96)
                                                                                elif day96.get()=="3":
                                                                                        schedule.every().wednesday.at(time96.get()).do(job96)
                                                                                elif day96.get()=="4":
                                                                                        schedule.every().thursday.at(time96.get()).do(job96)
                                                                                elif day96.get()=="5":
                                                                                        schedule.every().friday.at(time96.get()).do(job96)
                                                                                elif day96.get()=="6":
                                                                                        schedule.every().saturday.at(time96.get()).do(job96)
                                                                                elif day96.get()=="7":
                                                                                        schedule.every().sunday.at(time96.get()).do(job96)

                                                                                while True:
                                                                                     schedule.run_pending()
                                                                                     if day97.get()=="1":
                                                                                             schedule.every().monday.at(time97.get()).do(job97)
                                                                                     elif day97.get()=="2":
                                                                                             schedule.every().tuesday.at(time97.get()).do(job97)
                                                                                     elif day97.get()=="3":
                                                                                             schedule.every().wednesday.at(time97.get()).do(job97)
                                                                                     elif day97.get()=="4":
                                                                                             schedule.every().thursday.at(time97.get()).do(job97)
                                                                                     elif day97.get()=="5":
                                                                                             schedule.every().friday.at(time97.get()).do(job97)
                                                                                     elif day97.get()=="6":
                                                                                             schedule.every().saturday.at(time97.get()).do(job97)
                                                                                     elif day97.get()=="7":
                                                                                             schedule.every().sunday.at(time97.get()).do(job97)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day98.get()=="1":
                                                                                                  schedule.every().monday.at(time98.get()).do(job98)
                                                                                          elif day98.get()=="2":
                                                                                                  schedule.every().tuesday.at(time98.get()).do(job98)
                                                                                          elif day98.get()=="3":
                                                                                                  schedule.every().wednesday.at(time98.get()).do(job98)
                                                                                          elif day98.get()=="4":
                                                                                                  schedule.every().thursday.at(time98.get()).do(job98)
                                                                                          elif day98.get()=="5":
                                                                                                  schedule.every().friday.at(time98.get()).do(job98)
                                                                                          elif day98.get()=="6":
                                                                                                  schedule.every().saturday.at(time98.get()).do(job98)
                                                                                          elif day98.get()=="7":
                                                                                                  schedule.every().sunday.at(time98.get()).do(job98)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day99.get()=="1":
                                                                                                       schedule.every().monday.at(time99.get()).do(job99)
                                                                                               elif day99.get()=="2":
                                                                                                       schedule.every().tuesday.at(time99.get()).do(job99)
                                                                                               elif day99.get()=="3":
                                                                                                       schedule.every().wednesday.at(time99.get()).do(job99)
                                                                                               elif day99.get()=="4":
                                                                                                       schedule.every().thursday.at(time99.get()).do(job99)
                                                                                               elif day99.get()=="5":
                                                                                                       schedule.every().friday.at(time99.get()).do(job99)
                                                                                               elif day99.get()=="6":
                                                                                                       schedule.every().saturday.at(time99.get()).do(job99)
                                                                                               elif day99.get()=="7":
                                                                                                       schedule.every().sunday.at(time99.get()).do(job99)

                                                                                               while True:
                                                                                                    schedule.run_pending()
                                                                                                    if day100.get()=="1":
                                                                                                            schedule.every().monday.at(time100.get()).do(job100)
                                                                                                    elif day100.get()=="2":
                                                                                                            schedule.every().tuesday.at(time100.get()).do(job100)
                                                                                                    elif day100.get()=="3":
                                                                                                            schedule.every().wednesday.at(time100.get()).do(job100)
                                                                                                    elif day100.get()=="4":
                                                                                                            schedule.every().thursday.at(time100.get()).do(job100)
                                                                                                    elif day100.get()=="5":
                                                                                                            schedule.every().friday.at(time100.get()).do(job100)
                                                                                                    elif day100.get()=="6":
                                                                                                            schedule.every().saturday.at(time100.get()).do(job100)
                                                                                                    elif day100.get()=="7":
                                                                                                            schedule.every().sunday.at(time100.get()).do(job100)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         (job405())





    
def job403():
     
     if day61.get()=="1":
             schedule.every().monday.at(time61.get()).do(job61)
     elif day61.get()=="2":
             schedule.every().tuesday.at(time61.get()).do(job61)
     elif day61.get()=="3":
             schedule.every().wednesday.at(time61.get()).do(job61)
     elif day61.get()=="4":
             schedule.every().thursday.at(time61.get()).do(job61)
     elif day61.get()=="5":
             schedule.every().friday.at(time61.get()).do(job61)
     elif day61.get()=="6":
             schedule.every().saturday.at(time61.get()).do(job61)
     elif day61.get()=="7":
             schedule.every().sunday.at(time61.get()).do(job61)

     while True:
          schedule.run_pending()
          if day62.get()=="1":
                  schedule.every().monday.at(time62.get()).do(job62)
          elif day62.get()=="2":
                  schedule.every().tuesday.at(time62.get()).do(job62)
          elif day62.get()=="3":
                  schedule.every().wednesday.at(time62.get()).do(job62)
          elif day62.get()=="4":
                  schedule.every().thursday.at(time62.get()).do(job62)
          elif day62.get()=="5":
                  schedule.every().friday.at(time62.get()).do(job62)
          elif day62.get()=="6":
                  schedule.every().saturday.at(time62.get()).do(job62)
          elif day62.get()=="7":
                  schedule.every().sunday.at(time62.get()).do(job62)

          while True:
               schedule.run_pending()
               if day63.get()=="1":
                       schedule.every().monday.at(time63.get()).do(job63)
               elif day63.get()=="2":
                       schedule.every().tuesday.at(time63.get()).do(job63)
               elif day63.get()=="3":
                       schedule.every().wednesday.at(time63.get()).do(job63)
               elif day63.get()=="4":
                       schedule.every().thursday.at(time63.get()).do(job63)
               elif day63.get()=="5":
                       schedule.every().friday.at(time63.get()).do(job63)
               elif day63.get()=="6":
                       schedule.every().saturday.at(time63.get()).do(job63)
               elif day63.get()=="7":
                       schedule.every().sunday.at(time63.get()).do(job63)

               while True:
                    schedule.run_pending()
                    if day64.get()=="1":
                            schedule.every().monday.at(time64.get()).do(job64)
                    elif day64.get()=="2":
                            schedule.every().tuesday.at(time64.get()).do(job64)
                    elif day64.get()=="3":
                            schedule.every().wednesday.at(time64.get()).do(job64)
                    elif day64.get()=="4":
                            schedule.every().thursday.at(time64.get()).do(job64)
                    elif day64.get()=="5":
                            schedule.every().friday.at(time64.get()).do(job64)
                    elif day64.get()=="6":
                            schedule.every().saturday.at(time64.get()).do(job64)
                    elif day64.get()=="7":
                            schedule.every().sunday.at(time64.get()).do(job64)

                    while True:
                         schedule.run_pending()
                         if day65.get()=="1":
                                 schedule.every().monday.at(time65.get()).do(job65)
                         elif day65.get()=="2":
                                 schedule.every().tuesday.at(time65.get()).do(job65)
                         elif day65.get()=="3":
                                 schedule.every().wednesday.at(time65.get()).do(job65)
                         elif day65.get()=="4":
                                 schedule.every().thursday.at(time65.get()).do(job65)
                         elif day65.get()=="5":
                                 schedule.every().friday.at(time65.get()).do(job65)
                         elif day65.get()=="6":
                                 schedule.every().saturday.at(time65.get()).do(job65)
                         elif day65.get()=="7":
                                 schedule.every().sunday.at(time65.get()).do(job65)

                         while True:
                              schedule.run_pending()
                              if day66.get()=="1":
                                      schedule.every().monday.at(time66.get()).do(job66)
                              elif day66.get()=="2":
                                      schedule.every().tuesday.at(time66.get()).do(job66)
                              elif day66.get()=="3":
                                      schedule.every().wednesday.at(time66.get()).do(job66)
                              elif day66.get()=="4":
                                      schedule.every().thursday.at(time66.get()).do(job66)
                              elif day66.get()=="5":
                                      schedule.every().friday.at(time66.get()).do(job66)
                              elif day66.get()=="6":
                                      schedule.every().saturday.at(time66.get()).do(job66)
                              elif day66.get()=="7":
                                      schedule.every().sunday.at(time66.get()).do(job66)

                              while True:
                                   schedule.run_pending()
                                   if day67.get()=="1":
                                           schedule.every().monday.at(time67.get()).do(job67)
                                   elif day67.get()=="2":
                                           schedule.every().tuesday.at(time67.get()).do(job67)
                                   elif day67.get()=="3":
                                           schedule.every().wednesday.at(time67.get()).do(job67)
                                   elif day67.get()=="4":
                                           schedule.every().thursday.at(time67.get()).do(job67)
                                   elif day67.get()=="5":
                                           schedule.every().friday.at(time67.get()).do(job67)
                                   elif day67.get()=="6":
                                           schedule.every().saturday.at(time67.get()).do(job67)
                                   elif day67.get()=="7":
                                           schedule.every().sunday.at(time67.get()).do(job67)

                                   while True:
                                        schedule.run_pending()
                                        if day68.get()=="1":
                                                schedule.every().monday.at(time68.get()).do(job68)
                                        elif day68.get()=="2":
                                                schedule.every().tuesday.at(time68.get()).do(job68)
                                        elif day68.get()=="3":
                                                schedule.every().wednesday.at(time68.get()).do(job68)
                                        elif day68.get()=="4":
                                                schedule.every().thursday.at(time68.get()).do(job68)
                                        elif day68.get()=="5":
                                                schedule.every().friday.at(time68.get()).do(job68)
                                        elif day68.get()=="6":
                                                schedule.every().saturday.at(time68.get()).do(job68)
                                        elif day68.get()=="7":
                                                schedule.every().sunday.at(time68.get()).do(job68)

                                        while True:
                                             schedule.run_pending()
                                             if day69.get()=="1":
                                                     schedule.every().monday.at(time69.get()).do(job69)
                                             elif day69.get()=="2":
                                                     schedule.every().tuesday.at(time69.get()).do(job69)
                                             elif day69.get()=="3":
                                                     schedule.every().wednesday.at(time69.get()).do(job69)
                                             elif day69.get()=="4":
                                                     schedule.every().thursday.at(time69.get()).do(job69)
                                             elif day69.get()=="5":
                                                     schedule.every().friday.at(time69.get()).do(job69)
                                             elif day69.get()=="6":
                                                     schedule.every().saturday.at(time69.get()).do(job69)
                                             elif day69.get()=="7":
                                                     schedule.every().sunday.at(time69.get()).do(job69)

                                             while True:
                                                  schedule.run_pending()
                                                  if day70.get()=="1":
                                                          schedule.every().monday.at(time70.get()).do(job70)
                                                  elif day70.get()=="2":
                                                          schedule.every().tuesday.at(time70.get()).do(job70)
                                                  elif day70.get()=="3":
                                                          schedule.every().wednesday.at(time70.get()).do(job70)
                                                  elif day70.get()=="4":
                                                          schedule.every().thursday.at(time70.get()).do(job70)
                                                  elif day70.get()=="5":
                                                          schedule.every().friday.at(time70.get()).do(job70)
                                                  elif day70.get()=="6":
                                                          schedule.every().saturday.at(time70.get()).do(job70)
                                                  elif day70.get()=="7":
                                                          schedule.every().sunday.at(time70.get()).do(job70)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day71.get()=="1":
                                                               schedule.every().monday.at(time71.get()).do(job71)
                                                       elif day71.get()=="2":
                                                               schedule.every().tuesday.at(time71.get()).do(job71)
                                                       elif day71.get()=="3":
                                                               schedule.every().wednesday.at(time71.get()).do(job71)
                                                       elif day71.get()=="4":
                                                               schedule.every().thursday.at(time71.get()).do(job71)
                                                       elif day71.get()=="5":
                                                               schedule.every().friday.at(time71.get()).do(job71)
                                                       elif day71.get()=="6":
                                                               schedule.every().saturday.at(time71.get()).do(job71)
                                                       elif day71.get()=="7":
                                                               schedule.every().sunday.at(time71.get()).do(job71)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day72.get()=="1":
                                                                    schedule.every().monday.at(time72.get()).do(job72)
                                                            elif day72.get()=="2":
                                                                    schedule.every().tuesday.at(time72.get()).do(job72)
                                                            elif day72.get()=="3":
                                                                    schedule.every().wednesday.at(time72.get()).do(job72)
                                                            elif day72.get()=="4":
                                                                    schedule.every().thursday.at(time72.get()).do(job72)
                                                            elif day72.get()=="5":
                                                                    schedule.every().friday.at(time72.get()).do(job72)
                                                            elif day72.get()=="6":
                                                                    schedule.every().saturday.at(time72.get()).do(job72)
                                                            elif day72.get()=="7":
                                                                    schedule.every().sunday.at(time72.get()).do(job72)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day73.get()=="1":
                                                                         schedule.every().monday.at(time73.get()).do(job73)
                                                                 elif day73.get()=="2":
                                                                         schedule.every().tuesday.at(time73.get()).do(job73)
                                                                 elif day73.get()=="3":
                                                                         schedule.every().wednesday.at(time73.get()).do(job73)
                                                                 elif day73.get()=="4":
                                                                         schedule.every().thursday.at(time73.get()).do(job73)
                                                                 elif day73.get()=="5":
                                                                         schedule.every().friday.at(time73.get()).do(job73)
                                                                 elif day73.get()=="6":
                                                                         schedule.every().saturday.at(time73.get()).do(job73)
                                                                 elif day73.get()=="7":
                                                                         schedule.every().sunday.at(time73.get()).do(job73)

                                                                 while True:
                                                                      schedule.run_pending()
                                                                      if day74.get()=="1":
                                                                              schedule.every().monday.at(time74.get()).do(job74)
                                                                      elif day74.get()=="2":
                                                                              schedule.every().tuesday.at(time74.get()).do(job74)
                                                                      elif day74.get()=="3":
                                                                              schedule.every().wednesday.at(time74.get()).do(job74)
                                                                      elif day74.get()=="4":
                                                                              schedule.every().thursday.at(time74.get()).do(job74)
                                                                      elif day74.get()=="5":
                                                                              schedule.every().friday.at(time74.get()).do(job74)
                                                                      elif day74.get()=="6":
                                                                              schedule.every().saturday.at(time74.get()).do(job74)
                                                                      elif day74.get()=="7":
                                                                              schedule.every().sunday.at(time74.get()).do(job74)

                                                                      while True:
                                                                           schedule.run_pending()
                                                                           if day75.get()=="1":
                                                                                   schedule.every().monday.at(time75.get()).do(job75)
                                                                           elif day75.get()=="2":
                                                                                   schedule.every().tuesday.at(time75.get()).do(job75)
                                                                           elif day75.get()=="3":
                                                                                   schedule.every().wednesday.at(time75.get()).do(job75)
                                                                           elif day75.get()=="4":
                                                                                   schedule.every().thursday.at(time75.get()).do(job75)
                                                                           elif day75.get()=="5":
                                                                                   schedule.every().friday.at(time75.get()).do(job75)
                                                                           elif day75.get()=="6":
                                                                                   schedule.every().saturday.at(time75.get()).do(job75)
                                                                           elif day75.get()=="7":
                                                                                   schedule.every().sunday.at(time75.get()).do(job75)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day76.get()=="1":
                                                                                        schedule.every().monday.at(time76.get()).do(job76)
                                                                                elif day76.get()=="2":
                                                                                        schedule.every().tuesday.at(time76.get()).do(job76)
                                                                                elif day76.get()=="3":
                                                                                        schedule.every().wednesday.at(time76.get()).do(job76)
                                                                                elif day76.get()=="4":
                                                                                        schedule.every().thursday.at(time76.get()).do(job76)
                                                                                elif day76.get()=="5":
                                                                                        schedule.every().friday.at(time76.get()).do(job76)
                                                                                elif day76.get()=="6":
                                                                                        schedule.every().saturday.at(time76.get()).do(job76)
                                                                                elif day76.get()=="7":
                                                                                        schedule.every().sunday.at(time76.get()).do(job76)

                                                                                while True:
                                                                                     schedule.run_pending()
                                                                                     if day77.get()=="1":
                                                                                             schedule.every().monday.at(time77.get()).do(job77)
                                                                                     elif day77.get()=="2":
                                                                                             schedule.every().tuesday.at(time77.get()).do(job77)
                                                                                     elif day77.get()=="3":
                                                                                             schedule.every().wednesday.at(time77.get()).do(job77)
                                                                                     elif day77.get()=="4":
                                                                                             schedule.every().thursday.at(time77.get()).do(job77)
                                                                                     elif day77.get()=="5":
                                                                                             schedule.every().friday.at(time77.get()).do(job77)
                                                                                     elif day77.get()=="6":
                                                                                             schedule.every().saturday.at(time77.get()).do(job77)
                                                                                     elif day77.get()=="7":
                                                                                             schedule.every().sunday.at(time77.get()).do(job77)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day78.get()=="1":
                                                                                                  schedule.every().monday.at(time78.get()).do(job78)
                                                                                          elif day78.get()=="2":
                                                                                                  schedule.every().tuesday.at(time78.get()).do(job78)
                                                                                          elif day78.get()=="3":
                                                                                                  schedule.every().wednesday.at(time78.get()).do(job78)
                                                                                          elif day78.get()=="4":
                                                                                                  schedule.every().thursday.at(time78.get()).do(job78)
                                                                                          elif day78.get()=="5":
                                                                                                  schedule.every().friday.at(time78.get()).do(job78)
                                                                                          elif day78.get()=="6":
                                                                                                  schedule.every().saturday.at(time78.get()).do(job78)
                                                                                          elif day78.get()=="7":
                                                                                                  schedule.every().sunday.at(time78.get()).do(job78)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day79.get()=="1":
                                                                                                       schedule.every().monday.at(time79.get()).do(job79)
                                                                                               elif day79.get()=="2":
                                                                                                       schedule.every().tuesday.at(time79.get()).do(job79)
                                                                                               elif day79.get()=="3":
                                                                                                       schedule.every().wednesday.at(time79.get()).do(job79)
                                                                                               elif day79.get()=="4":
                                                                                                       schedule.every().thursday.at(time79.get()).do(job79)
                                                                                               elif day79.get()=="5":
                                                                                                       schedule.every().friday.at(time79.get()).do(job79)
                                                                                               elif day79.get()=="6":
                                                                                                       schedule.every().saturday.at(time79.get()).do(job79)
                                                                                               elif day79.get()=="7":
                                                                                                       schedule.every().sunday.at(time79.get()).do(job79)

                                                                                               while True:
                                                                                                    schedule.run_pending()
                                                                                                    if day80.get()=="1":
                                                                                                            schedule.every().monday.at(time80.get()).do(job80)
                                                                                                    elif day80.get()=="2":
                                                                                                            schedule.every().tuesday.at(time80.get()).do(job80)
                                                                                                    elif day80.get()=="3":
                                                                                                            schedule.every().wednesday.at(time80.get()).do(job80)
                                                                                                    elif day80.get()=="4":
                                                                                                            schedule.every().thursday.at(time80.get()).do(job80)
                                                                                                    elif day80.get()=="5":
                                                                                                            schedule.every().friday.at(time80.get()).do(job80)
                                                                                                    elif day80.get()=="6":
                                                                                                            schedule.every().saturday.at(time80.get()).do(job80)
                                                                                                    elif day80.get()=="7":
                                                                                                            schedule.every().sunday.at(time80.get()).do(job80)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         (job404())






    
    
def job402():
     
     if day41.get()=="1":
             schedule.every().monday.at(time41.get()).do(job41)
     elif day41.get()=="2":
             schedule.every().tuesday.at(time41.get()).do(job41)
     elif day41.get()=="3":
             schedule.every().wednesday.at(time41.get()).do(job41)
     elif day41.get()=="4":
             schedule.every().thursday.at(time41.get()).do(job41)
     elif day41.get()=="5":
             schedule.every().friday.at(time41.get()).do(job41)
     elif day41.get()=="6":
             schedule.every().saturday.at(time41.get()).do(job41)
     elif day41.get()=="7":
             schedule.every().sunday.at(time41.get()).do(job41)

     while True:
          schedule.run_pending()
          if day42.get()=="1":
                  schedule.every().monday.at(time42.get()).do(job42)
          elif day42.get()=="2":
                  schedule.every().tuesday.at(time42.get()).do(job42)
          elif day42.get()=="3":
                  schedule.every().wednesday.at(time42.get()).do(job42)
          elif day42.get()=="4":
                  schedule.every().thursday.at(time42.get()).do(job42)
          elif day42.get()=="5":
                  schedule.every().friday.at(time42.get()).do(job42)
          elif day42.get()=="6":
                  schedule.every().saturday.at(time42.get()).do(job42)
          elif day42.get()=="7":
                  schedule.every().sunday.at(time42.get()).do(job42)

          while True:
               schedule.run_pending()
               if day43.get()=="1":
                       schedule.every().monday.at(time43.get()).do(job43)
               elif day43.get()=="2":
                       schedule.every().tuesday.at(time43.get()).do(job43)
               elif day43.get()=="3":
                       schedule.every().wednesday.at(time43.get()).do(job43)
               elif day43.get()=="4":
                       schedule.every().thursday.at(time43.get()).do(job43)
               elif day43.get()=="5":
                       schedule.every().friday.at(time43.get()).do(job43)
               elif day43.get()=="6":
                       schedule.every().saturday.at(time43.get()).do(job43)
               elif day43.get()=="7":
                       schedule.every().sunday.at(time43.get()).do(job43)

               while True:
                    schedule.run_pending()
                    if day44.get()=="1":
                            schedule.every().monday.at(time44.get()).do(job44)
                    elif day44.get()=="2":
                            schedule.every().tuesday.at(time44.get()).do(job44)
                    elif day44.get()=="3":
                            schedule.every().wednesday.at(time44.get()).do(job44)
                    elif day44.get()=="4":
                            schedule.every().thursday.at(time44.get()).do(job44)
                    elif day44.get()=="5":
                            schedule.every().friday.at(time44.get()).do(job44)
                    elif day44.get()=="6":
                            schedule.every().saturday.at(time44.get()).do(job44)
                    elif day44.get()=="7":
                            schedule.every().sunday.at(time44.get()).do(job44)

                    while True:
                         schedule.run_pending()
                         if day45.get()=="1":
                                 schedule.every().monday.at(time45.get()).do(job45)
                         elif day45.get()=="2":
                                 schedule.every().tuesday.at(time45.get()).do(job45)
                         elif day45.get()=="3":
                                 schedule.every().wednesday.at(time45.get()).do(job45)
                         elif day45.get()=="4":
                                 schedule.every().thursday.at(time45.get()).do(job45)
                         elif day45.get()=="5":
                                 schedule.every().friday.at(time45.get()).do(job45)
                         elif day45.get()=="6":
                                 schedule.every().saturday.at(time45.get()).do(job45)
                         elif day45.get()=="7":
                                 schedule.every().sunday.at(time45.get()).do(job45)
                                 
                         while True:
                              schedule.run_pending()
                              if day46.get()=="1":
                                      schedule.every().monday.at(time46.get()).do(job46)
                              elif day46.get()=="2":
                                      schedule.every().tuesday.at(time46.get()).do(job46)
                              elif day46.get()=="3":
                                      schedule.every().wednesday.at(time46.get()).do(job46)
                              elif day46.get()=="4":
                                      schedule.every().thursday.at(time46.get()).do(job46)
                              elif day46.get()=="5":
                                      schedule.every().friday.at(time46.get()).do(job46)
                              elif day46.get()=="6":
                                      schedule.every().saturday.at(time46.get()).do(job46)
                              elif day46.get()=="7":
                                      schedule.every().sunday.at(time46.get()).do(job46)

                              while True:
                                   schedule.run_pending()
                                   if day47.get()=="1":
                                           schedule.every().monday.at(time47.get()).do(job47)
                                   elif day47.get()=="2":
                                           schedule.every().tuesday.at(time47.get()).do(job47)
                                   elif day47.get()=="3":
                                           schedule.every().wednesday.at(time47.get()).do(job47)
                                   elif day47.get()=="4":
                                           schedule.every().thursday.at(time47.get()).do(job47)
                                   elif day47.get()=="5":
                                           schedule.every().friday.at(time47.get()).do(job47)
                                   elif day47.get()=="6":
                                           schedule.every().saturday.at(time47.get()).do(job47)
                                   elif day47.get()=="7":
                                           schedule.every().sunday.at(time47.get()).do(job47)

                                   while True:
                                        schedule.run_pending()
                                        if day48.get()=="1":
                                                schedule.every().monday.at(time48.get()).do(job48)
                                        elif day48.get()=="2":
                                                schedule.every().tuesday.at(time48.get()).do(job48)
                                        elif day48.get()=="3":
                                                schedule.every().wednesday.at(time48.get()).do(job48)
                                        elif day48.get()=="4":
                                                schedule.every().thursday.at(time48.get()).do(job48)
                                        elif day48.get()=="5":
                                                schedule.every().friday.at(time48.get()).do(job48)
                                        elif day48.get()=="6":
                                                schedule.every().saturday.at(time48.get()).do(job48)
                                        elif day48.get()=="7":
                                                schedule.every().sunday.at(time48.get()).do(job48)

                                        while True:
                                             schedule.run_pending()
                                             if day49.get()=="1":
                                                     schedule.every().monday.at(time49.get()).do(job49)
                                             elif day49.get()=="2":
                                                     schedule.every().tuesday.at(time49.get()).do(job49)
                                             elif day49.get()=="3":
                                                     schedule.every().wednesday.at(time49.get()).do(job49)
                                             elif day49.get()=="4":
                                                     schedule.every().thursday.at(time49.get()).do(job49)
                                             elif day49.get()=="5":
                                                     schedule.every().friday.at(time49.get()).do(job49)
                                             elif day49.get()=="6":
                                                     schedule.every().saturday.at(time49.get()).do(job49)
                                             elif day49.get()=="7":
                                                     schedule.every().sunday.at(time49.get()).do(job49)

                                             while True:
                                                  schedule.run_pending()
                                                  if day50.get()=="1":
                                                          schedule.every().monday.at(time50.get()).do(job50)
                                                  elif day50.get()=="2":
                                                          schedule.every().tuesday.at(time50.get()).do(job50)
                                                  elif day50.get()=="3":
                                                          schedule.every().wednesday.at(time50.get()).do(job50)
                                                  elif day50.get()=="4":
                                                          schedule.every().thursday.at(time50.get()).do(job50)
                                                  elif day50.get()=="5":
                                                          schedule.every().friday.at(time50.get()).do(job50)
                                                  elif day50.get()=="6":
                                                          schedule.every().saturday.at(time50.get()).do(job50)
                                                  elif day50.get()=="7":
                                                          schedule.every().sunday.at(time50.get()).do(job50)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day51.get()=="1":
                                                               schedule.every().monday.at(time51.get()).do(job51)
                                                       elif day51.get()=="2":
                                                               schedule.every().tuesday.at(time51.get()).do(job51)
                                                       elif day51.get()=="3":
                                                               schedule.every().wednesday.at(time51.get()).do(job51)
                                                       elif day51.get()=="4":
                                                               schedule.every().thursday.at(time51.get()).do(job51)
                                                       elif day51.get()=="5":
                                                               schedule.every().friday.at(time51.get()).do(job51)
                                                       elif day51.get()=="6":
                                                               schedule.every().saturday.at(time51.get()).do(job51)
                                                       elif day51.get()=="7":
                                                               schedule.every().sunday.at(time51.get()).do(job51)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day52.get()=="1":
                                                                    schedule.every().monday.at(time52.get()).do(job52)
                                                            elif day52.get()=="2":
                                                                    schedule.every().tuesday.at(time52.get()).do(job52)
                                                            elif day52.get()=="3":
                                                                    schedule.every().wednesday.at(time52.get()).do(job52)
                                                            elif day52.get()=="4":
                                                                    schedule.every().thursday.at(time52.get()).do(job52)
                                                            elif day52.get()=="5":
                                                                    schedule.every().friday.at(time52.get()).do(job52)
                                                            elif day52.get()=="6":
                                                                    schedule.every().saturday.at(time52.get()).do(job52)
                                                            elif day52.get()=="7":
                                                                    schedule.every().sunday.at(time52.get()).do(job52)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day53.get()=="1":
                                                                         schedule.every().monday.at(time53.get()).do(job53)
                                                                 elif day53.get()=="2":
                                                                         schedule.every().tuesday.at(time53.get()).do(job53)
                                                                 elif day53.get()=="3":
                                                                         schedule.every().wednesday.at(time53.get()).do(job53)
                                                                 elif day53.get()=="4":
                                                                         schedule.every().thursday.at(time53.get()).do(job53)
                                                                 elif day53.get()=="5":
                                                                         schedule.every().friday.at(time53.get()).do(job53)
                                                                 elif day53.get()=="6":
                                                                         schedule.every().saturday.at(time53.get()).do(job53)
                                                                 elif day53.get()=="7":
                                                                         schedule.every().sunday.at(time53.get()).do(job53)

                                                                 while True:
                                                                      schedule.run_pending()
                                                                      if day54.get()=="1":
                                                                              schedule.every().monday.at(time54.get()).do(job54)
                                                                      elif day54.get()=="2":
                                                                              schedule.every().tuesday.at(time54.get()).do(job54)
                                                                      elif day54.get()=="3":
                                                                              schedule.every().wednesday.at(time54.get()).do(job54)
                                                                      elif day54.get()=="4":
                                                                              schedule.every().thursday.at(time54.get()).do(job54)
                                                                      elif day54.get()=="5":
                                                                              schedule.every().friday.at(time54.get()).do(job54)
                                                                      elif day54.get()=="6":
                                                                              schedule.every().saturday.at(time54.get()).do(job54)
                                                                      elif day54.get()=="7":
                                                                              schedule.every().sunday.at(time54.get()).do(job54)

                                                                      while True:
                                                                           schedule.run_pending()
                                                                           if day55.get()=="1":
                                                                                   schedule.every().monday.at(time55.get()).do(job55)
                                                                           elif day55.get()=="2":
                                                                                   schedule.every().tuesday.at(time55.get()).do(job55)
                                                                           elif day55.get()=="3":
                                                                                   schedule.every().wednesday.at(time55.get()).do(job55)
                                                                           elif day55.get()=="4":
                                                                                   schedule.every().thursday.at(time55.get()).do(job55)
                                                                           elif day55.get()=="5":
                                                                                   schedule.every().friday.at(time55.get()).do(job55)
                                                                           elif day55.get()=="6":
                                                                                   schedule.every().saturday.at(time55.get()).do(job55)
                                                                           elif day55.get()=="7":
                                                                                   schedule.every().sunday.at(time55.get()).do(job55)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day56.get()=="1":
                                                                                        schedule.every().monday.at(time56.get()).do(job56)
                                                                                elif day56.get()=="2":
                                                                                        schedule.every().tuesday.at(time56.get()).do(job56)
                                                                                elif day56.get()=="3":
                                                                                        schedule.every().wednesday.at(time56.get()).do(job56)
                                                                                elif day56.get()=="4":
                                                                                        schedule.every().thursday.at(time56.get()).do(job56)
                                                                                elif day56.get()=="5":
                                                                                        schedule.every().friday.at(time56.get()).do(job56)
                                                                                elif day56.get()=="6":
                                                                                        schedule.every().saturday.at(time56.get()).do(job56)
                                                                                elif day56.get()=="7":
                                                                                        schedule.every().sunday.at(time56.get()).do(job56)

                                                                                while True:
                                                                                     schedule.run_pending()
                                                                                     if day57.get()=="1":
                                                                                             schedule.every().monday.at(time57.get()).do(job57)
                                                                                     elif day57.get()=="2":
                                                                                             schedule.every().tuesday.at(time57.get()).do(job57)
                                                                                     elif day57.get()=="3":
                                                                                             schedule.every().wednesday.at(time57.get()).do(job57)
                                                                                     elif day57.get()=="4":
                                                                                             schedule.every().thursday.at(time57.get()).do(job57)
                                                                                     elif day57.get()=="5":
                                                                                             schedule.every().friday.at(time57.get()).do(job57)
                                                                                     elif day57.get()=="6":
                                                                                             schedule.every().saturday.at(time57.get()).do(job57)
                                                                                     elif day57.get()=="7":
                                                                                             schedule.every().sunday.at(time57.get()).do(job57)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day58.get()=="1":
                                                                                                  schedule.every().monday.at(time58.get()).do(job58)
                                                                                          elif day58.get()=="2":
                                                                                                  schedule.every().tuesday.at(time58.get()).do(job58)
                                                                                          elif day58.get()=="3":
                                                                                                  schedule.every().wednesday.at(time58.get()).do(job58)
                                                                                          elif day58.get()=="4":
                                                                                                  schedule.every().thursday.at(time58.get()).do(job58)
                                                                                          elif day58.get()=="5":
                                                                                                  schedule.every().friday.at(time58.get()).do(job58)
                                                                                          elif day58.get()=="6":
                                                                                                  schedule.every().saturday.at(time58.get()).do(job58)
                                                                                          elif day58.get()=="7":
                                                                                                  schedule.every().sunday.at(time58.get()).do(job58)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day59.get()=="1":
                                                                                                       schedule.every().monday.at(time59.get()).do(job59)
                                                                                               elif day59.get()=="2":
                                                                                                       schedule.every().tuesday.at(time59.get()).do(job59)
                                                                                               elif day59.get()=="3":
                                                                                                       schedule.every().wednesday.at(time59.get()).do(job59)
                                                                                               elif day59.get()=="4":
                                                                                                       schedule.every().thursday.at(time59.get()).do(job59)
                                                                                               elif day59.get()=="5":
                                                                                                       schedule.every().friday.at(time59.get()).do(job59)
                                                                                               elif day59.get()=="6":
                                                                                                       schedule.every().saturday.at(time59.get()).do(job59)
                                                                                               elif day59.get()=="7":
                                                                                                       schedule.every().sunday.at(time59.get()).do(job59)

                                                                                               while True:
                                                                                                    schedule.run_pending()
                                                                                                    if day60.get()=="1":
                                                                                                            schedule.every().monday.at(time60.get()).do(job60)
                                                                                                    elif day60.get()=="2":
                                                                                                            schedule.every().tuesday.at(time60.get()).do(job60)
                                                                                                    elif day60.get()=="3":
                                                                                                            schedule.every().wednesday.at(time60.get()).do(job60)
                                                                                                    elif day60.get()=="4":
                                                                                                            schedule.every().thursday.at(time60.get()).do(job60)
                                                                                                    elif day60.get()=="5":
                                                                                                            schedule.every().friday.at(time60.get()).do(job60)
                                                                                                    elif day60.get()=="6":
                                                                                                            schedule.every().saturday.at(time60.get()).do(job60)
                                                                                                    elif day60.get()=="7":
                                                                                                            schedule.every().sunday.at(time60.get()).do(job60)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         (job403())




 

def job401():
     
     if day21.get()=="1":
             schedule.every().monday.at(time21.get()).do(job21)
     elif day21.get()=="2":
             schedule.every().tuesday.at(time21.get()).do(job21)
     elif day21.get()=="3":
             schedule.every().wednesday.at(time21.get()).do(job21)
     elif day21.get()=="4":
             schedule.every().thursday.at(time21.get()).do(job21)
     elif day21.get()=="5":
             schedule.every().friday.at(time21.get()).do(job21)
     elif day21.get()=="6":
             schedule.every().saturday.at(time21.get()).do(job21)
     elif day21.get()=="7":
             schedule.every().sunday.at(time21.get()).do(job21)

     while True:
          schedule.run_pending()
          if day22.get()=="1":
                  schedule.every().monday.at(time22.get()).do(job22)
          elif day22.get()=="2":
                  schedule.every().tuesday.at(time22.get()).do(job22)
          elif day22.get()=="3":
                  schedule.every().wednesday.at(time22.get()).do(job22)
          elif day22.get()=="4":
                  schedule.every().thursday.at(time22.get()).do(job22)
          elif day22.get()=="5":
                  schedule.every().friday.at(time22.get()).do(job22)
          elif day22.get()=="6":
                  schedule.every().saturday.at(time22.get()).do(job22)
          elif day22.get()=="7":
                  schedule.every().sunday.at(time22.get()).do(job22)

          while True:
               schedule.run_pending()
               if day23.get()=="1":
                       schedule.every().monday.at(time23.get()).do(job23)
               elif day23.get()=="2":
                       schedule.every().tuesday.at(time23.get()).do(job23)
               elif day23.get()=="3":
                       schedule.every().wednesday.at(time23.get()).do(job23)
               elif day23.get()=="4":
                       schedule.every().thursday.at(time23.get()).do(job23)
               elif day23.get()=="5":
                       schedule.every().friday.at(time23.get()).do(job23)
               elif day23.get()=="6":
                       schedule.every().saturday.at(time23.get()).do(job23)
               elif day23.get()=="7":
                       schedule.every().sunday.at(time23.get()).do(job23)

               while True:
                    schedule.run_pending()
                    if day24.get()=="1":
                            schedule.every().monday.at(time24.get()).do(job24)
                    elif day24.get()=="2":
                            schedule.every().tuesday.at(time24.get()).do(job24)
                    elif day24.get()=="3":
                            schedule.every().wednesday.at(time24.get()).do(job24)
                    elif day24.get()=="4":
                            schedule.every().thursday.at(time24.get()).do(job24)
                    elif day24.get()=="5":
                            schedule.every().friday.at(time24.get()).do(job24)
                    elif day24.get()=="6":
                            schedule.every().saturday.at(time24.get()).do(job24)
                    elif day24.get()=="7":
                            schedule.every().sunday.at(time24.get()).do(job24)

                    while True:
                         schedule.run_pending()
                         if day25.get()=="1":
                                 schedule.every().monday.at(time25.get()).do(job25)
                         elif day25.get()=="2":
                                 schedule.every().tuesday.at(time25.get()).do(job25)
                         elif day25.get()=="3":
                                 schedule.every().wednesday.at(time25.get()).do(job25)
                         elif day25.get()=="4":
                                 schedule.every().thursday.at(time25.get()).do(job25)
                         elif day25.get()=="5":
                                 schedule.every().friday.at(time25.get()).do(job25)
                         elif day25.get()=="6":
                                 schedule.every().saturday.at(time25.get()).do(job25)
                         elif day25.get()=="7":
                                 schedule.every().sunday.at(time25.get()).do(job25)

                         while True:
                              schedule.run_pending()
                              if day26.get()=="1":
                                      schedule.every().monday.at(time26.get()).do(job26)
                              elif day26.get()=="2":
                                      schedule.every().tuesday.at(time26.get()).do(job26)
                              elif day26.get()=="3":
                                      schedule.every().wednesday.at(time26.get()).do(job26)
                              elif day26.get()=="4":
                                      schedule.every().thursday.at(time26.get()).do(job26)
                              elif day26.get()=="5":
                                      schedule.every().friday.at(time26.get()).do(job26)
                              elif day26.get()=="6":
                                      schedule.every().saturday.at(time26.get()).do(job26)
                              elif day26.get()=="7":
                                      schedule.every().sunday.at(time26.get()).do(job26)

                              while True:
                                   schedule.run_pending()
                                   if day27.get()=="1":
                                           schedule.every().monday.at(time27.get()).do(job27)
                                   elif day27.get()=="2":
                                           schedule.every().tuesday.at(time27.get()).do(job27)
                                   elif day27.get()=="3":
                                           schedule.every().wednesday.at(time27.get()).do(job27)
                                   elif day27.get()=="4":
                                           schedule.every().thursday.at(time27.get()).do(job27)
                                   elif day27.get()=="5":
                                           schedule.every().friday.at(time27.get()).do(job27)
                                   elif day27.get()=="6":
                                           schedule.every().saturday.at(time27.get()).do(job27)
                                   elif day27.get()=="7":
                                           schedule.every().sunday.at(time27.get()).do(job27)

                                   while True:
                                        schedule.run_pending()
                                        if day28.get()=="1":
                                                schedule.every().monday.at(time28.get()).do(job28)
                                        elif day28.get()=="2":
                                                schedule.every().tuesday.at(time28.get()).do(job28)
                                        elif day28.get()=="3":
                                                schedule.every().wednesday.at(time28.get()).do(job28)
                                        elif day28.get()=="4":
                                                schedule.every().thursday.at(time28.get()).do(job28)
                                        elif day28.get()=="5":
                                                schedule.every().friday.at(time28.get()).do(job28)
                                        elif day28.get()=="6":
                                                schedule.every().saturday.at(time28.get()).do(job28)
                                        elif day28.get()=="7":
                                                schedule.every().sunday.at(time28.get()).do(job28)

                                        while True:
                                             schedule.run_pending()
                                             if day29.get()=="1":
                                                     schedule.every().monday.at(time29.get()).do(job29)
                                             elif day29.get()=="2":
                                                     schedule.every().tuesday.at(time29.get()).do(job29)
                                             elif day29.get()=="3":
                                                     schedule.every().wednesday.at(time29.get()).do(job29)
                                             elif day29.get()=="4":
                                                     schedule.every().thursday.at(time29.get()).do(job29)
                                             elif day29.get()=="5":
                                                     schedule.every().friday.at(time29.get()).do(job29)
                                             elif day29.get()=="6":
                                                     schedule.every().saturday.at(time29.get()).do(job29)
                                             elif day29.get()=="7":
                                                     schedule.every().sunday.at(time29.get()).do(job29)

                                             while True:
                                                  schedule.run_pending()
                                                  if day30.get()=="1":
                                                          schedule.every().monday.at(time30.get()).do(job30)
                                                  elif day30.get()=="2":
                                                          schedule.every().tuesday.at(time30.get()).do(job30)
                                                  elif day30.get()=="3":
                                                          schedule.every().wednesday.at(time30.get()).do(job30)
                                                  elif day30.get()=="4":
                                                          schedule.every().thursday.at(time30.get()).do(job30)
                                                  elif day30.get()=="5":
                                                          schedule.every().friday.at(time30.get()).do(job30)
                                                  elif day30.get()=="6":
                                                          schedule.every().saturday.at(time30.get()).do(job30)
                                                  elif day30.get()=="7":
                                                          schedule.every().sunday.at(time30.get()).do(job30)

                                                  while True:
                                                       schedule.run_pending()
                                                       if day31.get()=="1":
                                                               schedule.every().monday.at(time31.get()).do(job31)
                                                       elif day31.get()=="2":
                                                               schedule.every().tuesday.at(time31.get()).do(job31)
                                                       elif day31.get()=="3":
                                                               schedule.every().wednesday.at(time31.get()).do(job31)
                                                       elif day31.get()=="4":
                                                               schedule.every().thursday.at(time31.get()).do(job31)
                                                       elif day31.get()=="5":
                                                               schedule.every().friday.at(time31.get()).do(job31)
                                                       elif day31.get()=="6":
                                                               schedule.every().saturday.at(time31.get()).do(job31)
                                                       elif day31.get()=="7":
                                                               schedule.every().sunday.at(time31.get()).do(job31)

                                                       while True:
                                                            schedule.run_pending()
                                                            if day32.get()=="1":
                                                                    schedule.every().monday.at(time32.get()).do(job32)
                                                            elif day32.get()=="2":
                                                                    schedule.every().tuesday.at(time32.get()).do(job32)
                                                            elif day32.get()=="3":
                                                                    schedule.every().wednesday.at(time32.get()).do(job32)
                                                            elif day32.get()=="4":
                                                                    schedule.every().thursday.at(time32.get()).do(job32)
                                                            elif day32.get()=="5":
                                                                    schedule.every().friday.at(time32.get()).do(job32)
                                                            elif day32.get()=="6":
                                                                    schedule.every().saturday.at(time32.get()).do(job32)
                                                            elif day32.get()=="7":
                                                                    schedule.every().sunday.at(time32.get()).do(job32)

                                                            while True:
                                                                 schedule.run_pending()
                                                                 if day33.get()=="1":
                                                                         schedule.every().monday.at(time33.get()).do(job33)
                                                                 elif day33.get()=="2":
                                                                         schedule.every().tuesday.at(time33.get()).do(job33)
                                                                 elif day33.get()=="3":
                                                                         schedule.every().wednesday.at(time33.get()).do(job33)
                                                                 elif day33.get()=="4":
                                                                         schedule.every().thursday.at(time33.get()).do(job33)
                                                                 elif day33.get()=="5":
                                                                         schedule.every().friday.at(time33.get()).do(job33)
                                                                 elif day33.get()=="6":
                                                                         schedule.every().saturday.at(time33.get()).do(job33)
                                                                 elif day33.get()=="7":
                                                                         schedule.every().sunday.at(time33.get()).do(job33)

                                                                 while True:
                                                                      schedule.run_pending()
                                                                      if day34.get()=="1":
                                                                              schedule.every().monday.at(time34.get()).do(job34)
                                                                      elif day34.get()=="2":
                                                                              schedule.every().tuesday.at(time34.get()).do(job34)
                                                                      elif day34.get()=="3":
                                                                              schedule.every().wednesday.at(time34.get()).do(job34)
                                                                      elif day34.get()=="4":
                                                                              schedule.every().thursday.at(time34.get()).do(job34)
                                                                      elif day34.get()=="5":
                                                                              schedule.every().friday.at(time34.get()).do(job34)
                                                                      elif day34.get()=="6":
                                                                              schedule.every().saturday.at(time34.get()).do(job34)
                                                                      elif day34.get()=="7":
                                                                              schedule.every().sunday.at(time34.get()).do(job34)

                                                                      while True:
                                                                           schedule.run_pending()
                                                                           if day35.get()=="1":
                                                                                   schedule.every().monday.at(time35.get()).do(job35)
                                                                           elif day35.get()=="2":
                                                                                   schedule.every().tuesday.at(time35.get()).do(job35)
                                                                           elif day35.get()=="3":
                                                                                   schedule.every().wednesday.at(time35.get()).do(job35)
                                                                           elif day35.get()=="4":
                                                                                   schedule.every().thursday.at(time35.get()).do(job35)
                                                                           elif day35.get()=="5":
                                                                                   schedule.every().friday.at(time35.get()).do(job35)
                                                                           elif day35.get()=="6":
                                                                                   schedule.every().saturday.at(time35.get()).do(job35)
                                                                           elif day35.get()=="7":
                                                                                   schedule.every().sunday.at(time35.get()).do(job35)

                                                                           while True:
                                                                                schedule.run_pending()
                                                                                if day36.get()=="1":
                                                                                        schedule.every().monday.at(time36.get()).do(job36)
                                                                                elif day36.get()=="2":
                                                                                        schedule.every().tuesday.at(time36.get()).do(job36)
                                                                                elif day36.get()=="3":
                                                                                        schedule.every().wednesday.at(time36.get()).do(job36)
                                                                                elif day36.get()=="4":
                                                                                        schedule.every().thursday.at(time36.get()).do(job36)
                                                                                elif day36.get()=="5":
                                                                                        schedule.every().friday.at(time36.get()).do(job36)
                                                                                elif day36.get()=="6":
                                                                                        schedule.every().saturday.at(time36.get()).do(job36)
                                                                                elif day36.get()=="7":
                                                                                        schedule.every().sunday.at(time36.get()).do(job36)

                                                                                while True:
                                                                                     schedule.run_pending()
                                                                                     if day37.get()=="1":
                                                                                             schedule.every().monday.at(time37.get()).do(job37)
                                                                                     elif day37.get()=="2":
                                                                                             schedule.every().tuesday.at(time37.get()).do(job37)
                                                                                     elif day37.get()=="3":
                                                                                             schedule.every().wednesday.at(time37.get()).do(job37)
                                                                                     elif day37.get()=="4":
                                                                                             schedule.every().thursday.at(time37.get()).do(job37)
                                                                                     elif day37.get()=="5":
                                                                                             schedule.every().friday.at(time37.get()).do(job37)
                                                                                     elif day37.get()=="6":
                                                                                             schedule.every().saturday.at(time37.get()).do(job37)
                                                                                     elif day37.get()=="7":
                                                                                             schedule.every().sunday.at(time37.get()).do(job37)

                                                                                     while True:
                                                                                          schedule.run_pending()
                                                                                          if day38.get()=="1":
                                                                                                  schedule.every().monday.at(time38.get()).do(job38)
                                                                                          elif day38.get()=="2":
                                                                                                  schedule.every().tuesday.at(time38.get()).do(job38)
                                                                                          elif day38.get()=="3":
                                                                                                  schedule.every().wednesday.at(time38.get()).do(job38)
                                                                                          elif day38.get()=="4":
                                                                                                  schedule.every().thursday.at(time38.get()).do(job38)
                                                                                          elif day38.get()=="5":
                                                                                                  schedule.every().friday.at(time38.get()).do(job38)
                                                                                          elif day38.get()=="6":
                                                                                                  schedule.every().saturday.at(time38.get()).do(job38)
                                                                                          elif day38.get()=="7":
                                                                                                  schedule.every().sunday.at(time38.get()).do(job38)

                                                                                          while True:
                                                                                               schedule.run_pending()
                                                                                               if day39.get()=="1":
                                                                                                       schedule.every().monday.at(time39.get()).do(job39)
                                                                                               elif day39.get()=="2":
                                                                                                       schedule.every().tuesday.at(time39.get()).do(job39)
                                                                                               elif day39.get()=="3":
                                                                                                       schedule.every().wednesday.at(time39.get()).do(job39)
                                                                                               elif day39.get()=="4":
                                                                                                       schedule.every().thursday.at(time39.get()).do(job39)
                                                                                               elif day39.get()=="5":
                                                                                                       schedule.every().friday.at(time39.get()).do(job39)
                                                                                               elif day39.get()=="6":
                                                                                                       schedule.every().saturday.at(time39.get()).do(job39)
                                                                                               elif day39.get()=="7":
                                                                                                       schedule.every().sunday.at(time39.get()).do(job39)

                                                                                               while True:
                                                                                                    schedule.run_pending()
                                                                                                    if day40.get()=="1":
                                                                                                            schedule.every().monday.at(time40.get()).do(job40)
                                                                                                    elif day40.get()=="2":
                                                                                                            schedule.every().tuesday.at(time40.get()).do(job40)
                                                                                                    elif day40.get()=="3":
                                                                                                            schedule.every().wednesday.at(time40.get()).do(job40)
                                                                                                    elif day40.get()=="4":
                                                                                                            schedule.every().thursday.at(time40.get()).do(job40)
                                                                                                    elif day40.get()=="5":
                                                                                                            schedule.every().friday.at(time40.get()).do(job40)
                                                                                                    elif day40.get()=="6":
                                                                                                            schedule.every().saturday.at(time40.get()).do(job40)
                                                                                                    elif day40.get()=="7":
                                                                                                            schedule.every().sunday.at(time40.get()).do(job40)

                                                                                                    while True:
                                                                                                         schedule.run_pending()
                                                                                                         (job402())
def job400():
    
    if day1.get()=="1":
            schedule.every().monday.at(time1.get()).do(job1)
    elif day1.get()=="2":
            schedule.every().tuesday.at(time1.get()).do(job1)
    elif day1.get()=="3":
            schedule.every().wednesday.at(time1.get()).do(job1)
    elif day1.get()=="4":
            schedule.every().thursday.at(time1.get()).do(job1)
    elif day1.get()=="5":
            schedule.every().friday.at(time1.get()).do(job1)
    elif day1.get()=="6":
            schedule.every().saturday.at(time1.get()).do(job1)
    elif day1.get()=="7":
            schedule.every().sunday.at(time1.get()).do(job1)

    while True:
         schedule.run_pending()       
         if day2.get()=="1":
                 schedule.every().monday.at(time2.get()).do(job2)
         elif day2.get()=="2":
                 schedule.every().tuesday.at(time2.get()).do(job2)
         elif day2.get()=="3":
                 schedule.every().wednesday.at(time2.get()).do(job2)
         elif day2.get()=="4":
                 schedule.every().thursday.at(time2.get()).do(job2)
         elif day2.get()=="5":
                 schedule.every().friday.at(time2.get()).do(job2)
         elif day2.get()=="6":
                 schedule.every().saturday.at(time2.get()).do(job2)
         elif day2.get()=="7":
                 schedule.every().sunday.at(time2.get()).do(job2)

         while True:
              schedule.run_pending()
              if day3.get()=="1":
                      schedule.every().monday.at(time3.get()).do(job3)
              elif day3.get()=="2":
                      schedule.every().tuesday.at(time3.get()).do(job3)
              elif day3.get()=="3":
                      schedule.every().wednesday.at(time3.get()).do(job3)
              elif day3.get()=="4":
                      schedule.every().thursday.at(time3.get()).do(job3)
              elif day3.get()=="5":
                      schedule.every().friday.at(time3.get()).do(job3)
              elif day3.get()=="6":
                      schedule.every().saturday.at(time3.get()).do(job3)
              elif day3.get()=="7":
                      schedule.every().sunday.at(time3.get()).do(job3)

              while True:
                   schedule.run_pending()        
                   if day4.get()=="1":
                           schedule.every().monday.at(time4.get()).do(job4)
                   elif day4.get()=="2":
                           schedule.every().tuesday.at(time4.get()).do(job4)
                   elif day4.get()=="3":
                           schedule.every().wednesday.at(time4.get()).do(job4)
                   elif day4.get()=="4":
                           schedule.every().thursday.at(time4.get()).do(job4)
                   elif day4.get()=="5":
                           schedule.every().friday.at(time4.get()).do(job4)
                   elif day4.get()=="6":
                           schedule.every().saturday.at(time4.get()).do(job4)
                   elif day4.get()=="7":
                           schedule.every().sunday.at(time4.get()).do(job4)

                   while True:
                        schedule.run_pending()
                        if day5.get()=="1":
                                schedule.every().monday.at(time5.get()).do(job5)
                        elif day5.get()=="2":
                                schedule.every().tuesday.at(time5.get()).do(job5)
                        elif day5.get()=="3":
                                schedule.every().wednesday.at(time5.get()).do(job5)
                        elif day5.get()=="4":
                                schedule.every().thursday.at(time5.get()).do(job5)
                        elif day5.get()=="5":
                                schedule.every().friday.at(time5.get()).do(job5)
                        elif day5.get()=="6":
                                schedule.every().saturday.at(time5.get()).do(job5)
                        elif day5.get()=="7":
                                schedule.every().sunday.at(time5.get()).do(job5)

                        while True:
                             schedule.run_pending()
                             if day6.get()=="1":
                                     schedule.every().monday.at(time6.get()).do(job6)
                             elif day6.get()=="2":
                                     schedule.every().tuesday.at(time6.get()).do(job6)
                             elif day6.get()=="3":
                                     schedule.every().wednesday.at(time6.get()).do(job6)
                             elif day6.get()=="4":
                                     schedule.every().thursday.at(time6.get()).do(job6)
                             elif day6.get()=="5":
                                     schedule.every().friday.at(time6.get()).do(job6)
                             elif day6.get()=="6":
                                     schedule.every().saturday.at(time6.get()).do(job6)
                             elif day6.get()=="7":
                                     schedule.every().sunday.at(time6.get()).do(job6)

                             while True:
                                  schedule.run_pending()       
                                  if day7.get()=="1":
                                          schedule.every().monday.at(time7.get()).do(job7)
                                  elif day7.get()=="2":
                                          schedule.every().tuesday.at(time7.get()).do(job7)
                                  elif day7.get()=="3":
                                          schedule.every().wednesday.at(time7.get()).do(job7)
                                  elif day7.get()=="4":
                                          schedule.every().thursday.at(time7.get()).do(job7)
                                  elif day7.get()=="5":
                                          schedule.every().friday.at(time7.get()).do(job7)
                                  elif day7.get()=="6":
                                          schedule.every().saturday.at(time7.get()).do(job7)
                                  elif day7.get()=="7":
                                          schedule.every().sunday.at(time7.get()).do(job7)

                                  while True:
                                       schedule.run_pending()
                                       if day8.get()=="1":
                                               schedule.every().monday.at(time8.get()).do(job8)
                                       elif day8.get()=="2":
                                               schedule.every().tuesday.at(time8.get()).do(job8)
                                       elif day8.get()=="3":
                                               schedule.every().wednesday.at(time8.get()).do(job8)
                                       elif day8.get()=="4":
                                               schedule.every().thursday.at(time8.get()).do(job8)
                                       elif day8.get()=="5":
                                               schedule.every().friday.at(time8.get()).do(job8)
                                       elif day8.get()=="6":
                                               schedule.every().saturday.at(time8.get()).do(job8)
                                       elif day8.get()=="7":
                                               schedule.every().sunday.at(time8.get()).do(job8)

                                       while True:
                                            schedule.run_pending()
                                            if day9.get()=="1":
                                                    schedule.every().monday.at(time9.get()).do(job9)
                                            elif day9.get()=="2":
                                                    schedule.every().tuesday.at(time9.get()).do(job9)
                                            elif day9.get()=="3":
                                                    schedule.every().wednesday.at(time9.get()).do(job9)
                                            elif day9.get()=="4":
                                                    schedule.every().thursday.at(time9.get()).do(job9)
                                            elif day9.get()=="5":
                                                    schedule.every().friday.at(time9.get()).do(job9)
                                            elif day9.get()=="6":
                                                    schedule.every().saturday.at(time9.get()).do(job9)
                                            elif day9.get()=="7":
                                                    schedule.every().sunday.at(time9.get()).do(job9)

                                            while True:
                                                 schedule.run_pending()
                                                 if day10.get()=="1":
                                                         schedule.every().monday.at(time10.get()).do(job10)
                                                 elif day10.get()=="2":
                                                         schedule.every().tuesday.at(time10.get()).do(job10)
                                                 elif day10.get()=="3":
                                                         schedule.every().wednesday.at(time10.get()).do(job10)
                                                 elif day10.get()=="4":
                                                         schedule.every().thursday.at(time10.get()).do(job10)
                                                 elif day10.get()=="5":
                                                         schedule.every().friday.at(time10.get()).do(job10)
                                                 elif day10.get()=="6":
                                                         schedule.every().saturday.at(time10.get()).do(job10)
                                                 elif day10.get()=="7":
                                                         schedule.every().sunday.at(time10.get()).do(job10)

                                                 while True:
                                                      schedule.run_pending()
                                                      if day11.get()=="1":
                                                              schedule.every().monday.at(time11.get()).do(job11)
                                                      elif day11.get()=="2":
                                                              schedule.every().tuesday.at(time11.get()).do(job11)
                                                      elif day11.get()=="3":
                                                              schedule.every().wednesday.at(time11.get()).do(job11)
                                                      elif day11.get()=="4":
                                                              schedule.every().thursday.at(time11.get()).do(job11)
                                                      elif day11.get()=="5":
                                                              schedule.every().friday.at(time11.get()).do(job11)
                                                      elif day11.get()=="6":
                                                              schedule.every().saturday.at(time11.get()).do(job11)
                                                      elif day11.get()=="7":
                                                              schedule.every().sunday.at(time11.get()).do(job11)

                                                      while True:
                                                           schedule.run_pending()
                                                           if day12.get()=="1":
                                                                   schedule.every().monday.at(time12.get()).do(job12)
                                                           elif day12.get()=="2":
                                                                   schedule.every().tuesday.at(time12.get()).do(job12)
                                                           elif day12.get()=="3":
                                                                   schedule.every().wednesday.at(time12.get()).do(job12)
                                                           elif day12.get()=="4":
                                                                   schedule.every().thursday.at(time12.get()).do(job12)
                                                           elif day12.get()=="5":
                                                                   schedule.every().friday.at(time12.get()).do(job12)
                                                           elif day12.get()=="6":
                                                                   schedule.every().saturday.at(time12.get()).do(job12)
                                                           elif day12.get()=="7":
                                                                   schedule.every().sunday.at(time12.get()).do(job12)

                                                           while True:
                                                                schedule.run_pending()
                                                                if day13.get()=="1":
                                                                        schedule.every().monday.at(time13.get()).do(job13)
                                                                elif day13.get()=="2":
                                                                        schedule.every().tuesday.at(time13.get()).do(job13)
                                                                elif day13.get()=="3":
                                                                        schedule.every().wednesday.at(time13.get()).do(job13)
                                                                elif day13.get()=="4":
                                                                        schedule.every().thursday.at(time13.get()).do(job13)
                                                                elif day13.get()=="5":
                                                                        schedule.every().friday.at(time13.get()).do(job13)
                                                                elif day13.get()=="6":
                                                                        schedule.every().saturday.at(time13.get()).do(job13)
                                                                elif day13.get()=="7":
                                                                        schedule.every().sunday.at(time13.get()).do(job13)

                                                                while True:
                                                                     schedule.run_pending()
                                                                     if day14.get()=="1":
                                                                             schedule.every().monday.at(time14.get()).do(job14)
                                                                     elif day14.get()=="2":
                                                                             schedule.every().tuesday.at(time14.get()).do(job14)
                                                                     elif day14.get()=="3":
                                                                             schedule.every().wednesday.at(time14.get()).do(job14)
                                                                     elif day14.get()=="4":
                                                                             schedule.every().thursday.at(time14.get()).do(job14)
                                                                     elif day14.get()=="5":
                                                                             schedule.every().friday.at(time14.get()).do(job14)
                                                                     elif day14.get()=="6":
                                                                             schedule.every().saturday.at(time14.get()).do(job14)
                                                                     elif day14.get()=="7":
                                                                             schedule.every().sunday.at(time14.get()).do(job14)

                                                                     while True:
                                                                          schedule.run_pending()        
                                                                          if day15.get()=="1":
                                                                                  schedule.every().monday.at(time15.get()).do(job15)
                                                                          elif day15.get()=="2":
                                                                                  schedule.every().tuesday.at(time15.get()).do(job15)
                                                                          elif day15.get()=="3":
                                                                                  schedule.every().wednesday.at(time15.get()).do(job15)
                                                                          elif day15.get()=="4":
                                                                                  schedule.every().thursday.at(time15.get()).do(job15)
                                                                          elif day15.get()=="5":
                                                                                  schedule.every().friday.at(time15.get()).do(job15)
                                                                          elif day15.get()=="6":
                                                                                  schedule.every().saturday.at(time15.get()).do(job15)
                                                                          elif day15.get()=="7":
                                                                                  schedule.every().sunday.at(time15.get()).do(job15)

                                                                          while True:
                                                                               schedule.run_pending()
                                                                               if day16.get()=="1":
                                                                                       schedule.every().monday.at(time16.get()).do(job16)
                                                                               elif day16.get()=="2":
                                                                                       schedule.every().tuesday.at(time16.get()).do(job16)
                                                                               elif day16.get()=="3":
                                                                                       schedule.every().wednesday.at(time16.get()).do(job16)
                                                                               elif day16.get()=="4":
                                                                                       schedule.every().thursday.at(time16.get()).do(job16)
                                                                               elif day16.get()=="5":
                                                                                       schedule.every().friday.at(time16.get()).do(job16)
                                                                               elif day16.get()=="6":
                                                                                       schedule.every().saturday.at(time16.get()).do(job16)
                                                                               elif day16.get()=="7":
                                                                                       schedule.every().sunday.at(time16.get()).do(job16)

                                                                               while True:
                                                                                    schedule.run_pending()
                                                                                    if day17.get()=="1":
                                                                                            schedule.every().monday.at(time17.get()).do(job17)
                                                                                    elif day17.get()=="2":
                                                                                            schedule.every().tuesday.at(time17.get()).do(job17)
                                                                                    elif day17.get()=="3":
                                                                                            schedule.every().wednesday.at(time17.get()).do(job17)
                                                                                    elif day17.get()=="4":
                                                                                            schedule.every().thursday.at(time17.get()).do(job17)
                                                                                    elif day17.get()=="5":
                                                                                            schedule.every().friday.at(time17.get()).do(job17)
                                                                                    elif day17.get()=="6":
                                                                                            schedule.every().saturday.at(time17.get()).do(job17)
                                                                                    elif day17.get()=="7":
                                                                                            schedule.every().sunday.at(time17.get()).do(job17)

                                                                                    while True:
                                                                                         schedule.run_pending()
                                                                                         if day18.get()=="1":
                                                                                                 schedule.every().monday.at(time18.get()).do(job18)
                                                                                         elif day18.get()=="2":
                                                                                                 schedule.every().tuesday.at(time18.get()).do(job18)
                                                                                         elif day18.get()=="3":
                                                                                                 schedule.every().wednesday.at(time18.get()).do(job18)
                                                                                         elif day18.get()=="4":
                                                                                                 schedule.every().thursday.at(time18.get()).do(job18)
                                                                                         elif day18.get()=="5":
                                                                                                 schedule.every().friday.at(time18.get()).do(job18)
                                                                                         elif day18.get()=="6":
                                                                                                 schedule.every().saturday.at(time18.get()).do(job18)
                                                                                         elif day18.get()=="7":
                                                                                                 schedule.every().sunday.at(time18.get()).do(job18)

                                                                                         while True:
                                                                                              schedule.run_pending()
                                                                                              if day19.get()=="1":
                                                                                                      schedule.every().monday.at(time19.get()).do(job19)
                                                                                              elif day19.get()=="2":
                                                                                                      schedule.every().tuesday.at(time19.get()).do(job19)
                                                                                              elif day19.get()=="3":
                                                                                                      schedule.every().wednesday.at(time19.get()).do(job19)
                                                                                              elif day19.get()=="4":
                                                                                                      schedule.every().thursday.at(time19.get()).do(job19)
                                                                                              elif day19.get()=="5":
                                                                                                      schedule.every().friday.at(time19.get()).do(job19)
                                                                                              elif day19.get()=="6":
                                                                                                      schedule.every().saturday.at(time19.get()).do(job19)
                                                                                              elif day19.get()=="7":
                                                                                                      schedule.every().sunday.at(time19.get()).do(job19)

                                                                                              while True:
                                                                                                   schedule.run_pending()
                                                                                                   if day20.get()=="1":
                                                                                                           schedule.every().monday.at(time20.get()).do(job20)
                                                                                                   elif day20.get()=="2":
                                                                                                           schedule.every().tuesday.at(time20.get()).do(job20)
                                                                                                   elif day20.get()=="3":
                                                                                                           schedule.every().wednesday.at(time20.get()).do(job20)
                                                                                                   elif day20.get()=="4":
                                                                                                           schedule.every().thursday.at(time20.get()).do(job20)
                                                                                                   elif day20.get()=="5":
                                                                                                           schedule.every().friday.at(time20.get()).do(job20)
                                                                                                   elif day20.get()=="6":
                                                                                                           schedule.every().saturday.at(time20.get()).do(job20)
                                                                                                   elif day20.get()=="7":
                                                                                                           schedule.every().sunday.at(time20.get()).do(job20)

                                                                                                   while True:
                                                                                                        schedule.run_pending()
                                                                                                        (job401())
                                                                                              
myButton = Button(second_frame, text= "         Ready!         ", command=job400, cursor="hand2")
myButton.pack()



root.mainloop()        
