#coding=utf-8
import Tkinter as tk
from tkinter import*

class Uygulama(object):

    def __init__(self):
        self.araclar()

    def araclar(self):


        self.hesapla = Button(text = 'Hesapla', command = self.hesapla)
        self.hesapla.place(relx=0.7, rely=0.7, relheight=0.1)

        self.dogru_etiketi = Label(text = 'Doğru')
        self.dogru_etiketi.place(relx=0.25, rely=0.02, relheight=0.08)

        self.yanlis_etiketi = Label(text = 'Yanlış')
        self.yanlis_etiketi.place(relx=0.45, rely=0.02, relheight=0.08)

        self.bos_etiketi = Label(text = 'Boş')
        self.bos_etiketi.place(relx=0.668, rely=0.02, relheight=0.08)

        self.net_etiketi = Label(text = 'Net')
        self.net_etiketi.place(relx=0.87, rely=0.02, relheight=0.08)




        self.turkce_etiketi = Label(text = 'Türkçe: ')
        self.turkce_etiketi.place(relx=0.06, rely=0.12, relheight=0.08)

        self.turkce_dogru = Entry(width=4)
        self.turkce_dogru.place(relx=0.25, rely=0.12, relheight=0.08)

        self.turkce_yanlis = Entry(width=4)
        self.turkce_yanlis.place(relx=0.45, rely=0.12, relheight=0.08)

        self.turkce_bos = Entry(width=4)
        self.turkce_bos.place(relx=0.65, rely=0.12, relheight=0.08)

        self.turkce_net = Entry(width=5)
        self.turkce_net.place(relx=0.85, rely=0.12, relheight=0.08)




        self.sosyal_etiketi = Label(text= 'Sosyal: ')
        self.sosyal_etiketi.place(relx=0.06, rely=0.25, relheight=0.08)

        self.sosyal_dogru = Entry(width=4)
        self.sosyal_dogru.place(relx=0.25, rely=0.25, relheight=0.08)

        self.sosyal_yanlis = Entry(width=4)
        self.sosyal_yanlis.place(relx=0.45, rely=0.25, relheight=0.08)

        self.sosyal_bos = Entry(width=4)
        self.sosyal_bos.place(relx=0.65, rely=0.25, relheight=0.08)

        self.sosyal_net = Entry(width=5)
        self.sosyal_net.place(relx=0.85, rely=0.25, relheight=0.08)




        self.matematik_etiketi = Label(text= 'Mat: ')
        self.matematik_etiketi.place(relx=0.06, rely=0.38, relheight=0.08)

        self.matematik_dogru = Entry(width=4)
        self.matematik_dogru.place(relx=0.25, rely=0.38, relheight=0.08)

        self.matematik_yanlis = Entry(width=4)
        self.matematik_yanlis.place(relx=0.45, rely=0.38, relheight=0.08)

        self.matematik_bos = Entry(width=4)
        self.matematik_bos.place(relx=0.65, rely=0.38, relheight=0.08)

        self.matematik_net = Entry(width=5)
        self.matematik_net.place(relx=0.85, rely=0.38, relheight=0.08)




        self.fen_etiketi = Label(text= 'Fen: ')
        self.fen_etiketi.place(relx=0.06, rely=0.51, relheight=0.08)

        self.fen_dogru = Entry(width=4)
        self.fen_dogru.place(relx=0.25, rely=0.51, relheight=0.08)

        self.fen_yanlis = Entry(width=4)
        self.fen_yanlis.place(relx=0.45, rely=0.51, relheight=0.08)

        self.fen_bos = Entry(width=4)
        self.fen_bos.place(relx=0.65, rely=0.51, relheight=0.08)

        self.fen_net = Entry(width=5)
        self.fen_net.place(relx=0.85, rely=0.51, relheight=0.08)

    def hesapla(self):

        self.td= self.turkce_dogru.get()
        self.ty = self.turkce_yanlis.get()
        self.tb_kontrol = self.turkce_bos.get()

        if self.tb_kontrol == str(''):
            self.turkce_bos.insert(0, int(0))
            self.tb_kontrol = self.turkce_bos.get()

        self.turkce_net_sayisi = int(self.td) - int(self.ty) * float(0.25) - int(self.tb_kontrol)

        self.turkce_net.delete(0, END)
        self.turkce_net.insert(0, self.turkce_net_sayisi)




        self.sd= self.sosyal_dogru.get()
        self.sy = self.sosyal_yanlis.get()
        self.sb_kontrol = self.sosyal_bos.get()

        if self.sb_kontrol == str(''):
            self.sosyal_bos.insert(0, int(0))
            self.sb_kontrol = self.sosyal_bos.get()

        self.sosyal_net_sayisi = int(self.sd) - int(self.sy) * float(0.25) - int(self.sb_kontrol)

        self.sosyal_net.delete(0, END)
        self.sosyal_net.insert(0, self.sosyal_net_sayisi)




        self.md= self.matematik_dogru.get()
        self.my = self.matematik_yanlis.get()
        self.mb_kontrol = self.matematik_bos.get()

        if self.mb_kontrol == str(''):
            self.matematik_bos.insert(0, int(0))
            self.mb_kontrol = self.matematik_bos.get()

        self.matematik_net_sayisi = int(self.md) - int(self.my) * float(0.25) - int(self.mb_kontrol)

        self.matematik_net.delete(0, END)
        self.matematik_net.insert(0, self.matematik_net_sayisi)




        self.fd= self.fen_dogru.get()
        self.fy = self.fen_yanlis.get()
        self.fb_kontrol = self.fen_bos.get()

        if self.fb_kontrol == str(''):
            self.fen_bos.insert(0, int(0))
            self.fb_kontrol = self.fen_bos.get()

        self.fen_net_sayisi = int(self.fd) - int(self.fy) * float(0.25) - int(self.fb_kontrol)

        self.fen_net.delete(0, END)
        self.fen_net.insert(0, self.fen_net_sayisi)



pencere = tk.Tk()
pencere.geometry('350x250')
pencere.resizable(width=NO, height=NO)

menu_araclari = Menu()
pencere.config(menu= menu_araclari)
baslik = pencere.title("Net Hesaplayıcı")
uyg = Uygulama()

mainloop()
