""" Mehmet Said Turken     180401030"""

from sympy import Symbol
x = Symbol('x')

dosya = open("veriler.txt", "r")
veri = []

for i in dosya:
    veri.append(int(i))
    
n = len(veri)
yitoplam = sum(veri)

def x_degerleri(list, n):    
    valuex = []
    for i in range(13):
        x = 0
        for j in range(n):
            x += (j+1) ** i
        valuex.append(x)
    return valuex

def toplam_xiyi(list, n):
    toplam_xiyi = []
    for i in range(7):
        xiyi = 0
        for j in range(n):
            xiyi += ((j+1) ** i) * (list[j])
        toplam_xiyi.append(xiyi)
    return toplam_xiyi

def gaussyontemi(matris):     #EBD (en buyuk deger)--- EBS(en buyuk satir)
    n = len(matris)
    for i in range(0, n):
        EBD = abs(matris[i][i])
        EBS = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) >EBD:
                EBD = abs(matris[k][i])
                EBS = k
                
                
        for k in range(i, n + 1):
            temp = matris[EBS][k]
            matris[EBS][k] = matris[i][k]
            matris[i][k] = temp
            
            
        for k in range(i + 1, n):
            c = -matris[k][i] / matris[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matris[k][j] = 0
                else:
                    matris[k][j] += c * matris[i][j]
                    
    son = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        son[i] =matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * son[i]
    return son                    
                    
                    
def liste_cozum(list, n):
    cozum = []
    for i in range(2, 8):
        degerler = []
        for j in range(i):
            degerler.append([])
            for k in range(i):
                degerler[j].append(x_degerleri(list, n)[k + j])
            degerler[j].append(toplam_xiyi(list, n)[j])
            if j == i - 1:
                cozum.append(gaussyontemi(degerler))
                degerler.clear()
    return cozum                    
                    
                    
def deger_st(x, veri, n, yitoplam):   #St nin degerini bulacagimiz fonksiyon
    y_ort = yitoplam / n
    st = 0
    for i in range(n):
        st += (veri[i] - y_ort) ** 2
    return st                    
                    
def sr_korelasyon(x, veri, n, yitoplam):  #sr'yi buluyoruz,korelasyon katsayilarini donduruyoruz.
    sr = 0
    for i in range(n):
        hesaplama = 0
        hesaplama += x[0]
        for j in range(1, len(x)):
            hesaplama += x[j] * (i + 1) ** j
        sr += (veri[i] - hesaplama) ** 2
        
    return ((deger_st(x, veri, n, yitoplam) - sr) / deger_st(x, veri, n, yitoplam)) ** (1/2)   
                    
                    
def korelasyon_list(korelasyon_degerleri, veri, n, yitoplam):
    deger = []
    for i in korelasyon_degerleri:
        deger.append(sr_korelasyon(i, veri, n, yitoplam))
    return deger


def optimaldeger(korelasyon_degerleri, veri, n, yitoplam):
    a = korelasyon_list(korelasyon_degerleri, veri, n, yitoplam)
    ilk = 150
    list = []
    for i in range(len(a)):
        degerr = abs(1-a[i])
        if int(degerr) < 0:
            degerr *= -1
        if degerr < ilk:
            ilk = degerr
            list.clear()
            list.append((i+1, a[i]))
    return list                    
                    
                    
def f(x):
    fonksiyon = 0
    a = optimaldeger(liste_cozum(veri, n), veri, n, yitoplam)[0][0]
    for i in liste_cozum(veri, n):
        if len(i) == a + 1:
            t = 0
            for j in range(0, a+1):
                fonksiyon += i[t]*(x**j)
                t += 1
    return fonksiyon 


def polinomluint():
    a = 10      #a okul numaramızın son rakamı,b dosyanın satır sayısı
    b = len(veri)
    deltax = 0.1
    integral = 0
    n = int((b - a) / deltax)
    denklem = f(x)
    for i in range(n):
        integral += deltax * (denklem.subs({x:a}) + denklem.subs({x:a + deltax}) ) / 2
        a += deltax

    return integral   
                
def polinomsuzint():
    a = 10        
    b = len(veri)
    deltax = 1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n-1):
        integral += deltax * (veri[a] + veri[a + deltax]) / 2
        a += deltax

    return integral                   

                 
print("Polinom kullanarak bulunan integral : ",polinomluint())

print("Polinom olmadan bulunan integral = ", polinomsuzint())                  
                    
yenidosya = open("180401030_yorum.txt", 'w', encoding='UTF8')
yenidosya.write("Polinomlu ve polinomsuz integralin değerlerinin farklı çıkmasının sebebi delta_x'e verilen değerdir.\n" )                   
yenidosya.write("Çünkü integral polinomu küçük parçalara ayırarak alanlarını hesaplar.\n")                    
yenidosya.write("Bu sebeple delta_x küçüldükçe hesaplanan alan artar yani hesapladığımız alan gerçeğe daha da yaklaşır.\n")                                              
yenidosya.write("Fakat deltax integral hesaplarındaki asıl farkı ortaya koymaz.\n")                    
yenidosya.write("Çünkü polinomlu ve polinomsuz integrallerdeki deltax değerini aynı bile versek sonucları farklı alırız.\n")                      
yenidosya.write("Bunun sebebi ilk integralimizi polinoma korelasyon sayısına göre yaklaştırmamızdır.\n")                     
yenidosya.close()                    
                    
                   
                    
                    
                    
                    
                    
                    
                    