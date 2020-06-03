#Oğuz BALKAYA 170401045
from sympy import Symbol,pprint
x = Symbol("x")
def verileriAl(dosyaAdresi):
    """
    dosyaAdresi parametresindeki dosyanın her bir satırını bir listenin elemanı olacak şekilde geri döner.
    :param dosyaAdresi: Okunacak dosyanın bilgisayardaki adresi
    """
    return [float(i) for i in (open(dosyaAdresi,"r+",encoding="UTF8",errors="ignore"))]
def gaussYontemi(matris):
    n = len(matris)
    for i in range(0, n):
        max = abs(matris[i][i])
        maxSatir = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) > max:
                max = abs(matris[k][i])
                maxSatir = k
        for k in range(i, n + 1):
            tmp = matris[maxSatir][k]
            matris[maxSatir][k] = matris[i][k]
            matris[i][k] = tmp
        for k in range(i + 1, n):
            c = -matris[k][i] / matris[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matris[k][j] = 0
                else:
                    matris[k][j] += c * matris[i][j]
    sonuc = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        sonuc[i] = matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * sonuc[i]
    return sonuc
def yi(veriler):
    """
    İşlem yapılacak verilerin toplamlarını bulur.
    :param veriler:İşlem yapılacak veriler. Liste tipinde olmalı.
    """
    toplam=0
    for veri in veriler:
        toplam+=veri
    return toplam
def yUssu(veriler):
    """
    İşlem yapılacak verilerin ortalamalarını bulur.
    :param veriler:İşlem yapılacak veriler. Liste tipinde olmalı.
    """
    return yi(veriler)/len(veriler)
def Sr(veriler,verilerim):
    """
    Hataların karelerinin toplamları.
    :param veriler:Gerçek veriler. Liste tipinde olmalı.
    :param verilerim:Yaklaşım yapılarak bulunan veriler. Liste tipinde olmalı.
    """
    Sr=0
    for i in range(0,len(veriler)):
        Sr+=(veriler[i]-verilerim[i])**2
    return Sr
def St(veriler):
    """
    :param veriler:İşlem yapılacak veriler. Liste tipinde olmalı.
    """
    St=0
    for veri in veriler:
        St+=(veri-yUssu(veriler))**2
    return St
def rHesapla(veriler,verilerim):
    """
    Tanım (Correlation) katsayısını bulur.
    :param veriler:Gerçek veriler. Liste tipinde olmalı.
    :param verilerim:Yaklaşım yapılarak bulunan veriler. Liste tipinde olmalı.
    """
    return ((abs((St(veriler)-Sr(veriler,verilerim)))/St(veriler)))**(1/2)

def xHesapla(sinir,veriler):
    """
    Yaklaşılacak polinomun derecesine göre x^ toplamlarını bulur.
    :param sinir: Yaklaşılacak polinomun derecesi. int tipinde olmalı.
    :param veriler: İşlem yapılacak veriler. Liste tipinde olmalı.
    """
    sonuc=[len(veriler)]
    for i in range(1,2*sinir+1):
        toplam=0
        for k in range(1,len(veriler)+1):
            toplam+=(k)**i
        sonuc.append(toplam)
    return sonuc
def yHesapla(sinir,veriler):
    """
    Yaklaşılacak polinomun derecesine göre x^.yi toplamlarını bulur.
    :param sinir: Yaklaşılacak polinomun derecesi.
    :param veriler: İşlem yapılacak veriler. Liste tipinde olmalı.
    """
    xySonuclari = []
    for m in range(sinir+1):
        toplam=0
        for n in range(len(veriler)):
            toplam +=  (veriler[n]*((n+1)**m))
        xySonuclari.append(toplam)
    return xySonuclari
def matrisOlustur(m,veriler):
    """
    Yaklaşılacak polinomun derecesine göre matrisi oluşturur.
    :param m: Yaklaşılacka polinomun derecesi. int tipinde olmalı.
    :param veriler: İşlem yapılacak veriler. Liste tipinde olmalı.
    """
    m+=1
    x,y=xHesapla(m,veriler),yHesapla(m,veriler)
    matris,satir=[],0
    for i in range(0,m):
        ekleneceksatir=[]
        for i in range(satir,m+satir):
            ekleneceksatir.append(x[i])
        ekleneceksatir.append(y[satir])
        satir+=1
        matris.append(ekleneceksatir)
    return matris
def enUygunBul(rDegerleri):
    """
    Yaklaşılan polinomların r değelerini karşılaştırarak en uygun polinomun derecesini bulur.
    :param rDegerleri: Polinomların r değerleri. Liste tipinde olmalı.
    """
    r,derece=abs(1-rDegerleri[0]),0
    for i in range(1,len(rDegerleri)):
        if(abs(1-rDegerleri[i]) < r):
            r,derece=rDegerleri[i],i
    return (r,derece+1)
def polinomuBul(veriler):
    """
    Verileri sırasıyla 1-6 arası dereceden polinomlara yaklaştırır.
    rHesapla ve enUygunBul fonksiyonlarının yardımıyla en uygun denklemi ve derecesini bulur.
    :param veriler: Kullanılacak veriler.Liste tipinde olmalı.
    """
    rDegerleri,denklemler=[],{}
    for i in range(1,7):
        verilerim=[]
        cozum=gaussYontemi(matrisOlustur(i,veriler))
        if len(cozum) < 7:
            while len(cozum)!=7:
                cozum.append(0)
        denklem=cozum[6]*x**6+cozum[5]*x**5+cozum[4]*x**4+cozum[3]*x**3+cozum[2]*x**2+cozum[1]*x+cozum[0]
        denklemler[i]=denklem
        for k in range(0,len(veriler)):
            verilerim.append(denklem.subs({x:k+1}))
        rDegerleri.append(rHesapla(veriler,verilerim))
    enUygun=enUygunBul(rDegerleri)
    return (denklemler[enUygun[1]],enUygun[1])
def integralHesapla(denklem):
    """
    Polinom kullanarak integral hesaplar.
    :param denklem: İntegrali hesaplanacak polinom.
    """
    a,b=5,len(anaVeriler)
    deltax = 0.1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n):
        integral += deltax * (denklem.subs({x:a}) + denklem.subs({x:a+deltax})) / 2
        a += deltax
    return integral
