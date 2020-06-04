
#Caner Kaya - 160401074


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
sonuclar=open("sonuc.txt","w",encoding='utf-8')
sonuclar.write("1.dereceden polinoma yaklaştırma : " +str(birinciderpol[1])+"x + "+str(birinciderpol[0])+"  Kolerasyon = "+ str(birinciderkolerasyon) + "\n")
sonuclar.write("2.dereceden polinoma yaklaştırma : " +str(ikinciderpol[2])+"x^2 + "+str(ikinciderpol[1])+"x + "+str(ikinciderpol[0])+"  Kolerasyon = " + str(ikinciderkolerasyon)+"\n")
sonuclar.write("3.dereceden polinoma yaklaştırma : " +str(ucuncuderpol[3])+"x^3 + "+str(ucuncuderpol[2])+"x^2 + "+str(ucuncuderpol[1])+"x + "+str(ucuncuderpol[0])+"  Kolerasyon = " + str(ucuncuderkolerasyon)+"\n")
sonuclar.write("4.dereceden polinoma yaklaştırma : " +str(dorduncuderpol[4])+"x^4 + " +str(dorduncuderpol[3])+"x^3 + "+str(dorduncuderpol[2])+"x^2 + " +str(dorduncuderpol[1])+"x + " +str(dorduncuderpol[0])+"  Kolerasyon = " + str(dorduncuderkolerasyon)+"\n")
sonuclar.write("5.dereceden polinoma yaklaştırma : " +str(besinciderpol[5])+"x^5 + "+str(besinciderpol[4])+"x^4 + " +str(besinciderpol[3])+"x^3 + " +str(besinciderpol[2])+"x^2 + " +str(besinciderpol[1])+"x + " +str(besinciderpol[0])+"  Kolerasyon = " + str(besinciderkolerasyon)+"\n")
sonuclar.write("6.dereceden polinoma yaklaştırma : " +str(altinciderpol[6])+"x^6 + "+str(altinciderpol[5])+"x^5 + "+str(altinciderpol[4])+"x^4 + " +str(altinciderpol[3])+"x^3 + " +str(altinciderpol[2])+"x^2 + " +str(altinciderpol[1])+"x + " +str(altinciderpol[0])+"  Kolerasyon = " + str(altinciderkolerasyon)+"\n")
sonuclar.write("En uygun polinom kolerasyonu 1'e en yakın olan 6.kolerasyon.Kolerasyon değeri = "+ str(enuygun))
sonuclar.close()
