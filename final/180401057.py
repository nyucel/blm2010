from sympy import Symbol
file = open("veriler.txt", "r")
veriler = []
# DeÄerleri veriler dizisine atiyorum
for i in file:  
    veriler.append(int(i))
# dizinin eleman sayisi
elemanSayisi = len(veriler)
toplam_y = 0
# dizideki elemanlarin toplamini buluyorum
for i in range(elemanSayisi):
    toplam_y += veriler[i] 

def gaussYontemi(liste):
    listeUzunlugu = len(liste)
    # sutundaki en yuksek degeri enBuyukDegere atiyorum.
    #enBuyukDegeredeki degerin satirini enbuyuksatira atiyorum.
    for i in range(0, listeUzunlugu):
        enBuyukDeger = abs(liste[i][i])
        enBuyukSatir = i
        for k in range(i + 1, listeUzunlugu):
            if abs(liste[k][i]) > enBuyukDeger:
                enBuyukDeger = abs(liste[k][i])
                enBuyukSatir = k

        # enBuyukDeger deger ile tutu tuttugumuz degerin yerini degistiriyorum.
        for k in range(i, listeUzunlugu + 1):
            tut = liste[enBuyukSatir][k]
            liste[enBuyukSatir][k] = liste[i][k]
            liste[i][k] = tut

        #Sutunlarin altindaki degerleri 0 yapmaya calisiyorum.
        for k in range(i + 1, listeUzunlugu):
            c = -(liste[k][i] / liste[i][i])
            for j in range(i, listeUzunlugu + 1):
                if i == j:
                    liste[k][j] = 0
                else:
                    liste[k][j] += c * liste[i][j]

    # Ust ucgensel matrise gore denklemi cozuyorum.
    sonuc = [0 for i in range(listeUzunlugu)]
    for i in range(listeUzunlugu - 1, -1, -1):
        sonuc[i] = liste[i][listeUzunlugu] / liste[i][i]
        for k in range(i - 1, -1, -1):
            liste[k][listeUzunlugu] -= liste[k][i] * sonuc[i]
    return sonuc#matrisi donduyorum

#Hafta 6 dersindeki denklem sisteminde x^2m e kadar olan x kuvvetleri toplamlarini bulunuyorum
def degerler_x(elemanSayisi):
    degerler = []
    for i in range(0, 13):
        x = 0
        for k in range(elemanSayisi):
            x += (k + 1) ** i
        degerler.append(x)
    return degerler#Dizeye atadıgım degerleri donduruyorum

# Hafta 6 dersindeki denklem sisteminde x^m*y'ye kadar olan toplamlari buluyorum.
def toplam_xy(veriler, elemanSayisi):
    degerler = []
    for i in range(7):
        xiyi = 0
        for k in range(elemanSayisi):
            xiyi += ((k + 1) ** i)*(veriler[k])
        degerler.append(xiyi)
    return degerler

#1. dereceden 6.dereceye kadar olan polinomlara degerleri yaklastiriyorum.
def katsayiBul(veriler, elemanSayisi):
    sonuc = []
    for i in range(2, 8):
        liste=[]
        for j in range(i):
            liste.append([])
            for k in range(i):  
                liste[j].append(degerler_x(elemanSayisi)[k + j])
            liste[j].append(toplam_xy(veriler, elemanSayisi)[j])
            if j == i - 1:  #katsayilari sonuc dizime ekliyorum
                sonuc.append(gaussYontemi(liste))
                liste.clear()
    return sonuc #katsayilari buldugum diziyi donduruyorum

#hafta 6 dersindeki korelasyon bulma formulunu uyguladim
def korelasyon(katSayi, veriler, elemanSayisi, toplam_y):
    ortalama = toplam_y / elemanSayisi
    st = 0
    sr = 0
    #formuldeki st degerimi buluyorum
    for i in range(elemanSayisi):
        st += (veriler[i] - ortalama) ** 2
    #formuldeki sr degerimi buluyorum
    for i in range(elemanSayisi):
        hesaplama = 0
        hesaplama += katSayi[0]
        for j in range(1, len(katSayi)):
            hesaplama += katSayi[j] * (i + 1) ** j
        sr += (veriler[i] - hesaplama) ** 2

    return ((st - sr) / st) ** (1 / 2)#r degerini donduruyorum.

