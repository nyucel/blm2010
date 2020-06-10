# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:48:12 2020
@author: Ozgur Kucet
"""

from math import sqrt

def MatrisinSatiriniKatsayıIleCarp(matris,katsayi,satir):
    for i in range(len(matris[0])):
        matris[satir][i] *= katsayi

def ElementerSatirIslemi(matris,i,j):#satırlar birbirinden çıkartılır...
    for k in range(len(matris[0])):
        matris[j][k] -= matris[i][k]
                  
def SatrıcaIndirgenmisEsolonaCevir(matris):#Gauss jordan yöntemi için önce alt üçgensel sonra üst üçgensel yaparak geri döndürür.
    for i in range(len(matris)):
        for j in range(i+1,len(matris)):
            katsayi = matris[i][i]/matris[j][i]
            MatrisinSatiriniKatsayıIleCarp(matris, katsayi, j)
            ElementerSatirIslemi(matris,i,j)
        
    for i in range(len(matris)-1,0,-1):
        for j in range(i,0,-1):
            katsayi=matris[j-1][i]/matris[i][i]
            MatrisinSatiriniKatsayıIleCarp(matris,katsayi,i)
            ElementerSatirIslemi(matris, i, j-1)
                    
    return matris
 
def sumxi_uzeri_n_x_yi(dizi,n):#çözülecek matris bulunurken kullandım.
    toplam = 0
    if n==0:
        return sum(dizi)
    for i in range(len(dizi)):
        toplam+=(dizi[i]*((i+1)**n))
    return toplam

def sumxi_uzeri_n1(dizi,n):#çözülecek matris bulunurken kullandım.
    if(n==0):
        return len(dizi)
    toplam = 0
    for i in range(1,len(dizi)+1):
        toplam+=i**n
    return toplam

def matriseDegeriYaz(matris,deger,neresi):#Çapraz değerler aynı olduğu için bunu kullanarak matrise yazdırdım.
    for i in range(len(matris)):
        for j in range(len(matris[1])-1):
            if i+j == neresi:
                matris[i][j] = deger
    return matris

def PolinomaYaklaştırmaMetodu(dizi,m):#Bu kusımda denklemler bulunup gauss jordan yöntemi ile çözülür ve sonuçlarıda geri döndürülür.
    n=len(dizi)
    matris = [[0 for x in range(m+2)]for y in range(m+1)] #(m+1)x(m+2) dinamik matris oluşturmak
    for i in range(len(matris)):
        matris[i][m+1] = sumxi_uzeri_n_x_yi(dizi,i)
    for i in range((m*2)+1):
        matriseDegeriYaz(matris,sumxi_uzeri_n1(dizi,i),i)
    #Denklemler artık oluştu ve matrise yazılıldı şimdi o matrisi çözüp sonuçlarını alıcam.
    matris = SatrıcaIndirgenmisEsolonaCevir(matris)  
    sonuclar = []
    for i in range(len(matris)):
        sonuc = matris[i][len(matris)]/matris[i][i]
        sonuclar.append(sonuc)
    return sonuclar

with open("veriler.txt","r") as dosya:#Dosyadan veriler okunur.
    icerik = dosya.read()
    sayilar = icerik.split("\n")
    j=0
    for i in range(len(sayilar)):
        if sayilar[j] == '': #Bunu yapmamın sebebi veriler.txt de alt satıra geçilmiş boş satırlar olmasıydı.
            sayilar.remove(sayilar[j])
            j+=-1
        j+=1
    for i in range(len(sayilar)):#sayıları string olarak alıyordu hesaplarken sıkıntı olmaması için.
        sayilar[i] = int(sayilar[i])
    n=len(sayilar)
       
def Sr(derece,liste,sayilar):
    n = len(sayilar)
    tüm = 0
    temp = 0
    for i in range(1,n+1):
        toplam = 0
        toplam += sayilar[i-1]-liste[0]
        for j in range(1,derece+1):
            temp += liste[j]*(i**j)
        toplam-=temp
        temp = 0
        tüm += toplam**2
    return tüm

def y_(sayilar):
    n = len(sayilar)
    toplam = 0
    for i in range(n):
        toplam+=sayilar[i]
    return toplam/n

def St(sayilar):
    toplam = 0
    n = len(sayilar)
    cızgı_y = y_(sayilar)
    for i in range(n):      
        toplam += (sayilar[i]-cızgı_y)**2
    return toplam

def sonuclarıYazma(sonuclar):#sonucları yazdırırken kullanıyorum
    if len(sonuclar)==2:
        print("1.dereceden polinom a0:"+str(sonuclar[0]) + "a1:"+str(sonuclar[1]))
    elif len(sonuclar)==3:
        print("2.dereceden polinom a0:"+str(sonuclar[0]) + "a1:"+str(sonuclar[1])+" a2:"+str(sonuclar[2]))
    elif len(sonuclar)==4:
        print("3.dereceden polinom a0:"+str(sonuclar[0]) + "a1:"+str(sonuclar[1])+" a2:"+str(sonuclar[2])+"a3:"+str(sonuclar[3]))
    elif len(sonuclar)==5:
        print("4.dereceden polinom a0:"+str(sonuclar[0]) + "a1:"+str(sonuclar[1])+" a2:"+str(sonuclar[2])+"a3:"+str(sonuclar[3])+"a4:"+str(sonuclar[4]))
    elif len(sonuclar)==6:
        print("5.dereceden polinom a0:"+str(sonuclar[0]) + "a1:"+str(sonuclar[1])+" a2:"+str(sonuclar[2])+"a3:"+str(sonuclar[3])+"a4:"+str(sonuclar[4])+"a5:"+str(sonuclar[5]))
    else:
        print("6.dereceden polinom a0:"+str(sonuclar[0]) + "a1:"+str(sonuclar[1])+" a2:"+str(sonuclar[2])+"a3:"+str(sonuclar[3])+"a4:"+str(sonuclar[4])+"a5:"+str(sonuclar[5])+"a6:"+str(sonuclar[6]))
      
def HangisiDahaBüyük(liste):
    enBuyuk = liste[0]
    index = 0   
    for i in range(1,len(liste)):
        if enBuyuk < liste[i]:
            enBuyuk = liste[i]
            index = i+1
    return index,enBuyuk

def UyumlulukHesabı(i,sonuclar,sayilar):
    a = Sr(i,sonuclar,sayilar)          
    b = St(sayilar)
    c = sqrt((b-a)/b)    
    return c

def f1(a):
    return sayilar[a-1]
"""
def EulerYöntemiVerilerİle():#Kendim denemek için yazdım arada ne kadar fark olur diye.      
    x0 = 10
    x1 = len(sayilar)
    y0 = sayilar[9]
    h = 1  
    while(x0<x1):
        y0 = y0 + f1(x0)*h
        x0 += h
    return y0
