# Şule Nur Yılmaz

from  math import sqrt


def fonksiyon(listeler, vaka):  #1-2-3-4-5-6. dereceden polinomların sonuçlarını yazdırır.
    k = 0
    for liste in listeler:
        k += 1
        print("{}. Dereceden Polinoma Yaklaşım: ".format(k))
        for i in range(len(vaka)):
            print("Gerçek değer: ", vaka[i], "Yaklaşım:", liste[0]+liste[1]*(i+1)+liste[2]*(i+1)**2+liste[3]*(i+1)**3+liste[4]*(i+1)**4+liste[5]*(i+1)**5+liste[6]*(i+1)**6)


def read_data():    # veriler.txt okur geriye veri listesini döndürür
    data_2 = list()
    data = open("veriler.txt","r")
    veriler = data.read().split("\n")
    data.close()
    for i in range(len(veriler)):
        data_2.append(int(veriler[i]))
    return data_2


#Polinom Yakınlaştırmalarında Katsayılar(a0,...,a7) Crout Bileşenlere Ayırma Yöntemi ile Bulunmuştur. (hafta5pdf//4.7.2)


def birinci_der(vaka):
    n = len(vaka)
    xtoplam = 0
    ytoplam = sum(vaka)
    xiyitoplam = 0
    xikaretoplam = 0
    for i in range(n):
        xtoplam += i+1
        xiyitoplam += (i+1)*vaka[i]
        xikaretoplam += (i+1)*(i+1)
    a1 = (n*xiyitoplam-xtoplam*ytoplam)/(n*xikaretoplam-xtoplam**2)
    a0 = (ytoplam-a1*xtoplam)/n
    return [a0,a1,0,0,0,0,0]

def toplam(vaka):   #matrisi oluşturan veriler döngü ile elde ediliyor liste olarak döndürülüyor.
    n=len(vaka)
    ytoplam = sum(vaka)
    xtoplam,xikaretoplam,xikuptoplam,xidorttoplam,xibestoplam,xialtitoplam,xiyeditoplam,xisekiztoplam,xidokuztoplam,xiontoplam,xionbirtoplam,xionikitoplam = 0,0,0,0,0,0,0,0,0,0,0,0
    xiyitoplam,xikareyitoplam,xikupyitoplam,xidortyitoplam,xibesyitoplam,xialtiyitoplam = 0,0,0,0,0,0
    for i in range(n):
        xtoplam += i + 1
        xikaretoplam += (i + 1) * (i + 1)
        xikuptoplam += (i + 1) ** 3
        xidorttoplam += (i + 1) ** 4
        xibestoplam += (i + 1) ** 5
        xialtitoplam += (i + 1) ** 6
        xiyeditoplam += (i + 1) ** 7
        xisekiztoplam += (i + 1) ** 8
        xidokuztoplam += (i + 1) ** 9
        xiontoplam += (i + 1) ** 10
        xionbirtoplam += (i + 1) ** 11
        xionikitoplam += (i + 1) ** 12
        xiyitoplam += (i + 1) * vaka[i]
        xikareyitoplam += (i + 1) ** 2 * vaka[i]
        xikupyitoplam += (i + 1) ** 3 * vaka[i]
        xidortyitoplam += (i + 1) ** 4 * vaka[i]
        xibesyitoplam += (i + 1) ** 5 * vaka[i]
        xialtiyitoplam += (i + 1) ** 6 * vaka[i]
    liste = [[ytoplam,xiyitoplam,xikareyitoplam,xikupyitoplam,xidortyitoplam,xibesyitoplam,xialtiyitoplam],[n,xtoplam,xikaretoplam,xikuptoplam,xidorttoplam,xibestoplam,xialtitoplam,xiyeditoplam,xisekiztoplam,xidokuztoplam,xiontoplam,xionbirtoplam,xionikitoplam]]
    return liste

