# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:28:06 2020

@author: 1buraknegis
"""


# -------------------------Button------------------#

import tkinter as tk # önce tkinter'ı import ederiz.

form = tk.Tk() # form oluştururuz.
form.title("Ders-5") #formun başlığını yazarız.
form.geometry("500x400") # formun ekrandaki konumunu belirleriz.


def topla():
    print("topla")
buton = tk.Button( form, text ="Tıkla", fg = "black", bg = "red", command = topla)
# buton oluşturup butonun ismini "Tıkla" diye belirledik. ve tıklayınca ne yapmasını
# istediğimiz işlevi bir fonksiyon yardımıyla belirleyip butona atadık.
buton.pack(side = tk.LEFT) #butonun form üzerinde ne tarafta durmasını istiyorsak
                           #orda durmasını istedik.

buton2 = tk.Button(form, text ="Tıkla2", command = topla)
buton2.pack(side = tk.LEFT)




form.mainloop() # formumuzun gözükmesini saplar.
    