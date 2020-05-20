#Ad: GÖKÇE NUR SARICI
#Numara: 170401032


def polinomaYakinlastirma(derece,vaka):
    matris = []
    gecici = 0
    for i in range(derece+1): 
        satir = []
        for j in range(derece+1):
            toplam = 0
            for k in range(1,len(vaka)+1):
                toplam += k**gecici
            satir.append(toplam)
            gecici += 1
        matris.append(satir)
        gecici -= derece
    sonuc = []
    for i in range(derece+1):
        toplam = 0
        for j in range(len(vaka)):
            toplam += vaka[j]*(j+1)**i
        sonuc.append(toplam)
    for i in range(derece+1):
        b = matris[i][i]
        for j in range(i+1,derece+1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]  
    for i in range(derece,-1,-1):
        b = matris[i][i]
        for j in range(i-1,-1,-1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]
    for i in range(derece+1):
        sonuc[i] = sonuc[i]/matris[i][i]
    yussu=0
    for i in range (len(vaka)):
        yussu += vakalar[i]
    yussu = yussu/len(vaka)
    st=0
    sr=0
    for i in range(len(vaka)):
        x = vaka[i]
        st +=(vaka[i]-yussu)**2
        for j in range(len(sonuc)):
            x -= sonuc[j]*(i+1)**j
        x=x**2
        sr += x
    korelasyon = ((st-sr)/st)**(1/2)
    return sonuc,korelasyon

def katsayilar(p1,p2,p3,p4,p5,p6,dosya):
    file.write("Birinci Dereceden Polinom : a0 = "+str(p1[0]) + " a1 = " + str(p1[1])+"\n" )
    file.write("İkinci Dereceden Polinom : a0 = "+str(p2[0]) + " a1 = " + str(p2[1]) + " a2 =" + str(p2[2]) + "\n")
    file.write("Üçüncü Dereceden Polinom : a0 = "+str(p3[0]) + " a1 = " + str(p3[1]) + " a2 =" + str(p3[2]) + " a3 = " + str(p3[3]) + "\n")
    file.write("Dördüncü Dereceden Polinom : a0 = "+str(p4[0]) + " a1 = " + str(p4[1]) + " a2 =" + str(p4[2]) + " a3 = " + str(p4[3]) + " a4 = " + str(p4[4]) + "\n")
    file.write("Beşinci Dereceden Polinom : a0 = "+str(p5[0]) + " a1 = " + str(p5[1]) + " a2 =" + str(p5[2]) + " a3 = " + str(p5[3]) + " a4 = " + str(p5[4]) + " a5 = "+ str(p5[5])+ "\n")
    file.write("Altıncı Dereceden Polinom : a0 = "+str(p6[0]) + " a1 = " + str(p6[1]) + " a2 =" + str(p6[2]) + " a3 = " + str(p6[3]) + " a4 = " + str(p6[4]) + " a5 = "+ str(p6[5])+" a6 = "+str(p6[6])+ "\n")


def enUygun(katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6,dosya):
    file.write("katsayi1 = "+str(katsayi1)+" katsayi2 = "+str(katsayi2)+" katsayi 3 = "+str(katsayi3)+" katsayi4 = "+str(katsayi4)+" katsayi5 = "+str(katsayi5)+" katsayi6 = "+str(katsayi6)+"\n")
    degerler = [katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6]
    for i in range(len(degerler)):
        if degerler[i] == max(degerler):
             file.write("korelasyon katsayisi 1 e en yakin olan sayi "+str(degerler[i])+" dir.Polinomlar arasinda en uygun olan "+str(i+1)+". polinomdur.\n")

file = open("veriler.txt","r",encoding="UTF-8")
vaka= file.readlines()
for i in range(len(vaka)):
    vaka[i]=int(vaka[i])



p1,katsayi1=polinomaYakinlastirma(1,vakalar)
p2,katsayi2=polinomaYakinlastirma(2,vakalar)
p3,katsayi3=polinomaYakinlastirma(3,vakalar)   
p4,katsayi4=polinomaYakinlastirma(4,vakalar)
p5,katsayi5=polinomaYakinlastirma(5,vakalar)
p6,katsayi6=polinomaYakinlastirma(6,vakalar)

file.close()
file = open("sonuc.txt","w",encoding="UTF-8")
katsayilar(p1,p2,p3,p4,p5,p6,file)
enUygun(katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6,dosya)
for i in range(len(vaka)//10):
    file.write("\n"+str(i+1)+". ONLU grup : \n")
    onluGruplar=[]
    for j in range(10):
        onluGruplar.append(vaka[10*i+j])
    
    p1,katsayi1=polinomaYakinlastirma(1,onluGruplar)
    p2,katsayi2=polinomaYakinlastirma(2,onluGruplar)
    p3,katsay3=polinomaYakinlastirma(3,onluGruplar)
    p4,katsayi4=polinomaYakinlastirma(4,onluGruplar)
    p5,katsayi5=polinomaYakinlastirma(5,onluGruplar)
    p6,katsayi6=polinomaYakinlastirma(6,onluGruplar)
    katsayilar(polinom1,polinom2,polinom3,polinom4,polinom5,polinom6,dosya)
    enUygun(katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6,dosya)
file.close()
