# Ad Soyad: Batuhan Okur    Numara: 180401011

def polinomaUydurma(pDerece,vakalar): # Polinomun derecesini ve verileri alarak polinoma uydurma işlemini yapar ve korelasyon katsayısını bularak en uygun polinomu seçer.
    matris = []
    temp = 0
    for i in range(pDerece+1): 
        satir = []
        for j in range(pDerece+1):
            toplam = 0
            for k in range(1,len(vakalar)+1):
                toplam += k**temp
            satir.append(toplam)
            temp += 1
        matris.append(satir)
        temp -= pDerece
    sonuc = []
    for i in range(pDerece+1):
        toplam = 0
        for j in range(len(vakalar)):
            toplam += vakalar[j]*(j+1)**i
        sonuc.append(toplam)
    for i in range(pDerece+1):
        b = matris[i][i]
        for j in range(i+1,pDerece+1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(pDerece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]  
    for i in range(pDerece,-1,-1):
        b = matris[i][i]
        for j in range(i-1,-1,-1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(pDerece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]
    for i in range(pDerece+1):
        sonuc[i] = sonuc[i]/matris[i][i]
    yOrt=0
    for i in range (len(vakalar)):
        yOrt += vakalar[i]
    yOrt = yOrt/len(vakalar)
    St=0
    Sr=0
    for i in range(len(vakalar)):
        x = vakalar[i]
        St +=(vakalar[i]-yOrt)**2
        for j in range(len(sonuc)):
            x -= sonuc[j]*(i+1)**j
        x=x**2
        Sr += x
    korelasyon = ((St-Sr)/St)**(1/2)
    return sonuc,korelasyon

def katsayilari_yazdirma(polinom1,polinom2,polinom3,polinom4,polinom5,polinom6,dosya):
    dosya2.write("1.dereceden polinom : a0 = "+str(polinom1[0]) + " a1 = " + str(polinom1[1])+"\n" )
    dosya2.write("2.dereceden polinom : a0 = "+str(polinom2[0]) + " a1 = " + str(polinom2[1]) + " a2 =" + str(polinom2[2]) + "\n")
    dosya2.write("3.dereceden polinom : a0 = "+str(polinom3[0]) + " a1 = " + str(polinom3[1]) + " a2 =" + str(polinom3[2]) + " a3 = " + str(polinom3[3]) + "\n")
    dosya2.write("4.dereceden polinom : a0 = "+str(polinom4[0]) + " a1 = " + str(polinom4[1]) + " a2 =" + str(polinom4[2]) + " a3 = " + str(polinom4[3]) + " a4 = " + str(polinom4[4]) + "\n")
    dosya2.write("5.dereceden polinom : a0 = "+str(polinom5[0]) + " a1 = " + str(polinom5[1]) + " a2 =" + str(polinom5[2]) + " a3 = " + str(polinom5[3]) + " a4 = " + str(polinom5[4]) + " a5 = "+ str(polinom5[5])+ "\n")
    dosya2.write("6.dereceden polinom : a0 = "+str(polinom6[0]) + " a1 = " + str(polinom6[1]) + " a2 =" + str(polinom6[2]) + " a3 = " + str(polinom6[3]) + " a4 = " + str(polinom6[4]) + " a5 = "+ str(polinom6[5])+" a6 = "+str(polinom6[6])+ "\n")


def uygunPolinomSec(katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6,dosya):
    dosya2.write("katsayi1 = "+str(katsayi1)+" katsayi2 = "+str(katsayi2)+" katsayi 3 = "+str(katsayi3)+" katsayi4 = "+str(katsayi4)+" katsayi5 = "+str(katsayi5)+" katsayi6 = "+str(katsayi6)+"\n")
    degerler = [katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6]
    for i in range(len(degerler)):
        if degerler[i] == max(degerler):
             dosya2.write("korelasyon katsayisi 1 e en yakin olan sayi "+str(degerler[i])+" dir.Polinomlar arasinda en uygun olan "+str(i+1)+". polinomdur.\n")


#main(işlemlerin yapıldığı) kısım
dosya = open("veriler.txt","r")
vakalar = dosya.readlines()
for i in range(len(vakalar)):
    vakalar[i]=int(vakalar[i])



polinom1,katsayi1=polinomaUydurma(1,vakalar)
polinom2,katsayi2=polinomaUydurma(2,vakalar)
polinom3,katsayi3=polinomaUydurma(3,vakalar)   #Polinomların katsayılarını hesaplama işlemini yapıyorum. (79-84. satılar)
polinom4,katsayi4=polinomaUydurma(4,vakalar)
polinom5,katsayi5=polinomaUydurma(5,vakalar)
polinom6,katsayi6=polinomaUydurma(6,vakalar)

dosya.close()
dosya2 = open("sonuc.txt","w")
katsayilari_yazdirma(polinom1,polinom2,polinom3,polinom4,polinom5,polinom6,dosya2)#katsayıları yazdırıyorum.
uygunPolinomSec(katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6,dosya2)#en uygun olan polinomu seçiyorum.
for i in range(len(vakalar)//10):#10 lu gruplar şeklinde kontrol yapıyorum.
    dosya2.write("\n"+str(i+1)+". 10'lu grup : \n")
    onluGruplar=[]
    for j in range(10):
        onluGruplar.append(vakalar[10*i+j])
    
    polinom1,katsayi1=polinomaUydurma(1,onluGruplar)
    polinom2,katsayi2=polinomaUydurma(2,onluGruplar)
    polinom3,katsay3=polinomaUydurma(3,onluGruplar)
    polinom4,katsayi4=polinomaUydurma(4,onluGruplar)
    polinom5,katsayi5=polinomaUydurma(5,onluGruplar)
    polinom6,katsayi6=polinomaUydurma(6,onluGruplar)
    katsayilari_yazdirma(polinom1,polinom2,polinom3,polinom4,polinom5,polinom6,dosya2)
    uygunPolinomSec(katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6,dosya2)
dosya2.close()
