# Süleyman Yalçınkaya 180401076

print("\n")



# veriler.txt dosyasına gider ve oradaki verilerin tamamını okur.

with open("veriler.txt", "r", encoding='utf-8') as file:

    dizi = []   #dizi oluşturuldu

    for i in file.read().split():

        dizi.append(int(i))  #okunan verileri diziye eklendi



def size(dizi):

    return len(dizi)

n = size(dizi)   #

  # kare matris oluşturma

def karematris(calculateMATRIS):

    dizi_m = calculateMATRIS.copy()

    column = len(calculateMATRIS[0])

    line = len(calculateMATRIS)





    # matris hesaplama

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


# y değerlerini hesaplandı

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





# (1,6) x^ derecelerini  tutan dizi

def xiyiToplam(n, dizi, totalY):

    derece_x_totaly = []

    for j in range(1, 7, 1): #6 polinom olduğu için 6 kere döndürdük.

        deger = 0

        for eleman in range(n):

            deger += (eleman + 1) ** j * dizi[eleman]

        derece_x_totaly.append(deger)

    derece_x_totaly.insert(0, totalY)

    return derece_x_totaly





def value_of_a(n, dizi, m=8):#6. polinoma kadar gittiğimiz için 7 tane a değerin oluşacak; bu yüzden  m=8 e kadar döngü devam eder

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


deger_a = value_of_a(n, dizi)#n. derece polinomun a değerlerini bir dizi olarak tutar



"""


Ödevde aynı yönde artan veriler üzerinde işlem yaptığımız için korelasyon katsayısı 1'e en yakın olan

polinomu, en uygun polinom olarak alacağız.

"""



def Hata_Hesaplama(x, dizi, n, totalY):#kolerasyon değerleri

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




KorelasyonValue = []

for i in deger_a:

    e = Hata_Hesaplama(i,dizi,n , totalyi)

    KorelasyonValue.append(e)





def en_iyi_kolerasyon(dizi):        #  Bu fonksiyon 1'e en yakın olan korelasyon değerini döndürür

    sirali_dizi = sorted(dizi)      

    biggest = sirali_dizi[-1]

    b = 1

    while (biggest != dizi[b - 1]):

        b = b + 1

    return b, biggest







sayici, en_iyi_korelasyon_degeri = en_iyi_kolerasyon(KorelasyonValue)

print("en düşük hata payı ile sonucu hesaplayanpolinomun derecesi ", sayici)

print("en düşük hata payı ile sonucu hesaplayan korelasyon değeri  ", en_iyi_korelasyon_degeri)

print("\n")

polinom = deger_a[sayici - 1]



def fonksiyon(w , polinom1 = polinom ):

    u = polinom1

    total_value = 0

    for i in range(len(u)):

        total_value += u[i] * (w ** i)

    return total_value





#2. soru için

def polinom_ile_integral_hesaplama(n):

    # okul numaram 180401076 olduğu için  a =6 aldım

    a = 6

    b = n

    deltax = 0.001

    integral = 0

    size = int((b - a) / deltax)

    for i in range(size):

        integral += deltax * (fonksiyon(a) + fonksiyon(a + deltax)) / 2

        a += deltax

    print("Polinom ile hesaplanan sonuç  :  ", integral)






#3. soru için
def veriler_ile_integral_hesaplama(n, dizi):

    # 180401076   a değerini  6 olarak aldım.

    a = 6

    b = n

    integral = 0

    for i in range(a - 1, b - 1):

        integral += (dizi[i] + dizi[i + 1]) / 2

    print("Veriler ile hesaplanan sonuç :  ", integral)




def yorumlar():

    with open("180401076_yorum.txt", "w", encoding='utf-8') as dosya :

        dosya.write(" süleyman yalçınkaya \n")

        dosya.write(" 180401076 \n")

        dosya.write(" yamuk metodunuda hesaplamalarda kullandım\n ")

        dosya.write("Hesapladigimiz 2 integral değeri birbirinden farklı  çikmistir. \n")

        dosya.write("  nedeni ise , \n")

        dosya.write("İntegral Hesabi yapılırken , verilen polinomu küçük dikdörtgenlere bölerek ve bunların alanlarını toplayarak hesaplamaya çalışırız. \n ")

        dosya.write("Deltax(dikdörtgenin eni) değerini ne kadar küçültürsek ,işleme katılacak alan sayısı artar ve  bulacağımız değer o kadar gerçeğe yakın olur\n ")

        dosya.write("Ancak bu iki integral arasındaki farkın temel sebebi , birinci integrali  polinom haline getirirken \n ")

        dosya.write("belirli bir korelasyon sayısına göre polinoma yaklaştırmamızdandır.\n ")

        dosya.write("Bu sebepten, deltax değerlerini eşit aldığımızda bile sonuç farklı  olur. \n ")





polinom_ile_integral_hesaplama(n)

veriler_ile_integral_hesaplama(n, dizi)

yorumlar()