# -*- coding: utf-8 -*-

# 170401009 ATAKAN TÜRKAY
# python3 ile kodlandı.


import decimal
import itertools  # RANGE STEPLERİ İNT DEĞER KABUL EDİYOR SADECE

# FLOAT BİR DEĞERLE İLERLETMEK İÇİN SEQ FONKSİYONU EKLENDİ

veriler_x = [[]]
veriler_y = [[]]
katsayilar_matrisi = []


def dosya_oku(dosya="veriler.txt", veriler_x=veriler_x,
              veriler_y=veriler_y):  # içerisine bir dosya ve boş bir dizi alır.
    with open('veriler.txt', 'r') as f:
        veriler_y[0].extend(map(int,
                                f.read().splitlines()))  # \n göstermeden dosyanın içindeki satırları dizinin içerisine aktarıyor ve integer yapıyor.
    for i in range(len(veriler_y[0])):
        veriler_x[0].append(i + 1)


def matris_olustur(satir_uzunlugu, sutun_uzunlugu, datas):
    vandermonde = []
    for k in range(0, satir_uzunlugu):
        vandermonde.append([])
    for i in range(satir_uzunlugu):
        for j in range(sutun_uzunlugu + 1):
            vandermonde[i].append(datas[i][0] ** (j))
    return vandermonde


def matris_transpose(matris):
    transposem = []
    sutun_uzunlugu = len(matris)
    satir_uzunlugu = len(matris[0])
    for k in range(satir_uzunlugu):
        transposem.append([])
    for n in range(satir_uzunlugu):
        for m in range(sutun_uzunlugu):
            transposem[n].append(matris[m][n])
    return transposem


def matris_carpimi(firstmatris, secondmatris):
    result = []
    for i in range(len(firstmatris)):
        result.append([])
        for j in range(len(secondmatris[0])):
            total = 0
            for k in range(len(secondmatris)):
                total += firstmatris[i][k] * int(secondmatris[k][j])
            result[i].append(total)
    return result