def ikinci_der(vaka):
    lis = toplam(vaka)
    liste = list()
    matris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        liste.append(lis[0][i])
    for i in range(3):
        k = i
        for j in range(3):
            matris[i][j]=lis[1][k]
            k +=1
    low = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    up = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for i in range(len(matris)):
        low[i][0] = matris[i][0]
    for i in range(len(matris[0])):
        up[0][i] = matris[0][i] / low[0][0]
    for i in range(1, 3):
        low[i][1] = matris[i][1] - low[i][0] * up[0][1]
    for i in range(2, 3):
        up[1][i] = (matris[1][i] - low[1][0] * up[0][i]) / low[1][1]
    for i in range(2, 3):
        low[i][2] = matris[i][2] - low[i][0] * up[0][2] - low[i][1] * up[1][2]
    d1 = liste[0] / low[0][0]
    d2 = (liste[1] - d1 * low[1][0]) / low[1][1]
    d3 = (liste[2] - d1 * low[2][0] - d2 * low[2][1]) / low[2][2]
    liste_2 = [d1, d2, d3]

    x2 = liste_2[2]
    x1 = liste_2[1] - x2 * up[1][2]
    x0 = liste_2[0] - x2 * up[0][2] - x1 * up[0][1]
    return [x0, x1, x2,0,0,0,0]

def ucuncu_der(vaka):
    lis = toplam(vaka)
    liste = list()
    matris = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        liste.append(lis[0][i])
    for i in range(4):
        k = i
        for j in range(4):
            matris[i][j] = lis[1][k]
            k += 1
    low = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    up = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    for i in range (len(matris)):
        low[i][0] = matris [i][0]

    for i in range (len(matris[0])):
        up[0][i] = matris[0][i]/low[0][0]
    for i in range(1,4):
        low[i][1] = matris[i][1] - low[i][0]*up[0][1]
    for i in range(2,4):
        up[1][i] = (matris[1][i] - low[1][0]*up[0][i])/low[1][1]
    for i in range(2,4):
        low[i][2] = matris[i][2] - low[i][0]*up[0][2] - low[i][1]*up[1][2]
    up[2][3] = (matris[2][3] - low[2][0] * up[0][3] - low[2][1] * up[1][3]) / low[2][2]
    temp = 0
    for i in range(3):
        temp -= low[3][i]*up[i][3]
    low[3][3] = matris[3][3] + temp
    d1 = liste[0]/low[0][0]
    d2 = (liste[1] - d1*low[1][0])/ low[1][1]
    d3 =  (liste[2] - d1*low[2][0] - d2* low[2][1]) /low[2][2]
    d4 = (liste[3] - d1* low[3][0] - d2* low[3][1] - d3*low[3][2])/ low[3][3]
    liste_2 = [ d1, d2, d3, d4]

    x3 = liste_2[3]
    x2 = liste_2[2] - x3*up[2][3]
    x1 = liste_2[1] - x3*up[1][3] - x2*up[1][2]
    x0 = liste_2[0] - x3*up[0][3] - x2*up[0][2] - x1*up[0][1]
    return [x0,x1,x2,x3,0,0,0]

