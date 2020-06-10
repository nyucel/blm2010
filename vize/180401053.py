#180401053 Halil Hilmi Namlı
#Korelasyon Katsayisi kullandiğimiz için 1'e ne kadar yakin olursa o kadar uygun bir polinomdur. 
#h'ler ile Korelasyon Katsayisi ,  pol'ler ile polinomlar , k'ler ile Polinom katsayilari temsil ediliyor.
def en_uygun_polinom(h1,h2,h3,h4,h5,h6,dosya):
    dosya.write(" h1 = "+str(h1)+"\n h2 = "+str(h2)+"\n h3 = "+str(h3)+"\n h4 = "+str(h4)+"\n h5 = "+str(h5)+"\n h6 = "+str(h6)+"\n")
    if h1>h2 and h1>h3 and h1>h4 and h1>h5 and h1>h6:
        dosya.write("Korelasyon kullandigimiz icin 1'e yakin olan alindigindan "+str(h1)+" Sayisiyla 1.polinomdur.\n  En uygun olan 1. polinomdur.\n")
    elif h2>h3 and h2>h4 and h2>h5 and h2>h6:
        dosya.write("Korelasyon kullandigimiz icin 1'e yakin olan alindigindan "+str(h2)+" Sayisiyla 2.polinomdur. \n En uygun olan 2. polinomdur.\n")
    elif h3>h4 and h3>h5 and h3>h6:
        dosya.write("Korelasyon kullandigimiz icin 1'e yakin olan alindigindan "+str(h3)+" Sayisiyla 3.polinomdur. \n En uygun olan 3. polinomdur.\n")
    elif h4>h5 and h4>h6:
        dosya.write("Korelasyon kullandigimiz icin 1'e yakin olan alindigindan "+str(h4)+" Sayisiyla 4.polinomdur. \n En uygun olan 4. polinomdur.\n")
    elif h5>h6:
        dosya.write("Korelasyon kullandigimiz icin 1'e yakin olan alindigindan "+str(h5)+" Sayisiyla 5.polinomdur. \n En uygun olan 5. polinomdur.\n")
    else:
        dosya.write("Korelasyon kullandigimiz icin 1'e yakin olan alindigindan "+str(h6)+" Sayisiyla 6.polinomdur. \n En uygun olan 6. polinomdur.\n")

#Katsayi yazdiran fonksiyon
def katsayilari_yazdirma(pol1,pol2,pol3,pol4,pol5,pol6,dosya):
    dosya.write("---1.Dereceden polinomun katsayilari bunlardir --- \nk0 = "+str(pol1[0]) + " k1 = " + str(pol1[1])+"\n" )
    dosya.write("---2.Dereceden polinomun katsayilari bunlardir ---\nk0 = "+str(pol2[0]) + " k1 = " + str(pol2[1]) + " k2 =" + str(pol2[2]) + "\n")
    dosya.write("---3.Dereceden polinomun katsayilari bunlardir --- \nk0 = "+str(pol3[0]) + " k1 = " + str(pol3[1]) + " k2 =" + str(pol3[2]) + " k3 = " + str(pol3[3]) + "\n")
    dosya.write("---4.Dereceden polinomun katsayilari bunlardir --- \nk0 = "+str(pol4[0]) + " k1 = " + str(pol4[1]) + " k2 =" + str(pol4[2]) + " k3 = " + str(pol4[3]) + " k4 = " + str(pol4[4]) + "\n")
    dosya.write("---5.Dereceden polinomun katsayilari bunlardir --- \nk0 = "+str(pol5[0]) + " k1 = " + str(pol5[1]) + " k2 =" + str(pol5[2]) + " k3 = " + str(pol5[3]) + " k4 = " + str(pol5[4]) + " k5 = "+ str(pol5[5])+ "\n")
    dosya.write("---6.Dereceden polinomun katsayilari bunlardir --- \nk0 = "+str(pol6[0]) + " k1 = " + str(pol6[1]) + " k2 =" + str(pol6[2]) + " k3 = " + str(pol6[3]) + " k4 = " + str(pol6[4]) + " k5 = "+ str(pol6[5])+" k6 = "+str(pol6[6])+ "\n")

