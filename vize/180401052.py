#Furkan Yazgan 180401052

def veri_oku():
    data = []
    dosya = open('veriler.txt', 'r')
    for i in dosya:
        data.append(int(i))
    dosya.close()
    return data



def toplam_formulu(min,max,üs):
    toplam = 0
    for i in range (min,max+1):
        toplam = toplam + (i**üs)

    return toplam

def xy_toplam_formulu(veri_dizisi,x_üs,x_baslangıc):
    toplam = 0
    for y in range(len(veri_dizisi)):
        toplam = toplam + veri_dizisi[y]*((y+x_baslangıc)**x_üs)

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


def matris_olustur(veri_dizisi , x_baslangıc):
    kat_sayılar = []

    if (x_baslangıc == 0):
        start = 1
    elif(x_baslangıc == 1):
        start = 0
    uzunluk = len(veri_dizisi)
    for i in range(1, 7):
        matris = []

        for k in range(i + 1):  # satır işlemleri
            satır = []

            for j in range(i + 1):  # sütun işlemleri

                if (k == 0 and j == 0):
                    satır.append(uzunluk)
                else:
                    satır.append(toplam_formulu(1, (uzunluk - start) , j + k))

            satır.append( xy_toplam_formulu(veri_dizisi,k,x_baslangıc))
            matris.append(satır)

        kat_sayılar.append(matris_cozum(matris))
    return kat_sayılar


def hata_oranı(katsatılar_matrisi,veri_dizisi,x_baslangıc):
    hata_oranları = []

    for denklem in katsatılar_matrisi:
        hesaplanan_veriler = []
        for x_verisi in range(x_baslangıc,len(veri_dizisi)+x_baslangıc):
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
        hata_oranları.append(standart_tahmini_hata)
    min_hata = hata_oranları[0]
    for i in hata_oranları:
        if (i < min_hata):
            min_hata = i


    return min_hata , (hata_oranları.index(min_hata)+1)





data = veri_oku()
data_uzunluk = len(data)







dosya = open('sonuc.txt','w')

# 1.Soru

dosya.write("--------------------------------------------------------------------------------------------\nFurkan Yazgan 180401052\n")
derece = 1
for i in matris_olustur(data,1):
    dosya.write(str(derece)+".Dereceden Polinomun Katsayilari " +  str(i) + "\n")
    derece +=1


# 2.Soru

hata_verisi = hata_oranı(matris_olustur(data,1),data,1)
dosya.write("\n \nTum veriler icin en uygun polinom = "+str(hata_verisi[1])+".Dereceden \nStandart tahmini hata = "+str(hata_verisi[0])+"\n\n\n")


#3.Soru
baslangıc = 0
bitis = 9

while(bitis != data_uzunluk ):
    dosya.write(str([baslangıc + 1, bitis + 1])+" -- ")

    temp = hata_oranı(matris_olustur(data[baslangıc:bitis+1], 1), data[baslangıc:bitis+1], 1)
    dosya.write( "Arasi verileri icin en uygun polinom = "+str(temp[1])+".Dereceden \n")


    baslangıc +=1
    bitis +=1

dosya.write("-----------------------------------------------------------------\n")

#Furkan Yazgan 180401052


