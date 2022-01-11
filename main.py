# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import font
def close_app():
    root.destroy()
def code_up():
    exttxt = enctxt.get().replace("a","ß").replace("b","à").replace("c","á").replace("d","â").replace("e","ã").replace("f","ä").replace("g","å").replace("h","²").replace("i","ç").replace("j","è").replace("k","é").replace("l","ê").replace("m","ë").replace("n","ì").replace("o","í").replace("p","î").replace("q","ï").replace("r","ð").replace("s","ñ").replace("t","ò").replace("u","ó").replace("v","õ").replace("w","ö").replace("x","ø").replace("y","│").replace("z","┌").replace(" ","┐").replace("@","┘").replace(",","║").replace(".","╔").replace("&","╝").replace("%","♫").replace("*","☺").replace("!","♠").replace("?","®")
    scrool.delete("1.0","end")
    scrool.insert(INSERT , f"{exttxt}")
    scrool.event_add("<<Copy>>")
def code_down():
    exttxt = enctxt.get().replace("ß","a").replace("à","b").replace("á","c").replace("â","d").replace("ã","e").replace("ä","f").replace("å","g").replace("²","h").replace("ç","i").replace("è","j").replace("é","k").replace("ê","l").replace("ë","m").replace("ì","n").replace("í","o").replace("î","p").replace("ï","q").replace("ð","r").replace("ñ","s").replace("ò","t").replace("ó","u").replace("õ","v").replace("ö","w").replace("ø","x").replace("│","y").replace("┌","z").replace("┐"," ").replace("┘","@").replace("║",",").replace("╔",".").replace("╝","&").replace("♫","%").replace("☺","*").replace("♠","!").replace("®","?")
    scrool.delete("1.0","end")
    scrool.insert(INSERT , f"{exttxt}")
root = Tk()
root.wm_overrideredirect(True)
root.title("Invento Security Encryptor 2.0")
root.geometry("700x400+350+200")
root.config(bg="#1f2c47")
enctxt = StringVar()
headbar = Label(bg="white")
headbar.pack(anchor=N,fill=X)
Label(headbar, text="Invento Encryptor 2.0 By Invento Securityð" , font=("Cascadia Mono", 10,font.BOLD)).pack(side=LEFT)
Button(headbar ,  command=close_app,text="❌", bg="white",fg="red", relief=FLAT, borderwidth=0).pack(side=RIGHT)
Label(text="Type Here to Encode and Decode:-", bg="#1f2c47",fg="white",font=("Reem Kufi", 15)).pack()
textis = Entry(relief=FLAT, font=("Reem Kufi", 13, font.BOLD), fg="#0f0f0f", textvariable=enctxt).pack(fill=X)
# ctc = StringVar()
Button(text="Encode",command=code_up , relief=FLAT , bg="#5980ff", fg="white", font=("Reem Kufi", 15), borderwidth=0, height=0, width=60).pack()
Button(text="Decode",command=code_down , relief=FLAT , bg="#6d59ff", fg="white", font=("Reem Kufi", 15), borderwidth=0, height=0, width=60).pack()
scrool = Text(bg="#1f2c47",fg="white", borderwidth=0,relief=FLAT)
scrool.pack(anchor=S)
root.mainloop()