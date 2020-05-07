# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:21:07 2020

@author: 1buraknegis
"""


# ------------------------Pencere Durumları--------------------- #

import tkinter as tk

form = tk.Tk()
form.geometry("500x500+350+250")
form.title("Ders-4")

form.state("normal")
# normal yazarsak istediğimiz boyutlarda form açılır.
# zoomed yazarsak tam ekranda form açılır.
# iconic yazarsak ikonik olarak gelir.

form.wm_attributes("-alpha", 0.3)
# formumuzun saydamlığını ya da netliğini belirlememizi sağlar. İkinci parametre 0-1 arası
# değerler alır.







form.mainloop()