def ilk(a,b): #fonksiyon ekledik
    hipo=(a**2)+(b**2)
    hipo= hipo**(1/2)
    return hipo
sayi1=int(input("Bir sayı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz:"))
print("hipotenüs=", round(ilk(sayi1,sayi2),2))