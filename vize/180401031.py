#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Harun ORHAN / 180401031

def diziye_atama(m):
    dizi = []
    for i in m:
        dizi.append(i[0])
    return dizi

def matris_carpimi(m1, m2):
    r, m = [], []
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            toplam = 0
            for k in range(len(m2)):
                toplam += (m1[i][k] * m2[k][j])
            r.append(toplam)
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
    xiussuToplam = [0] * m * 2
    xiussuyiToplam = []
    for i in range(n):
        for j in range(2 * m):
            xiussuToplam[j] += (i + 1) ** (j + 1)
        for k in range(m + 1):
            if(len(xiussuyiToplam) < m + 1):
                xiussuyiToplam.append([0])
            xiussuyiToplam[k][0] += (i + 1) ** k * veri[i]
    a = [[]]
    altSinir = 0
    ustSinir = m + 1
    for i in range(m + 1):
        if(i == 0):
            a[0].append(n)
            for j in range(0, m):
                a[0].append(xiussuToplam[j])
        else:
            a.append([])
            for k in range(altSinir, ustSinir):
                a[i].append(xiussuToplam[k])
            altSinir += 1
            ustSinir += 1
    katsayilar = denklem_coz(a, xiussuyiToplam)
    xtoplam = 0
    ytoplam = 0
    for i in range(n):
        xtoplam += i + 1
        ytoplam += veri[i]
    xortalama = xtoplam / n
    yortalama = ytoplam / n
    korelasyon = []
    toplamHata = []
    stahminiHata = []
    st = 0
    sr = 0
    for i in range(n):
        b = 0
        for j in range(len(katsayilar)):
            b += katsayilar[j] * (i + 1) ** (j)
        sr += (veri[i] - b) ** 2
        st += (veri[i] - yortalama) ** 2
    r = ((st - sr) / st)
    syx = (sr / (n - (m + 1))) ** (1 / 2) 
    toplamHata.append(sr)
    korelasyon.append(r)
    stahminiHata.append(syx)
    return katsayilar, korelasyon, toplamHata, stahminiHata

def birdenAltinciDereceyeKadar(dosya):
    veri = []
    r = [] # Korelasyon değerleri
    h = [] # Hata değerleri
    s = [] # Standart hata değerleri
    a = open("sonuc.txt", "w+")
    a.write("Tüm veri için\n")
    for i in range(1, 7):
        if(i != 1):
            a.write("\n")
        tumSonuc = polinoma_uydurma(i, veri)
        a.write(str(i) + ". derece ->\n")
        for j in range(len(tumSonuc[0])):
            f.write("a"+ str(j) +  " = " + str(tumSonuc[0][j]) + "\n")
        r.append(tumSonuc[1][0]**(1/2))
        h.append(tumSonuc[2][0])
        s.append(tumSonuc[3][0])
        f.write("R kare (r^2)= " + str(tumSonuc[1][0]) + "\n")
        f.write("Korelasyon değeri (r)= " + str(tumSonuc[1][0]**(1/2)) + "\n")
        f.write("Hataların karelerinin toplamı (Sr)= " + str(tumSonuc[2][0]) + "\n")
        f.write("Standart tahmini hata değeri (Sy/x)= " + str(tumSonuc[3][0]) + "\n")
    f.write("\n\nTüm veri için en yüksek korelasyon katsayısına sahip derece = " + str(r.index(max(r)) + 1) + "\n")
    f.write("Tüm veri için en düşük hataların karelerinin toplamına sahip derece = " + str(h.index(min(h)) + 1) + "\n")
    f.write("Tüm veri için en düşük standart tahmin hata değerine sahip derece = " + str(s.index(min(s)) + 1))
  
# onlu grup için
    if(len(veri) > 10):
        sinir = len(veri) - 9
        for i in range(sinir):
            r = [] # Korelasyon değerleri
            h = [] # Hata değerleri
            s = [] # Standart hata değerleri
            a.write("\n" + str(i + 1) + "-" + str(i + 10) + " satırlar\n")
            for j in range(1, 7):
                onluSonuc = polinoma_uydurma(j, veri[i:i + 10])
                a.write("\n" + str(j) + ". derece ->\n")
                for k in range(len(onluSonuc[0])):
                    a.write("a"+ str(k) +  " = " + str(onluSonuc[0][k]) + "\n")
                r.append(onluSonuc[1])
                h.append(onluSonuc[2])
                s.append(onluSonuc[3])
                a.write("R kare (r^2)= " + str(onluSonuc[1][0]) + "\n")
                a.write("Korelasyon değeri (r)= " + str(onluSonuc[1][0]**(1/2)) + "\n")
                a.write("Hataların karelerinin toplamı (Sr)= " + str(onluSonuc[2][0]) + "\n")
                a.write("Standart tahmini hata değeri (Sy/x)= " + str(onluSonuc[3][0]) + "\n")
            a.write("\n\n" + str(i + 1) + "-" + str(i + 10) + " satırlar için en yüksek korelasyon katsayısına sahip derece = " + str(r.index(max(r)) + 1) + "\n")
            a.write(str(i + 1) + "-" + str(i + 10) + " satırlar için en düşük hataların karelerinin toplamına sahip derece = " + str(h.index(min(h)) + 1) + "\n")
            a.write(str(i + 1) + "-" + str(i + 10) + " satırlar için en düşük standart tahmin hata değerine sahip derece = " + str(s.index(min(s)) + 1) + "\n\n")
    a.close()

    birdenAltinciDereceyeKadar("veriler.txt")

