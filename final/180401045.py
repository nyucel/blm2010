from sympy import Symbol

def polinom(derece,liste): 
    matris1 = []
    x = 0
    for i in range(derece+1): 
        matris1_deger = []
        for j in range(derece+1):
            top = 0
            for k in range(1,len(liste)+1):
                top += k**x
            matris1_deger.append(top)
            x += 1
        matris1.append(matris1_deger)
        x -= derece
    matris2 = []
    for i in range(derece+1):
        top = 0
        for j in range(len(liste)):
            top += liste[j]*(j+1)**i
        matris2.append(top)
    for i in range(derece+1):
        b = matris1[i][i]
        for j in range(i+1,derece+1):
            ortalama = b/matris1[j][i]
            matris2[j] = matris2[j]*ortalama-matris2[i]
            for k in range(derece+1):
                matris1[j][k] = matris1[j][k]*ortalama-matris1[i][k]  
    for i in range(derece,-1,-1):
        b = matris1[i][i]
        for j in range(i-1,-1,-1):
            ortalama = b/matris1[j][i]
            matris2[j] = matris2[j]*ortalama-matris2[i]
            for k in range(derece+1):
                matris1[j][k] = matris1[j][k]*ortalama-matris1[i][k]
    for i in range(derece+1):
        matris2[i] = matris2[i]/matris1[i][i]
    yOrt=0
    for i in range (len(liste)):
        yOrt += liste[i]
    yOrt = yOrt/len(liste)
    St=0
    Sr=0
    for i in range(len(liste)):
        x = liste[i]
        St +=(liste[i]-yOrt)**2
        for j in range(len(matris2)):
            x -= matris2[j]*(i+1)**j
        x=x**2
        Sr += x
    r = ((St-Sr)/St)**(1/2)
    return matris2,r


def polinom_kullanarak_int(polinom):
    x = Symbol('x')
    polinom1 = 0
    for i in range(len(polinom)):
        polinom1 += polinom[i] * (x ** i)
    a,b=5,len(liste)                                #18040145
    integral = 0
    deltax = 1
    n = int((b-a)/deltax)
    for j in range(n):
        integral += deltax * (polinom1.subs({x: a}) + polinom1.subs({x: a+deltax}))/2
        a += deltax
    return integral,polinom1



def polinom_kullanmadan_int(veriler):
    a,b=5,len(veriler) 
    integral = 0
    deltax = 1
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral += deltax * (veriler[a] + veriler[a+deltax])/2
        a += deltax
    return integral


def en_uygun_dereceyi_dondur(ksayılar):
    maksimumEleman = max(ksayılar)
    for i in range(len(ksayılar)):
        if ksayılar[i] == maksimumEleman:
            derece = i
    return derece



def yorumYap(dosya):
    yorum = """ Yusuf Çimenci / 180401045
            İki sonuç arasında fark olmasının nedeni delta uzunluğu ve alanı bölmesinden kaynaklanır.
            yani delta yı ne kadar küçük tutarsak hesaplanan alan o kadar çok artar ve gerçeğe daha yakın olur. 
            kısacası grafikte görünen alanın dah çoğunu kaplamış oluruz ve gerçeğe o kadar yaklaşırız. 
            Polinom kullanmadan alınan integral de deltax = 1 belirlediğimiz için alanı daha az parçaya böleceği için  az hassasiyeti azalır ."""
    yorumDosyasi = open(dosya,"w")
    yorumDosyasi.write(yorum)
    yorumDosyasi.close()



dosya = open("veriler.txt","r")
liste = dosya.readlines()
for i in range(len(liste)):
    liste[i]=int(liste[i])
polynoms, r2 = [0] * 6, [0] * 6
for indis in range(0, 6):
    polynoms[indis], r2[indis] = polinom(indis+1, liste)
dosya.close()
en_uygun_derece = en_uygun_dereceyi_dondur(r2)
print("Verilere en uygun polinomun derecesi : ",en_uygun_derece+1)
POLINOMLU,polinomum = polinom_kullanarak_int(polynoms[en_uygun_derece])
print("\nKullanılan polinom : ",polinomum)
print("\nPolinom kullanarak bulunan integral : ",POLINOMLU)
POLINOMSUZ = polinom_kullanmadan_int(liste)
print("\nPolinom kullanmadan bulunan integral : ",POLINOMSUZ)
yorumYap('180401045_yorum.txt')










