# ad-soyad : Ramazan AYDIN   ---  numara : 180401040

print("\n")

"""
Bu  python kodunda ;
parametre olarak verilen dosyadaki (veriler.txt) verilerin sırasıyla 1,2,3,4,5,6. dereceden polinoma yakınlaştırarak 
bu polinomlardan hangisinin en az hata ile sonucu bulduğunu hesaplayacağiz. 
Tespit   ettiğiniz   polinomunun  a ( öğrenci numarasının son rakamı) ile  b (dosyanın satır sayısı) arasındaki integrali
hesaplayacağız .
Aynı integrali veriler.txt dosyasındaki verileri kullanarak hesaplayacağız.
Son olarak hesapladığımız bu 2 integralin sonuclarının farklı çıkmasının nedenini yorum.txt dosyasında açıklayacağız.
"""

# veriler.txt dosyasına gider ve oradaki verilerin tamamını okur.  ***********
with open("veriler.txt", "r", encoding='utf-8') as file:
    dizi = []   #dizi adında bir liste oluşturduk.
    for i in file.read().split():
        dizi.append(int(i))  #veriler.txt dosyasından okuduğumuz verileri diziye ekledik.


#Dizinin boyutunu tutması için bir fonksiyon oluşturduk.
def size(dizi):
    return len(dizi)


n = size(dizi)   # n'ye dizinin boyutunu atadık


  # kare matris oluşturma
def karematris(calculateMATRIS):
    dizi_m = calculateMATRIS.copy()
    column = len(calculateMATRIS[0])
    line = len(calculateMATRIS)


    # left triangular matris hesaplama
    for s in range(line - 1):
        for y in range(line - 1 - s):
            multiplier = dizi_m[y][s] / dizi_m[y + 1][s]
            for b in range(column):
                dizi_m[y][b] += -multiplier * dizi_m[y + 1][b]

    # diagonal matris
    for m in range(line - 1, 0, -1):
        for n in range(line - 1, line - 1 - m, -1):
            multiplier = dizi_m[n][m] / dizi_m[n - 1][m]
            for h in range(column):
                dizi_m[n][h] += -multiplier * dizi_m[n - 1][h]
    cozum = []
    for s in range(line - 1, -1, -1):
        x = dizi_m[s][line] / dizi_m[s][line - s - 1]
        cozum.append(x)
    return cozum


# toplam y değerlerini hesapladık
def totalY(dizi):
    y = sum(dizi)
    return y


totalyi = totalY(dizi)


# xi toplamları tutan dizi
def totalxi(n):
    total_x_kare = [] #total_x_kare adında bir dizi olusturduk.
    for j in range(1, 13, 1):
        kare_x = 0     #kare_x in ilk değerini 0 a eşitledik.
        for p in range(n):
            kare_x += (p + 1) ** j  #dizideki eleman sayısı kadar, x lerin karelerini hesaplattık
        total_x_kare.append(kare_x)
    total_x_kare.insert(0, n)   #hesaplattığımız değerleri diziye ekledik
    return total_x_kare


#  bütün polinomların (1,6) x^ derecelerini  tutan dizi
def xiyiToplam(n, dizi, totalY):
    derece_x_totaly = []
    for j in range(1, 7, 1): #6 polinom olduğu için 6 kere döndürdük.
        deger = 0
        for eleman in range(n):
            deger += (eleman + 1) ** j * dizi[eleman]
        derece_x_totaly.append(deger)
    derece_x_totaly.insert(0, totalY)
    return derece_x_totaly


"""

6. polinoma kadar gittiğimiz için 7 tane a değerin oluşacak; bu yüzden  m=8 e kadar döngümüzü çalıştıracağız
a0, a1, a2, a3, a4, a5, a6, a7

"""

def value_of_a(n, dizi, m=8):
    cozum = []
    total_x_kare = totalxi(n)
    y = totalY(dizi)
    derece_x_totaly = xiyiToplam(n, dizi, y)
    for x in range(2, m, 1):
        yenidizi = []
        for i in range(x):
            yenidizi.append([])
            for j in range(x):
                yenidizi[i].append(total_x_kare[j + i])
            yenidizi[i].append(derece_x_totaly[i])
            if (i == x - 1):
                cozum.append(karematris(yenidizi))
                yenidizi.clear()
    return cozum


"""
 deger_a dizisi ;
 n. derece polinomun a değerlerini bir dizi olarak tutar
"""

deger_a = value_of_a(n, dizi)

"""

Korelasyon, iki değişken arasında doğrusal bir ilişkiyi ifade eder.
Korelasyon katsayısı ise değişkenler arasındaki ilişkiyi göstermek için kullanılan bir değerdir.
Korelasyon katsayısı;
   **   1′e yaklaştıkça iki değişken arasında aynı yöndeki ilişki artar.Değişkenlerden biri artarken diğeri de artar.
    **   -1′e yaklaştıkça iki değişen arasında ters yönde ilişki artar. Değişkenlerden biri artarken diğeri azalır.
     **    0’a yaklaştıkça iki değişken arasındaki ilişki azalır.
Ödevde aynı yönde artan veriler üzerinde işlem yaptığımız için korelasyon katsayısı 1'e en yakın olan
polinomu, en uygun polinom olarak alacağız.
"""



