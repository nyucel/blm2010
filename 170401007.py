# Arda Cem Bilecan 170401007 
import math
veriler=[]
korelasyonlar=[]
def dosyaOku():
    dosya = open('Veriler.txt','r')
    for satir in dosya:
        veriler.append(int(satir))
    dosya.close()

def yazdir(kendiSonuclarim,katSayilar,first,end,derece,r):
    dosya = open('sonuc.txt','a+')
    dosya.write('************  '+str(first)+' - '+ str(end-1)+'(dahil) ********INDEX ARALIKLARI ICIN  '+str(derece)+'.  DERECEDEN YAKLASIM \n')
    dosya.write('KORELASYON DEGERI:  '+str(r)+'\n')
    dosya.write(' Katsayilar: ')
    dosya.write('\n')
    for i in katSayilar:
        dosya.write(str(i))
        dosya.write('\t')
    dosya.write('\n')
    dosya.write('ASIL VERI , KENDI BULDUKLARMIZ: ')
    dosya.write('\n')
    for i in range(first,end):
        dosya.write(str(veriler[i]))
        dosya.write('\t')
        dosya.write(str(kendiSonuclarim[i-first]))
        dosya.write('\n')
    dosya.close()
    
      
def gauss(A):
    boyut = len(A)
    for i in range(0, boyut):
        maxSutun = abs(A[i][i])
        maxSatir = i
        for j in range(i + 1, boyut):
            if abs(A[j][i]) > maxSutun:
                maxSutun = abs(A[j][i])
                maxSatir = j
        for k in range(i, boyut + 1):
            temp = A[maxSatir][k]
            A[maxSatir][k] = A[i][k]
            A[i][k] = temp
            
        for l in range(i + 1, boyut):
            c = -A[l][i] / A[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    A[l][j] = 0
                else:
                    A[l][j] += c * A[i][j]

    matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        matris[i] = A[i][boyut] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][boyut] -= A[k][i] * matris[i]
    return matris


def korelasyon(kendiSonuclarim,first,end):
    n=end-first
    yi = 0
    for i in range(first,end):
        yi+=veriler[i]
    y_ussu = yi/n  #y'lerin ortalamsi
    Sr = 0
    for i in range(first,end):
        Sr = (kendiSonuclarim[i-first] - veriler[i]) ** 2 + Sr
    St = 0
    for i in range(first,end):
        St = St + (veriler[i] - y_ussu)**2
    rkare=  abs((St-Sr)/St)
    r = math.sqrt(rkare)
    return r



def veriBulma(first,end):     #10lu SEKLİNDE alip 6. dereceye kadar hesaplatİp en iyi derceyi buluyoruz veya bütün verili burda hesapliyoruz
    dizi=[]
    n = end-first
    for derece in range(1,7):
        xValue = []
        for i in range(n):
            xValue.append(i+1)
        # MATRIS Olusturuyoruz    
        matris = [[0 for i in range(derece+1)] for j in range(derece+1)]
        boyut = len(matris)
    
        for i in range(boyut):
            for j in range(boyut):
                xToplamlari=0
                for k in range(n):
                    matris[0][0] = len(xValue) # matrisin 0,0 x veri sayisi kadar olmali
                    xToplamlari=xValue[k]**(i+j)+ xToplamlari  
                    matris[i][j] = xToplamlari
                
        
        
        # y , y*x , y*xkare , y*xkup gibi ifadeleri buluyoruz. 
        xySonuclari = []
        for i in range(boyut):
            toplam=0
            for j in range(first,end):
                toplam = toplam + (veriler[j]*(xValue[j-first]**i))    
            xySonuclari.append(toplam)
        
        # Buldugumuz sonuclari da matrisin en sutunlarina atiyoruz.
        k = 0        
        for i in matris:
            i.append(xySonuclari[k])
            k=k+1
    
    
            
        katSayilar=gauss(matris)
        
        kendiSonuclarim=[]
        for i in range(n):
            toplam = 0
            for j in range(len(katSayilar)):
                toplam = toplam + katSayilar[j]*((i+1)**j)
                if j == derece:
                    kendiSonuclarim.append(int(toplam))
        r = korelasyon(kendiSonuclarim,first,end) 
        dizi.append(r)
        yazdir(kendiSonuclarim,katSayilar,first,end,derece,r) # r = korelasyon degeri
        
        # 1'den 6ya kdar olan butun derecelerin korelasyondaki diziye atadik simdi ise
        # 1'e en yakin sonuc veren kolerasyon bizim icin en ideal kolerasyondur bunu bulcagiz.
        # bazi sonuclar 1'den buyuk deger dondrdigi icin abs aldik
    eniyisi = 100
    index=0
    for i in range(len(dizi)):
        temp = abs(1-dizi[i])
        if temp<eniyisi:
            eniyisi = temp
            index = i+1
    
    dosya = open('sonuc.txt','a+')
    dosya.write(str(first)+'-'+str(end-1)+' araliklarinda en iyi korelasyona sahip olan derece: '+str(index)+'\n')
    dosya.write('KORELASYON DEGERI ISE:  '+str(dizi[index-1])+'\n')
    dosya.write('********************************************')
    dosya.write('\n')
    dosya.close()
    

    


dosyaOku()    
veriBulma(0,len(veriler))  # önce burada bütün veriler için sonuçları vs bulup korelasyonu bulduk

bas = 0
son = 10   # for i in range (bas,son) olacağı için 0dan 9'a akadar alacak 
# daha sonra da 10ar 10ar alıp 1den 6. dereceye kadar yaklaştırıp en iyi korelasyon hangi derecede ise onları yazdırdık
while(son<=len(veriler)): 
       veriBulma (bas,son)
       bas = bas+10
       son = son+10



                



      

    