def polinomsuzIntegralHesapla(veriler):
    """
    Gelen verileri kullanarak integral hesaplar.
    :param veriler: İntegrali hesaplanacak veriler. Liste tipinde olmalı.
    """
    a,b=5,len(veriler)
    deltax = 1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n-1):
        integral += deltax * (veriler[a] + veriler[a+deltax]) / 2
        a += deltax
    return integral
anaVeriler = verileriAl("veriler.txt")
def islemleriYap(dosya):
    """
    Ekrana polinomun derecesini,polinomu ; dosya ya polinomlu ve polinomsuz hesaplanan integralin arasındaki farkın yorumunu yazar.
    :param dosya: Yorumların yazılacağı dosya yolu.
    :return:
    """
    polinom=polinomuBul(anaVeriler)
    print("En uygun polinomun derecesi "+str(polinom[1]))
    print("Polinom = ")
    pprint(polinom[0])
    print("Polinom ile hesaplanan integralin değeri = ",integralHesapla(polinomuBul(anaVeriler)[0]))
    print("Polinom olmadan hesaplanan integralin değeri = ",polinomsuzIntegralHesapla(anaVeriler))
    yorumDosyasi=open(dosya,'w',encoding='UTF8')
    yorum="(Oğuz BALKAYA 170401045)\n" \
          "Polinomla ve polinomsuz hesaplanan integralin değerinin farklı çıkma sebebi aldığımız diktörtgenlerin enidir.\n" \
          "İntegral hesabı yaparken verilen polinomu küçük dikdörtgenlere böler ve bu dikdörtgenlerin alanlarını hesaplayıp toplarız.\n" \
          "Bu dikdörtgenlerin eni ne kadar küçük olursa okadar çok alan hesaplar ve integrale okadar çok yaklaşırız.\n" \
          "Polinom ile hesaplamada denklem bilindiği için istediğimiz kadar küçük dikdörtgenlere bölebiliyoruz.Bu nedenle daha hassas bilgiler elde edebiliyoruz.\n" \
          "Polinomsuz hesaplamada ise istediğimiz kadar parçaya bölemediğimiz için arada bu fark oluşuyor."
    yorumDosyasi.write(yorum)
    yorumDosyasi.close()
islemleriYap('yorum-170401045.txt')