def matris_ters(old_matris):
    matris = old_matris
    Imatris = []  # Birim Matris
    for i in range(len(matris)):  # Matris ile boyutu aynı birim matris oluşturma
        Imatris.append([])
        for j in range(len(matris)):
            if (i == j):
                Imatris[i].append(1)
            else:
                Imatris[i].append(0)

    for i in range(len(matris)):
        bolen = matris[i][i]
        for j in range(len(matris)):
            matris[i][j] = matris[i][j] / bolen
            Imatris[i][j] = Imatris[i][j] / bolen
        for k, z in zip(matris[i + 1:], Imatris[i + 1:]):
            carpan = k[i]
            for m in range(len(k)):
                k[m] = k[m] - matris[i][m] * carpan
                z[m] = z[m] - Imatris[i][m] * carpan

    for i in range(len(matris) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            carpan = matris[j][i] / matris[i][i]
            for k in range(len(matris)):
                matris[j][k] -= carpan * matris[i][k]
                Imatris[j][k] -= carpan * Imatris[i][k]
    return Imatris


def olustur(katsayilar_matrisi=katsayilar_matrisi, veriler_x=veriler_x, veriler_y=veriler_y):
    for degree in range(1, 7):
        katsayilar_matrisi.append([])
        vandermondematris = matris_olustur(len(veriler_x), degree, veriler_x)
        transpose = matris_transpose(vandermondematris)
        product = matris_carpimi(transpose, vandermondematris)
        mult = matris_carpimi(matris_ters(product), transpose)
        sonuc = matris_carpimi(mult, veriler_y)
        for m in range(len(sonuc)):
            katsayilar_matrisi[degree - 1].append(sonuc[m])
    # f = open('sonuc.txt', 'w')
    # f.write("----- Elde Edilen Katsayilar(a0 a1 a2) -----\n")
    # f.close()
    # for i in range(6):
    #     with open('sonuc.txt', 'a') as f:
    #         f.write(f"{i + 1}. derece polinomun katsayıları:{katsayilar_matrisi[i]}\n")


def hata_hesapla(veriler_x, veriler_y, katsayilar_matrisi):
    hm1, hm2, hm3, hm4, hm5, hm6 = [], [], [], [], [], []
    for i in veriler_x:
        # print((veriler_y[i[0]-1][0],(katsayilar_matrisi[5][0][0]+katsayilar_matrisi[5][1][0]*i[0]+katsayilar_matrisi[5][2][0]*(i[0]**2)+katsayilar_matrisi[5][3][0]*(i[0]**3)+katsayilar_matrisi[5][4][0]*(i[0]**4)+katsayilar_matrisi[5][5][0]*(i[0]**5)+katsayilar_matrisi[5][6][0]*(i[0]**6),veriler_y[i[0]-1][0]-(katsayilar_matrisi[5][0][0]+katsayilar_matrisi[5][1][0]*i[0]+katsayilar_matrisi[5][2][0]*(i[0]**2)+katsayilar_matrisi[5][3][0]*(i[0]**3)+katsayilar_matrisi[5][4][0]*(i[0]**4)+katsayilar_matrisi[5][5][0]*(i[0]**5)+katsayilar_matrisi[5][6][0]*(i[0]**6)))))

        # Hata miktarlarını hesaplıyor.

        hm1.append(abs(veriler_y[i[0] - 1][0] - (katsayilar_matrisi[0][0][0] + katsayilar_matrisi[0][1][0] * i[0])))
        hm2.append(abs(veriler_y[i[0] - 1][0] - (
                katsayilar_matrisi[1][0][0] + katsayilar_matrisi[1][1][0] * i[0] + katsayilar_matrisi[1][2][0] * (
                i[0] ** 2))))
        hm3.append(abs(veriler_y[i[0] - 1][0] - (
                katsayilar_matrisi[2][0][0] + katsayilar_matrisi[2][1][0] * i[0] + katsayilar_matrisi[2][2][0] * (
                i[0] ** 2) + katsayilar_matrisi[2][3][0] * (i[0] ** 3))))
        hm4.append(abs(veriler_y[i[0] - 1][0] - (
                katsayilar_matrisi[3][0][0] + katsayilar_matrisi[3][1][0] * i[0] + katsayilar_matrisi[3][2][0] * (
                i[0] ** 2) + katsayilar_matrisi[3][3][0] * (i[0] ** 3) + katsayilar_matrisi[3][4][0] * (
                        i[0] ** 4))))
        hm5.append(abs(veriler_y[i[0] - 1][0] - (
                katsayilar_matrisi[4][0][0] + katsayilar_matrisi[4][1][0] * i[0] + katsayilar_matrisi[4][2][0] * (
                i[0] ** 2) + katsayilar_matrisi[4][3][0] * (i[0] ** 3) + katsayilar_matrisi[4][4][0] * (
                        i[0] ** 4) + katsayilar_matrisi[4][5][0] * (i[0] ** 5))))
        hm6.append(abs(veriler_y[i[0] - 1][0] - (
                katsayilar_matrisi[5][0][0] + katsayilar_matrisi[5][1][0] * i[0] + katsayilar_matrisi[5][2][0] * (
                i[0] ** 2) + katsayilar_matrisi[5][3][0] * (i[0] ** 3) + katsayilar_matrisi[5][4][0] * (
                        i[0] ** 4) + katsayilar_matrisi[5][5][0] * (i[0] ** 5) + katsayilar_matrisi[5][6][0] * (
                        i[0] ** 6))))

    return hm1, hm2, hm3, hm4, hm5, hm6


def en_az_hata_hesapla(hm):
    en_az = 9999999999999999  # ilk küçük gelende değişmesi için böyle değer verildi.
    indis = 0
    for i in range(6):
        kare_toplamları = 0
        for j in hm[i]:
            kare_toplamları = kare_toplamları + j ** 2  # ÖNCEKİ KODDA BURADA HATA VARDI FİXLEDİM.
        if kare_toplamları < en_az:
            en_az = kare_toplamları
            indis = i
    return en_az, indis


def en_az_hata_aralık(hm, x, y):
    en_az = 9999999999999999  # ilk küçük gelende değişmesi için böyle değer verildi.
    indis = 0
    for i in range(6):
        kare_toplamları = 0
        for j in hm[i][x - 1:y]:
            kare_toplamları = kare_toplamları + j ** 2  # ÖNCEKİ KODDA BURADA HATA VARDI FİXLEDİM.
        if kare_toplamları < en_az:
            en_az = kare_toplamları
            indis = i
    return en_az, indis


def fonksiyon(x, fonksiyon_derece):
    y_degeri = 0
    for i in range(fonksiyon_derece + 1):
        y_degeri += (katsayilar_matrisi[fonksiyon_derece - 1][i][0] * (
                x ** i))  # Fonksiyonu a0 a1 değerlerine x değerlerini yerleştirip hesaplar

    # print(y_degeri)
    return y_degeri


def seq(start, end, step):  # Bu fonksiyonu range yerine kullanıyorum.Float için
    assert (step != 0)
    sample_count = int(abs(end - start) / step)
    return itertools.islice(itertools.count(start, step), sample_count)


def integral_hesabi_polinom(fonksiyon_derece):
    a, b = 9, len(veriler_x)  # 170401009 -> 9
    deltax = 0.001
    temp_integral = 0.0
    for i in seq(a, len(veriler_x) + 1, deltax):  # delta x kadar artarak tek tek hesaplayacak. Len alınan verilerin sonuncusuna kadar eşitlendi çünkü
        if i == len(veriler_x):  # son değerde ilerisi olmadığı için hesaplaması fazlalık oluyor.deltax ilerisi yok
            break
        # print("HESAPLANAN ARALIK" + str(i) + "-" + str(i + deltax))

        temp_integral += abs((deltax / 2) * (fonksiyon(i, fonksiyon_derece) + fonksiyon(i + deltax, fonksiyon_derece)))
    print(str(a) + "-" + str(b) + " Aralığında (delta = "+str(deltax)+") polinom ile hesaplanan integral değeri= " + str(temp_integral))
    return temp_integral


def integral_hesabi_veriler():
    a, b = 9, len(veriler_x)  # 170401009 -> 9
    deltax = 1 #günler 1 er 1 er ilerlediği için deltamızın aralığı 1
    temp_integral = 0.0
    for i in seq(a-1, len(veriler_x), deltax):  # delta x kadar artarak tek tek hesaplayacak. Len alınan verilerin sonuncusuna kadar eşitlendi çünkü
        if i == len(veriler_x)-1:  # son değerde ilerisi olmadığı için hesaplaması fazlalık oluyor.deltax ilerisi yok
            break
        # print("HESAPLANAN ARALIK" + str(i+1) + "-" + str(i + deltax+1))

        temp_integral += abs((deltax / 2) * (veriler_y[i][0] + veriler_y[i+1][0]))
        # print(temp_integral)
    print(str(a)+"-"+str(b)+" Aralığında (delta = "+str(deltax)+") değerler ile hesaplanan integral değeri= "+str(temp_integral))
    return temp_integral







#######################################
print("Program çalışmaya başladı.")
dosya_oku()
#######################################
veriler_y = matris_transpose(veriler_y)
veriler_x = matris_transpose(veriler_x)
olustur(katsayilar_matrisi, veriler_x, veriler_y)  # katsayıları hesaplıyorum.
print("Katsayılar bulundu...")
# print(*katsayilar_matrisi, sep="\n")
#######################################
hm = hata_hesapla(veriler_x, veriler_y,
                  katsayilar_matrisi)  # her derece için ayrı şekilde diziler halinde hesaplanıyor.Hm içinde diziler tutan bir tuple.
print("Hatalar hesaplandı...")
# print(*hm,sep="\n") #hataları basar.
#######################################
enaz, indis = en_az_hata_hesapla(hm)  # en az miktarda hatayı sağlayan dereceyi buluyor.
print("Hata miktarı " + str(round(enaz, 2)) + " ile en uygun polinom " + str(
    indis + 1) + ". dereceden polinom olmuştur...")
#######################################
integral_polinom = integral_hesabi_polinom(indis+1)
integral_veriler  =integral_hesabi_veriler()
#######################################
file = open("170401009_yorum.txt", "w", encoding="utf-8")
file.write(str(indis+1) + ". dereceden polinom en uygun polinomdur.\n")
file.write("Polinom kullanılarak alınan integral değeri: " + str(integral_polinom) + "\n")
file.write("Polinom kullanılmadan alınan integral değeri: " + str(integral_veriler) + "\n")
file.write("----------------------------------------------\n")
file.write("----------------------------------------------\n")
file.write("----------------------------------------------\n")
file.write("""3. ve 4. adımlarda bulunan sonuçlar arasındaki farkın nedeni

  Polinomla yapılan hesapta tamamen uygun değerlerle değil,yakınsama yapılarak elde
edilen değerler ile işlem yapıyoruz.Bazı değerler gerçek değerlerden daha yüksek iken 
bazı değerler alçak.Bu da sonuçta farklılık ortaya çıkartıyor.Hesapladığımız polinom
gerçekteki hastalık fonksiyonunu tam olarak örtmüyor.
  Eğer hata miktarımız 0 olsaydı ve 2 integrali de deltax=1 olarak alsaydık aynı sonuç
elde edilebilirdi.
""")
file.write("----------------------------------------------\n")
file.write("----------------------------------------------\n")
file.write("----------------------------------------------\n")
file.close()


#######################################
print("Program sonlanacak...")

"""
Değişkenler

enaz               #en az hata miktarı(float)
indis+1            #en az hata miktarı olan fonksiyon(int)
hm                 #her polinom için gerçek değerlerdeki hata miktarlarını tutan tuple hm[0-5][0-81]
katsayilar_matrisi #katsayıları tutan matristir katsayilar_matrisi[0-5][]
veriler_x          #günleri tutuyor.(list)
veriler_y          #değerleri tutuyor.(list)
"""