# Ad Soyad: Batuhan Okur    Numara: 180401011
from sympy import Symbol

def polinomaUydurma(pDerece,vakalar): # Polinomun derecesini ve verileri alarak polinoma uydurma işlemini yapar ve korelasyon katsayısını bularak en uygun polinomu seçer.
    matris = []
    temp = 0
    for i in range(pDerece+1): 
        satir = []
        for j in range(pDerece+1):
            toplam = 0
            for k in range(1,len(vakalar)+1):
                toplam += k**temp
            satir.append(toplam)
            temp += 1
        matris.append(satir)
        temp -= pDerece
    sonuc = []
    for i in range(pDerece+1):
        toplam = 0
        for j in range(len(vakalar)):
            toplam += vakalar[j]*(j+1)**i
        sonuc.append(toplam)
    for i in range(pDerece+1):
        b = matris[i][i]
        for j in range(i+1,pDerece+1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(pDerece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]  
    for i in range(pDerece,-1,-1):
        b = matris[i][i]
        for j in range(i-1,-1,-1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(pDerece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]
    for i in range(pDerece+1):
        sonuc[i] = sonuc[i]/matris[i][i]
    yOrt=0
    for i in range (len(vakalar)):
        yOrt += vakalar[i]
    yOrt = yOrt/len(vakalar)
    St=0
    Sr=0
    for i in range(len(vakalar)):
        x = vakalar[i]
        St +=(vakalar[i]-yOrt)**2
        for j in range(len(sonuc)):
            x -= sonuc[j]*(i+1)**j
        x=x**2
        Sr += x
    korelasyon = ((St-Sr)/St)**(1/2)
    return sonuc,korelasyon

def uygunPolinomDerecesiDondur(katsayilar):
    maksimumEleman = max(katsayilar)
    for i in range(len(katsayilar)):
        if katsayilar[i] == maksimumEleman:
            derece = i
    return derece


def polinomluIntegralBul(polinomlar):
    x = Symbol('x')
    polinom = 0
    for i in range(len(polinomlar)):
        polinom += polinomlar[i] * (x ** i)
    a,b=1,len(vakalar) #18040101(1)
    integral = 0
    deltax = 1
    n = int((b-a)/deltax)
    for j in range(n):
        integral += deltax * (polinom.subs({x: a}) + polinom.subs({x: a+deltax}))/2
        a += deltax
    return integral,polinom


def polinomsuzİntegralBul(veriler):
    a,b=1,len(veriler) #18040101(1)
    integral = 0
    deltax = 1
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral += deltax * (veriler[a] + veriler[a+deltax])/2
        a += deltax
    return integral

def yorumYap(dosya):
    yorum = "Batuhan Okur / 180401011 \n " \
            "Integral hesaplarken hesapladığımız polinomu dikdörtgenlere böler ve bu dikdörtgenlerin alanlarını hesaplayıp toplarız.\n" \
            "Bu dikdörtgenlerin eni ne kadar küçük olursa sonuç o kadar gerçeğe yakın olur. \n" \
            "Fakat bu hesaplanan iki fonksiyonda da dikdörtgenin eni(deltax) eşit alındı ve farklı sonuç çıktı. \n" \
            "Bunun sebebi bulduğumuz 6. dereceden polinomun orjinal polinoma belirli bir hata oranı olacak şekilde yakın olmasıdır." \
            "Eğer orjinal polinomu elde etmiş olsaydık(korelasyon katsayısı 1 olsaydı) sonuçlar aynı çıkacaktı."
    yorumDosyasi = open(dosya,"w")
    yorumDosyasi.write(yorum)
    yorumDosyasi.close()


#main(işlemlerin yapıldığı) kısım
dosya = open("veriler.txt","r")
vakalar = dosya.readlines()
for i in range(len(vakalar)):
    vakalar[i]=int(vakalar[i])
polynoms, korelasyonlar = [0] * 6, [0] * 6
for indis in range(0, 6):
    polynoms[indis], korelasyonlar[indis] = polinomaUydurma(indis+1, vakalar)
dosya.close()
uygunPolinomDerecesi = uygunPolinomDerecesiDondur(korelasyonlar)
print("Verilere en uygun polinomun derecesi : ",uygunPolinomDerecesi+1)
polinomluIntegral,kullanilanPolinom = polinomluIntegralBul(polynoms[uygunPolinomDerecesi])
print("\nKullanılan polinom : ",kullanilanPolinom)
print("\nPolinom kullanarak bulunan integral : ",polinomluIntegral)
polinomsuzİntegral = polinomsuzİntegralBul(vakalar)
print("\nPolinom kullanmadan bulunan integral : ",polinomsuzİntegral)
yorumYap('180401011_yorum.txt')