"""
 korelasyon değerlerini hesaplayacagız
"""

def Hata_Hesaplama(x, dizi, n, totalY):
    S_R = 0
    S_T = 0
    y = totalY / n
    size = len(x)
    for i in range(n):
        gecici = 0
        for j in range(size):
            if j == 0:
                gecici += x[j]
            else:
                gecici += x[j] * (i + 1) ** j
        S_R += (dizi[i] - gecici) ** 2
        S_T += (dizi[i] - y) ** 2
    r = ((S_T - S_R) / S_T) ** (1 / 2)
    return r

"""

hesapladığımız korelasyon değerleri içinde 1 en yakın kolerasyon değerini bulmalıyız ve bunu döndürmeliyiz

"""

'''
Bu fonksiyonumda , elde ettiğimiz korelasyon değerlerini bir dizi oluşturup ,bu dizi içerisinde tutacağız. 
'''

KorelasyonValue = []
for i in deger_a:
    e = Hata_Hesaplama(i,dizi,n , totalyi)
    KorelasyonValue.append(e)


def en_iyi_kolerasyon(dizi):        #  Bu fonksiyon 1'e en yakın olan kolerasyon değerini döndürür
    sirali_dizi = sorted(dizi)      # sorted fonksiyonu ile diziyi sıraladık.
    biggest = sirali_dizi[-1]
    b = 1
    while (biggest != dizi[b - 1]):
        b = b + 1
    return b, biggest



sayici, en_iyi_korelasyon_degeri = en_iyi_kolerasyon(KorelasyonValue)
print("Sonucu en düşük hata payi ile hesaplayan polinomun derecesi : ", sayici)
print("Sonucu en düşük hata payi ile hesaplayan polinomun Korelasyon değeri : ", en_iyi_korelasyon_degeri)
print("\n")
polinom = deger_a[sayici - 1]

def fonksiyon(w , polinom1 = polinom ):
    u = polinom1
    total_value = 0
    for i in range(len(u)):
        total_value += u[i] * (w ** i)
    return total_value




"""
Bu fonksiyonda 2.soruyu cevaplayacağız.
Integrali tespit ettiğimiz en iyi korelasyon değerine sahip polinomu kullanarak hesapladık ve sonucu ekrana yazdırdık
"""

def polinom_ile_integral_hesaplama(n):
    # okul numaram 180401040 olduğu için son rakamı 0 . Bu yüzden a =10 alacağız.
    a = 10
    b = n
    deltax = 0.001
    integral = 0
    size = int((b - a) / deltax)
    for i in range(size):
        integral += deltax * (fonksiyon(a) + fonksiyon(a + deltax)) / 2
        a += deltax
    print("Polinom kullanarak hesaplanan sonuc  :  ", integral)




"""
Bu fonksiyonda 3.soruyu cevaplayacağız.
Integrali veriler.txt dosyasındaki verileri kullanarak (polinomu   kullanmadan) hesaplayıp bu sonucu da ekrana yazdırdık.
"""

def veriler_ile_integral_hesaplama(n, dizi):
    # 180401040 (0)  . a değerini  10 olarak alacağız.
    a = 10
    b = n
    integral = 0
    for i in range(a - 1, b - 1):
        integral += (dizi[i] + dizi[i + 1]) / 2
    print("Veriler kullanılarak hesaplanan sonuc :  ", integral)



"""
yorum.txt dosyasının içerisinde hesapladimiz 2 integral değerininde neden farklı sonuçlar verdiğini açıklayacağız. 
"""

def yorumlarim():
    with open("180401040_yorum.txt", "w", encoding='utf-8') as dosya :
        dosya.write("ad - soyad : Ramazan AYDIN \n")
        dosya.write("NUMARA     : 180401040 \n")
        dosya.write(" Hesaplamalarımda yamuk metodunu kullandım.\n ")
        dosya.write("Hesapladigimiz 2 integral değeri de öngördüğümüz gibi birbirinden farkli çikmistir. \n")
        dosya.write(" Bunun nedeni ; \n")
        dosya.write("İntegral Hesabi yapılırken , verilen polinomu küçük dikdörtgenlere bölerek ve bunların alanlarını toplayarak hesaplamaya çalışırız. \n ")
        dosya.write("Deltax(dikdörtgenin eni) değerini ne kadar küçültürsek ,işleme katılacak alan sayısı artar ve  bulacağımız değer o kadar gerçeğe yakın olur.\n ")
        dosya.write("Ancak bu iki integral arasındaki farkın temel sebebi , birinci integrali  polinom haline getirirken \n ")
        dosya.write("belirli bir korelasyon sayısına göre polinoma yaklaştırmamızdandır.\n ")
        dosya.write("Bu sebepten, deltax değerlerini eşit aldığımızda bile sonuç farklı  olur. \n ")


polinom_ile_integral_hesaplama(n)
veriler_ile_integral_hesaplama(n, dizi)
yorumlarim()
