
#Furkan Yazgan 180401052

def veri_oku():
    data = []
    dosya = open('veriler.txt', 'r')
    for i in dosya:
        data.append(int(i))
    dosya.close()
    return data



def toplam_formulu(min,max,us):
    toplam = 0
    for i in range (min,max+1):
        toplam = toplam + (i**us)

    return toplam

def xy_toplam_formulu(veri_dizisi,x_us,x_baslangic):
    toplam = 0
    for y in range(len(veri_dizisi)):
        toplam = toplam + veri_dizisi[y]*((y+x_baslangic)**x_us)

    return toplam

def matris_cozum(veri_matris):

    uzunluk = len(veri_matris)

    for i in range(0, uzunluk):
        max_Sutun = abs(veri_matris[i][i])
        max_Satir = i
        for j in range(i + 1, uzunluk):
            if abs(veri_matris[j][i]) > max_Sutun:
                max_Sutun = abs(veri_matris[j][i])
                max_Satir = j
        for k in range(i, uzunluk + 1):
            temp = veri_matris[max_Satir][k]
            veri_matris[max_Satir][k] = veri_matris[i][k]
            veri_matris[i][k] = temp

        for l in range(i + 1, uzunluk):
            c = -veri_matris[l][i] / veri_matris[i][i]
            for j in range(i, uzunluk + 1):
                if i == j:
                    veri_matris[l][j] = 0
                else:
                    veri_matris[l][j] += c * veri_matris[i][j]

    matris = [0 for i in range(uzunluk)]
    for i in range(uzunluk - 1, -1, -1):
        matris[i] = veri_matris[i][uzunluk] / veri_matris[i][i]
        for k in range(i - 1, -1, -1):
            veri_matris[k][uzunluk] -= veri_matris[k][i] * matris[i]
    return matris


def matris_olustur(veri_dizisi , x_baslangic):
    kat_sayilar = []

    if (x_baslangic == 0):
        start = 1
    elif(x_baslangic == 1):
        start = 0
    uzunluk = len(veri_dizisi)
    for i in range(1, 7):
        matris = []

        for k in range(i + 1):
            satir = []

            for j in range(i + 1):

                if (k == 0 and j == 0):
                    satir.append(uzunluk)
                else:
                    satir.append(toplam_formulu(1, (uzunluk - start) , j + k))

            satir.append( xy_toplam_formulu(veri_dizisi,k,x_baslangic))
            matris.append(satir)

        kat_sayilar.append(matris_cozum(matris))
    return kat_sayilar


def hata_orani(katsatilar_matrisi,veri_dizisi,x_baslangic):
    hata_oranlari = []

    for denklem in katsatilar_matrisi:
        hesaplanan_veriler = []
        for x_verisi in range(x_baslangic,len(veri_dizisi)+x_baslangic):
            hesaplanan_veri = 0
            for k in range(len(denklem)):
                hesaplanan_veri = hesaplanan_veri + denklem[k]*(x_verisi**k)
            hesaplanan_veriler.append(hesaplanan_veri)

        #Sr hesaplama bloğu
        sr = 0
        for index in range(len(veri_dizisi)):
            sr = sr + (veri_dizisi[index] - hesaplanan_veriler[index])**2

        n = len(veri_dizisi)
        m = (len(denklem)-1)
        payda = n - (m+1)
        if ( payda == 0):
            payda = -1

        standart_tahmini_hata = (sr/payda)**(1/2)
        hata_oranlari.append(standart_tahmini_hata)
    min_hata = hata_oranlari[0]
    for i in hata_oranlari:
        if (i < min_hata):
            min_hata = i


    return  (hata_oranlari.index(min_hata)+1),katsatilar_matrisi[hata_oranlari.index(min_hata)]


def polinom_f_x (x):
    katsayilar = en_uygun_polinom_katsaylari
    hesaplanan_veri = 0
    for i in range(len(katsayilar)):
        hesaplanan_veri = hesaplanan_veri + katsayilar[i] * (x ** i)
    return hesaplanan_veri

def a_parametresini_bulma(numara):
    temp = str(numara)
    son_deger = int(temp[len(temp) - 1])
    if(son_deger == 0):
        return 10
    else:
        return son_deger




data = veri_oku()




#soru 1 en uygun dereceli polinom bulundu.
hata_verisi = hata_orani(matris_olustur(data,1),data,1)
en_uygun_polinom_katsaylari = hata_verisi[1]


dosya = open('180401052_yorum.txt', 'w')
dosya.write("Furkan Yazgan 180401052\nSoru 4-)\n")

#soru 1

dosya.write("\nEn dusuk hata oranina sahip olan polinom    : "+str(hata_verisi[0])+".Dereceden olarak bulunmustur.\n")
print("En dusuk hata oranina sahip olan polinom    : "+str(hata_verisi[0])+".Dereceden olarak bulunmustur.")



#soru 2

ogrenci_no = 180401052
a = a_parametresini_bulma(ogrenci_no)
b = len(data)



delta_x = 0.001
integral_sonucu_a = 0
n = int((b-a)/delta_x)

for i in range(n):


    integral_sonucu_a +=delta_x*(polinom_f_x(a)+polinom_f_x(a+delta_x))/2
    a +=delta_x

print("Polinom kullanilarak alan hesabinin sonucu  : "+str(integral_sonucu_a))

#soru3

ogrenci_no = ogrenci_no #yukardaki ogrenci numarasını tekrar aynısını kullandık => 180401052
a = a_parametresini_bulma(ogrenci_no)
b = len(data)

integral_sonucu_b = 0
for i in range(a-1,b-1):

    integral_sonucu_b += (data[i] + data[i + 1]) / 2





print("Polinom kullanmadan  alan hesabinin sonucu  : "+str(integral_sonucu_b))

dosya.write("2.Soruda polinom kullanarak hesapladığım alan : " + str(integral_sonucu_a))

dosya.write("\n3.Soruda polinom kullanmadan hesapladığım alan : " + str(integral_sonucu_b))

dosya.write("""\n\nİki sonuç arasındaki farkın temel nedeni delta_x uzunluğu ve alanı hesaplarken parçalara bölme sayımızdır.
delta_x'i ne kadar küçük alırsak o kadar parça sayımız artar ve parçalar ile grafik arasında boşluklar veya taşmalar
azalacaktır ve hata oranımız düşecektir.

Yani 3.Soruda polinom kullanmadığımız için delta_x'i minimum 1 alabiliyoruz.
Çünkü örnek 82 adet verimiz olsun burada herhangi sıralı iki veri arasındaki verileri bilemediğimiz için
parçalama işlemini bir veriden bir sonraki veriye olacak şekilde yaparız.Bu nedenle delta_x minimum 1 olur ve
oluşturulan parçaların grafik ile arasındaki taşma veya boşluklar artar ve hata oranımız artar.

Son olarak her iki çözümde de yamuk parçaları oluşturarak alan hesapladım, 
yamuk metotunda parça ve grafik arasında taşmalar oluşabiliyor.
Polinom kullanmadığım alan hesabında hata oranı daha fazla olduğu için taşmalar da artmış,
bu nedenle polinom kullanmadan alan hesabının sonucu polinom kullandığım alan hesabının sonucundan fazla çıkmıştır.""")


dosya.close()

#Furkan Yazgan 180401052













