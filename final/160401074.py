
#Caner Kaya-160401074


def polinom_yaklastir(derece,verilerlist):
    matris=[]
    a=0

    for i in range(derece+1):
        elemanlar=[]
        for j in range(derece+1):
            toplam=0
            for k in range(a,len(verilerlist)+1):
                toplam += k**a
            elemanlar.append(toplam)
            a += 1
        matris.append(elemanlar)
        a -=derece


    indirgenmisMatris=[]
    for i in range(derece+1):
        toplam=0
        for j in range(len(verilerlist)):
            toplam += verilerlist[j]*(j+1)**i
        indirgenmisMatris.append(toplam)
    for i in range(derece+1):
        alt=matris[i][i]
        for j in range(i+1,derece+1):
            carpan=alt/matris[j][i]
            indirgenmisMatris[j]=indirgenmisMatris[j]*carpan-indirgenmisMatris[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*carpan-matris[i][k]
    for i in range(derece,-1,-1):
        ust = matris[i][i]
        for j in range(i-1,-1,-1):
            carpan=ust/matris[j][i]
            indirgenmisMatris[j] = indirgenmisMatris[j]*carpan-indirgenmisMatris[i]
            for k in range(derece+1):
                matris[j][k]= matris[j][k]*carpan-matris[i][k]

    for i in range(derece+1):
        indirgenmisMatris[i]=indirgenmisMatris[i]/matris[i][i]
    return indirgenmisMatris

def kolerasyonHesapla(verilerlist,matris):
    y=0
    x=len(verilerlist)
    for i in range (x):
        y += verilerlist[i]
    y = y/x
    S_t=0
    S_r=0
    for i in range(x):
        x =verilerlist[i]
        S_t +=(verilerlist[i]-y)**2
        for j in range(len(matris)):
            x -= matris[j]*(i+1)**j
        x=x**2
        S_r += x
    kolerasyon=((S_t-S_r)/S_t)**(1/2)
    return kolerasyon


def bestKolerasyon(r1,r2,r3,r4,r5,r6):
    best=0
    kolerasyonlist=[r1,r2,r3,r4,r5,r6]
    for i in kolerasyonlist:
        if(i>best):
            best=i
    return best



def bestPolinom():
    polinomList=[birinciderpol,ikinciderpol,ucuncuderpol,dorduncuderpol,besinciderpol,altinciderpol]
    kolerasyonList=[birinciderkolerasyon,ikinciderkolerasyon,ucuncuderkolerasyon,dorduncuderkolerasyon,besinciderkolerasyon,altinciderkolerasyon]
    r,p=0,0
    
    for i in range(len(kolerasyonList)):
        if(kolerasyonList[i]>r):
            r=kolerasyonList[i]
            p=polinomList[i]
    return p


def toplam(best,deger):
    toplam=0
    for i in range(len(best)):
        toplam+=best[i]*(deger**i)
    return toplam



def polinomluIntegral():
    best=bestPolinom()
    altDeger=4
    ustDeger=len(verilerlist)
    x=1
    integral=0
    sinirdeger=int((ustDeger-altDeger)/x)
    for i in range(1,sinirdeger):
        integral+=toplam(best,altDeger+i*x)
    sonuc=(x/2)*(toplam(best,altDeger)+toplam(best,ustDeger)+2*integral)
    return sonuc

def polinomsuzVerilerIleIntegral(veriler):
    altDeger=4
    ustDeger=len(veriler)
    x=1
    sonuc=0
    sinirdeger=int((ustDeger-altDeger)/x)
    for i in range(1,sinirdeger):
        sonuc+= x*(veriler[altDeger]+veriler[altDeger+x])/2
        altDeger+=x
    return sonuc


veriler = open("veriler.txt","r",encoding='utf-8')
verilerlist = veriler.readlines()
for i in range(len(verilerlist)):
    verilerlist[i]=int(verilerlist[i])

birinciderpol=polinom_yaklastir(1,verilerlist)
ikinciderpol=polinom_yaklastir(2,verilerlist)
ucuncuderpol=polinom_yaklastir(3,verilerlist)
dorduncuderpol=polinom_yaklastir(4,verilerlist)
besinciderpol=polinom_yaklastir(5,verilerlist)
altinciderpol=polinom_yaklastir(6,verilerlist)
birinciderkolerasyon=kolerasyonHesapla(verilerlist,birinciderpol)
ikinciderkolerasyon=kolerasyonHesapla(verilerlist,ikinciderpol)
ucuncuderkolerasyon=kolerasyonHesapla(verilerlist,ucuncuderpol)
dorduncuderkolerasyon=kolerasyonHesapla(verilerlist,dorduncuderpol)
besinciderkolerasyon=kolerasyonHesapla(verilerlist,besinciderpol)
altinciderkolerasyon=kolerasyonHesapla(verilerlist,altinciderpol)
enuygun=bestKolerasyon(birinciderkolerasyon,ikinciderkolerasyon,ucuncuderkolerasyon,dorduncuderkolerasyon,besinciderkolerasyon,altinciderkolerasyon)
veriler.close()

polinomlu=polinomluIntegral()
verilerIle=polinomsuzVerilerIleIntegral(verilerlist)
print("Polinomlu integralin sonucu : ",polinomlu)
print("Polinomsuz integralin sonucu : ",verilerIle)

yorum=open("160401074_yorum.txt","w",encoding='utf-8')
yorum.write("Polinomlu integral ile alan hesabı yaparken gerçek polinoma yaklaştırdığımız polinomun alan hesabını yaparız.\n")
yorum.write("Polinomsuz integralde ise gerçek polinomun altında kalan alanı yamuklara bölerek yamukların alanlarını toplarız.\n")
yorum.write("Delta x değeri yamukların en değeridir.Yani delta x küçüldükçe alanı daha fazla yamuğa böleriz ve hata payımız düşer.\n")
yorum.write("Polinom her ne kadar doğrusal olmasa da çembere bile yeterince küçük ölçekte baktığımızda düz gibi olur.Polinomda ")
yorum.write("ölçeği yani delta x değerini küçülterek doğrusala daha yakınmış gibi görür ve buna göre hesap yaparız bu da hata payımızı küçültür.\n")
yorum.write("Aradaki fark da buradan gelmektedir.Polinomlu integralde gerçek polinoma yakın bir polinomun alanını bulurken ")
yorum.write("polinomsuz integralde gerçek polinomu parçalara bölerek her parçanın alanını buluruz.")
yorum.close()