# Buraya korelasyondan gonderdigim r degerlerini yolluyorum
#r degerlerini bir liste haline getiriyorum
def rDegerleriniListele(degerler, veriler, elemanSayisi, toplam_y):
    deger_r = []
    for i in degerler:
        deger_r.append(korelasyon(i, veriler, elemanSayisi, toplam_y))
    return deger_r

#Burada en az hata degerine sahip korelasyonu ve bunun kacıncı dereceden parabol oldugunu bulamaya calisiyorum.
#yani 1 e en yakin parabolu ve degeri.
def enAzHatayiBul(degerler, veriler, elemanSayisi, toplam_y):
    a = rDegerleriniListele(degerler, veriler, elemanSayisi, toplam_y)
    min = 999
    tut = 0
    for i in range(len(a)):
        if int(a[i]) < 1:
            tut = abs(1 - a[i])
        else:
            tut = abs(a[i] - 1)
        if tut < min:
            min = tut
            dondurDeger = a[i]
            dondurDerece = i + 1
    return dondurDerece, dondurDeger

x = Symbol('x')
def fonksiyonYap(x):
    denklem=0
    maxDerece=enAzHatayiBul(katsayiBul(veriler, elemanSayisi), veriler, elemanSayisi, toplam_y)[0]
    for katSayilar in katsayiBul(veriler, elemanSayisi):
        if len(katSayilar) == maxDerece+1:
            z = 0
            for i in range(0,maxDerece+1):
                denklem += katSayilar[z]*(x**i)
                z += 1
    return denklem

def polinomDenklemliIntegral():
    a,b=180401057%10,len(veriler)
    deltax=0.1
    sonuc=0
    n = int((b - a) / deltax)
    polinom=fonksiyonYap(x)
    for i in range(n):
        sonuc += deltax * (polinom.subs({x:a}) + polinom.subs({x:a + deltax}) ) / 2
        a += deltax

    return sonuc

def polinomDenklemsizIntegral():
    a,b=180401057%10,len(veriler)
    deltax=1
    sonuc=0
    n = int((b - a) / deltax)
    for i in range(n-1):
        sonuc += deltax * (veriler[a] + veriler[a + deltax]) / 2
        a += deltax
    return sonuc

def yorum():
    yaz = open("180401057_yorum.txt", 'w', encoding= 'UTF8')
    yaz.write("Deltax ne kadar küçük olursa o kadar gerçek değere okadar yakın bir değer elde ederiz.\n Çünkü polinomu dikdörtgenlere böleriz. Bu sayede dikdörgen alanllarından polinonu buluruz.\nBu sayede deltax i ne kadar küçültürsek dikdortgenlerin alanıda bi okadar küçülücek ve daha hassas bir şekilde polinomu bulmuş olacağız.\n Bununla birlikte, bu iki integral arasındaki farkın ana nedeni deltaks değildir, çünkü ilk integrali polinom haline getirdik, bu nedenle polinomu belirli sayıda korelasyona göre yaklaşıklaştırdık.\n Bu nedenle, eşit deltax değerleri alınsa  bile sonuçların farklı olduğunu görüyoruz. ")
    yaz.close()

print("                     A Şıkkı\n")
print("En Uygun Polinomun Derecesi = ",enAzHatayiBul(katsayiBul(veriler, elemanSayisi), veriler, elemanSayisi, toplam_y),". Derecedir.\n")
print("6. Dereceden Denklemim = ",fonksiyonYap(x))
print("<----------------------------->")
print("                     B Şıkkı\n")
print("Polinomlu İntegral = ", polinomDenklemliIntegral())
print("<----------------------------->")
print("                     C Şıkkı\n")
print("Polinomsuz İntegral = ", polinomDenklemsizIntegral())
print("<----------------------------->")
print("                     D Şıkkı\n")
yorum()
