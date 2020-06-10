#Mehmet Akif Selbi 170401041
import math
def dosya_oku():
    dosya = open("veriler.txt")
    y = dosya.readlines()
    x=[]
    for i in range(len(y)):
        y[i]=int(y[i])
        x.append(i)
    return x,y

def matris_olustur(x,y,n,m):
    matris=[]
    for i in range(m+1):
        satir=[]
        for j in range(m+1):
            if(i==0 and j==0):
                satir.append(n)
            else:
                x_toplam = 0
                for x_eleman in x:
                    x_toplam += x_eleman**(i+j)
                satir.append(x_toplam)
        sum_= 0
        for eleman in range(n):
            sum_ += (x[eleman]**i)*y[eleman]
        satir.append(sum_)
        matris.append(satir)
    return matris

def matris_coz(matris):#Gauss
    boyut = len(matris)
    for i in range(0, boyut):
        maxSutun = abs(matris[i][i])
        maxSatir = i
        for j in range(i + 1, boyut):
            if abs(matris[j][i]) > maxSutun:
                maxSutun = abs(matris[j][i])
                maxSatir = j
        for k in range(i, boyut + 1):
            temp = matris[maxSatir][k]
            matris[maxSatir][k] = matris[i][k]
            matris[i][k] = temp
            
        for l in range(i + 1, boyut):
            c = -matris[l][i] / matris[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    matris[l][j] = 0
                else:
                    matris[l][j] += c * matris[i][j]

    r_matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        r_matris[i] = matris[i][boyut] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][boyut] -= matris[k][i] * r_matris[i]
    return r_matris

def korelasyon(x,y,n,katsayilar,m):
    Sr,St,y_= 0,0,0
    for i in y:
        y_+= i
    y_ /= len(y)
    for i in range(n):
        Sr_1=0
        St += (y[i]-y_)**2
        Sr_1 += y[i]-katsayilar[0]
        for j in range(1,m+1):
            Sr_1 -= katsayilar[j]*(x[i]**j)
        Sr_1 = Sr_1**2
        Sr+=Sr_1
    r = math.sqrt(abs((St-Sr)/St)) #korelasyon
    return r

def polinom_yakinlastirma(x,y):
    r =[]
    polinom_katsayilari = []
    for i in range(1,7):
        katsayilar = matris_coz(matris_olustur(x,y,len(y),i))
        r.append(korelasyon(x,y,len(y),katsayilar,i))
        polinom_katsayilari.append(katsayilar)
    max_= r[0]
    temp = 0
    for z in range(len(r)):
        if(r[z]> max_):
            max_ = r[z]
            temp = z+1
    print("en buyuk korelasyon : "+str(max_))
    print("en uygun polinom: "+str(temp)+". dereceden")
    return polinom_katsayilari[temp-1]



def fonksiyon(katsayilar,x):
    y=0
    for i in range(len(katsayilar)):
        y+=katsayilar[i]*(x**i) #a_0+a_1*x+....+a_m*x**m
    return y
 
def polinom_integrali(b,katsayilar):
    a=1 #170401041
    deltax = 0.1
    integral=0
    
    n = int((b-a)/deltax)
    for i in range(n):
        integral +=  deltax*(fonksiyon(katsayilar,a)+fonksiyon(katsayilar,a+deltax))/2
        a+=deltax
    print("integral = ",integral)        

def polinomsuz_integral(y):
    a=1  # 170401041
    b=len(y) 
    deltax=1
    integral=0
    
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral+=deltax*(y[a]+y[a+deltax])/2
        a+=deltax
    print("polinomsuz integral = ",integral)

def yorum():
    dosya = open("170401041_yorum.txt","w")
    dosya.write("Hesapladigimiz 2 integralin farkli cikmasinin nedeni\n")
    dosya.write("integral hesabi yaparken verilen polinomu kucuk diktorgenlere bolup ,alanlarini hesaplayip ,toplariz\n")
    dosya.write("Aldigimiz dikdortgenlerin ne kadar kucuk olursa o kadar fazla dikdortgen alani hesaplar ve integrale yakin deger elde ederiz\n")
    dosya.write("Biz bu olayi bu fonksiyonlarda deltax ile yapiyoruz\n")
    dosya.write("Polinomluda deltax i kucuk secebiliyoruz\n")
    dosya.write("Polinomsuzda deltax 1 oldugu icin belli sayida yaklasabiliyoruz\n")
    dosya.write("Bu yuzden polinomlu da hassas bir sekilde integrali hesaplayabiliyorken polinomsuz da bunu yapamiyoruz\n")
    dosya.close()



x,y = dosya_oku()
polinom_katsayilari = polinom_yakinlastirma(x,y)
polinom_integrali(len(y),polinom_katsayilari)
polinomsuz_integral(y)
yorum()
