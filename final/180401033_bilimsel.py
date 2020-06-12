#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Kerem KECEL 180401033

from sympy import Symbol
import math 



def polinom(derece, veri):          #eğriye uydurma işlemi
    matrix = []
    b = 0

    for i in range(derece+1):
        satir= []
        for j in range(derece + 1):
            toplam = 0
            for k in range(1, len(veri)+1):
                toplam += k**b
            satir.append(toplam)
            b += 1
        matrix.append(satir)
        b -= derece

    sonuç = []
    for i in range(derece+1):
        toplam = 0
        for j in range(len(veri)):
            toplam += veri[j]*(j+1)**i
        sonuç.append(toplam)

    for i in range(derece+1):  # Alt üçgensel matris
        bölen = matrix[i][i]
        for j in range(i+1, derece+1):
            bölüm = bölen/matrix[j][i]
            sonuç[j] = sonuç[j]*bölüm-sonuç[i]
            for k in range(derece+1):
                matrix[j][k] = matrix[j][k]*bölüm-matrix[i][k]

    for i in range(derece, -1, -1):  # Üst üçgensel matris 
        bölen = matrix[i][i]
        for j in range(i-1, -1, -1):
            bölüm = bölen/matrix[j][i]
            sonuç[j] = sonuç[j]*bölüm-sonuç[i]
            for k in range(derece+1):
                matrix[j][k] = matrix[j][k]*bölüm-matrix[i][k]

    for i in range(derece+1):
        sonuç[i] = sonuç[i]/matrix[i][i]

    toplam_y = 0
    for i in range(len(veri)):
        toplam_y += veri[i]
    y_ortalama = toplam_y/len(veri)

    toplam_t, toplam_r = 0, 0
    for i in range(len(veri)):
        e = veri[i]
        toplam_t += (veri[i]-y_ortalama)**2
        for j in range(len(sonuç)):
            e -= sonuç[j]*(i+1)**j
        e = e**2
        toplam_r += e
    korelasyon = ((toplam_t-toplam_r)/toplam_t)**(1/2)
    return sonuç, korelasyon


def uygun_derece(k1,k2,k3,k4,k5,k6):
    Korelasyon_Katsayıları=[k1,k2,k3,k4,k5,k6]
    maxeleman = max(Korelasyon_Katsayıları)
    max_k=0
    for i in range(len(Korelasyon_Katsayıları)):
        if Korelasyon_Katsayıları[i] == maxeleman:
            max_k=i
    return max_k




def polinomlu(polinom):
    x = Symbol('x')
    polinomk = 0
    for i in range(len(polinom)):
        polinomk += polinom[i] * (x ** i)
        
    #180401033    
    a=3     
    b=len(liste)                                
    integral = 0
    deltax = 1
    
    
    n = int((b-a)/deltax)
    for j in range(n):
        integral += deltax * (polinomk.subs({x: a}) + polinomk.subs({x: a+deltax}))/2
        a += deltax
    return integral,polinomk


def polinomsuz(veri):
    a=3
    b=len(veri) 
    integral = 0
    deltax = 1
   
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral += deltax * (veri[a] + veri[a+deltax])/2
        a += deltax
    return integral






dosya = open("veriler.txt","r")
liste = dosya.readlines()
for i in range(len(liste)):
    liste[i]=int(liste[i])
polinomlar, k2 = [0] * 6, [0] * 6
for indis in range(0, 6):
    polinomlar[indis], k2[indis] = polinom(indis+1, liste)
dosya.close()
en_uygun_derece = uygun_derece(k2[0],k2[1],k2[2],k2[3],k2[4],k2[5])
print("En uygun polinomun derecesi === ",en_uygun_derece+1)
PolinomluÇözüm= polinomlu(polinomlar[en_uygun_derece])
print(en_uygun_derece+1,". dereceden Polinom kullanarak bulunan integral: ",PolinomluÇözüm)
PolinomsuzÇözüm= polinomsuz(liste)
print("Polinomdan yararlanmadan  bulduğumuz  integral ==== ",PolinomsuzÇözüm)


dosya = open('180401033_yorum.txt','w',encoding='UTF8')
dosya.write('Polinomlu ve polinomsuz hesapladığımız integraller sonuçları birbirinden farklı ama birbirine çok yakındır .\n')
dosya.write('İntegral ile işlem yaparken polinomu dikdörtgenlere ayırıp alanlarını hesapladıktan sonra toplarız.\n')
dosya.write('Bu dikdörtgenlerin enlerini ne kadar küçük değer verirsek ters orantılı olarak o kadar dikdörtgen elde ederiz.\n')
dosya.write('Yani integrale en yakın değeri elde ederiz.Bizde bunu deltax ile belirliyoruz.')
dosya.write('Polinomluda deltaximizi biz seçiyorken polinomsuzda 1dir\n')
dosya.write('Bu yüzden kendi belirlediğimiz değerlerle daha hassas bir yaklaşım elde ederiz. ')

dosya.close()

