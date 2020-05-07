# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:19:17 2020

@author: 1buraknegis
"""


import tkinter as tk

form = tk.Tk()
form.title("Tkinter Dersleri Formu") #Formumuzun ismini(başlığını) belirlememizi sağlar.

etiket = tk.Label(form, text = "Python Tkinter") #form ismini belirtmemiz lazım ilk parametrede
etiket.pack() #oluşturduğumuz label'ın form üzerinde görünmesini sağlar.

etiket2 = tk.Label(form, text = "Python Tkinter Dersleri-2", fg = "red")
etiket2.pack()

etiket3 = tk.Label(form, text = "Ders-2 Arkaplan", fg = "black", bg = "green")
etiket3.pack()

etiket4 = tk.Label(form, text = "yeni label", fg ="blue", bg = "yellow", font = "Times 30 italic")
etiket4.pack()

etiket5 = tk.Label(form, text = "En son label", fg = "green", bg = "red", font = "Times 22 bold")
etiket5.pack()


form.mainloop() #formu gösterir.


# fg = yazı tipi rengi
# bg = arka plan rengi
# font = yazı tipi, yazı boyutu, yazı türü