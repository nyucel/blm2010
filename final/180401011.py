# Ad Soyad: Batuhan Okur    Numara: 180401011

from sympy import Symbol,pprint
x = Symbol('x')

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
        c = vakalar[i]
        St +=(vakalar[i]-yOrt)**2
        for j in range(len(sonuc)):
            c -= sonuc[j]*(i+1)**j
        c=c**2
        Sr += c
    korelasyon = ((St-Sr)/St)**(1/2)
    return sonuc,korelasyon

def katsayilari_yazdirma(polinom1,polinom2,polinom3,polinom4,polinom5,polinom6,dosya):
    dosya.write("1.dereceden polinom : a0 = "+str(polinom1[0]) + " a1 = " + str(polinom1[1])+"\n" )
    dosya.write("2.dereceden polinom : a0 = "+str(polinom2[0]) + " a1 = " + str(polinom2[1]) + " a2 =" + str(polinom2[2]) + "\n")
    dosya.write("3.dereceden polinom : a0 = "+str(polinom3[0]) + " a1 = " + str(polinom3[1]) + " a2 =" + str(polinom3[2]) + " a3 = " + str(polinom3[3]) + "\n")
    dosya.write("4.dereceden polinom : a0 = "+str(polinom4[0]) + " a1 = " + str(polinom4[1]) + " a2 =" + str(polinom4[2]) + " a3 = " + str(polinom4[3]) + " a4 = " + str(polinom4[4]) + "\n")
    dosya.write("5.dereceden polinom : a0 = "+str(polinom5[0]) + " a1 = " + str(polinom5[1]) + " a2 =" + str(polinom5[2]) + " a3 = " + str(polinom5[3]) + " a4 = " + str(polinom5[4]) + " a5 = "+ str(polinom5[5])+ "\n")
    dosya.write("6.dereceden polinom : a0 = "+str(polinom6[0]) + " a1 = " + str(polinom6[1]) + " a2 =" + str(polinom6[2]) + " a3 = " + str(polinom6[3]) + " a4 = " + str(polinom6[4]) + " a5 = "+ str(polinom6[5])+" a6 = "+str(polinom6[6])+ "\n")


def uygunPolinomSecVeDondur(katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6,dosya):
    dosya.write("katsayi1 = "+str(katsayi1)+" katsayi2 = "+str(katsayi2)+" katsayi 3 = "+str(katsayi3)+" katsayi4 = "+str(katsayi4)+" katsayi5 = "+str(katsayi5)+" katsayi6 = "+str(katsayi6)+"\n")
    degerler = [katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6]
    for i in range(len(degerler)):
        if degerler[i] == max(degerler):
             dosya.write("korelasyon katsayisi 1 e en yakin olan sayi "+str(degerler[i])+" dir.Polinomlar arasinda en uygun olan "+str(i+1)+". polinomdur.\n")
             polinomDerece=i+1
    if polinomDerece == 1:
        denklem = polinom1[0]*x + polinom1[1]
    elif polinomDerece == 2:
        denklem = polinom2[0]*x**2 + polinom2[1]*x + polinom2[2]
    elif polinomDerece == 3:
        denklem = polinom3[0]*x**3 + polinom3[1]*x**2 + polinom3[2]*x + polinom3[3]
    elif polinomDerece == 4:
        denklem = polinom4[0]*x**4 + polinom4[1]*x**3 + polinom4[2]*x**2 + polinom4[3]*x + polinom4[4]
    elif polinomDerece == 5:
        denklem = polinom5[0]*x**5 + polinom5[1]*x**4 + polinom5[2]*x**3 + polinom5[3]*x**2 + polinom5[4]*x + polinom5[5]
    else:
        denklem = polinom6[0]*x**6 + polinom6[1]*x**5 + polinom6[2]*x**4 + polinom6[3]*x**3 + polinom6[4]*x**2 + polinom6[5]*x + polinom6[6]
    print("En uygun polinomun derecesi : ",str(polinomDerece))
    return denklem

def polinomluIntegralHesapla(denklem):
    a,b=1,len(vakalar) #18040101(1)
    deltaX = 0.1
    integral = 0
    n = int((b - a) / deltaX)
    for i in range(n):
        integral += deltaX * (denklem.subs({x:a}) + denklem.subs({x:a+deltaX})) / 2
        a += deltaX
    return integral

def polinomsuzIntegralHesapla(veriler):
    a,b=1,len(veriler) #18040101(1)
    deltaX = 1
    integral = 0
    n = int((b - a) / deltaX)
    for i in range(n-1):
        integral += deltaX * (veriler[a] + veriler[a+deltaX]) / 2
        a += deltaX
    return integral

def yorumYap(dosya):
    yorum = "Batuhan Okur / 180401011 \n " \
            "Integral hesaplarken hesapladığımız polinomu dikdörtgenlere böler ve bu dikdörtgenlerin alanlarını hesaplayıp toplarız.\n" \
            "Bu dikdörtgenlerin eni ne kadar küçük olursa sonuç o kadar gerçeğe yakın olur. \n" \
            "Polinomla hesaplarken hesaplanan yeri, denklem bilindiği için istediğimiz kadar küçük dikdörtgenlere bölebiliyoruz.Bu da gerçeğe daha yakın sonuç elde etmemizi sağlıyor. \n" \
            "Polinomsuz hesaplarken istediğimiz kadar küçük parçaya bölemediğimiz için hata oranı daha fazla oluyor."
    yorumDosyasi = open(dosya,"w")
    yorumDosyasi.write(yorum)
    yorumDosyasi.close()
            

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
dosya = open("sonuc.txt","w")
katsayilari_yazdirma(polinom1,polinom2,polinom3,polinom4,polinom5,polinom6,dosya)#katsayıları yazdırıyorum.
denklem = uygunPolinomSecVeDondur(katsayi1,katsayi2,katsayi3,katsayi4,katsayi5,katsayi6,dosya)#en uygun olan polinomu seçiyorum.
dosya.write("En Uygun Denklem : ") 
dosya.write(str(denklem))
dosya.write("\nPolinom kullanarak hesaplanan integral : ")
dosya.write(str(polinomluIntegralHesapla(denklem)))
dosya.write("\nPolinomsuz hesaplanan integral : ")
dosya.write(str(polinomsuzIntegralHesapla(vakalar)))
dosya.close()

print("En Uygun Denklem : ")
pprint(denklem) #Hem çıktı olarak veriliyor hem de sonuç dosyasına yazdırılıyor.
print("Polinom kullanarak hesaplanan integral : \n",polinomluIntegralHesapla(denklem)) #Hem çıktı olarak veriliyor hem de sonuç dosyasına yazdırılıyor.
print("Polinomsuz hesaplanan integral : \n",polinomsuzIntegralHesapla(vakalar)) #Hem çıktı olarak veriliyor hem de sonuç dosyasına yazdırılıyor.
yorumYap('180401011_yorum.txt')
