""" Mehmet Said Turken     180401030"""


dosya = open("veriler.txt.txt", "r")
veri = []

for i in dosya.read().split():   
        veri.append(int(i))

n = len(veri)
yitoplam = sum(veri)

def x_degerleri(list, n):    
    valuex = []
    for i in range(13):
        x = 0
        for k in range(n):
            x += (k+1)**i
        valuex.append(x)
    return valuex
def toplam_xiyi(list, n):
    toplam_xiyi = []
    for i in range(7):
        xiyi = 0
        for k in range(n):
            xiyi += ((k+1)**i)*(list[k])
        toplam_xiyi.append(xiyi)
    return toplam_xiyi

def gaussyontemi(matris):     #EBD (en buyuk deger)--- EBS(en buyuk satir)
    n = len(matris)
    for i in range(0, n):
        EBD = abs(matris[i][i])
        EBS = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) >EBD:
                EBD = abs(matris[k][i])
                EBS = k
       
        
        for k in range(i, n + 1):
            temp = matris[EBS][k]
            matris[EBS][k] = matris[i][k]
            matris[i][k] = temp
       
        
        for k in range(i + 1, n):
            c = -matris[k][i] / matris[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matris[k][j] = 0
                else:
                    matris[k][j] += c * matris[i][j]
                      
    son = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        son[i] =matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * son[i]
    return son
#polinomlarin denklemlere yaklastirip katsayilarin return edildigi fonksiyon
def liste_cozum(list, n):
    cozum = []
    for i in range(2, 8):
        degerler = []
        for j in range(i):
            degerler.append([])
            for k in range(i):
                degerler[j].append(x_degerleri(list, n)[k + j])
            degerler[j].append(toplam_xiyi(list, n)[j])
            if j == i - 1:
                cozum.append(gaussyontemi(degerler))
                degerler.clear()
    return cozum
                    
def deger_st(x, veri, n, yitoplam):   #St nin degerini bulacagimiz fonksiyon
    y_ort = yitoplam / n
    st = 0
    for i in range(n):
        st += (veri[i] - y_ort) ** 2
    return st

def sr_korelasyon(x, veri, n, yitoplam):  #sr'yi buluyoruz,korelasyon katsayilarini donduruyoruz.
    sr = 0
    for i in range(n):
        hesaplama = 0
        hesaplama += x[0]
        for j in range(1, len(x)):
            hesaplama += x[j] * (i + 1) ** j
        sr += (veri[i] - hesaplama) ** 2
        
    return ((deger_st(x, veri, n, yitoplam) - sr) / deger_st(x, veri, n, yitoplam)) ** (1/2)   


def korelasyon_list(korelasyon_degerleri, veri, n, yitoplam):
    deger = []
    for i in korelasyon_degerleri:
        deger.append(sr_korelasyon(i, veri, n, yitoplam))
    return deger

def optimaldeger(korelasyon_degerleri, veri, n, yitoplam):
    a = korelasyon_list(korelasyon_degerleri, veri, n, yitoplam)
    ilk = 150
    list = []
    for i in range(len(a)):
        degerr = abs(1-a[i])
        if int(degerr) < 0:
            degerr *= -1
        if degerr < ilk:
            ilk = degerr
            list.clear()
            list.append((i+1, a[i]))
    return list

def yaz():
    filenew = open("sonuc.txt", "w+")
    filenew.write("*tum degerler icin**" + "\n")
    a = 0
    for i in liste_cozum(veri, n):
        filenew.write("\t"+ str(a+1) + ". derece"+ "\n")
        b = 0
        for k in i:
            filenew.write(str(b+1) + ". deger = " + str(k)+"\n")
            b += 1
        filenew.write("Korelasyon = " + str(korelasyon_list(liste_cozum(veri, n), veri, n, yitoplam)[a])+"\n")
        a += 1
    filenew.write("\n*En uygun polinom ve korelasyon degeri = " + str( optimaldeger(liste_cozum(veri, n), veri, n, yitoplam)[0]) + "*\n")
    
    for j in range(len(veri)):
        a = 0
        newlist = []
        if(j + 10 > len(veri)):
            break
        for l in range(j, j+10):
            newlist.append(veri[l])
        filenew.write("*" + str(j+1) + " ile " + str(j+10) + " arasindaki degerler icin*")
        filenew.write("\n*En uygun polinom ve korelasyon degeri = " + str( optimaldeger(liste_cozum(newlist, len(newlist)), newlist, len(newlist), sum(newlist))[0]) + "*\n")
           
    bas = 1
    bit = 10
    a = 0
    for j in range(len(veri)):
        newlist = []
        if ((bit*a)+10 > len(veri)):
            break
        for l in range((bas*a*10), bit*a + 9):
            newlist.append(veri[l])
        filenew.write("**" + str(bas*a*10) + " ile " + str(bit*a + 9) + " arasindaki degerler icin**")
        filenew.write("\n*En uygun polinom ve korelasyon degeri = " + str(optimaldeger(liste_cozum(newlist, len(newlist)), newlist, len(newlist), sum(newlist))[0]) + "*\n")
        a += 1
    filenew.close()
yaz()    
