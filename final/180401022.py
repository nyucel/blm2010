#Hazirlayan: Ahmet Osman Sezgin
import math
def f(x): 
    k = 0
    for i in range(len(z)): #z'uygun katasyilari tutuyor.
        k += z[i]*x**i 
        
    return (k)


def polinomlar(derece):
    
    if(derece == 1):
        a1 = ((xiler[0]*xiyiler[1])-(xiler[1]*xiyiler[0]))/ ((xiler[0]*xiler[2])-(xiler[1])**(2))
        a0 = (xiyiler[0]-(a1*xiler[1]))/xiler[0] 
        katsayilar = [a0,a1]
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1)))
        return b,katsayilar
    
    matris = matris_olustur(derece)             #Matris olusturulup cozulur.
    m = gauss(matris)                           #Katsayilar hesaplanir ve elde edilen tahmini vakalar liste seklinde dondurulur.
    
    if(derece == 2):
        a2 = m[2][3]
        a1 = m[1][3] - m[1][2]*a2    
        a0 = m[0][3] - m[0][1]*a1 - m[0][2]*a2
        katsayilar = [a0,a1,a2]
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2)))
        return b,katsayilar
    
    if(derece == 3):
        a3 = m[3][4]
        a2 = m[2][4] - m[2][3]*a3
        a1 = m[1][4] - m[1][3]*a3 - m[1][2]*a2
        a0 = m[0][4] - m[0][3]*a3 - m[0][2]*a2 - m[0][1]*a1
        katsayilar = [a0,a1,a2,a3]
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2) + a3*((i+1)**3)))
        return b,katsayilar
    
    if(derece == 4):
        a4 = m[4][5]
        a3 = m[3][5] - m[3][4]*a4
        a2 = m[2][5] - m[2][4]*a4 - m[2][3]*a3
        a1 = m[1][5] - m[1][4]*a4 - m[1][3]*a3 - m[1][2]*a2
        a0 = m[0][5] - m[0][4]*a4 - m[0][3]*a3 - m[0][2]*a2 - m[0][1]*a1
        katsayilar = [a0,a1,a2,a3,a4]
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2) + a3*((i+1)**3) + a4*((i+1))**4))
        return b,katsayilar
    
    if(derece == 5):
        a5 = m[5][6]
        a4 = m[4][6] - m[4][5]*a5
        a3 = m[3][6] - m[3][5]*a5 - m[3][4]*a4
        a2 = m[2][6] - m[2][5]*a5 - m[2][4]*a4 - m[2][3]*a3
        a1 = m[1][6] - m[1][5]*a5 - m[1][4]*a4 - m[1][3]*a3 - m[1][2]*a2
        a0 = m[0][6] - m[0][5]*a5 - m[0][4]*a4 - m[0][3]*a3 - m[0][2]*a2 - m[0][1]*a1
        katsayilar = [a0,a1,a2,a3,a4,a5]
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2) + a3*((i+1)**3) + a4*((i+1)**4) +a5*((i+1))**5))
        return b,katsayilar
    
    if(derece == 6):
        a6 = m[6][7]
        a5 = m[5][7] - m[5][6]*a6
        a4 = m[4][7] - m[4][6]*a6 - m[4][5]*a5
        a3 = m[3][7] - m[3][6]*a6 - m[3][5]*a5 - m[3][4]*a4
        a2 = m[2][7] - m[2][6]*a6 - m[2][5]*a5 - m[2][4]*a4 - m[2][3]*a3
        a1 = m[1][7] - m[1][6]*a6 - m[1][5]*a5 - m[1][4]*a4 - m[1][3]*a3 - m[1][2]*a2
        a0 = m[0][7] - m[0][6]*a6 - m[0][5]*a5 - m[0][4]*a4 - m[0][3]*a3 - m[0][2]*a2 - m[0][1]*a1
        katsayilar = [a0,a1,a2,a3,a4,a5,a6]
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2) + a3*((i+1)**3) + a4*((i+1)**4) +a5*((i+1)**5) + a6*((i+1)**6)))
        return b,katsayilar
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def matris_olustur(derece):
    matris=[]
    for k in range(0,derece+1):
        matris.append(xiler[k:k+derece+1])      #Girilen polinom derecesine gore xiler ve xiyiler'den olusan matrisi olusturuyor.
        matris[k].append(xiyiler[k])
    return matris
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def gauss(matris):
    boyut = len(matris)
    for n in range(boyut):
        kat = int(matris[n][n])             
        for m in range(boyut+1):                    #Elimizdeki matrisi alt ucgensel yaparak
            matris[n][m]=int(matris[n][m])/kat      #Katsayilari bulmamizi saglayan fonksiyon.
        for p in range(1,boyut-n):
            kat = float(matris[n+p][n])        
            for q in range(boyut+1):
                matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))
    return matris         
#-------------------------------------------------------------------------------------------------------------------------------------------------------    
def hata_hesapla(vaka,bulunan,derece):
    sr = 0
    st = 0
    yus = xiyiler[0]/len(vaka)
    for i in range(len(vaka)):              #Gercek vakalar ile fonksiona gelen dereceden polinomunlarin urettigi degerler arasindaki
        sr += (vaka[i] - bulunan[i])**2     #hata oranlari hespalaniyor.
        st += (vaka[i] - yus)**2
    
    r = math.sqrt((st-sr)/st)
    return r
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def polinomsuzIntegral():
        integral = 0
        a=2  #180401022 (2)
        b=len(vaka) 
        deltax=1
        n = int((b-a)/deltax)
        for i in range(n-1):
            integral+=deltax*(vaka[a]+vaka[a+deltax])/2
            a+=deltax
        print("Polinomsuz,gercek veriler ile Integral degeri: ",integral)
    
def polinom_integral():
    a = 2 #numara sonu
    b = len(vaka)
    deltax = 1
    integral = 0
    n = int((b-a)/deltax)
    
    for i in range(n):
        integral += deltax*(f(a)+f(a+deltax))/2 #yamuk yöntemi
        a += deltax
        
    print("Uygun olan polinom ile Integral degeri: ",integral)
#******************************************************main*********************************************************************************************
vaka = []
with open("veriler.txt","r") as file:
    for i in file.readlines():          #Verileri vaka'listesine aktariyor.
        i = i.rsplit('\n')
        vaka.append(int(i[0]))

n = len(vaka)
yitoplam = sum(vaka)
xler = [0,0,0,0,0,0,0,0,0,0,0,0]      #xler'listesinin 0.indeksi:xitoplam,1.indeksi:xi2toplam...
xiler = [n]
xyler = [0,0,0,0,0,0]                 #yler'listesinin 0.indeksi:xiyitoplam,1.indeksi:xi2yitoplam... seklinde tutuluyor.
xiyiler = [yitoplam]
#-------------------------------------------------------------------------------------------------------------------------------------------------------
for i in range(n):
    for j in range(12):
        xler[j] += (i+1)**(j+1)
    for j in range(6):
        xyler[j] += vaka[i]*(i+1)**(j+1)      #Bu kisimda:xitoplam,xi2toplam,xi3toplam...
                                              #ve xiyitoplam,xi2yitoplam,xi3yitoplam ... degerleri olarak kullanilacak olan degerler listede tutuluyor.
for i in xler:                                
    xiler.append(i)                           
for i in xyler:                               #islemlerin sonunda elimizde,n defa arttirilmis xiler ve xiyilerden olusan 2 adet liste olmus oluyor.
    xiyiler.append(i)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
bulunanlar = [0]
butun_katsayilar = []
for i in range(1,7):
    x,y = polinomlar(i)
    bulunanlar.append(x)  #bulunanlar'listesi:polinomlarin urettigi degerleri listeler halinde tutuyor.
    butun_katsayilar.append(y)
#print(butun_katsayilar)
rler = []
for i in range(1,len(bulunanlar)):
    rler.append(hata_hesapla(vaka,bulunanlar[i],i)) #rler'listesi:her polinomun urettigi degerler ile gercek veriler arasindaki oranlari tutuyor.

uzaklik = []
for i in rler:
   uzaklik.append(abs(1-i)) #uzaklik'listesi polinomlarin hata oranlarinin 1'e olan uzakliklarini tutuyor.

indeksi = uzaklik.index(min(uzaklik))
print("Verilere en uygun polinom,{}.dereceden polinomdur ".format((indeksi+1)))
uygun_polinom = indeksi + 1
k,z = polinomlar(uygun_polinom)

#print(z) #uygun polinomun katsayilari z'de
polinom_integral()
polinomsuzIntegral()

with open("180401022_yorum.txt","w") as file:    
            file.write("Ahmet Osman Sezgin\n\n"
                      "2. ve 3. sorularda bulunan sonuclarin farkli olma nedeni:\n\n"
                      "Polinomlu integral hesaplamada kullandigimiz polinomun,bize verilen diger polinomlara kiyasla en uygun polinomdur.\n"
                      "Yani bu polinomun korelasyon degeri, (kiyasladigimiz diger polinomlara gore) 1'e daha yakin oldugu icin sectik.\n"
                      "Fakat bu polinomun da korelasyon degeri = 1 olmadigi icin gercek polinom degildir ve gercek sonuclari alamayacagiz.\n"
                      "Integral hesaplarken kullandigimiz yamuklarin enini ne kadar kucultursek(deltax),gercek polinom ile yamuklar arasindaki bosluk azalicagi icin:\n"
                      "Gercege daha yakin sonuclar hesaplanacaktir.\n\n "
                      "Polinomsuz hesaplama ve polinomlu hesaplamamizin farkli cikmasinin nedenleri bunlardir.")