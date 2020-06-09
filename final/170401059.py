#Taha Emre UGUR 170401059
def yorum(dosya):
    dosya.write("Taha Emre UGUR 170401059 \n"
                "Verileri polinoma uydurarak kullandigim, delta x = 0.001 olan yamuk yontemi kullanilan sonuc ile \n"
                "direk verileri kullandigim, h=1 olan heun yontemi ile yapilan sonucun arasinda bu kadar farkin olma sebebi \n"
                "egriye uydurulan polinomun verinin gercek polinomu olmadigi icin. Cunku odev harici yaptigim denemelerde \n"
                "polinomla yaptigim integral de ara degerleri almadan yani delta x = 1 yaparak yaptigim sonuc ayni direk verilerden\n"
                "aldigim integral gibi sonuc cikarmasi gerekirken yine cok farkli bir sonuc cikiyor. Bundan dolayi bu \n"
                "aralarindaki farkin sebebi polinomdan cikan veriler ile gercek verilerin farkli olmasindan kaynaklidir.\n"
                "verinin gercek polinomu olsaydi (korelasyon katsayisi = 1) boyle fark olmayacakti.")
def veriler_ile(veriler,a,b):
    h=1
    y0=veriler[a-1]
    while(a<b):
        y0 = y0 + (veriler[a-1]+veriler[a+h-1])*h/2
        a += h
    print("veriler ile yapilan integralin sonucu : " ,y0)


def f(p,x):
    toplam=0
    for i in range(len(p)):
        toplam += p[i]*(x**i)
    return toplam

def yamuk_yontemi(p,a,b):
    delta_x= 0.0001
    n= int((b-a)/delta_x)
    toplam=0
    for i in range(1,n):
        toplam += f(p,a+i*delta_x)
    I=(delta_x/2)*(f(p,a)+f(p,b)+2*toplam)
    print("polinom ile yapilan integralin sonucu : ", I)


def en_iyi_polinımu_bulma(p,r):
    best_r=0
    best_p=0
    for i in range(len(r)):
        if (r[i]>best_r):
            best_r=r[i]
            best_p=p[i]
    return best_p

def egriye_uydurma(derece,veriler):
    matris=[]
    l=0

    for i in range(derece+1):#satırlar olustrulup matris dizisine atılıyor
        satir=[]
        for j in range(derece+1):
            toplam=0
            for k in range(1,len(veriler)+1):
                toplam += k**l
            satir.append(toplam)
            l += 1
        matris.append(satir)
        l -=derece


    cevap=[]
    for i in range(derece+1):#cevaplar farklı diziye atılıyor
        toplam=0
        for j in range(len(veriler)):
            toplam += veriler[j]*(j+1)**i
        cevap.append(toplam)

    #gaus yöntemi alt üçgen
    for i in range(derece+1):
        benzetme=matris[i][i]
        for j in range(i+1,derece+1):
            oran=benzetme/matris[j][i]
            cevap[j]=cevap[j]*oran-cevap[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*oran-matris[i][k]
    #gaus üst üçgen
    for i in range(derece,-1,-1):
        benzetme = matris[i][i]
        for j in range(i-1,-1,-1):
            oran=benzetme/matris[j][i]
            cevap[j] = cevap[j]*oran-cevap[i]
            for k in range(derece+1):
                matris[j][k]= matris[j][k]*oran-matris[i][k]

    for i in range(derece+1):#alt ve üst üçgen 0 olduğuna göre katsayıların cevaplarını buluyoruz
        cevap[i]=cevap[i]/matris[i][i]
    y_ort=0
    for i in range (len(veriler)):
        y_ort += veriler[i]
    y_ort = y_ort/len(veriler)
    S_t=0
    S_r=0
    for i in range(len(veriler)):
        x =veriler[i]
        S_t +=(veriler[i]-y_ort)**2
        for j in range(len(cevap)):
            x -= cevap[j]*(i+1)**j
        x=x**2
        S_r += x
    r=((S_t-S_r)/S_t)**(1/2)#korelasyon katsayısı
    return cevap,r

dosya = open("../../Documents/GitHub/blm2010/final/veriler.txt", "r")
veriler = dosya.readlines()
for i in range(len(veriler)):
    veriler[i]=int(veriler[i])
#fonksiyonlar x=1 ile başlıyordur..

p1,r1=egriye_uydurma(1,veriler)
p2,r2=egriye_uydurma(2,veriler)
p3,r3=egriye_uydurma(3,veriler)
p4,r4=egriye_uydurma(4,veriler)
p5,r5=egriye_uydurma(5,veriler)
p6,r6=egriye_uydurma(6,veriler)

dosya.close()
r=[r1,r2,r3,r4,r5,r6]
p=[p1,p2,p3,p4,p5,p6]



best_p=en_iyi_polinımu_bulma(p,r)
a=9
b=len(veriler)
yamuk_yontemi(best_p,a,b)#polinomla
veriler_ile(veriler,a,b)#polinomsuz

dosya2 = open("170401059_yorum.txt","w")
yorum(dosya2)
dosya2.close()
