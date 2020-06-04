#Ahmet Furkan KURT 170401002

file = open("veriler.txt", "r")
datas = []

for i in file:
    datas.append(int(i))


n = len(datas)
yitoplam = sum(datas)


def xiyitoplamlari(list, n):
    xiyiler = []
    for i in range(7):
        xiyi = 0
        for k in range(n):
            xiyi += ((k+1)**i)*(list[k])
        xiyiler.append(xiyi)
    return xiyiler


def kullanilacakxdegerleri(list, n):
    xler = []
    for i in range(13):
        x = 0
        for k in range(n):
            x += (k+1)**i
        xler.append(x)
    return xler






def gausselemeyontemi(degerler):
    n = len(degerler)

    for i in range(0, n):
       
        maxdeger = abs(degerler[i][i])
        maxsatir = i
        for k in range(i + 1, n):
            if abs(degerler[k][i]) > maxdeger:
                maxdeger = abs(degerler[k][i])
                maxsatir = k

     
        for k in range(i, n + 1):
            temp = degerler[maxsatir][k]
            degerler[maxsatir][k] = degerler[i][k]
            degerler[i][k] = temp

        
        for k in range(i + 1, n):
            c = -degerler[k][i] / degerler[i][i]
            for j in range(i, n + 1):
                if i == j:
                    degerler[k][j] = 0
                else:
                    degerler[k][j] += c * degerler[i][j]

    
    sonmatris = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        sonmatris[i] = degerler[i][n] / degerler[i][i]
        for k in range(i - 1, -1, -1):
            degerler[k][n] -= degerler[k][i] * sonmatris[i]
    return sonmatris


def stdeger(x, datas, n, yitoplam):
    yort = yitoplam / n
    st = 0
    for i in range(n):
        st += (datas[i] - yort) ** 2
    return st


def cozumlerilistele(list, n):
    cozum = []
    for i in range(2, 8):
        degerlistesi = []
        for j in range(i):
            degerlistesi.append([])
            for k in range(i):
                degerlistesi[j].append(kullanilacakxdegerleri(list, n)[k + j])
            degerlistesi[j].append(xiyitoplamlari(list, n)[j])
            if j == i - 1:
                cozum.append(gausselemeyontemi(degerlistesi))
                degerlistesi.clear()
    return cozum



def korelasyonvesrdegeri(x, datas, n, yitoplam):
    sr = 0
    for i in range(n):
        hesaplama = 0
        hesaplama += x[0]
        for j in range(1, len(x)):
            hesaplama += x[j] * (i + 1) ** j
        sr += (datas[i] - hesaplama) ** 2

    return ((stdeger(x, datas, n, yitoplam) - sr) / stdeger(x, datas, n, yitoplam)) ** (1/2)

def korelasyonliste(korelasyondegerleri, datas, n, yitoplam):
    rdegerleri = []
    for i in korelasyondegerleri:
        rdegerleri.append(korelasyonvesrdegeri(i, datas, n, yitoplam))
    return rdegerleri


def bireenyakindeger(korelasyondegerleri, datas, n, yitoplam):
    a = korelasyonliste(korelasyondegerleri, datas, n, yitoplam)
    first = 150
    list = []
    for i in range(len(a)):
        deger = abs(1-a[i])
        if int(deger) < 0:
            deger *= -1
        if deger < first:
            first = deger
            list.clear()
            list.append((i+1, a[i]))
    return list


def yazdirma():
    filenew = open("sonuc.txt", "w+")
    filenew.write("*******************BUTUN DEGERLER ICIN*******************" + "\n\n\n")
    a = 0
    for i in cozumlerilistele(datas, n):
        filenew.write("\t\t"+ str(a+1) + ". derece"+ "\n")
        b = 0
        for k in i:
            filenew.write(str(b+1) + ". deger = " + str(k)+"\n")
            b += 1
        filenew.write("Korelasyon = " + str(korelasyonliste(cozumlerilistele(datas, n), datas, n, yitoplam)[a])+"\n")
        a += 1
    filenew.write("\n\t***Butun degerler icin en uygun polinom ve korelasyon degeri = " + str(
        bireenyakindeger(cozumlerilistele(datas, n), datas, n, yitoplam)[0]) + "***\n\n\n")


    for j in range(len(datas)):
        a = 0
        yeniliste = []
        if(j + 10 > len(datas)):
            break
        for l in range(j, j+10):
            yeniliste.append(datas[l])
        filenew.write("*******************" + str(j+1) + " ile " + str(j+10) + " arasindaki degerler icin*******************")
        filenew.write("\n\t***Bu araliktakiler icin en uygun polinom ve korelasyon degeri = " + str(
            bireenyakindeger(cozumlerilistele(yeniliste, len(yeniliste)), yeniliste, len(yeniliste), sum(yeniliste))[0]) + "***\n\n\n")

    bas = 1
    bit = 10
    a = 0
    for j in range(len(datas)):
        yeniliste = []
        if ((bit*a)+10 > len(datas)):
            break
        for l in range((bas*a*10), bit*a + 9):
            yeniliste.append(datas[l])
        filenew.write(
            "*******************" + str(bas*a*10) + " ile " + str(bit*a + 9) + " arasindaki degerler icin*******************")
        filenew.write("\n\t***Bu araliktakiler icin en uygun polinom ve korelasyon degeri = " + str(
            bireenyakindeger(cozumlerilistele(yeniliste, len(yeniliste)), yeniliste, len(yeniliste), sum(yeniliste))[0]) + "***\n\n\n")
        a += 1
    filenew.close()
yazdirma()
