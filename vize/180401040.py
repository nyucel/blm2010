# ad-soyad : Ramazan AYDIN   ---  numara : 180401040

print("\n\n")

"""

Bu  python kodunda ;
parametre olarak verilen dosyadaki (veriler.txt) verilerin hem hepsini hem de onlu  veri grupları
için sırasıyla 1,2,3,4,5,6. dereceden polinoma yakınlaştırarak bu polinomların hata değerlerini, katsayı
değerlerini ve en uygun polinomları sonuc.txt dosyasına yazacagız.

"""

# veriler.txt dosyasına gider ve oradaki verilerin tamamını okur.
with open("veriler.txt", "r", encoding='utf-8') as file:
    dizi = []   #dizi adında bir liste oluşturduk.
    for i in file.read().split():
        dizi.append(int(i))  #veriler.txt dosyasından okuduğumuz verileri diziye ekledik.

n = len(dizi)   # n'ye dizinin boyutunu atadık

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

def en_iyi_kolerasyon(dizi):        #  Bu fonksiyon 1'e en yakın olan kolerasyon değerini döndürür
    sirali_dizi = sorted(dizi)      # sorted fonksiyonu ile diziyi sıraladık.
    biggest = sirali_dizi[-1]
    b = 1
    while (biggest != dizi[b - 1]):
        b = b + 1
    return b, biggest

"""
bu fonksiyonda 0-9 , 10-19... gibi onlu gruplar için hesaplama yapacagız.
"""

def grupların_korelasyonu_hesapla(dizi):
    kolerasyon_gruplar = []    #bir dizi oluşturduk ; bulduğumuz korelasyonları bu diziye atacağız
    x = int(len(dizi) / 10)    #diziyi onar onar alacağımız için 10'a böldük

    ilk = 0
    son = 0

    for i in range(x):
        ilk = i * 10
        son = (i + 1) * 10

        gecici = []
        for j in range(ilk, son, 1):
            gecici.append(dizi[j])
        kolerasyon_gruplar.append(gecici)
    return kolerasyon_gruplar


"""
tüm veriler için buldugumuz sonuçlar
"""

with open("sonuc.txt", "a", encoding='utf-8') as dosya:
    dosya.write("polinomların yazim biçimi \n")
    dosya.write("1.  derece polinom için : a,bx    2. derece polinom için : a,bx,cx²    3. derece polinom için : a,bx,cx²,dx³ \n")
    dosya.write("4.  derece polinom için : a,bx,cx²,dx³,ex⁴   5. derece polinom için : a,bx,cx²,dx³,ex⁴,fx⁵ \n ")
    dosya.write("6.  derece polinom için : a,bx,cx²,dx³,ex⁴,fx⁵,gx⁶ \n\n ")
    dosya.write("Bütün polinomlar için katsayı değerleri :" + '\n\n')

    for i in deger_a:
        dosya.write(str(len(i) - 1) + ".Derece Polinom için Katsayılar" + "\n\n")

        for j in i:

            dosya.write(  str(j) + "\n")
        x = Hata_Hesaplama(i, dizi, n, totalyi)
        dosya.write("\n"+ str(len(i) - 1) + ".Derece Polinom için Korelasyon Değeri" +"\n")
        dosya.write(str(x) + "\n")

        dosya.write("\n")
        dosya.write("****************************\n")

    dosya.write("Tüm veriler için en uygun Polinom  6. Derece Polinom : " + "\n")
    dosya.write("6. Derece Polinom için korelasyon değeri : " + str(x) + "\n")

# 10 lu gruplar için buldugumuz sonuçlar

    grup = grupların_korelasyonu_hesapla(dizi)
    aralik = 0
    for o in grup:
        Korelasyons = []
        dosya.write("******************************\n")
        dosya.write(str(aralik * 10) + '-' + str((aralik + 1) * 10 - 1) + ' aralığındaki veriler için katsayılar:' + "\n")
        yeniDeger = value_of_a(len(o), o)
        for p in yeniDeger:
            dosya.write(str(len(p) - 1) + ".Derece Polinom için katsayılar" + "\n")
            for r in p:
                dosya.write(str(r) + '\n')
            s = Hata_Hesaplama(p, o, len(o), sum(o))
            Korelasyons.append(s)

            dosya.write("\n" +str(len(p) - 1) + ". Derece Polinom için Korelasyon Değeri :" + '\n')
            dosya.write(str(s)+ "\n")
            dosya.write("******************************\n")
            dosya.write('\n')
        index, bestKol = en_iyi_kolerasyon(Korelasyons)
        dosya.write(str(aralik * 10) + '-' + str((aralik + 1) * 10 - 1) + " verileri arasında en uygun polinom =>  " + str(
            index) + ".Derece Polinom: " + "\n")
        dosya.write(str(index) +".Derece polinomun korelasyon değeri : "+str(bestKol)+ "\n" )
        aralik = aralik + 1