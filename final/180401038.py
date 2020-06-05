with open('veriler.txt','r') as data:
    dataList = [int(veri) for veri in data]
data.close()

def xy_toplam(veriler,üs,baslangıc):
    toplam = 0
    for x in range(len(veriler)):
        toplam += veriler[x]*((x+baslangıc)**üs)
    return toplam

def xToplam(min,max,üs):
    toplam = 0
    for i in range (min,max+1):
        toplam = toplam + (i**üs)

    return toplam

def matrisÇöz(veriMatrisi):
    uzunluk = len(veriMatrisi)
    for i in range(0, uzunluk):
        max_Sutun = abs(veriMatrisi[i][i])
        max_Satir = i
        for j in range(i + 1, uzunluk):
            if abs(veriMatrisi[j][i]) > max_Sutun:
                max_Sutun = abs(veriMatrisi[j][i])
                max_Satir = j
        for k in range(i, uzunluk + 1):
            temp = veriMatrisi[max_Satir][k]
            veriMatrisi[max_Satir][k] = veriMatrisi[i][k]
            veriMatrisi[i][k] = temp

        for l in range(i + 1, uzunluk):
            c = -veriMatrisi[l][i] / veriMatrisi[i][i]
            for j in range(i, uzunluk + 1):
                if i == j:
                    veriMatrisi[l][j] = 0
                else:
                    veriMatrisi[l][j] += c * veriMatrisi[i][j]

    matris = [0 for i in range(uzunluk)]
    for i in range(uzunluk - 1, -1, -1):
        matris[i] = veriMatrisi[i][uzunluk] / veriMatrisi[i][i]
        for k in range(i - 1, -1, -1):
            veriMatrisi[k][uzunluk] -= veriMatrisi[k][i] * matris[i]
    return matris

def matris_olustur(veriler , xBas):
    kat_sayılar = []
    if (xBas == 0):
        temp = 1
    elif(xBas == 1):
        temp = 0
    uzunluk = len(veriler)
    for derece in range(1, 7):
        matris = []
        for k in range(derece + 1):  # satır işlemleri
            satır = []
            for j in range(derece + 1):  # sütun işlemleri
                if (k == 0 and j == 0):
                    satır.append(uzunluk)
                else:
                    satır.append(xToplam(1, (uzunluk - temp) , j + k))

            satır.append(xy_toplam(veriler,k,xBas))
            matris.append(satır)

        kat_sayılar.append(matrisÇöz(matris))
    return kat_sayılar

def hataOranı(katsayılar,veri_dizisi,xBas):
    hata_oranları = []

    for denklem in katsayılar:
        hesaplar = []
        for x_verisi in range(xBas,len(veri_dizisi)+xBas):
            hesaplanan_veri = 0
            for k in range(len(denklem)):
                hesaplanan_veri = hesaplanan_veri +  denklem[k]*(x_verisi**k)
            hesaplar.append(hesaplanan_veri)

        sr = 0
        for index in range(len(veri_dizisi)):
            sr = sr + ((veri_dizisi[index] - hesaplar[index])**2)

        a1 = len(veri_dizisi)
        a2 = (len(denklem)-1)
        payda = a1 - (a2+1)
        if (payda == 0):
            payda = -1

        standart_tahmini_hata = (sr/payda)**(1/2)
        hata_oranları.append(standart_tahmini_hata)
    min_hata = hata_oranları[0]
    for i in hata_oranları:
        if (i < min_hata):
            min_hata = i

    return min_hata , (hata_oranları.index(min_hata)+1), katsayılar[hata_oranları.index(min_hata)]

def fxPol(x):
    katsayilar = bestPolyCoeff
    hesaplanan = 0
    for i in range(len(katsayilar)):
        hesaplanan += katsayilar[i] * (x ** i)
    return hesaplanan


hata,oran,bestPolyCoeff = hataOranı(matris_olustur(dataList,1),dataList,1)
dosya = open('180401038_yorum.txt', 'w')

# Öğrenci numaram 180401038 a değeri = 8
a = 8
b = len(dataList)

deltaX = 0.001
integralSonuc = 0
n = int((b - a) / deltaX)

for i in range(n):
    integralSonuc += deltaX * (fxPol(a) + fxPol(a + deltaX)) / 2
    a += deltaX

print("Polinom kullanarak çıkan integral sonucu : " + str(integralSonuc))
dosya.write("Polinom kullanarak hesaplanan alan : " + str(integralSonuc))

# Öğrenci numaram 180401038 a değeri = 8
a = 8
b = len(dataList)

integralSonuc = 0
for i in range(a - 1, b - 1):
    integralSonuc += (dataList[i] + dataList[i + 1]) / 2

print("Polinom kullanmadan çıkan integral sonucu : " + str(integralSonuc))

dosya.write("\nPolinom kullanmadan hesaplanan alan : " + str(integralSonuc))
dosya.write("""\nSonuçların farklı çıkma sebebi delta_x'e verdiğimiz değerden dolayıdır.
delta_x ne kadar küçük olursa hesaplanan alan o kadar çok artar ve gerçeğe daha yakın olur.
Grafik ile alan arasındaki boşluklar kapanır ve taşmalar azalır bu sebepten dolayı hata oranıda azalır.
Polinomlu olan hesaplamada delta_x daha küçük olduğundan daha çok alan hesabı yapabiliyoruz. Bu da polinomsuza göre
istenilen sonuca daha yakın bir cevap çıkarıyor.
Polinomsuz olanda delta_x'i 1 alıyoruz bu da aslında sadece elimizdeki verileri kullandığımızı gösteriyor. Hata oranı daha fazla
oluyor, taşmalar yaşanabiliyor. Sonuçların farklı çıkmasının nedenleri bunlardır.

""")
