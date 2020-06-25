#Bedirhan Karakaya  180401057
from sympy import Symbol
from sympy import pprint

"""kaca_kadar=600
satir_sayisi=1
asallar = [2]

for i in range(3,kaca_kadar,2):
    bolundu = False
    limit = (i ** 0.5) + 1
    for j in asallar:
        if i % j == 0:
            bolundu=True
            break
        if j > limit:
            break
    if bolundu == False:
        asallar.append(i)
        satir_sayisi += 1
filenew = open("asallar.txt", "w+")
for i in asallar :
    filenew.write(str(i))
    filenew.write("\n")
filenew.close()
#print("asallar.txt nin satir sayisi = ",satir_sayisi)
"""
f = open("asallar.txt", "r")
asallar = []
satir_sayisi = 0
for i in f:
    asallar.append(int(i))
    satir_sayisi += 1


def GaussYontemi(liste):
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

def degerler_xi(elemanSayisi):
    degerler = []
    for i in range(0, 7):
        x = 0
        for k in range(elemanSayisi):
            x += (k + 1) ** i
        degerler.append(x)
    return degerler

def toplam_xiyi(veriler, elemanSayisi):
    degerler = []
    for i in range(4):
        xiyi = 0
        for k in range(elemanSayisi):
            xiyi += ((k + 1) ** i)*(veriler[k])
        degerler.append(xiyi)
    return degerler

def katsayiBulma(veriler, elemanSayisi):
    sonuc=[]
    liste=[]
    for j in range(4):
        liste.append([])
        for k in range(4):
            liste[j].append(degerler_xi(elemanSayisi)[k + j])
        liste[j].append(toplam_xiyi(veriler, elemanSayisi)[j])
        if j == 4 - 1:  #katsayilari sonuc dizime ekliyorum
            sonuc.append(GaussYontemi(liste))
            liste.clear()
    return sonuc
x = Symbol('x')
def f(x):
    denklem=0
    maxDerece=3
    for katSayilar in katsayiBulma(asallar,satir_sayisi):
        if len(katSayilar) == maxDerece+1:
            z = 0
            for i in range(0,maxDerece+1):
                denklem += katSayilar[z]*(x**i)
                z += 1
    return denklem

#Merkezi Farklar Yöntemi ile Yaptım.
def polinomluTurev():
    x0 = 180401057 % 100
    h = 0.001
    denklem=f(x)
    xprime = (denklem.subs({x:x0+h})-denklem.subs({x:x0-h}))/(2*h)
    return xprime

def polinomsuzTurev():
    x0 =180401057 % 100
    h = 1
    xprime=(asallar[x0-1+h]-asallar[x0-1-h])/(2*h)
    return xprime

def yorum():
    yaz = open("yorum.txt", 'w', encoding= 'UTF8')
    yaz.write(" Bu iki fonkiyonun  sonuçlarının farkının en önemli sebeplerinden biri polinomsuz türevde aralığı yani h değerini \n")
    yaz.write("1 tutabiliyoruz çünkü polinomsuz türevde h değeri önemli değil öenmli olan değer sayısıdır. polinomlu türevde \n")
    yaz.write("ise gerçeğe yaklaşmak için h değerimizi olabildiğince küçültmek isteriz. Çünkü ne kadar\n")
    yaz.write("h değerini küçültürsek hesaplayacağımız alan daha küçük olur ve bu sayede daha hassas olçüm yapıp değerimizin gerçeğe daha yakın olmasını sağlarız.")
    yaz.close()

def printer():
    print("            A ŞIKKI")
    katSayilar=katsayiBulma(asallar,satir_sayisi)
    print("polinomun katsayıları : ", katSayilar)
    print("<--------------------------------->")
    print("            B ŞIKKI")
    print("Polinom Kullanarak Bulduğum Sonuç : ",polinomluTurev())
    print("<--------------------------------->")
    print("            C ŞIKKI")
    print("Polinom Kullanmadan Bulduğum Sonuç : ",polinomsuzTurev())
    print("<--------------------------------->")
    # D şıkkı
    yorum()
printer()