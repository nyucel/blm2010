#Simay Hoşmeyve
#180401017
degerler = []
with open ("veriler.txt","r")as dosya:
    for line in dosya.readlines():
        degerler.append(int(line))

def textYazdir(katsayi,sonuc,ilk,son):
    text = open("sonuc.txt", "a",encoding="utf-8") 
    text.write(str(len(katsayi)-1)+'. derece\n')
    text.write('Katsayılar:')
    text.write('\n')
    for i in katsayi:
        text.write(str(i))
        text.write('\n')
    text.write('\n')
    text.write('Veriler:')
    text.write('\n')
    for i in range(ilk,son):
        text.write('Veri:')
        text.write(str(degerler[i]))
        text.write('\t')
        text.write('Sonuç:')
        text.write(str(sonuc[i-ilk]))
        text.write('\n')
    
    text.write('#'*50)
    text.write('\n')
    text.close

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

def linearsolver(A,b):#matris hesaplama
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
        
        katsayi=linearsolver(matris,xy_sonuc)
        sonuc= []
        for i in range(aralik):
            toplam = 0
            for j in range(len(katsayi)):
                toplam = toplam + katsayi[j]*((i+1)**j)
                if j == derece:
                    sonuc.append(int(toplam))
        k = hataPayi(sonuc,ilk,son) 
        korelasyon.append(k)
        textYazdir(katsayi,sonuc,ilk,son)
    max = 100
    index=0
    for i in range(len(korelasyon)):
        temp = abs(1-korelasyon[i])
        if temp<max:
            max = temp
            index = i+1
    dosya = open('sonuc.txt','a+')
    dosya.write(str(ilk)+'-'+str(son)+' verilerinde en uygun derece: '+str(index)+'\n')
    dosya.write('Korelasyonu:  '+str(korelasyon[index-1])+'\n')
    dosya.write('\n')
    dosya.close()
    
yaklastirma(0,len(degerler))  
a = 0
b = 10
while(b<=len(degerler)):#10lu aralıklar icin yaklastirma
       yaklastirma(a,b)
       a += 10
       b += 10
