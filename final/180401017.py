#Simay Hoşmeyve 180401017
from sympy import Symbol
from sympy import pprint
degerler = []
with open ("veriler.txt","r")as dosya:
    for line in dosya.readlines():
        degerler.append(int(line))

def karekok(sayi):
    #NEWTON RAPHSON İLE KAREKÖK HESAPLAMA
    def f(x):
        return(x**2-sayi) 
    #x**2=sayi eşitliğinden a sayısının karekökü hesaplanır
    def fi(x):
        return(2*x)
    x2,t=0,1
    def hata(x1,x2):
        return((x1-x2)/x1)
    x1 =100 #yaklaştırma istenen bir tahmin
    while(abs(hata(t,x2))> 0.0001):  
        x2 = x1 - f(x1)/fi(x1)  
        t=x1
        x1=x2
    return x1

def hataPayi(sonuc,ilk,son):
    n=son-ilk
    yi = 0
    for i in range(ilk,son):
        yi+=degerler[i]
    y_ort = yi/n  
    Sr = 0
    for i in range(ilk,son):
        Sr = (sonuc[i-ilk] - degerler[i]) ** 2 + Sr
    St = 0
    for i in range(ilk,son):
        St = St + (degerler[i] - y_ort)**2
    rkare=  abs((St-Sr)/St)
    r = karekok(rkare)
    return r

def matriscoz(A,b):#matris hesaplama
        n = len(A)
        M = A

        i = 0
        for x in M:
            x.append(b[i])
            i += 1

        for k in range(n):
            for i in range(k,n):
                if abs(M[i][k]) > abs(M[k][k]):
                    M[k], M[i] = M[i],M[k]
                else:
                    pass

            for j in range(k+1,n):
                q = float(M[j][k] / M[k][k])
                for m in range(k, n+1):
                    M[j][m] -=  q * M[k][m]

        x = [0 for i in range(n)]

        x[n-1] = float(M[n-1][n]/M[n-1][n-1])
        for i in range (n-1,-1,-1):
            z = 0
            for j in range(i+1,n):
                z = z  + float(M[i][j])*x[j]
            x[i] = float(M[i][n] - z)/M[i][i]
        return x


def yaklastirma(ilk,son):     
    korelasyon=[]
    aralik = son-ilk
    for derece in range(1,7):
        x_val = []
        #y_val = []
        for i in range(aralik):
            #y_val.append(degerler[i])
            x_val.append(i+1)

                
        matris = [[0 for i in range(derece+1)] for j in range(derece+1)]
        x=len(matris)


        for i in range(x): #x toplamları
            for j in range(x):
                sum_x=0
                for k in range(aralik):
                    matris[0][0] = len(x_val)
                    sum_x +=x_val[k]**(i+j)
                    matris[i][j] = sum_x

        
        xy_sonuc = [] #xy carpımlarının toplamları
        for m in range(x):
            sum_xy = 0
            for n in range(ilk,son):
                sum_xy = sum_xy + (degerler[n]*(x_val[n-ilk]**m))
            xy_sonuc.append(sum_xy)
        
        katsayi=matriscoz(matris,xy_sonuc)
        sonuc= []
        for i in range(aralik):
            toplam = 0
            for j in range(len(katsayi)):
                toplam = toplam + katsayi[j]*((i+1)**j)
                if j == derece:
                    sonuc.append(int(toplam))
        k = hataPayi(sonuc,ilk,son) 
        korelasyon.append(k)
    max = 100
    index=0
    for i in range(len(korelasyon)):
        temp = abs(1-korelasyon[i])
        if temp<max:
            max = temp
            index = i+1
    print('En uygun derece:'+str(index))

    x = Symbol("x")
    if len(katsayi) < 7:
        while len(katsayi)!=7:
            katsayi.append(0)
    polinom=katsayi[6]*x**6+katsayi[5]*x**5+katsayi[4]*x**4+katsayi[3]*x**3+katsayi[2]*x**2+katsayi[1]*x+katsayi[0]
    print("Polinom:")
    pprint(polinom)

    a = 7 #öğrenci numarasının son rakamından başlıyor
    b = len(degerler)
    deltax = 0.1 #daha küçük değerlerde daha iyi sonuç alırız fakat yavaş hesaplar
    integral = 0

    n = int((b-a)/deltax)
    for i in range(n):
        #yamuklar ile alan hesaplaması yaptık
        #polinomda xlere değer atadık  
        integral += deltax*(polinom.subs({x:a})+polinom.subs({x:a+deltax}))/2
        a += deltax 
    print("Polinom kullanılan integral ile: ",integral)  

def polinomsuz():
    a=7  
    b=len(degerler) 
    deltax=1 #polinom kullanmadığımız için iki değer arası küçük aralıkları alamayız
    integral = 0
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral+=deltax*(degerler[a]+degerler[a+deltax])/2
        a+=deltax
    print("Polinomsuz integral ile: ",integral)

yaklastirma(0,len(degerler))  
polinomsuz()

yorum = open('180401017_yorum.txt','w',encoding='UTF8')
yorum.write("Simay Hoşmeyve 180401017 \n" \
             "Polinom yardımıyla hesaplama yaparken deltax aralığımızı daha küçük alabiliyoruz." \
             "Böylece alan hesaplamak için dikdörtgen veya yamuk yöntemi ile oluşturduğumuz alan" \
             "daha detaylı hesaplama yapabiliyor taşmalar veya eksilmeler daha az oluyor. \n" \
             "Polinomsuz hesaplarken ise bu aralıkları en küçük 1'den yani bir x verisinden bir sonrakine kadar"  
             "alabiliyoruz.Polinomsuz hesaplamada sonuçlarımız gerçek sonuca daha uzak çıkıyor.\n" 
             "Bu nedenlerden sonuçlar arasında fark buluyoruz.")
yorum.close()