def interpolasyon(Derece,veriler):
    matris=[]
    l=0

    for i in range(Derece+1):
        satir=[]
        for j in range(Derece+1):
            toplam=0
            for k in range(1,len(veriler)+1):
                toplam += k**l
            satir.append(toplam)
            l += 1
        matris.append(satir)
        l -=Derece


    Listecozum=[]
    for i in range(Derece+1):
        toplam=0
        for j in range(len(veriler)):
            toplam += veriler[j]*(j+1)**i
        Listecozum.append(toplam)

    #ALT ucgen sifirlamak icin 
    for i in range(Derece+1):
        yaklasma=matris[i][i]
        for j in range(i+1,Derece+1):
            oran=yaklasma/matris[j][i]
            Listecozum[j]=Listecozum[j]*oran-Listecozum[i]
            for k in range(Derece+1):
                matris[j][k] = matris[j][k]*oran-matris[i][k]
    #UST ucgen sifirlamak icin 
    for i in range(Derece,-1,-1):
        yaklasma = matris[i][i]
        for j in range(i-1,-1,-1):
            oran=yaklasma/matris[j][i]
            Listecozum[j] = Listecozum[j]*oran-Listecozum[i]
            for k in range(Derece+1):
                matris[j][k]= matris[j][k]*oran-matris[i][k]

    
    for i in range(Derece+1):
        Listecozum[i]=Listecozum[i]/matris[i][i]
    y_top=0
    for i in range (len(veriler)):
        y_top += veriler[i]
    y_ort = y_top/len(veriler)
    S_t,S_r=0,0
    for i in range(len(veriler)):
        x =veriler[i]
        S_t +=(veriler[i]-y_ort)**2
        for j in range(len(Listecozum)):
            x -= Listecozum[j]*(i+1)**j
        x=x**2
        S_r += x
    r=((S_t-S_r)/S_t)**(1/2)
    return Listecozum,r


Verilerdosya = open("veriler.txt","r")
veriler = Verilerdosya.readlines()
for i in range(len(veriler)):
    veriler[i]=int(veriler[i])


pol1,h1=interpolasyon(1,veriler)

pol2,h2=interpolasyon(2,veriler)

pol3,h3=interpolasyon(3,veriler)

pol4,h4=interpolasyon(4,veriler)

pol5,h5=interpolasyon(5,veriler)

pol6,h6=interpolasyon(6,veriler)

Verilerdosya.close()
sonuclardosya = open("sonuc.txt","w")
katsayilari_yazdirma(pol1,pol2,pol3,pol4,pol5,pol6,sonuclardosya)
en_uygun_polinom(h1,h2,h3,h4,h5,h6,sonuclardosya)
for i in range(len(veriler)//10):

    sonuclardosya.write("\n"+str(i+1)+". 10'lu gruptaki polinomlar icin \n")
    sirali_onlu=[]
    for j in range(10):
        sirali_onlu.append(veriler[10*i+j])
    pol1,h1=interpolasyon(1,sirali_onlu)
    pol2,h2=interpolasyon(2,sirali_onlu)
    pol3,h3=interpolasyon(3,sirali_onlu)
    pol4,h4=interpolasyon(4,sirali_onlu)
    pol5,h5=interpolasyon(5,sirali_onlu)
    pol6,h6=interpolasyon(6,sirali_onlu)
    katsayilari_yazdirma(pol1,pol2,pol3,pol4,pol5,pol6,sonuclardosya)
    en_uygun_polinom(h1,h2,h3,h4,h5,h6,sonuclardosya)
sonuclardosya.close()