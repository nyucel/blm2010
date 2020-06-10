#Can Kurttekin 170401015

import sympy as sym

import math

x = sym.Symbol('x')

veriler = []
korelasyonlar = []


with open("veriler.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        veriler.append(int(line))



def gaussjordan(x):
    size = len(x)
    for i in range(0, size):
        maxColumn = abs(x[i][i])
        maxrow = i
        for j in range(i + 1, size):
            if abs(x[j][i]) > maxColumn:
                maxColumn = abs(x[j][i])
                maxrow = j
        for k in range(i, size + 1):
            temp = x[maxrow][k]
            x[maxrow][k] = x[i][k]
            x[i][k] = temp
        for l in range(i + 1, size):
            c = -(x[l][i]/x[i][i])
            for j in range(i, size + 1):
                if i == j:
                    x[l][j] = 0
                else:
                    x[l][j] += (c * x[i][j])
    matris = [0 for i in range(size)]
    for i in range(size - 1, -1, -1):
        matris[i] = x[i][size] / x[i][i]
        for k in range(i - 1, -1, -1):
            x[k][size] -= x[k][i] * matris[i]
    return matris

def korelasyon(results, first, last):
    n = last - first
    yi = 0
    for i in range(first, last):
        yi += veriler[i]
    y_ussu = yi/n
    Sr = 0
    for i in range(first, last):
        Sr = (results[i-first] - veriler[i])**2 + Sr
    St = 0
    for i in range(first, last):
        St = St + (veriler[i] - y_ussu)**2
    r2 = abs((St-Sr)/St)
    r = math.sqrt(r2)
    return r



def veriHesap(first, last):
    dizi = []
    n = last - first
    for derece in range(1, 7):
        xVal = []
        for i in range(n):
            xVal.append(i+1)
        m = [[0 for i in range(derece+1)] for j in range(derece+1)]
        size = len(m)
        for i in range(size):
            for j in range(size):
                xSum = 0
                for k in range(n):
                    m[0][0] = len(xVal)
                    xSum = xVal[k]**(i+j) + xSum
                    m[i][j] = xSum
        xyResults = []
        for i in range(size):
            Sum = 0
            for j in range(first, last):
                Sum = Sum + (veriler[j]*(xVal[j-first]**i))
            xyResults.append(Sum)
        k = 0
        for i in m:
            i.append(xyResults[k])
            k = k+1
        katsayi = gaussjordan(m)
        results = []
        for i in range(n):
            toplam = 0
            for j in range(len(katsayi)):
                toplam = toplam + katsayi[j]*((i+1)**j)
                if j == derece:
                    results.append(int(toplam))
        r = korelasyon(results, first, last)
        dizi.append(r)

        best = 100
        index = 0
        for i in range(len(dizi)):
            temp = abs(1-dizi[i])
            if temp < best:
                best = temp
                index = i+1
    print("polinom derecesi: ", index)
    wPol(index, 0, len(veriler))

def wPol(derece, first, last):
    n = last - first
    xdegerleri = []
    for i in range(n):
        xdegerleri.append(i + 1)

    m = [[0 for i in range(derece + 1)] for j in range(derece + 1)]
    size = len(m)

    for i in range(size):
        for j in range(size):
            xSums = 0
            for k in range(n):
                m[0][0] = len(xdegerleri)
                xSums = xdegerleri[k] ** (i + j) + xSums
                m[i][j] = xSums

    xyResults = []
    for i in range(size):
        sum = 0
        for j in range(first, last):
            sum = sum + (values[j] * (xdegerleri[j - first] ** i))
        xyResults.append(sum)

    k = 0
    for i in m:
        i.append(xyResults[k])
        k = k + 1
    katsayilar = gaussjordan(m)
    if len(katsayilar) < 7:
        while len(katsayilar) != 7:
            katsayilar.append(0)

    print("polinom sonucu: \n")
    eq = katsayilar[6] * x ** 6 + katsayilar[5] * x ** 5 + katsayilar[4] * x ** 4 + \
               katsayilar[3] * x ** 3 + katsayilar[2] * x ** 2 + \
               katsayilar[1] * x + katsayilar[0]

    print(eq)

    integral = 0
    a = 5 #170401015
    b = len(values)
    deltax = 0.1
    n = int((b - a) / deltax)
    for i in range(n):
        integral += deltax * (eq.subs({x: a}) + eq.subs({x: a + deltax})) / 2
        a += deltax
    print("integral sonucu : ", integral)


def woPol():
    integral = 0
    a = 5  #170401015
    b = len(values)
    deltax = 1
    n = int((b - a) / deltax)
    for i in range(n - 1):
        integral += deltax * (values[a] + values[a + deltax]) / 2
        a += deltax
    print("polinomsuz integral sonucu: ", integral)


with open("170401015_yorum.txt","w", encoding="utf-8") as f:
    f.write("can kurttekin 170401015\n")
    f.write("Polinomlu ve polinomsuz integral hesaplamalarında farklı sonuçlar çıkmasının nedeni\n")
    f.write("Polinomlu hesapta %100 uygun değerlerle işlem yapmıyoruz. Eğer hata 0 olsaydı ve 2 integral hesabında da delta x'i 1 alsaydık aynı sonucu alırdık.\n")
    f.close()

veriHesap(0, len(veriler))
woPol()
