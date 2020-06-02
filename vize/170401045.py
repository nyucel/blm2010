#170401045 Oğuz BALKAYA
from sympy import Symbol
from math import sqrt
x = Symbol("x")
def verileriAl(dosyaAdresi):
    """
    dosyaAdresi parametresindeki dosyanın her bir satırını bir listenin elemanı olacak şekilde geri döner.
    :param dosyaAdresi: Okunacak dosyanın bilgisayardaki adresi
    """
    return [float(i) for i in (open(dosyaAdresi,"r+",encoding="UTF8",errors="ignore"))]
anaVeriler = verileriAl("veriler.txt") #dosyadan okuduğumuz veriler.
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

def sonucYazdir(katsayilar,derece,r,veriler,verilerim,baslangic):
    """
    Sonucu ve elde edilen verileri sonuc.txt dosyasına yazdırır.
    :param katsayilar: Polinomun katsayıları.
    :param derece:Polinomun derecesi
    :param r: Correlation katsayısı
    :param baslangic: Kullanılacak verilerin ana veri grubu üzerindeki başlangıç indexi.
    """
    dosya = open("sonuc.txt","a+",encoding="UTF8",errors="ignore")
    dosya.write("\n("+str(baslangic)+"-"+str(len(veriler)+baslangic)+" ARASI VERİLER) **** "+str(derece)+". derece yaklaştırma katsayıları ****\n")
    for i in range(0,derece+1):
        dosya.write("a"+str(i)+"="+str(katsayilar[i])+" | ")
    dosya.write("\n")
    dosya.write("r değeri = "+str(r)+"\n\n")
    for i in range(len(veriler)):
        dosya.write(str(baslangic+i+1)+".GÜN | Gerçek veri: "+str(veriler[i])+" , Yaklaşım verisi : "+str(verilerim[i])+"\n")
    dosya.close()
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
    r (correlation katsayısı) değerlerine göre en uygun dereceli polinomu bulur ve sonuc.txt dosyasına yazdırır.
    :param rDegerleri: Karşılaştırılacak r (correlation katsayısı) değerleri. Liste tipinde olmalı.
    """
    r,derece=abs(1-rDegerleri[0]),0
    for i in range(1,len(rDegerleri)):
        if(abs(1-rDegerleri[i]) < r):
            r,derece=rDegerleri[i],i
    dosya=open("sonuc.txt","a+",encoding="UTF8",errors="ignore")
    dosya.write("En uygun polinom "+str(r)+" r değeri ile "+str(derece+1)+". derece polinom.\n\n")
    dosya.close()
def test(veriler,baslangic):
    """
    Gelen verileri diğer fonksiyonların da yardımıyla sırasıyla 1-6 dereceli polinomlara yaklaştırır ve sonuc.txt dosyasına yazar.
    :param veriler:İşlem yapılacak veriler. Liste tipinde olmalı.
    :param baslangic: Kullanılacak verilerin ana veri grubu üzerindeki başlangıç indexi.
    """
    rDegerleri=[]
    for i in range(1,7):
        verilerim=[]
        cozum=gaussYontemi(matrisOlustur(i,veriler))
        if len(cozum) < 7:
            while len(cozum)!=7:
                cozum.append(0)
        denklem=cozum[6]*x**6+cozum[5]*x**5+cozum[4]*x**4+cozum[3]*x**3+cozum[2]*x**2+cozum[1]*x+cozum[0]
        for k in range(0,len(veriler)):
            verilerim.append(denklem.subs({x:k+1}))
        rDegerleri.append(rHesapla(veriler,verilerim))
        sonucYazdir(cozum,i,rHesapla(veriler,verilerim),veriler,verilerim,baslangic)
        #print("Derece : ",i,"İçin veirler : ")
        #for j in range(len(veriler)):
           # print("veri : ",veriler[j]," tahmin : ",verilerim[j])
    enUygunBul(rDegerleri)
def calistir(veriler,baslangic=0,bitis=0):
    """
    Kullanılacak veri aralıklarını alıp bu aralıklardaki verileri test fonksiyonuna yollar.
    :param veriler: Tüm veriler.
    :param baslangic: Kullanılacak verilerin başlangıç indexi.
    :param bitis: Kullanılacak verilerin bitiş indexi.
    """
    if(baslangic==0 and bitis==0):
        test(veriler,0)
    else:
        test(veriler[baslangic:bitis],baslangic)
calistir(anaVeriler) #Tüm veriler için.
for i in range(0,len(anaVeriler)-(len(anaVeriler)%10)+1,10): #10 lu gruplar için
    if(i==len(anaVeriler)-(len(anaVeriler)%10)):
        calistir(anaVeriler,i,len(anaVeriler)+1)
        break
    calistir(anaVeriler, i, i + 10)
