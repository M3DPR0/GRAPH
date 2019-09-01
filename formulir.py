class MembuatKolomTeks(Frame) :
    def __init__(self) :
        self.buatTeks()
        self.buatKolom()

    def buatTeks(self):
        Label(text="First Name").grid(row=0)
        Label(text="Last Name").grid(row=1)

    def buatKolom(self):
        Entry().grid(row=0, column=1)
        Entry().grid(row=1, column=1)

master = Tk()
MembuatKolomTeks()
mainloop()