def dort_der(vaka):
    lis = toplam(vaka)
    liste = list()
    matris = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
    for i in range(5):
        liste.append(lis[0][i])
    for i in range(5):
        k = i
        for j in range(5):
            matris[i][j] = lis[1][k]
            k += 1
    low = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
    up = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0],[0, 0, 0, 0, 1]]
    for i in range (len(matris)):
        low[i][0] = matris [i][0]
    for i in range (len(matris[0])):
        up[0][i] = matris[0][i]/low[0][0]
    for i in range(1,5):
        low[i][1] = matris[i][1] - low[i][0]*up[0][1]
    for i in range(2,5):
        up[1][i] = (matris[1][i] - low[1][0]*up[0][i])/low[1][1]
    for i in range(2,5):
        low[i][2] = matris[i][2] - low[i][0] * up[0][2] - low[i][1] * up[1][2]
    for i in range(3,5):
        up[2][i] = (matris[2][i] - low[2][0]*up[0][i] - low[2][1]*up[1][i])/low[2][2]
    for i in range(3,5):
        low[i][3] = matris[i][3] - low[i][0] * up[0][3] - low[i][1] * up[1][3] - low[i][2]*up[2][3]
    up[3][4] = (matris[3][4] - low[3][0]*up[0][4] - low[3][1]*up[1][4] - low[3][2]*up[2][3])/low[3][3]
    temp = 0
    for i in range(4):
        temp -= low[4][i]*up[i][4]
    low[4][4] = matris[4][4] + temp

    d1 = liste[0] / low[0][0]
    d2 = (liste[1] - d1 * low[1][0]) / low[1][1]
    d3 = (liste[2] - d1 * low[2][0] - d2 * low[2][1]) / low[2][2]
    d4 = (liste[3] - d1 * low[3][0] - d2 * low[3][1] - d3 * low[3][2]) / low[3][3]
    d5 = (liste[4]- d1 * low[4][0] - d2 * low[4][1] - d3 * low[4][2] - d4 * low[4][3]) / low[4][4]
    liste_2 = [d1, d2, d3, d4,d5]

    x4 = liste_2[4]
    x3 = liste_2[3] - x4 * up[3][4]
    x2 = liste_2[2] - x4 * up[2][4] - x3 * up[2][3]
    x1 = liste_2[1] - x4 * up[1][4] - x3 * up[1][3] - x2 * up[1][2]
    x0 = liste_2[0] - x4 * up[0][4] - x3 * up[0][3] - x2 * up[0][2] - x1 * up[0][1]
    return [x0, x1, x2, x3,x4,0,0]

def bes_der(vaka):
    lis = toplam(vaka)
    liste = list()
    matris = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for i in range(6):
        liste.append(lis[0][i])
    for i in range(6):
        k = i
        for j in range(6):
            matris[i][j] = lis[1][k]
            k += 1
    low = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    up = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0,1]]
    for i in range(len(matris)):
        low[i][0] = matris[i][0]
    for i in range(len(matris[0])):
        up[0][i] = matris[0][i] / low[0][0]
    for i in range(1, 6):
        low[i][1] = matris[i][1] - low[i][0] * up[0][1]
    for i in range(2, 6):
        up[1][i] = (matris[1][i] - low[1][0] * up[0][i]) / low[1][1]
    for i in range(2, 6):
        low[i][2] = matris[i][2] - low[i][0] * up[0][2] - low[i][1] * up[1][2]
    for i in range(3, 6):
        up[2][i] = (matris[2][i] - low[2][0] * up[0][i] - low[2][1] * up[1][i]) / low[2][2]
    for i in range(3, 6):
        low[i][3] = matris[i][3] - low[i][0] * up[0][3] - low[i][1] * up[1][3] - low[i][2] * up[2][3]
    for i in range(4,6):
        up[3][i] = (matris[3][i] - low[3][0] * up[0][i] - low[3][1] * up[1][i] - low[3][2] * up[2][i]) / low[3][3]
    for i in range(4,6):
        low[i][4] = matris[i][4] - low[i][0] * up[0][4] - low[i][1] * up[1][4] - low[i][2] * up[2][4] - low[i][3] * up[3][4]
    up[4][5] = (matris[4][5] - low[4][0] * up[0][5] - low[4][1] * up[1][5] - low[4][2] * up[2][5] - low[4][3] * up[3][5]) / low[4][4]
    temp = 0
    for i in range(5):
        temp -= low[5][i] * up[i][5]
    low[5][5] = matris[5][5] + temp

    d1 = liste[0] / low[0][0]
    d2 = (liste[1] - d1 * low[1][0]) / low[1][1]
    d3 = (liste[2] - d1 * low[2][0] - d2 * low[2][1]) / low[2][2]
    d4 = (liste[3] - d1 * low[3][0] - d2 * low[3][1] - d3 * low[3][2]) / low[3][3]
    d5 = (liste[4] - d1 * low[4][0] - d2 * low[4][1] - d3 * low[4][2] - d4 * low[4][3]) / low[4][4]
    d6 = (liste[5] - d1 * low[5][0] - d2 * low[5][1] - d3 * low[5][2] - d4 * low[5][3] - d5 * low[5][4]) / low[5][5]
    liste_2 = [d1, d2, d3, d4, d5, d6]

    x5 = liste_2[5]
    x4 = liste_2[4] - x5 * up[4][5]
    x3 = liste_2[3] - x5 * up[3][5] - x4 * up[3][4]
    x2 = liste_2[2] - x5 * up[2][5] - x4 * up[2][4] - x3 * up[2][3]
    x1 = liste_2[1] - x5 * up[1][5] - x4 * up[1][4] - x3 * up[1][3] - x2 * up[1][2]
    x0 = liste_2[0] - x5 * up[0][5] - x4 * up[0][4] - x3 * up[0][3] - x2 * up[0][2] - x1 * up[0][1]
    return [x0, x1, x2, x3, x4, x5,0]

