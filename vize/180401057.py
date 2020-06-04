#                                 BEDIRHAN KARAKAYA
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

#c sikki icin yapmam gereneken gruplandirma islemlerini yaptigim fonksiyon
def grupOlustur(i):
    liste = []
    for j in range(i, i + 10):
        liste.append(veriler[j])
    return liste

#Yazdirma islemlerini yaptigim fonksiyon
def printer():
    filenew = open("sonuc.txt", "w+")
    filenew.write("                    A SIKKI\n")
    filenew.write("       Polinom Degerlerinin Katsayilari\n")
    a = 1
    for i in katsayiBul(veriler, elemanSayisi):
        filenew.write(str(a) + ". polinomun degerleri :")
        for k in i:
            filenew.write("\n" + str(k))

        filenew.write("\n\n" + str(a) + ". elemanin korelasyonu = " + str(korelasyon(i, veriler, elemanSayisi, toplam_y)) + "\n\n")
        a += 1
    filenew.write("                    B SIKKI\n")
    filenew.write("       Polinomlarin En Iyi Korelasyon Degeri\n")
    filenew.write("\nEn iyi korelasyon degeri = " + str(enAzHatayiBul(katsayiBul(veriler, elemanSayisi), veriler, elemanSayisi, toplam_y)) + "\n\n")
    filenew.write("\n                    C SIKKI\n")
    filenew.write("    Onarli Sayi Gruplarinin Korelasyon Degerleri\n")
    for i in range(len(veriler)):
        if i + 10 > len(veriler):
            break
        liste = grupOlustur(i)
        filenew.write("\n"+str(i+1)+" ile "+str(i+10)+" arasindaki degerler\n")
        filenew.write("En iyi korelasyon degeri = " + str(enAzHatayiBul(katsayiBul(liste, len(liste)), liste, len(liste), sum(liste))) + "\n")

    filenew.close()


printer()