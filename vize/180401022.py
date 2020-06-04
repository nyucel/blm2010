#Hazirlayan: Ahmet Osman Sezgin
import math
def polinomlar(derece):
    if(derece == 1):
        a1 = ((xiler[0]*xiyiler[1])-(xiler[1]*xiyiler[0]))/ ((xiler[0]*xiler[2])-(xiler[1])**(2))
        a0 = (xiyiler[0]-(a1*xiler[1]))/xiler[0]
        
        with open("sonuc.txt","w") as file:     #sonuc.txt dosyasini temizleyip yeniden yazmak icin 'w' kullandim.
            file.write("1.Derece:\n")
            file.write("\ta1: {}\n\ta0: {}".format(a1,a0))
    
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1)))
        
        return b
    
    matris = matris_olustur(derece)             #Matris olusturulup cozulur.
    m = gauss(matris)                           #Katsayilar hesaplanir ve elde edilen tahmini vakalar liste seklinde dondurulur.
    
    if(derece == 2):
        a2 = m[2][3]
        a1 = m[1][3] - m[1][2]*a2    
        a0 = m[0][3] - m[0][1]*a1 - m[0][2]*a2
      
        with open("sonuc.txt","a") as file:
            file.write("\n2.Derece:\n")
            file.write("\ta2: {}\n\ta1: {}\n\ta0: {}".format(a2,a1,a0))
            
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2)))
        return b
    if(derece == 3):
        a3 = m[3][4]
        a2 = m[2][4] - m[2][3]*a3
        a1 = m[1][4] - m[1][3]*a3 - m[1][2]*a2
        a0 = m[0][4] - m[0][3]*a3 - m[0][2]*a2 - m[0][1]*a1
        with open("sonuc.txt","a") as file:
            file.write("\n3.Derece:\n")
            file.write("\ta3: {}\n\ta2: {}\n\ta1: {}\n\ta0: {}".format(a3,a2,a1,a0))
    
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2) + a3*((i+1)**3)))
        return b
    if(derece == 4):
        a4 = m[4][5]
        a3 = m[3][5] - m[3][4]*a4
        a2 = m[2][5] - m[2][4]*a4 - m[2][3]*a3
        a1 = m[1][5] - m[1][4]*a4 - m[1][3]*a3 - m[1][2]*a2
        a0 = m[0][5] - m[0][4]*a4 - m[0][3]*a3 - m[0][2]*a2 - m[0][1]*a1
        with open("sonuc.txt","a") as file:
            file.write("\n4.Derece:\n")
            file.write("\ta4 {}\n\ta3: {}\n\ta2: {}\n\ta1: {}\n\ta0: {}".format(a4,a3,a2,a1,a0))
    
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2) + a3*((i+1)**3) + a4*((i+1))**4))
        return b
    if(derece == 5):
        a5 = m[5][6]
        a4 = m[4][6] - m[4][5]*a5
        a3 = m[3][6] - m[3][5]*a5 - m[3][4]*a4
        a2 = m[2][6] - m[2][5]*a5 - m[2][4]*a4 - m[2][3]*a3
        a1 = m[1][6] - m[1][5]*a5 - m[1][4]*a4 - m[1][3]*a3 - m[1][2]*a2
        a0 = m[0][6] - m[0][5]*a5 - m[0][4]*a4 - m[0][3]*a3 - m[0][2]*a2 - m[0][1]*a1
        with open("sonuc.txt","a") as file:
            file.write("\n5.Derece:\n")
            file.write("\ta5 {}\n\ta4 {}\n\ta3: {}\n\ta2: {}\n\ta1: {}\n\ta0: {}".format(a5,a4,a3,a2,a1,a0))
        
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2) + a3*((i+1)**3) + a4*((i+1)**4) +a5*((i+1))**5))
        return b
    if(derece == 6):
        a6 = m[6][7]
        a5 = m[5][7] - m[5][6]*a6
        a4 = m[4][7] - m[4][6]*a6 - m[4][5]*a5
        a3 = m[3][7] - m[3][6]*a6 - m[3][5]*a5 - m[3][4]*a4
        a2 = m[2][7] - m[2][6]*a6 - m[2][5]*a5 - m[2][4]*a4 - m[2][3]*a3
        a1 = m[1][7] - m[1][6]*a6 - m[1][5]*a5 - m[1][4]*a4 - m[1][3]*a3 - m[1][2]*a2
        a0 = m[0][7] - m[0][6]*a6 - m[0][5]*a5 - m[0][4]*a4 - m[0][3]*a3 - m[0][2]*a2 - m[0][1]*a1    
        with open("sonuc.txt","a") as file:
            file.write("\n6.Derece:\n")
            file.write("\ta6: {}\n\ta5 {}\n\ta4 {}\n\ta3: {}\n\ta2: {}\n\ta1: {}\n\ta0: {}".format(a6,a5,a4,a3,a2,a1,a0))
    
        b = []
        for i in range(xiler[0]):
            b.append(int(a0 + a1*(i+1) + a2*((i+1)**2) + a3*((i+1)**3) + a4*((i+1)**4) +a5*((i+1)**5) + a6*((i+1)**6)))
        return b
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
for i in range(1,7):
    bulunanlar.append(polinomlar(i))  #bulunanlar'listesi:polinomlarin urettigi degerleri listeler halinde tutuyor.

rler = []
for i in range(1,len(bulunanlar)):
    rler.append(hata_hesapla(vaka,bulunanlar[i],i)) #rler'listesi:her polinomun urettigi degerler ile gercek veriler arasindaki oranlari tutuyor.

uzaklik = []
for i in rler:
   uzaklik.append(abs(1-i)) #uzaklik'listesi polinomlarin hata oranlarinin 1'e olan uzakliklarini tutuyor.

indeksi = uzaklik.index(min(uzaklik))
print("Veriler butun polinomlara yakinlastirildi,en uygun polinom: {}.Dereceden Polinomdur ve Korelasyon degeri: {}".format((indeksi+1),rler[indeksi]))