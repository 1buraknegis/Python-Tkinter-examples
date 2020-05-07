# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:09:17 2020

@author: 1buraknegis
"""


# ------------------Tkinter PEncere Boyutlandırma------------- #

import tkinter as tk

form = tk.Tk()
form.title("Tkinter Dersleri-3")
form.geometry("500x250+500+350") # Formun ekrana açıldığında konumunu belirledik.
form.minsize(450, 400) #Formun min boyutunu belirledik
form.maxsize(550, 550) # Formun maksimum boyutunu belirledik.

# form.resizable(False, False) # Formun boyutunu değiştiremememizi sağlar.


etiket = tk.Label(text = "Ders-3")
etiket.pack()


form.mainloop()
