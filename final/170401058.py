# Şule Nur Yılmaz - 170401058

from math import sqrt

# Veriler

veriler = list()
f = open("veriler.txt", "r")
text = f.readlines()
f.close()
for i in text:
    veriler.append(int(i))


def fonksiyon(a, katsayilar):
    y = 0
    for i in range(len(katsayilar)):
        y += katsayilar[i] * (a) ** i
    return y

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

def en_iyi_polinom(veriler,katsayilar):
    n = len(veriler)
    katsayi_derece = list()
    r_liste = list()
    for j in range(len(katsayilar)):
        katsayi_derece.append([katsayilar[j], j+1])
        yort = 0
        Sr = 0
        St = 0
        for i in range(n):
            yort += veriler[i]
        yort = yort / n
        for k in range(n):
            St += (veriler[k] - yort) ** 2
            Sr += veriler[k] - fonksiyon(k, katsayi_derece[j - 1][0])
        r_kare = abs((St - Sr) / St)
        r = sqrt(r_kare)
        r_liste.append(r)
    en_iyi = r_liste[0]
    index = 0
    for i in range(1, len(r_liste)):
        if en_iyi >= r_liste[i]:
            en_iyi = r_liste[i]
            index = i

    return (katsayi_derece[index], en_iyi)

def polinomluİnt(katsayi, veriler):
    integral = 0
    a = 8 #170401058
    b = len(veriler)
    deltax = 0.01
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral += deltax * (fonksiyon(a,katsayi) + fonksiyon(a+deltax,katsayi)) / 2
        a += deltax
    print("Polinomlu integral : ", integral)

def polinomsuzInt():
    integral = 0
    a = 8  # 170401058
    b = len(veriler)
    deltax = 1
    n = int((b - a) / deltax)
    for i in range(n - 1):
        integral += deltax * (veriler[a] + veriler[a + deltax]) / 2
        a += deltax
    print("Polinomsuz İntegral Değeri: ", integral)

def yorum():
    dosya = open('170401058_yorum.txt', 'w', encoding="UTF-8")
    dosya.write('İntegral sonuclarinin farkli çikmasinin nedeni: \n \n')
    dosya.write("""İntegral hesaplanirken verilen polinom yamuklara bolunur ve bunlarin alanlarini toplayarak hesaplariz.\n
Yamukların eni ne kadar kucuk olursa o kadar ayrintili hesaplama yapilmis olur boylece istedigimiz degere daha yakin bir sonuc elde ederiz. \n
deltax degeri bize bu yamugun enini verir. Polinomlu integralde bu deltax degerini istedigimiz kadar kuculterek yani daha ayrintili hesaplama \n
yaparak polinomsuz integrale gore daha iyi sonuclar elde ederiz. Cunku polinomsuz integralde verilen veriler uzerinden deltax 1 olacak şekilde \n
hesaplama yaparız. Yani yamugun enini 1 alarak çok daha yuzeysel hesaplama yapariz \n
Ozetle polinomlu integral sonucu deltax i daha kucuk tutabilecegimizden polinomsuza gore daha iyi sonuclar verecektir.""")
    dosya.close()



x = en_iyi_polinom(veriler,sonuc(veriler))
print("En düşük hata ile uyan polinom katsayıları: {} \n polinom derecesi: {} \n kolerasyon: {}".format(x[0][0],x[0][1],x[1]))
polinomluİnt(x[0][0],veriler)
polinomsuzInt()
yorum()