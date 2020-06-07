import math
import sympy as syp

def oku():
    dosya = open("veriler.txt")
    y = dosya.readlines()
    x=[]
    for i in range(len(y)):
        y[i]=int(y[i])
        x.append(i)
    return x,y

def matris_olustur(x, y, n, m):
    matris = []
    for i in range(m + 1):
        satir = []
        for j in range(m + 1):
            if (i == 0 and j == 0):
                satir.append(n)
            else:
                x_toplam = 0
                for x_eleman in x:
                    x_toplam += x_eleman ** (i + j)
                satir.append(x_toplam)
        sum_ = 0
        for eleman in range(n):
            sum_ += (x[eleman] ** i) * y[eleman]
        satir.append(sum_)
        matris.append(satir)
    return matris


def gausselimination(matris):  # Gauss
    boyut = len(matris)
    for i in range(0, boyut):
        maxSutun = abs(matris[i][i])
        maxSatir = i
        for j in range(i + 1, boyut):
            if abs(matris[j][i]) > maxSutun:
                maxSutun = abs(matris[j][i])
                maxSatir = j
        for k in range(i, boyut + 1):
            temp = matris[maxSatir][k]
            matris[maxSatir][k] = matris[i][k]
            matris[i][k] = temp

        for l in range(i + 1, boyut):
            c = -matris[l][i] / matris[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    matris[l][j] = 0
                else:
                    matris[l][j] += c * matris[i][j]

    r_matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        r_matris[i] = matris[i][boyut] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][boyut] -= matris[k][i] * r_matris[i]
    return r_matris

def korelasyon_ve_hata(x,y,n,katsayilar,m):
    Sr,St,y_= 0,0,0
    for i in y:
        y_+= i
    y_ /= len(y)
    for i in range(n):
        Sr_1=0
        St += (y[i]-y_)**2
        Sr_1 += y[i]-katsayilar[0]
        for j in range(1,m+1):
            Sr_1 -= katsayilar[j]*(x[i]**j)
        Sr_1 = Sr_1**2
        Sr+=Sr_1
    S_y_x = math.sqrt(abs(Sr/(n-(m+1)))) #Standart tahmini hata
    r = math.sqrt(abs((St-Sr)/St)) #korelasyon
    return r,S_y_x

def enuygunhesapla(x,y,dosya):
    korel = []
    dosya.write('------------------------------------------------------- \n')
    for i in range(1,7):
        matris = matris_olustur(x,y,len(y),i)
        katsayılar = gausselimination(matris)
        korel.append(korelasyon_ve_hata(x,y,len(y),katsayılar,i))
    max,min,temp,w =korel[0][0],korel[0][1],0,0
    for i in range(len(korel)):
        if korel[i][0] > max:
            temp = max
            w = i
            max = korel[i][0]
            if temp < min:
                min = temp
    print(f'en büyük korelasyon: {max}\nen küçük korelasyon: {min}\nen uygun {w+1}. polinom \n')
    bestmatriskatsayi = gausselimination(matris_olustur(x,y,len(y),w+1))
    integ = integral(bestmatriskatsayi,len(y))
    sembolikdenk = sembolikdenklem(bestmatriskatsayi)
    print(f'Denklem : {sembolikdenk} \n {w+1}. dereceden bir denklem \n')
    print(f'Polinomlu Integralin Sonucu: {integ} \n')
    polinomsuz = polinomsuzintegral(y)
    print(f'Polinomsuz Integralin Sonucu : {polinomsuz} \n')


def fonk (bestmatriskatsayi,x):
    denklem = bestmatriskatsayi
    asıldenk = x**6*denklem[6] + x**5*denklem[5]+x**4*denklem[4] +x**3*denklem[3] +x**2*denklem[2] + x*denklem[1] + denklem[0]
    return asıldenk


def integral(bestmatriskatsayi,satirsayisi):
    baslangic = 1 # numaram 170401021
    bitis = satirsayisi
    deltax = 0.01
    integral  =0
    n = int((bitis-baslangic) / deltax)
    for i in range(n):
        integral += deltax* (fonk(bestmatriskatsayi,baslangic) + fonk(bestmatriskatsayi,baslangic+deltax)) / 2
        baslangic = baslangic + deltax
    return integral
def sembolikdenklem(denklem):
    x = syp.symbols('x')
    sd = x**6 * denklem[6] + x**5 * denklem[5]+x**4 * denklem[4] +x**3 * denklem[3] +x**2 * denklem[2] + x * denklem[1] + denklem[0]
    return sd

def polinomsuzintegral(data):
    a = 1
    b = len(data)
    deltax = 1
    integral = 0
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral+= deltax * (data[a] + data[a+deltax])/2
        a+=deltax
    return integral
def yorumyap(sonuc):
    sonuc.write('Buldugumuz polinomda gercek veriler bire bir ayni bulunmaz, ustune ustluk sayisal integral aliyoruz sayisal integralde de deltanin buyuk ya da \n'
                'kucuk olmasina gore bir hata payi vardir. Polinomsuz verilerle aldigimiz integralde ise delta 1 dir. Polinomluda 0.1 aliyorum .\n Farkli cikmasinin sebebi budur.\n '
                'Delta ne kadar kucuk olursa gercek sonuca o kadar yaklasiriz.')
    sonuc.close()


x,y = oku()
sonuc = open('170401021_yorum.txt','w')
enuygunhesapla(x,y,sonuc)
yorumyap(sonuc)
