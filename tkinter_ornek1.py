# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:40:24 2020

@author: 1buraknegis
"""


import tkinter as tk
import random as rd

form = tk.Tk()
form.title("Tekrar Uygulaması")
form.geometry("500x400+500+350")

liste = []
for i in range(5):
    while len(liste) != 6:
        a = rd.randint(1,50)
        if a not in liste:
            liste.append(a)

def goster():
    label.config(text = liste, bg = "green")
    

def saydamlastir():
    form.wm_attributes("-alpha", 0.3)
    
def dondur():
    form.wm_attributes("-alpha", 0.9)

def max_yap():
    form.state("zoomed")
    
def min_yap():
    form.state("iconic")
    
label = tk.Label(form, fg ="red", bg = "red", font = "Times 20 bold")
label.pack()

goster = tk.Button(form, text = "göster", fg = "black", bg ="yellow", command = goster)
goster.pack(side = tk.LEFT)

goster = tk.Button(form, text = "saydamlaştır", fg = "black", bg ="yellow", command = saydamlastir)
goster.pack(side = tk.LEFT)

goster = tk.Button(form, text = "döndür", fg = "black", bg ="yellow", command = dondur)
goster.pack(side = tk.LEFT)

goster = tk.Button(form, text = "max yap", fg = "black", bg ="yellow", command = max_yap)
goster.pack(side = tk.LEFT)

goster = tk.Button(form, text = "min yap", fg = "black", bg ="yellow", command = min_yap)
goster.pack(side = tk.LEFT)










form.mainloop()