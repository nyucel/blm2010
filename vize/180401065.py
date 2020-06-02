#180401065 Onur Askin
with open("veriler.txt", "r", encoding='utf-8') as file:
    liste = []
    for i in file.read().split():
        liste.append(int(i))
uzunluk = len(liste)#okuduğum dosyadaki verilerin uzunluğu
yToplam=sum(liste)



def xitoplam(uzunluk):
    xKareToplam=[]
    xKareToplam.append(uzunluk)
    for j in range(1,13):
        deger=0
        for i in range(uzunluk):
            deger += (i + 1) ** j
        xKareToplam.append(deger)
    return xKareToplam



def xiyiToplam(uzunluk,liste):
    xi_yi_toplam = []
    xi_yi_toplam.append(sum(liste))
    for i in range(1, 7, 1):
        deger=0
        for j in range(uzunluk):
            deger += (j + 1) ** i * liste[j]
        xi_yi_toplam.append(deger)
    return xi_yi_toplam


#Elementer satır işlemleriyle bilinmeyen değerleri bu şekilde buldum
def gaussYontemi(matris):
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



#Yaklaşılacak polinomun derecesine göre matrisi oluşturuyor.
def matrisOlustur(uzunluk,liste,m):
    x,y=xitoplam(uzunluk),xiyiToplam(uzunluk,liste)
    matris,satir=[],0
    for i in range(0,m):
        ekleneceksatir=[]
        for i in range(satir,m+satir):
            ekleneceksatir.append(x[i])
        ekleneceksatir.append(y[satir])
        satir+=1
        matris.append(ekleneceksatir)
    return matris


#Matris değişkenine a.? değerlerini eklediğim func.
def cagir(liste):
    x = []
    for i in range(2,8):

        x.append(gaussYontemi(matrisOlustur(len(liste),liste,i)))
    return x
matrix=cagir(liste)


#Hata payını bulduğum func.
def Kolerasyon(x,liste,n):
    sr = 0
    st = 0
    yToplam=sum(liste)
    y = yToplam/n
    size = len(x)
    for i in range(n):
        temp = 0
        for j in range(size):
            if j == 0:
                temp +=x[j]
            else:
                temp += x[j]*(i+1)**j
        sr +=(liste[i]-temp)**2
        st +=(liste[i]-y)**2
    r = ((st-sr)/st)**(1/2)
    return r



dizi=[]
for i in range(0,6):
    x=Kolerasyon(matrix[i],liste,uzunluk)
    dizi.append(x)
#print(dizi)
lastArray = sorted(dizi)

#Sonuçları yazdığım yer  . . .

with open("sonuc.txt","a",encoding='utf-8') as file:
    sayac = 1
    for j in matrix:
        x= len(j)
        file.write(str(sayac)+".Derece"+'\n')
        for y in range(x):
            file.write(str(j[y])+'\n')
        file.write("Kolerasyon:"+str(lastArray[sayac-1])+'\n')
        sayac +=1
        file.write('\n')
    file.write("Tüm veriler için en iyi kolarasyon değer:"+str(lastArray[-1])+'\n')


