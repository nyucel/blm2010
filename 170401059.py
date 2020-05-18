#Taha Emre UGUR 170401059
def korelasyon_katsayilari_ile_uygun_polinomu_bulma(r1,r2,r3,r4,r5,r6,dosya):
    dosya2.write("r1 = "+str(r1)+" r2 = "+str(r2)+" r3 = "+str(r3)+" r4 = "+str(r4)+" r5 = "+str(r5)+" r6 = "+str(r6)+"\n")
    if r1>r2 and r1>r3 and r1>r4 and r1>r5 and r1>r6:
        dosya2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(r1)+" ile 1.polinomdur. Polinomlar arasinda en uygun olan 1. polinomdur.\n")
    elif r2>r3 and r2>r4 and r2>r5 and r2>r6:
        dosya2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(r2)+" ile 2.polinomdur. Polinomlar arasinda en uygun olan 2. polinomdur.\n")
    elif r3>r4 and r3>r5 and r3>r6:
        dosya2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(r3)+" ile 3.polinomdur. Polinomlar arasinda en uygun olan 3. polinomdur.\n")
    elif r4>r5 and r4>r6:
        dosya2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(r4)+" ile 4.polinomdur. Polinomlar arasinda en uygun olan 4. polinomdur.\n")
    elif r5>r6:
        dosya2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(r5)+" ile 5.polinomdur. Polinomlar arasinda en uygun olan 5. polinomdur.\n")
    else:
        dosya2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(r6)+" ile 6.polinomdur. Polinomlar arasinda en uygun olan 6. polinomdur.\n")

def katsayilari_yazdirma(p1,p2,p3,p4,p5,p6,dosya):
    dosya2.write("1.dereceden polinom icin a0 = "+str(p1[0]) + " a1 = " + str(p1[1])+"\n" )
    dosya2.write("2.dereceden polinom icin a0 = "+str(p2[0]) + " a1 = " + str(p2[1]) + " a2 =" + str(p2[2]) + "\n")
    dosya2.write("3.dereceden polinom icin a0 = "+str(p3[0]) + " a1 = " + str(p3[1]) + " a2 =" + str(p3[2]) + " a3 = " + str(p3[3]) + "\n")
    dosya2.write("4.dereceden polinom icin a0 = "+str(p4[0]) + " a1 = " + str(p4[1]) + " a2 =" + str(p4[2]) + " a3 = " + str(p4[3]) + " a4 = " + str(p4[4]) + "\n")
    dosya2.write("5.dereceden polinom icin a0 = "+str(p5[0]) + " a1 = " + str(p5[1]) + " a2 =" + str(p5[2]) + " a3 = " + str(p5[3]) + " a4 = " + str(p5[4]) + " a5 = "+ str(p5[5])+ "\n")
    dosya2.write("6.dereceden polinom icin a0 = "+str(p6[0]) + " a1 = " + str(p6[1]) + " a2 =" + str(p6[2]) + " a3 = " + str(p6[3]) + " a4 = " + str(p6[4]) + " a5 = "+ str(p6[5])+" a6 = "+str(p6[6])+ "\n")

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


dosya = open("veriler.txt","r")
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
dosya2 = open("sonuc.txt","w")
katsayilari_yazdirma(p1,p2,p3,p4,p5,p6,dosya2)#ödev par1
korelasyon_katsayilari_ile_uygun_polinomu_bulma(r1,r2,r3,r4,r5,r6,dosya2)#ödev part2
for i in range(len(veriler)//10):#ödev part3 -> sadece 10 lu grupları alıyor.

    dosya2.write("\n"+str(i+1)+". 10'lu grup icin \n")
    onlu_grup=[]
    for j in range(10):
        onlu_grup.append(veriler[10*i+j])
    p1,r1=egriye_uydurma(1,onlu_grup)
    p2,r2=egriye_uydurma(2,onlu_grup)
    p3,r3=egriye_uydurma(3,onlu_grup)
    p4,r4=egriye_uydurma(4,onlu_grup)
    p5,r5=egriye_uydurma(5,onlu_grup)
    p6,r6=egriye_uydurma(6,onlu_grup)
    korelasyon_katsayilari_ile_uygun_polinomu_bulma(r1,r2,r3,r4,r5,r6,dosya2)
dosya2.close()
