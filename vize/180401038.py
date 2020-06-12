#Berat Safran 180401038
#1. ve 2. maddeleri yapabildim. 3.'nün çıktısı yok hocam.
import math
list = []
data = []
def createListandData():
    file = open('Veriler.txt','r')
    i = 1
    for veri in file:
        data.append(int(veri))
        list.append(i)
        i += 1
def yaz(katsayi,derece,deg):
    dosya = open('sonuc.txt', 'a+')
    dosya.write('\n')
    dosya.write(str(derece) + '. DERECEDEN YAKLASIM \n')

    dosya.write(' Katsayilar: ')
    dosya.write('\n')
    for i in katsayi:
        dosya.write(str(i))
        dosya.write('\t')
    dosya.write('\n' + '-----------------------------' + '\n')
def faultFunc(sonuclarim, first, end):
    n = end - first
    yi = 0
    for i in range(first, end):
        yi += data[i]
    y_ussu = yi / n  # y'lerin ortalamsi
    w1 = 0
    for i in range(first, end):
        w1 = (sonuclarim[i - first] - data[i]) ** 2 + w1
    w2 = 0
    for i in range(first, end):
        w2 = w2 + (data[i] - y_ussu) ** 2
    rkare = abs((w2 - w1) / w2)
    r = math.sqrt(rkare)
    return r
def gauss(A):
    boyut = len(A)
    for i in range(0, boyut):
        maxSutun = abs(A[i][i])
        maxSatir = i
        for j in range(i + 1, boyut):
            if abs(A[j][i]) > maxSutun:
                maxSutun = abs(A[j][i])
                maxSatir = j
        for k in range(i, boyut + 1):
            temp = A[maxSatir][k]
            A[maxSatir][k] = A[i][k]
            A[i][k] = temp

        for l in range(i + 1, boyut):
            c = -A[l][i] / A[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    A[l][j] = 0
                else:
                    A[l][j] += c * A[i][j]

    matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        matris[i] = A[i][boyut] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][boyut] -= A[k][i] * matris[i]
    return matris
def veri():
    hata = []
    n = len(data)
    for derece in range(1,7):
        xToplamlari = []
        if derece == 1:
            for i in range(derece + 1):
                xToplamlari.append([])
                for j in range(i,i+2):
                    xToplam = 0
                    for k in range(len(list)):
                        xToplam += list[k] ** j
                    xToplamlari[i].append(xToplam)

            xyToplamlari = []
            for i in range(derece+1):
                toplam = 0
                for k in range(len(data)):
                    toplam += data[k] * list[k] ** i
                xyToplamlari.append(toplam)

            k = 0
            for b in xToplamlari:
                b.append(xyToplamlari[k])
                k = k + 1

            katsayilar = gauss(xToplamlari)

            myResult = []
            for i in range(len(list)):
                toplam = 0
                for j in range(len(katsayilar)):
                    toplam += katsayilar[j] * ((i + 1) ** j)
                    if j == derece:
                        myResult.append(int(toplam))
            f = faultFunc(myResult, 0, len(data))
            hata.append(f)
            yaz(katsayilar,derece,f)
        else:
            a = 0
            for i in range(derece + 1):
                temp = a
                xToplamlari.append([])
                for j in range(derece + 1):
                    xToplam = 0
                    for k in range(len(list)):
                        xToplam += list[k] ** a
                    a += 1
                    xToplamlari[i].append(xToplam)
                temp += derece - 1
                a = 0
                a += temp
            xyToplamlari = []
            for i in range(derece+1):
                toplam = 0
                for k in range(len(data)):
                    toplam += data[k] * list[k] ** i
                xyToplamlari.append(toplam)
            k = 0
            for b in xToplamlari:
                b.append(xyToplamlari[k])
                k = k + 1

            katsayilar = gauss(xToplamlari)

            myResult = []
            for i in range(len(list)):
                toplam = 0
                for j in range(len(katsayilar)):
                    toplam += katsayilar[j] * ((i+1) ** j)
                    if (j == derece):
                        myResult.append(int(toplam))

            f = faultFunc(myResult,0,n)

            hata.append(f)
            yaz(katsayilar,derece, f)
    bestChoice = 100
    index = 0

    for i in range(len(hata)):
        temp = abs(1 - hata[i])

        if temp < bestChoice:
            bestChoice = temp
            index = i + 1

    dosya = open('sonuc.txt', 'a+')
    dosya.write(
        str(0) + '-' + str(n - 1) + ' aralığında en uygun polinom: ' + str(6) + '\n')
    dosya.write('\n ---------------------------------------------- \n')
    dosya.write('\n')
    dosya.close()

createListandData()
veri()

