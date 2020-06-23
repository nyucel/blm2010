#Şule Nur Yılmaz  -  170401058

def oku():  #asallar.txt verileri oku - diziye ata - diziyi döndür
    f = open("asallar.txt","r")
    text = f.readlines()
    f.close()
    asallar = list()
    for i in text:
        asallar.append(int(i))
    return asallar


#Global Veriler 3. derece polinom yakınlaştırmasında kullanılacak
xi = [0 for i in range(7)]  #xi toplamları (n/xi/xi2/xi3/xi4/xi5/xi6)
yi = [0 for i in range(4)]  #yi toplamları (yi/yixi/yixi2/yixi3)

#3. dereceden polinom yakınlaştırma (matris verilerinin hesaplanması, matris oluşturma, katsayıları bulma, katsayıları geriye döndürme)
def ucuncu_der(i,veri): # i = satır sayısı veri = satırdaki veri
    if i != -1:
        for k in range(len(xi)):
            xi[k] += (i) ** k
        for l in range(len(yi)):
            yi[l] += veri * ((i) ** l)
    else:
        matris = [[0 for p in range(4)] for r in range(4)]
        for x in range(len(matris)):
            for y in range(len(matris[x])):
                matris[x][y] = xi[x+y]
        row = len(matris)
        col = len(matris[0])

        for k in range(row):
            for l in range(k+1,row):
                a = - matris[l][k] / matris[k][k]
                for m in range(k,col):
                    if  m == k:
                        matris[l][m] = 0.0
                    else:
                        matris[l][m] += a * matris[k][m]
                yi[l] += a * yi[k]

        katsayilar = [0 for t in range(col)]

        for x in range(row-1,-1,-1):
            katsayilar[x] = yi[x] / matris[x][x]
            for y in range(x-1,-1,-1):
                yi[y] -= katsayilar[x] * matris[y][x]
        print("Katsayılar a0: {} a1: {} a2: {} a3: {}".format(katsayilar[0],katsayilar[1],katsayilar[2],katsayilar[3]))
        return katsayilar

#Polinom yakınlaştırması için yardımcı fonksiyon (satır sayısı ve o satırdaki veriyi ilgili fonksiyona yolluyor)
def yardimci(asallar):
    for i in range(len(asallar)):
        ucuncu_der(i+1, asallar[i])
    q = ucuncu_der(-1, None)    #veriler(satırlar) bittiğinde polinomun bulunması için fonksiyon son kez çağırılıyor.
    return q


def f(i):   # 3. dereceden polinomumuz
    return (katsayi[0]+katsayi[1]*i+katsayi[2]*(i**2)+katsayi[3]*(i**3))


#İleri Sonlu Farklar Yöntemi Kullanıldı (sayısal türev)

#a=58   - 170401058

def turev_1(x=58):  
    x0 = x
    h = 0.01
    xprime = (f(x0+h)-f(x0))/h
    print("(POLİNOMLU) x={}'ken türev: ".format(x),xprime)

def turev_2(x=58):
    x0 = x - 1  # dizi indeks 0'dan başladığından istenen veriyi elde etmek için bir eksiğini alıyoruz.
    h = 1
    xprime = (asallar[x0+h]-asallar[x0])/h
    print("(POLİNOMSUZ) x={}'ken türev: ".format(x),xprime)


def yorum():
    f = open("yorum.txt","w",encoding="UTF-8")
    f.write(""" Şule Nur Yılmaz
 Polinomlu ve polinomsuz sayısal türev sonuçlarının farkının en büyük sebebi
polinomlu sayısal türevde hesaplama yaparken aralığı istediğimiz ölçüde azaltarak gerçek sonuca
çok daha yakın anlamlı bir sonuç bulabiliyor olmamız. Polinomsuz sayısal türevde en iyi ihtimalle aralığı (h=1)
tutabilirken polinomlu sayısal türevde ara değerleri elimizde bulunan polinom ile hesaplayabileceğimizden
aralığı çok daha küçük (örneğin h=0.1) tutabiliyoruz. 
 Bir diğer sebep ise elimizdeki polinom var olan gerçek değerleri (asal sayıları) vermediğinden aynı aralık (h=1)
için sayısal türev hesapladığımızda bile türev sonuçlarının aynı değere sahip olmamasına sebep oluyor. """)
    f.close()


asallar = oku() #veriler
katsayi = yardimci(asallar) #3. dereceden polinomun katsayıları
turev_1()   #polinomlu 
turev_2()   #polinomsuz
yorum()
