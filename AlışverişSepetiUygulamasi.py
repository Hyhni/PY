# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16CLvjyziwTvHhAJWjoBQWUh8MMfGktKH
"""

class Urun:
    def __init__(self, ad, fiyat, miktar):
        self.ad = ad
        self.fiyat = fiyat
        self.miktar = miktar

    def __str__(self):
        return f"Ürün: {self.ad}, Fiyat: {self.fiyat} TL, Miktar: {self.miktar}"


class Sepet:
    def __init__(self):
        self.urunler = [
            {"urunisim": "ayakkabı", "fiyat": 15, "miktar": 1},
            {"urunisim": "telefon", "fiyat": 5, "miktar": 1}
        ]

    def urun_ekle(self, ad, fiyat, miktar):
        for urun in self.urunler:
            if urun["urunisim"].lower() == ad.lower():
                urun["miktar"] += miktar
                print(f"{ad} sepetinizde mevcut, miktarı güncellendi: {urun['miktar']}")
                return
        yeni_urun = {"urunisim": ad, "fiyat": fiyat, "miktar": miktar}
        self.urunler.append(yeni_urun)
        print(f"Ürün eklendi: Ürün: {ad}, Fiyat: {fiyat} TL, Miktar: {miktar}")

    def urun_cikar(self, ad):
        for urun in self.urunler:
            if urun["urunisim"].lower() == ad.lower():
                self.urunler.remove(urun)
                print(f"{ad} sepetten çıkarıldı.")
                return
        print(f"{ad} adlı ürün sepetinizde bulunamadı.")

    def sepeti_listele(self):
        if not self.urunler:
            print("Sepetiniz boş.")
        else:
            print("\nSepetiniz:")
            for urun in self.urunler:
                print(f"Ürün: {urun['urunisim']}, Fiyat: {urun['fiyat']} TL, Miktar: {urun['miktar']}")

    def toplam_tutar(self):
        toplam = sum(urun["fiyat"] * urun["miktar"] for urun in self.urunler)
        print(f"Toplam tutar: {toplam:.2f} TL")


def menu():
    sepet = Sepet()

    while True:
        print("\nAlışveriş Sepeti Uygulaması")
        print("1. Ürün Ekle")
        print("2. Sepeti Listele")
        print("3. Ürün Çıkar")
        print("4. Toplam Tutarı Gör")
        print("5. Çıkış")
        secim = input("Seçiminizi yapın (1-5): ")

        if secim == "1":
            ad = input("Ürün adı: ")
            fiyat = float(input("Ürün fiyatı: "))
            miktar = int(input("Ürün miktarı: "))
            sepet.urun_ekle(ad, fiyat, miktar)
        elif secim == "2":
            sepet.sepeti_listele()
        elif secim == "3":
            ad = input("Çıkarmak istediğiniz ürünün adı: ")
            sepet.urun_cikar(ad)
        elif secim == "4":
            sepet.toplam_tutar()
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

try:
    menu()
except KeyboardInterrupt:
    print("\nProgram kullanıcı tarafından durduruldu. Çıkılıyor...")