def alti_der(vaka):
    lis = toplam(vaka)
    liste = list()
    matris = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
    for i in range(7):
        liste.append(lis[0][i])
    for i in range(7):
        k = i
        for j in range(7):
            matris[i][j] = lis[1][k]
            k += 1
    low = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
    up = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0, 1]]
    for i in range(len(matris)):
        low[i][0] = matris[i][0]
    for i in range(len(matris[0])):
        up[0][i] = matris[0][i] / low[0][0]
    for i in range(1, 7):
        low[i][1] = matris[i][1] - low[i][0] * up[0][1]
    for i in range(2, 7):
        up[1][i] = (matris[1][i] - low[1][0] * up[0][i]) / low[1][1]
    for i in range(2, 7):
        low[i][2] = matris[i][2] - low[i][0] * up[0][2] - low[i][1] * up[1][2]
    for i in range(3, 7):
        up[2][i] = (matris[2][i] - low[2][0] * up[0][i] - low[2][1] * up[1][i]) / low[2][2]
    for i in range(3, 7):
        low[i][3] = matris[i][3] - low[i][0] * up[0][3] - low[i][1] * up[1][3] - low[i][2] * up[2][3]
    for i in range(4, 7):
        up[3][i] = (matris[3][i] - low[3][0] * up[0][i] - low[3][1] * up[1][i] - low[3][2] * up[2][i]) / low[3][3]
    for i in range(4, 7):
        low[i][4] = matris[i][4] - low[i][0] * up[0][4] - low[i][1] * up[1][4] - low[i][2] * up[2][4] - low[i][3] * up[3][4]
    for i in range(5,7):
        up[4][i] = (matris[4][i] - low[4][0] * up[0][i] - low[4][1] * up[1][i] - low[4][2] * up[2][i] - low[4][3] * up[3][i]) / low[4][4]
    for i in range(5,7):
        low[i][5] = matris[i][5] - low[i][0] * up[0][5] - low[i][1] * up[1][5] - low[i][2] * up[2][5] - low[i][3] * up[3][5] - low[i][4] * up[4][5]
    up[5][5] = (matris[5][5] - low[5][0] * up[0][5] - low[5][1] * up[1][5] - low[5][2] * up[2][5] - low[5][3] * up[3][5] - low[5][4] * up[4][5]) / low[5][5]
    temp = 0
    for i in range(6):
        temp -= low[6][i] * up[i][6]
    low[6][6] = matris[6][6] + temp

    d1 = liste[0] / low[0][0]
    d2 = (liste[1] - d1 * low[1][0]) / low[1][1]
    d3 = (liste[2] - d1 * low[2][0] - d2 * low[2][1]) / low[2][2]
    d4 = (liste[3] - d1 * low[3][0] - d2 * low[3][1] - d3 * low[3][2]) / low[3][3]
    d5 = (liste[4] - d1 * low[4][0] - d2 * low[4][1] - d3 * low[4][2] - d4 * low[4][3]) / low[4][4]
    d6 = (liste[5] - d1 * low[5][0] - d2 * low[5][1] - d3 * low[5][2] - d4 * low[5][3] - d5 * low[5][4]) / low[5][5]
    d7 = (liste[6] - d1 * low[6][0] - d2 * low[6][1] - d3 * low[6][2] - d4 * low[6][3] - d5 * low[6][4] - d6 * low[6][5]) / low[6][6]
    liste_2 = [d1, d2, d3, d4, d5, d6, d7]

    x6 = liste_2[6]
    x5 = liste_2[5] - x6 * up[5][6]
    x4 = liste_2[4] - x6 * up[4][6] - x5 * up[4][5]
    x3 = liste_2[3] - x6 * up[3][6] - x5 * up[3][5] - x4 * up[3][4]
    x2 = liste_2[2] - x6 * up[2][6] - x5 * up[2][5] - x4 * up[2][4] - x3 * up[2][3]
    x1 = liste_2[1] - x6 * up[1][6] - x5 * up[1][5] - x4 * up[1][4] - x3 * up[1][3] - x2 * up[1][2]
    x0 = liste_2[0] - x6 * up[0][6] - x5 * up[0][5] - x4 * up[0][4] - x3 * up[0][3] - x2 * up[0][2] - x1 * up[0][1]
    return [x0, x1, x2, x3, x4, x5, x6]

