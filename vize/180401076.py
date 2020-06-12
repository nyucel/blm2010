#180401076 Süleyman YALÇINKAYA


with open("veriler.txt", "r", encoding='utf-8') as file:
    list1 = []
    for i in file.read().split():
        list1.append(int(i))
genislik= len(list1)#veriler.txt dosyasındaki değerlerin uzunluğu
toplam_veriler=sum(list1)



def x_hesapla(genislik):
    xKareToplam=[]
    xKareToplam.append(genislik)
    for j in range(1,13):
        deger=0
        for i in range(genislik):
            deger += (i + 1) ** j
        xKareToplam.append(deger)
    return xKareToplam



def x_y_hesapla(genislik,list1):
    xi_yi_toplam = []
    xi_yi_toplam.append(sum(list1))
    for i in range(1, 7, 1):
        deger=0
        for j in range(genislik):
            deger += (j + 1) ** i * list1[j]
        xi_yi_toplam.append(deger)
    return xi_yi_toplam


#gauss eleme yöntemi ile değerlerin bulunması
def gauss_eleme(matris):
    n = len(matris)
    for i in range(0, n):
        max = abs(matris[i][i])
        maxSatir = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) > max:
                max = abs(matris[k][i])
                maxSatir = k
        for k in range(i, n + 1):
            tmp = matris[maxSatir][k]
            matris[maxSatir][k] = matris[i][k]
            matris[i][k] = tmp
        for k in range(i + 1, n):
            c = -matris[k][i] / matris[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matris[k][j] = 0
                else:
                    matris[k][j] += c * matris[i][j]
    sonuc = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        sonuc[i] = matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * sonuc[i]
    return sonuc



#polinomun derecesine göre değer yaklaşılır ve matrisi hesaplanır
def olustur_matris(genislik,list1,z):
    x,y=x_hesapla(genislik),x_y_hesapla(genislik,list1)
    matris,satir=[],0
    for i in range(0,z):
        ekleneceksatir=[]
        for i in range(satir,z+satir):
            ekleneceksatir.append(x[i])
        ekleneceksatir.append(y[satir])
        satir+=1
        matris.append(ekleneceksatir)
    return matris



#oluşan matrise a değerlerinin eklenmesi
def iste(list1):
    t = []
    for i in range(2,8):

        t.append(gauss_eleme(olustur_matris(len(list1),list1,i)))
    return t
matrix=iste(list1)


#hesaplanan yeni değerlerin kolarasyonunun çıktı olarak verilmesi,sonuc.txt yazılması

with open("sonuc.txt","a",encoding='utf-8') as file:
    artan = 1
    for j in matrix:
        t= len(j)
        file.write(str(artan)+" .derece"+'\n')
        for y in range(t):
            file.write(str(j[y])+'\n')
        file.write("Kolerasyon:"+str(lastArray[artan-1])+'\n')
        artan +=1
        file.write('\n')
    file.write("verilerin en iyi oluşturulmuş kolerasyon değeri :"+str(lastArray[-1])+'\n')


#oluşacak hata payını bulan fonksiyon
def hesapla_kolerasyon(t,list1,n):
    sr = 0
    st = 0
    toplam_veriler=sum(list1)
    y = toplam_veriler/n
    size = len(t)
    for i in range(n):
        temp = 0
        for j in range(size):
            if j == 0:
                temp +=t[j]
            else:
                temp += t[j]*(i+1)**j
        sr +=(list1[i]-temp)**2
        st +=(list1[i]-y)**2
    r = ((st-sr)/st)**(1/2)
    return r



ata_dizi=[]
for i in range(0,6):
    t=hesapla_kolerasyon(matrix[i],list1,genislik)
    ata_dizi.append(t)

lastArray = sorted(ata_dizi)