"""
def VerilerİleBulunan():
    x0 = 10#numaramın sonu
    x1 = len(sayilar)
    y0 = sayilar[9]
    h = 1#Burası bir olmalı çünkü elimizde sadece txt de satır sayılarına göre alıyoruz.  
    while(x0<x1):
        y0 = y0 + (f1(x0)+f1(x0+h))*h/2
        x0 += h
    return y0 
"""
def PolinomİleBulan(enUyumluGrafikKatsayıları):#VerilerİleBulunanın aynısının Polinomla yapıyor sadece deneme amaçlı yazdım...
    x0 = 10#numaramın sonu
    x1 = len(sayilar)
    y0 = sayilar[9]
    h = 0.001  
    while(x0<x1):
        y0 = y0 + (f(enUyumluGrafikKatsayıları,x0)+f(enUyumluGrafikKatsayıları,(x0+h)))*h/2
        x0 += h
    return y0 
"""
def f(katsayilar,x):
    dongu = len(katsayilar)
    toplam = 0
    for i in range(dongu):
        toplam += katsayilar[i]*(x**i)
    return toplam

def YamukYöntemiPolinomKullanarak(enUyumluGrafikKatsayıları,deltax):
    a = 10#numaramın sonu 0 ile bitiyor.
    b = len(sayilar)
    integral = 0      
    n = int((b-a)/deltax)      
    for i in range(n):
        integral += deltax*(f(enUyumluGrafikKatsayıları,a)+f(enUyumluGrafikKatsayıları,(a+deltax)))/2
        a += deltax
    return integral

Uyumluluk = []
tumSonuclar = []
for i in range(1,7):#Bu kısımda Polinoma yaklaştırma metodundan gelen sonucları txt ye yazdırıyorum
    sonuclar = PolinomaYaklaştırmaMetodu(sayilar,i)
    #sonuclarıYazma(sonuclar)#Katsayıları yazıyorum.
    tumSonuclar.append(sonuclar)
    c = UyumlulukHesabı(i,sonuclar,sayilar)
    #print(str(i)+".polinomun     "+"r degeri:"+str(c))
    Uyumluluk.append(c)
a,b = HangisiDahaBüyük(Uyumluluk)#Hangi grafiğin daha uyumlu olduğunu r değerlerine bakarak karşılaştırır.

print("En uyumlu grafik:"+str(a)+".polinom     "+"r degeri:"+str(b))
print("Uyumlu Polinom katsayilari =" )
sonuclarıYazma(tumSonuclar[a-1])
enUyumluGrafikKatsayıları = tumSonuclar[a-1]#a burada bulunan en uyumlu polinomun kaçıncı olduğu

print("Polinom kullanarak bulunan integral=",YamukYöntemiPolinomKullanarak(enUyumluGrafikKatsayıları,0.001))
print("Veriler kullanılarak bulunan integral=",VerilerİleBulunan())


def yorum(dosya):
    dosya.write("Özgür KÜÇET 170401050 \n"
                "Her 2 yöntemdede sayısal yöntemler kullanarak hesapladığımız için gerçek doğru sonuca ulaşamadık aslında. \n"
                "Polinom gerçek polinoma yakın bir polinom gerçek denklemi değil o yüzden aldığımız kolerasyon sayısının \n"
                "1 e uzaklığı artıkça daha kötü sonuç vericektir.Direk verileri kullanarak yaptığımızda ise kullandığımız \n"
                "yönteme göre daha iyi bir sonuç vermesini sağlayabiliriz. Verilerde h'ı 1 almak zorunda olduğumuz için \n"
                "yöntemin kendisini iyi almamız gerekiyor euler yöntemi gibi yöntemler bunu yaparken iyi sonuç vermiyor. \n"
                "Polinomun r değeri 0.99994 olan veriler ile yaptığımda veriler yöntemi ve polinom yöntemi\n"
                "arasındaki fark çok az oldu bunun nedeni polinomu iyi olmasıydı.")

dyazılar = open("170401050_yorum.txt","w", encoding='utf8')
yorum(dyazılar)
dyazılar.close()