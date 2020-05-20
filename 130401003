#Mahmud Gülercan 130401003




def katsayilari_yazdirma(p1,p2,p3,p4,p5,p6,file):
    file2.write("1.dereceden polinom icin a0 = "+str(p1[0]) + " a1 = " + str(p1[1])+"\n" )
    file2.write("2.dereceden polinom icin a0 = "+str(p2[0]) + " a1 = " + str(p2[1]) + " a2 =" + str(p2[2]) + "\n")
    file2.write("3.dereceden polinom icin a0 = "+str(p3[0]) + " a1 = " + str(p3[1]) + " a2 =" + str(p3[2]) + " a3 = " + str(p3[3]) + "\n")
    file2.write("4.dereceden polinom icin a0 = "+str(p4[0]) + " a1 = " + str(p4[1]) + " a2 =" + str(p4[2]) + " a3 = " + str(p4[3]) + " a4 = " + str(p4[4]) + "\n")
    file2.write("5.dereceden polinom icin a0 = "+str(p5[0]) + " a1 = " + str(p5[1]) + " a2 =" + str(p5[2]) + " a3 = " + str(p5[3]) + " a4 = " + str(p5[4]) + " a5 = "+ str(p5[5])+ "\n")
    file2.write("6.dereceden polinom icin a0 = "+str(p6[0]) + " a1 = " + str(p6[1]) + " a2 =" + str(p6[2]) + " a3 = " + str(p6[3]) + " a4 = " + str(p6[4]) + " a5 = "+ str(p6[5])+" a6 = "+str(p6[6])+ "\n")




def katsayi_ile_polinom_bulma(m1,m2,m3,m4,m5,m6,file):
    file2.write("m1 = "+str(m1)+" m2 = "+str(m2)+" m3 = "+str(m3)+" m4 = "+str(m4)+" m5 = "+str(m5)+" m6 = "+str(m6)+"\n")
    if m1>m2 and m1>m3 and m1>m4 and m1>m5 and m1>m6:
        file2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(m1)+" ile 1.polinomdur.\n")
    elif m2>m3 and m2>m4 and m2>m5 and m2>m6:
        file.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(m2)+" ile 2.polinomdur. \n")
    elif m3>m4 and m3>m5 and m3>m6:
       file2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(m3)+" ile 3.polinomdur. \n")
    elif m4>m5 and m4>m6:
        file2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(m4)+" ile 4.polinomdur. \n")
    elif m5>m6:
        file2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(m5)+" ile 5.polinomdur. \n")
    else:
        file2.write("korelasyon iliskisi 1 e en yakin olan sayi "+str(m6)+" ile 6.polinomdur. \n")


def egri_uydurma(der,veri):
    matris=[]
    l=0

    for i in range(der+1):
        satir=[]
        for j in range(der+1):
            toplam=0
            for k in range(1,len(veri)+1):
                toplam += k**l
            satir.append(toplam)
            l += 1
        matris.append(satir)
        l -=der


    cevap=[]
    for i in range(der+1):
        toplam=0
        for j in range(len(veri)):
            toplam += veri[j]*(j+1)**i
        cevap.append(toplam)

   
    for i in range(der+1):
        benzer=matris[i][i]
        for j in range(i+1,der+1):
            oran=benzer/matris[j][i]
            cevap[j]=cevap[j]*oran-cevap[i]
            for k in range(der+1):
                matris[j][k] = matris[j][k]*oran-matris[i][k]
   
    for i in range(der,-1,-1):
        benzer = matris[i][i]
        for j in range(i-1,-1,-1):
            oran=benzer/matris[j][i]
            cevap[j] = cevap[j]*oran-cevap[i]
            for k in range(der+1):
                matris[j][k]= matris[j][k]*oran-matris[i][k]

    for i in range(der+1):
        cevap[i]=cevap[i]/matris[i][i]
    ortalamay=0
    for i in range (len(veri)):
        ortalamay+= veri[i]
    ortalamay = ortalamay/len(veri)
    S_t=0
    S_r=0
    for i in range(len(veri)):
        x =veri[i]
        S_t +=(veri[i]-ortalamay)**2
        for j in range(len(cevap)):
            x -= cevap[j]*(i+1)**j
        x=x**2
        S_r += x
    r=((S_t-S_r)/S_t)**(1/2)
    return cevap,r


dosya = open("veri.txt","r")
veri = dosya.readlines()
for i in range(len(veri)):
    veri[i]=int(veri[i])



p1,m1=egriye_uydurma(1,veri)
p2,m2=egriye_uydurma(2,veri)
p3,m3=egriye_uydurma(3,veri)
p4,m4=egriye_uydurma(4,veri)
p5,m5=egriye_uydurma(5,veri)
p6,m6=egriye_uydurma(6,veri)

file.close()
file2 = open("sonuc.txt","w")
katsayilari_yazdirma(p1,p2,p3,p4,p5,p6,file2)
katsayi_ile_polinom_bulma(m1,m2,m3,m4,m5,m6,file2)
for i in range(len(veri)//10):

    file2.write("\n"+str(i+1)+" \n")
    onar_grup=[]
    for j in range(10):
        onar_grup.append(veri[10*i+j])
    p1,m1=egriye_uydurma(1,onar_grup)
    p2,m2=egriye_uydurma(2,onar_grup)
    p3,m3=egriye_uydurma(3,onar_grup)
    p4,m4=egriye_uydurma(4,onar_grup)
    p5,m5=egriye_uydurma(5,onar_grup)
    p6,m6=egriye_uydurma(6,onar_grup)
    katsayilari_yazdirma(p1,p2,p3,p4,p5,p6,file2)
    katsayi_ile_polinom_bulma(m1,m2,m3,m4,m5,m6,file2)
file2.close()
