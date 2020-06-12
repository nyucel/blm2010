#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import Symbol

def polinoma_cevirme(derece,veriler):
    matris = []
    a = 0
    for i in range(derece+1):
        satir = []
        for j in range(derece+1):
            toplam = 0
            for k in range(1,len(veriler)+1):
                toplam += k**a
            satir.append(toplam)
            a += 1
        matris.append(satir)
        a -= derece
    sonuc = []
    for i in range(derece+1):
        toplam = 0
        for j in range(len(veriler)):
            toplam += veriler[j]*(j+1)**i
        sonuc.append(toplam)
    for i in range(derece+1):
        b = matris[i][i]
        for j in range(i+1,derece+1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]
    for i in range(derece,-1,-1):
        b = matris[i][i]
        for j in range(i-1,-1,-1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]
    for i in range(derece+1):
        sonuc[i] = sonuc[i]/matris[i][i]
    y_ort=0
    for i in range (len(veriler)):
        y_ort += veriler[i]
    y_ort = y_ort/len(veriler)
    St=0
    Sr=0
    for i in range(len(veriler)):
        x = veriler[i]
        St +=(veriler[i]-y_ort)**2
        for j in range(len(sonuc)):
            x -= sonuc[j]*(i+1)**j
        x=x**2
        Sr += x
    korelasyon = ((St-Sr)/St)**(1/2)
    return sonuc,korelasyon

def uygun_polinom_derecesini_bul(katsayilar):
    max_eleman = max(katsayilar)
    for i in range(len(katsayilar)):
        if katsayilar[i] == max_eleman:
            derece = i
    return derece


def polinomlu_integral_bul(polinomlar):
    x = Symbol('x')
    polinom = 0
    for i in range(len(polinomlar)):
        polinom += polinomlar[i] * (x ** i)
    a,b=1,len(veriler)
    integral = 0
    deltax = 1
    n = int((b-a)/deltax)
    for j in range(n):
        integral += deltax * (polinom.subs({x: a}) + polinom.subs({x: a+deltax}))/2
        a += deltax
    return integral,polinom


def polinomsuz_integral_bul(veriler):
    a,b=1,len(veriler)
    integral = 0
    deltax = 1
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral += deltax * (veriler[a] + veriler[a+deltax])/2
        a += deltax
    return integral

def yorum(dosya):
    yorum = "Lara Betül Arslantaş / 180401024 \n "             "Integral hesaplarken hesapladığımız polinomu dikdörtgenlere böler ve bu dikdörtgenlerin alanlarını hesaplayıp toplarız.\n"             "Bu dikdörtgenlerin eni ne kadar küçük olursa sonuç o kadar gerçeğe yakın olur. \n"             "Fakat bu hesaplanan iki fonksiyonda da dikdörtgenin eni(deltax) eşit alındı ve farklı sonuç çıktı. \n"             "Bunun sebebi bulduğumuz 6. dereceden polinomun orjinal polinoma belirli bir hata oranı olacak şekilde yakın olmasıdır."             "Eğer orjinal polinomu elde etmiş olsaydık(korelasyon katsayısı 1 olsaydı) sonuçlar aynı çıkacaktı."
    yorum_dosyasi = open(dosya,"w")
    yorum_dosyasi.write(yorum)
    yorum_dosyasi.close()


#main
dosya = open("veriler.txt","r")
veriler = dosya.readlines()
for i in range(len(veriler)):
    veriler[i]=int(veriler[i])
p, korelasyonlar = [0] * 6, [0] * 6
for s in range(0, 6):
    p[s], korelasyonlar[s] = polinoma_cevirme(s+1, veriler)
dosya.close()
en_uygun_polinom_derecesi = uygun_polinom_derecesini_bul(korelasyonlar)
print("Verilere en uygun polinomun derecesi : ",en_uygun_polinom_derecesi+1)
polinomlu_integral,kullanilan_polinom = polinomlu_integral_bul(p[en_uygun_polinom_derecesi])
print("\nKullanılan polinom : ",kullanilan_polinom)
print("\nPolinom kullanarak bulunan integral : ",polinomlu_integral)
polinomsuz_integral = polinomsuz_integral_bul(veriler)
print("\nPolinom kullanmadan bulunan integral : ",polinomsuz_integral)
yorum('180401024_yorum.txt')


# In[ ]:
