

def main():
    print("Hesap Makinası Uygulamasına Hoş Geldiniz")
    print("Çıkış yapmak için istediğiniz zaman 'q' veya 'Q' tuşuna basabilirsiniz")

    adimSayisi = 1

    while adimSayisi <= 3:
        if adimSayisi == 1:
            ilkGiris = input("İlk Sayıyı Giriniz: ")
            if CikalimMi(ilkGiris):
                adimSayisi = 4
            elif SayiMi(ilkGiris):
                ilkSayi = int(ilkGiris)
                adimSayisi = 2
            else:
                print("Lütfen Bir Sayi Giriniz")
        elif adimSayisi == 2:
            operator = input("İşlem Operatörünü Giriniz: ")
            if CikalimMi(operator):
                adimSayisi = 4
            elif operator == "+":
                islem = "topla"
                adimSayisi = 3
            elif operator == "-":
                islem = "Çikar"
                adimSayisi = 3
            elif operator == "*" or operator == "x":
                islem = "çarp"
                adimSayisi = 3
            elif operator == "/":
                islem = "böl"
                adimSayisi = 3
            else:
                print("Hatalı Operatör Girdiniz. Lütfen Aşağıdaki Operatörlerden Birini Seçiniz:")
                print("+ : Toplama")
                print("- : Çıkarma")
                print("* veya x : Çarpma")
                print("/ : Bölme")
                print("q : Çıkış")
        elif adimSayisi == 3:
            ikinciGirdi = input("İkinci Sayıyı Giriniz: ")
            if CikalimMi(ikinciGirdi):
                adimSayisi = 4
            elif SayiMi(ikinciGirdi):
                ikinciSayi = int(ikinciGirdi)
                islemYap(ilkSayi, ikinciSayi, islem)
                adimSayisi = 1
            else:
                print("Lütfen Bir Sayi Giriniz")
        

    print("İşlem yaptığınız için teşekkür ederiz")


def CikalimMi(giris):
    if giris == "q" or giris == "Q":
        return True
    else:
        return False

def SayiMi(girdi):
    try:
        deneme = int(girdi)
        if deneme == int(girdi):
            return True
    except:
        return False

def islemYap(ilkSayi, ikinciSayi, islem):
    if islem == "topla":
        print(f"{ilkSayi} + {ikinciSayi} = {ilkSayi + ikinciSayi}")
    elif islem == "çikar":
        print(f"{ilkSayi} - {ikinciSayi} = {ilkSayi - ikinciSayi}")
    elif islem == "çarp":
        print(f"{ilkSayi} * {ikinciSayi} = {ilkSayi * ikinciSayi}")
    elif islem == "böl":
        if ikinciSayi == 0:
            print("0'a bölme işlemi yapılamaz")
        else:
            print(f"{ilkSayi} / {ikinciSayi} = {ilkSayi / ikinciSayi:.3f}")


if __name__ == "__main__":
    main()