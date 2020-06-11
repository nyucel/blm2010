import math
#xdegerlerinin üslü değerlerinin toplamını tutar
#xpow[x0toplam,x1toplam,x2toplam,...,xm2toplam] verilerini tutar
xpow=[]
#x**i*y degerlerini tutar
#ytoplam,xytoplam,x2ytoplam,...,xmytoplam (derece+1 değere ihtiyaç vardır)
xy=[]
#veriler.txt dosyası okunur ve degerler dictionary nesnesine atanır. 
def verioku():
        f=open("veriler.txt")
        j=0
        degerler={}
        for satır in f:
            degerler[j]=int(satır)
            j+=1
        f.close()
        return degerler
#Polinom Hesaplanır
def polinomKatsayi(derece,veri):
        degerler=veri
        xpow.clear()
        xy.clear()
        #ihtiyacımız olan en büyük x üssü 2*derece ye kadardır
        for i in range(0,(derece*2)+1):
            xpow.append(0)#diziye ilk değer ataması yapıldı
            for j in range(0,len(degerler)): #x degerleri içinde gezerek üslü değerler hesaplandı
                xpow[i]+=j**i
        for i in range (0,derece+1):
            xy.append(0)
            for j in range(0,len(degerler)):
                  xy[i]+=j**i*degerler[j]
        matris=[]
        for i in range(derece+1):
            line=[]
            for j in range(0,derece+2):
                if(j>=derece+1):
                    line.append(xy[i])
                else:
                   line.append(xpow[i+j])
            matris.append(line)
        
        for i in range(derece+2):
            if(i<derece+1):
                s=matris[i][i]
                for j in range(derece+2):
                        matris[i][j]=matris[i][j]/s    
           # for j in range(derece+1):
            if(i==derece+1):
                break
            
            for j in range(derece+1):
                if(i!=j):
                    kat=matris[j][i]
                    for k in range(derece+2):
                        matris[j][k]=matris[i][k]*kat-matris[j][k]
        return matris
#Matris ters çevrilir ve katsayı dizisi geri döndürülür
def reverse(matris):
    boyut=len(matris)
    r_matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        r_matris[i] = matris[i][boyut] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][boyut] -= matris[k][i] * r_matris[i]
    return r_matris
#Hata oranı hesaplanır
def hatahesapla(veri,matris,derece):
    y=0
    n=len(veri)
    for i in range (n):
        y += veri[i]
    y = y/n
    St=0
    Sr=0
    Sr_=0
    for i in range(n):
        Sr_=0
        St += (veri[i]-y)**2
        Sr_ += veri[i]-matris[0]
        for j in range(1,derece+1):
            Sr_ -= matris[j]*(i**j)
        Sr_ = Sr_**2
        Sr+=Sr_
    S_y_x = math.sqrt(abs(Sr/(n-(derece+1))))
    r = math.sqrt(abs((St-Sr)/St))
    return r
dosya=open("sonuc.txt","w")
veri=verioku()

#1.Soru
dosya.write("1. Soru -)\n")
hataoranlari=[]
for i in range(1,7):
    matris=polinomKatsayi(i,veri)
    reversematris=reverse(matris)
    hataoranlari.append(hatahesapla(veri,reversematris,i))

index=hataoranlari.index(max(hataoranlari))+1
hataorani=max(hataoranlari)
matris=polinomKatsayi(index,veri)
reversematris=reverse(matris)    
polinom=""

for j in range (0,len(reversematris)):
    if(j>=len(reversematris)-1):
        polinom+="%fx^%d"%(reversematris[j],j)
    elif(j==0):
        polinom+="%f + "%(reversematris[j])
    else:
        polinom+="%fx^%d +"%(reversematris[j],j)
dosya.write("En düşük hata ile uygulanan polinom %d. dereceden polinomdur. Hata oranı %f'dır."%(j,hataorani))     
dosya.write("\n") 
dosya.write("polinom = %s"%(polinom))  
dosya.write("\n\n")

                       
#SORU2
def f(x):
    fonksiyon=0
    for j in range (0,len(reversematris)):
        fonksiyon+=reversematris[j]*(x**j)
    return(fonksiyon)
a,b = 6,len(veri)
n=len(veri)-1
integral = 0
h = (b-a)/n
for i in range(n):
    integral = integral + (h/2)*(f(a) + f(a+h))
    a = a + h
dosya.write("2. Soru -) İntegral = %d"%(integral))
dosya.write("\n\n")

#SORU3
def f_(y):
    return veri[y]
a,b = 6,len(veri)
n=len(veri)-1
integral = 0
h =int(round((b-a)/n,0))
for i in range(n):
    if(a+h<=n):
        integral = integral + (h/2)*(f_(i) + f_(a+h))
        a = a + h
dosya.write("3. Soru -) İntegral = %d"%(integral))
dosya.write("\n\n")

dosya.write("Soru 4-) Polinom kullanmadan yapılan integral çözümünde değerlere erişmek için int veri tipine yuvarlama yapıldı.\n Bu durumda küsüratlı kısımlar göz ardı edildiğinden hata oranı daha yüksek olacaktır.\n"+
"Polinom belirleyerek yapılan çözümde sonuca en uygun polinom seçilmiş ve virgüllü değerlerde kullanılarak integral değeri daha doğru hesaplanmıştır.\n Polinom ile belirlenen integralin hata oranı polinom olamdan belirlenen değere göre daha düşük olacaktır.")
dosya.close()

