#Mehmet Salih ÇELİK - 170401073

dosya=open("veriler.txt","r")
liste = dosya.read().split()
for i in range(len(liste)):
    liste[i]=int(liste[i])
dosya.close()

#İlk kısımlar için vize kodlarımdan alıntı yaptım.
#Polinoma yaklastirma metodundaki formullere gore xi ve xiyi degerlerini hesapliyoruz.
def gunleritopla(n):
    gunler=[]
    liste2=[]
    for i in range(13):
        gunler.append(0)
    for i in range(1,len(n)+1):
        liste2.append(i)
    for i in range(13):
        for j in range(len(n)):
            gunler[i]+=liste2[j]**i
    return gunler

a=gunleritopla(liste)

def xiyi(n):
    liste2=[]
    for i in range(len(n)):
        x=0
        for j in range(1,len(n)+1):
            x+=(j**i)*(n[j-1])
        liste2.append(x)
    return liste2

b=xiyi(liste)

#gun toplamlari ve xiyi degerlerini bulduktan sonra 6. slayttaki formulu kod haline getirip bir matris olusturduk
def matris_olustur(aa,bb):
    dereceler = []
    birinci=[]
    for i in range(-1,1):
        birinci.append([aa[i+1],aa[i+2],bb[i+1]])
    dereceler.append([birinci[0],birinci[1]])
    ikinci=[]
    for i in range(-1,2):
        ikinci.append([aa[i+1],aa[i+2],aa[i+3],bb[i+1]])
    dereceler.append([ikinci[0],ikinci[1],ikinci[2]])
    ucuncu=[]
    for i in range(-1,3):
        ucuncu.append([aa[i+1],aa[i+2],aa[i+3],aa[i+4],bb[i+1]])
    dereceler.append([ucuncu[0],ucuncu[1],ucuncu[2],ucuncu[3]])
    dorduncu=[]
    for i in range(-1,4):
        dorduncu.append([aa[i+1],aa[i+2],aa[i+3],aa[i+4],aa[i+5],bb[i+1]])
    dereceler.append([dorduncu[0], dorduncu[1], dorduncu[2], dorduncu[3],dorduncu[4]])
    besinci=[]
    for i in range(-1,5):
        besinci.append([aa[i+1],aa[i+2],aa[i+3],aa[i+4],aa[i+5],aa[i+6],bb[i+1]])
    dereceler.append([besinci[0], besinci[1], besinci[2], besinci[3],besinci[4],besinci[5]])
    altinci=[]
    for i in range(-1,6):
        altinci.append([aa[i+1],aa[i+2],aa[i+3],aa[i+4],aa[i+5],aa[i+6],a[i+7],bb[i+1]])
    dereceler.append([altinci[0], altinci[1], altinci[2], altinci[3], altinci[4], altinci[5],altinci[6]])
    return dereceler

dereceler=matris_olustur(a,b)


def gauss(matris):
    n = len(matris)
    for i in range(0, n):
        max = abs(matris[i][i])
        maxrow = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) > max:
                max = abs(matris[k][i])
                maxrow = k
        for k in range(i, n + 1):
            tmp = matris[maxrow][k]
            matris[maxrow][k] = matris[i][k]
            matris[i][k] = tmp
        for k in range(i + 1, n):
            c = -matris[k][i] / matris[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matris[k][j] = 0
                else:
                    matris[k][j] += c * matris[i][j]
    result = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        result[i] = matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * result[i]
    return result

katsayilar=[gauss(dereceler[0]),gauss(dereceler[1]),gauss(dereceler[2]),gauss(dereceler[3]),gauss(dereceler[4]),gauss(dereceler[5])]


def yustu(n):
    x=0
    for i in range(len(n)):
        x+=(n[i])
    x=x/len(n)
    return x

y_ustu=yustu(liste)

def st(y,n):
    x=0
    for i in range(len(n)):
        x+=((n[i]-y)**2)
    return x

s_t=st(y_ustu,liste)

def kolerasyon(matris,n):
    sr=0
    for i in range(len(n)):
        tmp=0
        for j in range(len(matris)):
            if(j==0):
                tmp+=matris[j]
            else:
                tmp+=matris[j]*(i+1)**j
        sr +=(n[i]-tmp)**2
    r=abs((s_t-sr)/s_t)**(1/2)
    return r

sr=[]
for i in range(len(katsayilar)):
    sr.append(kolerasyon(katsayilar[i],liste))

sr_sirali=sorted(sr,reverse=True)

#Final 1. soru Uygun degerler
en_uygun_hata_degeri=sr_sirali[0]
uygun_polinom_indexi=sr.index(sr_sirali[0])
uygun_polinom_derecesi=sr.index(sr_sirali[0])+1


def f(x,polinom=katsayilar[uygun_polinom_indexi]):
    p = 0
    for i in range(len(polinom)):
        p += polinom[i] * (x ** i)
    return p

def integralhes(n):
    #170401073
    a=3
    b=n
    deltax=0.001
    integral=0
    size=int((b-a)/deltax)
    for i in range(size):
        integral+=deltax*(f(a)+f(a+deltax))/2
        a+=deltax
    print("polinomlu integralin sonucu :",integral)

def integralhes2(veri):
    # 170401073
    a = 3
    b = len(veri)
    integral = 0
    for i in range(a - 1, b - 1):
        integral += (veri[i] + veri[i + 1]) / 2
    print("polinomsuz integralin sonucu :",integral)

integralhes(len(liste))
integralhes2(liste)


dosya=open("170401073_yorum.txt","w")
dosya.write("İntegral hesaplaması yapılırken polinom dikdörtgenlere bölünür ve bunların alanları toplanarak sonuç elde edilir.");
dosya.write("Bu sonuca ulaşırken dikdörtgenlerin enini ne kadar küçük seçersek polinomu daha çok dikdörtgene böleriz ve gerçek integral değerine o kadar yaklaşırız.")
dosya.write("Yani hesaplamalardaki deltax değerini küçük seçmemiz polinomu daha çok böleceğimiz ve gerçeğe daha yakın değer elde edeceğimiz anlamına gelir.")
dosya.write("Polinom kullanmadan hesapladığımız integralde deltax'i ayarlayamadığımız için düşük deltax değerleri kullanarak hesaplanan integral kadar hassas sonuçlar elde edemeyiz.")
dosya.close()



