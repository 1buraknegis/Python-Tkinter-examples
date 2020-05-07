import tkinter as tk
from tkinter import messagebox

form = tk.Tk()
form.title("MessageBox")
form.geometry("500x500")


def mesaj():
    messagebox.showinfo(
        title="Mesaj1", message="Lütfen mesaja riayet ediniz !!")
    messagebox.askretrycancel(title="Mesaj2", message="Lütfen et artık")
    messagebox.askyesno(title="Mesaj3", message="E hadi artık")
    messagebox.askquestion(title="Mesaj4", message="Son Uyarı")


buton = tk.Button(form, text="Tıkla Mesaj Gelsin", command=mesaj).pack()

form.mainloop()
