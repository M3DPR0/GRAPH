# file: demoBallon.py
# Deskripsi: Menampilkan popup-message
#       pada komponen Tkinter dengan Tix.
#
# Python ver. 2.6
# Sistem Operasi: Debian 6 (squeeze)
# Tgl pembuatan: 4 Januari 2013 at 15.35 WIB
# Penulis: KlinikPython.wordpress.com
#
 
 
from Tkinter import 
import Tix # Jangan lupa!
import tkMessageBox as mb
 
class DemoBallon:
    def __init__(self, induk, judul):
        self.induk = induk
         
        self.induk.geometry("300x200")
        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.tutup)
        self.induk.resizable(False, False)
         
        self.aturKomponen()
        self.aturKejadian()
         
    def aturKomponen(self):
        # atur frame utama
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)
         
        # buat frame untuk tombol
        fr_tombol = Frame(mainFrame, bd=10)
        fr_tombol.pack(side=TOP)
         
        # buat tombol Pesan
        self.btnPesan = Button(fr_tombol, text='Pesan',
                command=self.pesan)
        self.btnPesan.pack(side=LEFT)
         
        # buat tombol Keluar
        self.btnKeluar = Button(fr_tombol, text='Keluar',
                command=self.tutup)
        self.btnKeluar.pack(side=LEFT)
         
        # buat statusbar menggunakan komponen Label
        self.lblStatus = Label(mainFrame, relief=RIDGE, bd=1)
        self.lblStatus.pack(side=BOTTOM, fill=X)
         
        # pasang komponen balloon (Tix) --> membuat popup-message
        self.balStatus = Tix.Balloon(mainFrame, statusbar=self.lblStatus)
         
    def aturKejadian(self):
        # menghubungkan komponen Balloon pada setiap tombol.
        # jika kursor menunjuk tombol, maka akan muncul pesan pop-up.
        self.balStatus.bind_widget(self.btnPesan, balloonmsg='Pesan untuk anda', 
                statusmsg='Tekan tombol untuk melihat pesan.')
        self.balStatus.bind_widget(self.btnKeluar, balloonmsg='Keluar dari program', 
                statusmsg='Tekan tombol untuk keluar aplikasi.')
         
    def pesan(self, event=None):
        # menampilkan pesan ketika tombol Pesan diklik.
        mb.showinfo("pesan", "Salam PythonMania!")
                 
    def tutup(self, event=None):
        self.induk.destroy()
         
if __name__ == '__main__':
    root = Tix.Tk()
     
    app = DemoBallon(root, ":: Demo Ballon (Tix) ::")
     
    root.mainloop()
