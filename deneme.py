print("""
*************
basit hesap makinası yapma programı:
1.Toplama İşlemi
2.Çıkarma İşlemi
3.Çarpma İşlemi
4.Bölme işlemi
************
""")
a=int(input("Birinci Sayı:"))
b=int(input("İkinci Sayı:"))

İşlem=input("İşlemi Giriniz:")

if İşlem=="1":
    print("{}ile {}'nın toplamı {}'dir..".format(a,b,a+b))
elif İşlem=="2":
    print("{}ile {}'nın farkı {}'dir..".format(a,b,a-b))
elif İşlem=="3":
    print("{}ile {}'nın çarpımı {}'dir..".format(a,b,a*b))
elif İşlem=="4":
    print("{} ile {}'nın bölümü {}'dir..".format(a,b,a/b))
else:
    print("Geçersiz İşlem Yaptınız..")