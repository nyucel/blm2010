# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:06:31 2020

@author: Ozgur Kucet 170401050
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
    #print(sonuclar)
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
    for i in range(len(sonuclar)):
        a2,a3,a4,a5,a6 = [],[],[],[],[]
        a0 = sonuclar[0]
        a1 = sonuclar[1]
        if(len(sonuclar) > 2):
            a2 = sonuclar[2]
        if(len(sonuclar) > 3):
            a3 = sonuclar[3]
        if(len(sonuclar) > 4):
            a4 = sonuclar[4]
        if(len(sonuclar) > 5):
            a5 = sonuclar[5]
        if(len(sonuclar) > 6):
            a6 = sonuclar[6]
    return a0,a1,a2,a3,a4,a5,a6

def sonuclarıStringeYazma(liste,i):#Sonuçları yazdırırken kullanıyorum.
    yazı = "a0:"+str(liste[0])+"  a1:"+str(liste[1])+" "
    yazı1 = "1.dereceden "
            
    if(i > 1):
        yazı += " a2:"+str(liste[2])+" "
        yazı1 = "2.dereceden "
    if(i > 2):
        yazı += " a3:"+str(liste[3])+" "
        yazı1 = "3.dereceden "
    if(i > 3):
        yazı += " a4:"+str(liste[4])+" "
        yazı1 = "4.dereceden "
    if(i > 4):
        yazı += " a5:"+str(liste[5])+" "
        yazı1 = "5.dereceden "
    if(i > 5):
        yazı += " a6:"+str(liste[6])+" "
        yazı1 = "6.dereceden "
    yazı += "\n"    
    
    return yazı1,yazı

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
    #print(a)          
    b = St(sayilar)
    #print(b)
    c = sqrt((b-a)/b)    
    #print(c)
    return c

def KatsayılarıTxtYaz(sayilar):
    with open("sonuc.txt","w") as dosya:
        Uyumluluk = []
        for i in range(1,7):#Bu kısımda Polinoma yaklaştırma metodundan gelen sonucları txt ye yazdırıyorum
            sonuclar = PolinomaYaklaştırmaMetodu(sayilar,i)
            a0,a1,a2,a3,a4,a5,a6 = sonuclarıYazma(sonuclar)#Katsayıları yazıyorum.
            liste = [a0,a1,a2,a3,a4,a5,a6]
            yazı1,yazı = sonuclarıStringeYazma(liste,i)    
            dosya.write(yazı1+yazı)
            c = UyumlulukHesabı(i,sonuclar,sayilar)
            Uyumluluk.append(c)
                   
        a,b = HangisiDahaBüyük(Uyumluluk)#Hangi grafiğin daha uyumlu olduğunu r değerlerine bakarak karşılaştırır.
        uyumlulukyazı = "En uyumlu grafik:"+str(a)+".polinom     "+"r degeri:"+str(b)
        dosya.write("\n\n")
        dosya.write(uyumlulukyazı)
        dosya.write("\n\n")
        
        t = int(n/10) #Bu kısımda 10 lu grupları alıyorum ve aynı işlemi yapıyorum.
        Uyumluluk = []
        for i in range(t):
            dosya.write("\n\n")
            dosya.write(str(i+1)+".10lu grup:")
            dosya.write("\n")
            x = i*10
            y = (i+1)*10
            sayilar1 = sayilar[x:y]
            for i in range(1,7):
                sonuclar = PolinomaYaklaştırmaMetodu(sayilar1,i)
                a0,a1,a2,a3,a4,a5,a6 = sonuclarıYazma(sonuclar)
                liste = [a0,a1,a2,a3,a4,a5,a6]
                yazı1,yazı = sonuclarıStringeYazma(liste,i)    
                dosya.write(yazı1+yazı)
                c = UyumlulukHesabı(i,sonuclar,sayilar1)
                Uyumluluk.append(c)            
            a,b = HangisiDahaBüyük(Uyumluluk)
            uyumlulukyazı = "En uyumlu grafik:"+str(a)+".polinom     "+"r degeri:"+str(b)           
            dosya.write("\n\n")
            dosya.write(uyumlulukyazı)
            dosya.write("\n\n")  
            Uyumluluk = []    
                
KatsayılarıTxtYaz(sayilar)
