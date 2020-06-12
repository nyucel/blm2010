#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sympy import Symbol


def polinomsuz(a, b, veri):
    c = 0
    d = 1
    n = int((b - a) / d)
    for i in range(n - 1):
        c += d * (veri[a] + veri[a + d]) / 2
        a += d
    return c


def polinom(Po, a, b):
    x = Symbol('x')
    p = 0
    for i in range(len(Po)):
        p += Po[i] * (x ** i)
    c = 0
    d = 1
    n = int((b - a) / d)
    for i in range(n):
        c += d * (p.subs({x: a}) + p.subs({x: a + d})) / 2
        a += d
    return c


def Eniyi(k1, k2, k3, k4, k5, k6):
    kt = [k1, k2, k3, k4, k5, k6]
    maxi = max(kt)
    po = 0
    for i in range(len(kt)):
        if maxi == kt[i]:
            po = i
    return po


def interpolasyon(d, veri):
    m = []
    base = 0

    for i in range(d + 1):
        stri = []
        for j in range(d + 1):
            top = 0
            for k in range(1, len(veri) + 1):
                top += k ** base
            stri.append(top)
            base += 1
        m.append(stri)
        base -= d

        di = []
    for i in range(d + 1):
        top = 0
        for j in range(len(veri)):
            top += veri[j] * (j + 1) ** i
        di.append(top)

    for i in range(d + 1):  # lower triangular with gaussian elimination
        f = m[i][i]
        for j in range(i + 1, d + 1):
            ra = f / m[j][i]
            di[j] = di[j] * ra - di[i]
            for k in range(d + 1):
                m[j][k] = m[j][k] * ra - m[i][k]

    for i in range(d, -1, -1):  # upper triangular with gaussian elimination
        f = m[i][i]
        for j in range(i - 1, -1, -1):
            ra = f / m[j][i]
            di[j] = di[j] * ra - di[i]
            for k in range(d + 1):
                m[j][k] = m[j][k] * ra - m[i][k]

    for i in range(d + 1):
        di[i] = di[i] / m[i][i]

    sy = 0
    for i in range(len(veri)):
        sy += veri[i]
    yg = sy / len(veri)

    st, sr = 0, 0
    for i in range(len(veri)):
        et = veri[i]
        st += (veri[i] - yg) ** 2
        for j in range(len(di)):
            et -= di[j] * (i + 1) ** j
        et = et ** 2
        sr += et
    kt = ((st - sr) / st) ** (1 / 2)
    return di, kt


file = open("veriler.txt", "r")
veri = file.readlines()
a = 4
b = len(veri)
for i in range(len(veri)):
    veri[i] = int(veri[i])
po, k = [0] * 6, [0] * 6
for i in range(0, 6):
    po[i], k[i] = interpolasyon(i + 1, veri)
file.close()

bestpol = Eniyi(k[0], k[1], k[2], k[3], k[4], k[5])
poli = polinom(po[bestpol], a, b)
nopoli = polinomsuz(a, b, veri)
print("İnterpolasyonda ", bestpol + 1, ". derece polinom en düşük korelasyona sahiptir.")
print(bestpol + 1, ". derece polinomun integral değeri: ", poli)
print("Polinomsuz integral değeri: ", nopoli)


def yorum(dosya):
    dosya.write("Ezgi Cengiz 18040134 \n"
                "Sonuclarin farkli cikmasinin nedeni polinom kullanarak yaptigimiz fonksiyonda deltaya cok kucuk degerler  \n"
                "verebildigimiz icin tasmalar azaliyor ve gercege daha yakin sonuc elde ediyoruz. \n"
                "Verileri kullanarak yaptigimiz fonksiyonda ise deger aralıgına en az 1 verdigimiz icin hata payi daha cok artiyor \n")


file1 = open("yorum.txt", "w")
yorum(file1)
file.close()

# In[ ]:
