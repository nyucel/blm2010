# ARDA CEM BİLECAN 170401007
import math
import sympy as sp
sp.init_printing()
x = sp.Symbol('x')
veriler=[]
korelasyonlar=[]
def dosyaOku():
    dosya = open('veriler.txt','r')
    for satir in dosya:
        veriler.append(int(satir))
    dosya.close()


def gauss(A):
    boyut = len(A)
    for i in range(0, boyut):
        maxSutun = abs(A[i][i])
        maxSatir = i
        for j in range(i + 1, boyut):
            if abs(A[j][i]) > maxSutun:
                maxSutun = abs(A[j][i])
                maxSatir = j
        for k in range(i, boyut + 1):
            temp = A[maxSatir][k]
            A[maxSatir][k] = A[i][k]
            A[i][k] = temp
            
        for l in range(i + 1, boyut):
            c = -A[l][i] / A[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    A[l][j] = 0
                else:
                    A[l][j] += c * A[i][j]

    matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        matris[i] = A[i][boyut] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][boyut] -= A[k][i] * matris[i]
    return matris

def korelasyon(kendiSonuclarim,first,end):
    n=end-first
    yi = 0
    for i in range(first,end):
        yi+=veriler[i]
    y_ussu = yi/n  #y'lerin ortalamsi
    Sr = 0
    for i in range(first,end):
        Sr = (kendiSonuclarim[i-first] - veriler[i]) ** 2 + Sr
    St = 0
    for i in range(first,end):
        St = St + (veriler[i] - y_ussu)**2
    rkare=  abs((St-Sr)/St)
    r = math.sqrt(rkare)
    return r

def veriBulma(first,end):     #10lu SEKLİNDE alip 6. dereceye kadar hesaplatİp en iyi derceyi buluyoruz veya bütün verili burda hesapliyoruz
    dizi=[]
    n = end-first
    for derece in range(1,7):
        xValue = []
        for i in range(n):
            xValue.append(i+1)
        # MATRIS Olusturuyoruz    
        matris = [[0 for i in range(derece+1)] for j in range(derece+1)]
        boyut = len(matris)
    
        for i in range(boyut):
            for j in range(boyut):
                xToplamlari=0
                for k in range(n):
                    matris[0][0] = len(xValue) # matrisin 0,0 x veri sayisi kadar olmali
                    xToplamlari=xValue[k]**(i+j)+ xToplamlari  
                    matris[i][j] = xToplamlari
                
        
        
        # y , y*x , y*xkare , y*xkup gibi ifadeleri buluyoruz. 
        xySonuclari = []
        for i in range(boyut):
            toplam=0
            for j in range(first,end):
                toplam = toplam + (veriler[j]*(xValue[j-first]**i))    
            xySonuclari.append(toplam)
        
        # Buldugumuz sonuclari da matrisin en sutunlarina atiyoruz.
        k = 0        
        for i in matris:
            i.append(xySonuclari[k])
            k=k+1
    
    
            
        katSayilar=gauss(matris)
        
        kendiSonuclarim=[]
        for i in range(n):
            toplam = 0
            for j in range(len(katSayilar)):
                toplam = toplam + katSayilar[j]*((i+1)**j)
                if j == derece:
                    kendiSonuclarim.append(int(toplam))
        r = korelasyon(kendiSonuclarim,first,end) 
        dizi.append(r)
        

    eniyisi = 100
    index=0
    for i in range(len(dizi)):
        temp = abs(1-dizi[i])
        if temp<eniyisi:
            eniyisi = temp
            index = i+1

    print("En iyi dereceli polinom:  ",index)
    enİyiPolinomVeIntegralYazdir(index,0,len(veriler))
    

def enİyiPolinomVeIntegralYazdir(derece,first,end):
        n = end - first 
        xValue = []
        for i in range(n):
            xValue.append(i+1)
        # MATRIS Olusturuyoruz    
        matris = [[0 for i in range(derece+1)] for j in range(derece+1)]
        boyut = len(matris)
    
        for i in range(boyut):
            for j in range(boyut):
                xToplamlari=0
                for k in range(n):
                    matris[0][0] = len(xValue) # matrisin 0,0 x veri sayisi kadar olmali
                    xToplamlari=xValue[k]**(i+j)+ xToplamlari  
                    matris[i][j] = xToplamlari
                
        
        
        # y , y*x , y*xkare , y*xkup gibi ifadeleri buluyoruz. 
        xySonuclari = []
        for i in range(boyut):
            toplam=0
            for j in range(first,end):
                toplam = toplam + (veriler[j]*(xValue[j-first]**i))    
            xySonuclari.append(toplam)
        
        # Buldugumuz sonuclari da matrisin en sutunlarina atiyoruz.
        k = 0        
        for i in matris:
            i.append(xySonuclari[k])
            k=k+1
        katSayilar=gauss(matris)
        if len(katSayilar) < 7:
            while len(katSayilar)!=7:
                katSayilar.append(0)
        
        print("POLİNOM DENKLEMİ: \n")       
        denklem=katSayilar[6]*x**6+katSayilar[5]*x**5+katSayilar[4]*x**4+katSayilar[3]*x**3+katSayilar[2]*x**2+katSayilar[1]*x+katSayilar[0]
        sp.pprint(denklem)
        
        integral = 0
        a=7  # 17040100(7)
        b=len(veriler) 
        deltax=0.01
        n = int((b-a)/deltax)
        for i in range(n):
            integral+=deltax*(denklem.subs({x:a})+denklem.subs({x:a+deltax}))/2
            a+=deltax
        
        print("İntegral Değeri: ",integral)


def polinomsuzIntegral():
        integral = 0
        a=7  # 17040100(7)
        b=len(veriler) 
        deltax=1
        n = int((b-a)/deltax)
        for i in range(n-1):
            integral+=deltax*(veriler[a]+veriler[a+deltax])/2
            a+=deltax
        print("Polinomsuz İntegral Değeri: ",integral)
    
def yorumYap():
    dosya = open('170401007_yorum.txt','w',encoding='UTF8')
    dosya.write('2 İntegral Sonucunun Farklı Çıkmasının Nedeni: \n')
    dosya.write('İntegral Hesabi yapılırken verilen polinom küçük dikdörtgenlere bölerek ve bunların alanlarını toplayarak hesaplamaya çalışırız\n')
    dosya.write('Aldığımız dikdörtgenlerin eni ne kadar küçük olursa o kadar fazla dikdörtgen alanı hesaplamış ve bir o kadar da istedğimize yakın değer elde ederiz\n')
    dosya.write('Deltax dedğimiz ise bizim dikdörtgenlerimizin enidir\n')
    dosya.write('Polinomlu Dettax i 0.1 aldığımızda 2 sayı arasında 10 tane diködrtgen alanı hesplamış oluruz\n')
    dosya.write('Polinomsuz hespalama dedğimiz aslında deltax i 1 alıp verilerle integral hesaplamaktır\n')
    dosya.write('Polinomlu kısımda daha çok alan hesabı yapıldığından polinomsuza göre farklı sonuç vermesi doğaldır.\n')
    dosya.write('Polinomlu integral sonucu polinomsuza göre istediğimiz sonuca daha yakın bir sonuç verir.')
    dosya.write('Deltax arttıkça hespalacak dikdörtgen artacağından işlem daha uzun sürer\n')
    dosya.close()

    
dosyaOku()    
veriBulma(0,len(veriler))
polinomsuzIntegral()
yorumYap()
