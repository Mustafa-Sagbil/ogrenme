# Bu kod iki sayının toplamını bulmak için yazılmıştır.
# Verilen liste içinde arama yapılır ve hedef değer ile eşleşen iki sayının indexleri geri döndürülür.
# Örnek: VERILER = [2,5,3,8,12,9,21] ve target = 15 için, [0, 3] geri döndürülür.
# Çünkü 2 + 12 = 15 ve 0. ve 3. indexler bu sayıların indexleridir.
# Veriler ve target değerleri örnek olarak verilmiştir.




VERILER = [2,5,3,8,12,9,21] # verilen liste. Aramalar bu liste içerisinde yapılacak.
target = 15 # Hedef değer. Amaç toplamı bu hedef değeri veren iki sayı bulmak.




def main():
    # Ana Fonksiyon. Herşey burada oluyor.
    yazdir = ikıSayiToplami().toplam_bulucu(target, VERILER)
    print(str(yazdir) + "indeksli sayılar toplanıyor") # Sonucu Konsola Yazdıran Fonksiyon.
    print(str(VERILER[yazdir[0]]) + " + " + str(VERILER[yazdir[1]]) + " = " + str(target) ) 






class ikıSayiToplami:
    # Bu sınıf iki sayının toplamını bulmak için yazılmıştır.
    # Verilen liste içinde arama yapılır ve hedef değer ile eşleşen iki sayının indexleri geri döndürülür.
    # Örnek: VERILER = [2,5,3,8,12,9,21] ve target = 15 için, [0, 3] geri döndürülür.
    # Çünkü 2 + 12 = 15 ve 0. ve 3. indexler bu sayıların indexleridir.
    # Veriler ve target değerleri örnek olarak verilmiştir.


    def toplam_bulucu(self, hedef, veriler):
        # Verileri sete çevirip tekrar tekrar kontrol etmek yerine sadece bir kere kontrol etmek için kullanıyoruz.
        # Bu sayede kontrol sayısı azalır ve performans artar.
        

        liste = set(veriler)
        sonuc = [] # Geri döndürülecek sonuç.
        for i in range(len(veriler)): # Verilen liste içinde tarama yapan döngü.
            fark = hedef - veriler[i] # Hedef değerden verilen liste içindeki elemanı çıkarıp fark değerini buluyoruz.
            if fark in liste: # Eğer fark değeri verilen liste içinde varsa, o elemanın indexini sonuca ekliyoruz.
                sonuc.append(i)
        
        return sonuc # Sonucu geri döndürüyoruz.
        
        
        
if __name__ == "__main__":
    main()