def sonuc(vaka):    # veri listesini alır geriye tüm polinomların katsayılarını tutan listeyi döndürür
    katsayi = list()
    #1. derece
    katsayi.append(birinci_der(vaka))
    #2. derece
    katsayi.append(ikinci_der(vaka))
    #3.derece
    katsayi.append(ucuncu_der(vaka))
    #4.derece
    katsayi.append(dort_der(vaka))
    #5.derece
    katsayi.append(bes_der(vaka))
    #6.derece
    katsayi.append(alti_der(vaka))
    return katsayi

def tek_deger(liste,i):     # katsayıları liste halinde alır, x'in o anki değerini (i) y'yi döndürür.
    return liste[0]+liste[1]*(i+1)+liste[2]*(i+1)**2+liste[3]*(i+1)**3+liste[4]*(i+1)**4+liste[5]*(i+1)**5+liste[6]*(i+1)**6

def onlu_grup(vaka):    #  her bir 10'lu grup için en uygun polinom yaklaşımını tutan listeyi(hata ve kaçıncı polinom) döndürür.
    text = list()
    k = 10
    i = 0
    while i <= len(vaka):
        katsayilar = sonuc(vaka[i:k])
        min = hata (vaka,katsayilar)
        text.append(min)
        i = k
        k += 10
    return text

def hata(vaka,katsayilar):  # En düşük hata oranı ve onun kaçıncı polinom olduğunu tutan tuple'ı döndürür.
    hatalar = list()
    for j in range(len(katsayilar)):
        Sr = 0
        for i in range(len(vaka)):
            Sr += (vaka[i] - tek_deger(katsayilar[j],i))**2
        standarthata = sqrt(Sr/(len(vaka)-(j+1)))
        hatalar.append(standarthata)
    min = (hatalar[0],1)
    for i in range(1,len(hatalar)):
        if hatalar[i] < min[0]:
            min =(hatalar[i],i+1)
    return min

def sonuc_text(katsayilar ,min, onlu):  # Tüm sonuçları sonuc.txt dosyasına yazdırma
    text = open("sonuc.txt","w")
    k,l=0,9
    for i in katsayilar:
        text.write("a0= {} a1= {} a2= {} a3= {} a4= {} a5= {} a6= {} \n".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    text.write("hata: {} {}. polinoma uygun \n".format(min[0], min[1]))
    for i in onlu:
        text.write("{} - {}  --> hata: {} {}. polinoma uygun \n".format(k,l,i[0],i[1]))
        k +=10
        l +=10
    text.close()


vaka = read_data()  #Verilerin listesi

katsayilar = sonuc(vaka)    #katsayı değerlerinin listesi

min = hata(vaka,katsayilar) #Ana veri grubuna en uygun polinom yaklaşımı ve hata değeri

onlu = onlu_grup(vaka)  #Onlu gruplar için

sonuc_text(katsayilar,min,onlu) #Tüm istenen verilerin sonuc.txt dosyasına yazdırılması

fonksiyon(katsayilar,vaka)  #Gerçek değer ve  tüm polinom yaklaşımlarının değerlerini yazdrıma