# KULLANICI GİRİŞİ UYGULAMASI

import tkinter as tk

form = tk.Tk()
form.title("UYGULAMA")
form.geometry("500x300")

mail = tk.Label(form, text="Mail: ", fg="black",
                bg="blue", font="Times 10 bold")
mail.place(x=10, y=30)

sifre = tk.Label(form, text="Şifre: ", fg="black",
                 bg="blue", font="Times 10 bold")
sifre.place(x=10, y=60)

mail_entry = tk.Entry()
mail_entry.place(x=50, y=30)

sifre_entry = tk.Entry(form, show="*")
sifre_entry.place(x=50, y=62)


def kayıtol():
    mail = tk.Label(form, text="Mail: ", fg="black",
                    bg="blue", font="Times 10 bold")
    mail.place(x=10, y=150)

    sifre = tk.Label(form, text="Şifre: ", fg="black",
                     bg="blue", font="Times 10 bold")
    sifre.place(x=10, y=180)
    ad = tk.Label(form, text="Ad: ", fg="black",
                  bg="blue", font="Times 10 bold")
    ad.place(x=10, y=120)
    mail_entry = tk.Entry()
    mail_entry.place(x=50, y=150)
    sifre = tk.Entry(form, show="*")
    sifre.place(x=50, y=180)
    ad = tk.Entry()
    ad.place(x=50, y=120)


kayitol_btn = tk.Button(form, text="Kayıt Ol",
                        fg="black", bg="green", command=kayıtol)
kayitol_btn.place(x=50, y=90)


def giris():
    mail_entry.delete(0, "end")
    sifre_entry.delete(0, "end")


giris_btn = tk.Button(form, text="Giriş", fg="black",
                      bg="green", command=giris)
giris_btn.place(x=120, y=90)


form.mainloop()
