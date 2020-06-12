#!/usr/bin/env python
# coding: utf-8

# In[4]:


def yp(x, ks):#ks=katsayı
    fonk = 0
    for i in range(len(ks)):
        fonk += ks[i] * x ** i 
    return fonk
def polinom(veri, ks):
    a = 1 #numara sonundaki rakam
    b = len(veri) #satır
    delta = 1
    integral = 0
    n = int((b - a) / delta)
    for i in range(n):
        integral += delta * (dp(a, ks) + dp(a + delta, ks)) / 2
        a += delta
    return integral
def polinomsuz(veri):
    a = 1
    b = len(veri) 
    delta = 1
    integral = 0
    n = int((b-a) / delta)
    for i in range(n - 1):
        integral += delta * (veri[a] + veri[a + delta]) / 2
        a += delta
    return integral 

def diziye_atama(d):
    dizi = []
    for i in d:
        dizi.append(i[0])
    return dizi

def matris_carpimi(m1, m2):
    r, m = [], []
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            top = 0
            for k in range(len(m2)):
                top += (m1[i][k] * m2[k][j])
            r.append(top)
        m.append(r)
        r = []
    return m

def denklem_coz(m1,m2):
    n = len(m1)
    idizi = list(range(n))
    for i in range(n):
        a = 1.0 / m1[i][i]
        for j in range(n):
            m1[i][j] *= a
        m2[i][0] *= a
        for j in idizi[0:i] + idizi[i+1:]:
            b = m1[j][i]
            for k in range(n):
                m1[j][k] = m1[j][k] - b * m1[i][k]
            m2[j][0] = m2[j][0] - b * m2[i][0]
    return diziye_atama(m2)

def polinoma_uydurma(m, veri):

    n = len(veri)
    xiusToplam = [0] * m * 2
    xiusyiToplam = []
    for i in range(n):
        for j in range(2 * m):
            xiusToplam[j] += (i + 1) ** (j + 1)
        for k in range(m + 1):
            if(len(xiusyiToplam) < m + 1):
                xiusyiToplam.append([0])
            xiusyiToplam[k][0] += (i + 1) ** k * veri[i]
    a = [[]]
    altSinir = 0
    ustSinir = m + 1
    for i in range(m + 1):
        if(i == 0):
            a[0].append(n)
            for j in range(0, m):
                a[0].append(xiusToplam[j])
        else:
            a.append([])
            for k in range(altSinir, ustSinir):
                a[i].append(xiusToplam[k])
            altSinir += 1
            ustSinir += 1
    katsayilar = denklem_coz(a, xiusyiToplam)
    xtoplam = 0
    ytoplam = 0
    for i in range(n):
        xtoplam += i + 1
        ytoplam += veri[i]
    xortalama = xtoplam / n
    yortalama = ytoplam / n
    korelasyon = []
    st = 0
    sr = 0
    for i in range(n):
        b = 0
        for j in range(len(katsayilar)):
            b += katsayilar[j] * (i + 1) ** (j)
        sr += (veri[i] - b) ** 2
        st += (veri[i] - yortalama) ** 2
    r = ((st - sr) / st)
    korelasyon.append(r)
    return katsayilar, korelasyon

def test(dosya):
    veriler = []
    try:
        f = open(dosya, "r")
        for i in f.read().split():
            veriler.append(float(i))
    except IOError:
        print("Veriler bulunamiadı,veriler.txt doyasini kontrol edin.")
    finally:
      f.close()
    korelasyon = [] 
    katsayilar = [] 
    for i in range(1,7):
        tumSonuc = polinoma_uydurma(i, veriler)
        katsayilar.append(tumSonuc[0])
        korelasyon.append(tumSonuc[1][0] ** (1 / 2))
    maxkorelasyon = korelasyon.index(max(korelasyon)) + 1

    print("Polinomlu integral = " , polinom(veriler, katsayilar[maxkorelasyon-1]))
    print("Polinomsuz integral = " , polinomsuz(veriler))

    test("veriler.txt")
def yorum(dosya):
    dosya.write("Harun Orhan 180401031 \n"
                "Yakınlaştırma yapılacak olan polinom derecelerinin küçük değerlerde seçilmesi, sonucun hata payını arttırır. \n"
                "Bu da integral sonuçlarının arasındaki farkın büyümesine neden olur. \n"
                "Böylece sonuçların doğruluk payını arttırabilmek için polinomu daha yüksek dereceden seçeriz. \n"
                )
    
dosya2 = open("yorum.txt","w")
yorum(dosya2)
dosya2.close()

