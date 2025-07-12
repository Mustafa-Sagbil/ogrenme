import tkinter as tk

def main():
    # Ana Klasör.
    cikti = "Merhaba Dünya"
    # Konsol Çıktısı
    konsol_yazdir(cikti)
    # Pencere Çıktısı
    pencere_yazdir(cikti)

def konsol_yazdir(yazi):
    print(yazi)
    
def pencere_yazdir(yazi):
    pencere = tk.Tk()
    pencere.title(yazi)
    pencere.geometry("300x200")
    satir = tk.Label(pencere, text=yazi, fg="white")
    satir.place(x=100, y=100)
    pencere.mainloop()





if __name__ == "__main__":
    main()