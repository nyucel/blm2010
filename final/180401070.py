#Berkay Yanık 180401070

with open("veriler.txt", "r", encoding='utf-8') as file:
    liste = []
    for i in file.read().split():
        liste.append(int(i))
b = len(liste)
listetoplam =sum(liste)



def xitoplam(b):
    xKareToplam=[]
    xKareToplam.append(b)
    for j in range(1,13):
        deger=0
        for i in range(b):
            deger += (i + 1) ** j
        xKareToplam.append(deger)
    return xKareToplam



def xiyiToplam(b,liste):
    xi_yi_toplam = []
    xi_yi_toplam.append(sum(liste))
    for i in range(1, 7, 1):
        deger=0
        for j in range(b):
            deger += (j + 1) ** i * liste[j]
        xi_yi_toplam.append(deger)
    return xi_yi_toplam




def matrishesaplama(matris):
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





def matris(b,liste,m):
    x,y=xitoplam(b),xiyiToplam(b,liste)
    matris,satir=[],0
    for i in range(0,m):
        ekleneceksatir=[]
        for i in range(satir,m+satir):
            ekleneceksatir.append(x[i])
        ekleneceksatir.append(y[satir])
        satir+=1
        matris.append(ekleneceksatir)
    return matris




def matriscagir(liste):
    x = []
    for i in range(2,8):

        x.append(matrishesaplama(matris(len(liste),liste,i)))
    return x
matris1 = matriscagir(liste)




def Kolerasyon(x,liste,n):
    sr = 0
    st = 0
    y = sum(liste)/n
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
    x=Kolerasyon(matris1[i],liste,b)
    dizi.append(x)




def bestKolerasyon(colerasyon):
    enBuyuk=max(colerasyon)
    sayac=1
    while(enBuyuk!=colerasyon[sayac-1]):
        sayac+=1
    return sayac

polinom=matris1[bestKolerasyon(dizi)-1]
def f(x,pol=polinom):
    return(pol[0] + pol[1]*x + pol[2]*x**2 + pol[3]*x**3 + pol[4]*x**4 + pol[5]*x**5 + pol[6]*x**6)



def polinomluIntegral(liste):

    a=10
    b=len(liste)
    deltax = 0.1
    integral = 0
    n = int((b - a)/deltax)
    for i in range(n):
        integral = deltax * (f(a) + f(a+ deltax)) / 2+integral
        a = deltax+a
    return integral



def polinomsuzIntegral(liste):
    a=10
    b=len(liste)
    deltax=1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n-1):
        integral += deltax * (liste[a] + liste[a + deltax]) / 2
        a += deltax
    return integral
print("Polinomlu integral : ",polinomluIntegral(liste))
print("Polinomsuz integral : ",polinomsuzIntegral(liste))



with open("180401070_yorum.txt","w",encoding='utf-8') as file:
    file.write("Berkay Yanik  180401070 \n")
    file.write("Polinomlu ve polinomsuz integralin değerlerinin farkli çıkmasinin sebebi delta_x'e verilen değerdir.\n" )
    file.write("delta_x küçüldükçe hesaplanan alan artar ve hesaplanan değer gerçeğe daha yakın olur.\n")
    file.write("Polinomsuz integralde delta_x 1 polinomlu integralde delta_x daha küçüktür  \n")
    file.write("Bu yüzden polinomlu integral polinomsuza göre istediğimiz sonuca daha yakın bir sonuç verir. \n")
    file.write("Polinomsuz hesaplamada istediğimiz kadar parçaya bölemediğimiz için  hata oranı daha fazladır ve taşmalar olur bu yüzden aralarında fark vardır.\n")






