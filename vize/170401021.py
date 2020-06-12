#Cihan Kavuk
#170401021



import math

def oku():
    dosya = open("veriler.txt")
    y = dosya.readlines()
    x=[]
    for i in range(len(y)):
        y[i]=int(y[i])
        x.append(i)
    return x,y

def matris_olustur(x, y, n, m):
    matris = []
    for i in range(m + 1):
        satir = []
        for j in range(m + 1):
            if (i == 0 and j == 0):
                satir.append(n)
            else:
                x_toplam = 0
                for x_eleman in x:
                    x_toplam += x_eleman ** (i + j)
                satir.append(x_toplam)
        sum_ = 0
        for eleman in range(n):
            sum_ += (x[eleman] ** i) * y[eleman]
        satir.append(sum_)
        matris.append(satir)
    return matris


def gausselimination(matris):  # Gauss
    boyut = len(matris)
    for i in range(0, boyut):
        maxSutun = abs(matris[i][i])
        maxSatir = i
        for j in range(i + 1, boyut):
            if abs(matris[j][i]) > maxSutun:
                maxSutun = abs(matris[j][i])
                maxSatir = j
        for k in range(i, boyut + 1):
            temp = matris[maxSatir][k]
            matris[maxSatir][k] = matris[i][k]
            matris[i][k] = temp

        for l in range(i + 1, boyut):
            c = -matris[l][i] / matris[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    matris[l][j] = 0
                else:
                    matris[l][j] += c * matris[i][j]

    r_matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        r_matris[i] = matris[i][boyut] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][boyut] -= matris[k][i] * r_matris[i]
    return r_matris

def korelasyon_ve_hata(x,y,n,katsayilar,m):
    Sr,St,y_= 0,0,0
    for i in y:
        y_+= i
    y_ /= len(y)
    for i in range(n):
        Sr_1=0
        St += (y[i]-y_)**2
        Sr_1 += y[i]-katsayilar[0]
        for j in range(1,m+1):
            Sr_1 -= katsayilar[j]*(x[i]**j)
        Sr_1 = Sr_1**2
        Sr+=Sr_1
    S_y_x = math.sqrt(abs(Sr/(n-(m+1)))) #Standart tahmini hata
    r = math.sqrt(abs((St-Sr)/St)) #korelasyon
    return r,S_y_x

def pol_yakinlastir(x,y,dosya):
    korel = []
    dosya.write('------------------------------------------------------- \n')
    for i in range(1,7):
        matris = matris_olustur(x,y,len(y),i)
        katsayılar = gausselimination(matris)
        dosya.write(f'{i}. dereceden fonkisyonun katsayıları: {katsayılar} \n')
        korel.append(korelasyon_ve_hata(x,y,len(y),katsayılar,i))
        dosya.write(f'Korelasyon katsayısı= {korel[i-1][0]} \n')
        dosya.write(f'Standart tahmini hata= {korel[i-1][1]} \n')
    max,min,temp,w =korel[0][0],korel[0][1],0,0
    for i in range(len(korel)):
        if korel[i][0] > max:
            temp = max
            w = i
            max = korel[i][0]
            if temp < min:
                min = temp
    dosya.write(f'en büyük korelasyon: {max}\nen küçük korelasyon: {min}\nen uygun {w+1}. polinom \n')
    onlusirala(y,dosya)

def onlusirala(y,dosya):
    liste=[]
    liste2=[]
    uzunluk = len(y)
    uzunluk10 = int(uzunluk/10)
    sonsayi,baslangic = 10,0
    korel = []
    z = 0
    for x in range(uzunluk10):
        for i in range(baslangic,sonsayi):
            liste.append(y[i])
        for i in range(len(liste)):
            liste2.append(i)
        for t in range(1,7):
            katsayilar = gausselimination(matris_olustur(liste2,liste,len(liste),t))
            korel.append(korelasyon_ve_hata(liste2,liste,len(liste),katsayilar,t))
            max, min, temp, w = korel[0][0], korel[0][1], 0, 0
            for i in range(len(korel)):
                if korel[i][0] > max:
                    temp = max
                    w = i
                    max = korel[i][0]
                    if temp < min:
                        min = temp
        dosya.write(f'{z+1}. aralikta en uygun polinom : {w+1}. polinom \n')
        w = 0
        baslangic+=10
        sonsayi+=10
        korel.clear()
        liste.clear()
        liste2.clear()
        z+=1



x,y = oku()
sonuc = open('sonuc.txt','w')
pol_yakinlastir(x,y,sonuc)

