#Musa Odabaşı
#ilk değer x=0 noktası olarak alındı
from math import sqrt

#verilen sayıları m.dereceden polinoma yaklaştırır
def yaklastir(sayi_dizisi,m=2):
    n = len(sayi_dizisi)
    x_uzeri_toplamlari=[]# [0]->xtoplam  [1]->x**2toplam [2]->x**3toplam...
    for i in range(2*m):#toplamları ekleneceğinden tüm elemanlara 0 yazılır
        x_uzeri_toplamlari.append(0)
    
    sabit_terimler=[]# [0]->y toplam  [1]->x*y toplam [2]->x**2 *y toplam ...
    for i in range(m+1):#toplamları ekleneceğinden tüm elemanlara 0 yazılır
        sabit_terimler.append(0)
    
    for x in range(n):#x üzeri ifadelerinin ve x üzeri *y ifadelerinin toplamları hesaplanır
        for j in range(2*m):
            x_uzeri_toplamlari[j] += x**(j+1)
        for j in range(m+1):
            sabit_terimler[j] += sayi_dizisi[x] * x**(j)
    a={} # a[0] -> a0'ın yanındaki ifadeler. a[1] -> a1'in yanındaki ifadeler... (a0+a1*x+a1*x**2...=sabit) denklemi için
    for i in range(m+1):#her katsayı için boş küme oluşturulur
        a[i]=[]
    #bulunan toplam değerleri formüle göre a katsayılarının yanına yazılır
    for i in range(m+1):
        if i!=0:
            for j in range(m+1):
                a[j].append(x_uzeri_toplamlari[i+j-1])#hafta6 ders notu 4.sayfa formülü
        else:#ilk denklem için 1.eleman olarak n kullanılıyor
            for j in range(m+1):
                if j!=0:
                    a[j].append(x_uzeri_toplamlari[i+j-1])
                else:#i=0 j=0 yani ilk denklemin ilk elemanı n
                    a[j].append(n)
    #bulunan katsayılar matrisi çözen fonksiyona yollanır. Katsayılar bulunmuş olur
    katsayilar_polinom=denklem_sistemi_coz(a,sabit_terimler)
    return katsayilar_polinom


#verilen matrisi çözerek bulduğu katsayıları döndürür
def denklem_sistemi_coz(a,sabit_terim):
    katsayilar=[]
    #len(a)->satır,sütun sayısı
    for t in range(1,len(a)):
        for i in range(t,len(a)):
            eksilt = (a[t-1][i] / a[t-1][t-1])#tüm satır için çıkarılcak değerin ilk çarpanı
            for j in range(t-1,len(a)):#satırın tamamını çıkarılması gereken değerlerden çıkarır
                a[j][i] -= eksilt * a[j][t-1]#çıkarılacak değerin ikinci çarpanı her eleman için ayrı hesaplanır
            sabit_terim[i] -= eksilt * sabit_terim[t-1]#sabit terim için de ikinci çarpan hesaplanıp çıkarılır
    #verilen matris üst üçgensel hale geldikten sonra katsayılar bulunur
    for i in range(len(a)-1,-1,-1):#sondan başa doğru katsayılar
        c=0
        if(katsayilar!=[]):#son katsayının yanında başka ifade olmadığından sabit terim eksiltilmez
            for j in range(i+1,len(a)):#diğer katsayılar için önce bulunan diğer katsayılar, sabit terimden çıkarılır 
                sabit_terim[i] -= a[j][i] * katsayilar[len(katsayilar)-1-c]
                c+=1
        katsayilar.append(sabit_terim[i] / a[i][i])#sabit terim/katsayının yanındaki değerler
    katsayilar.reverse()#katsayılar tersine doğru bulunduğu için dizi ters çevirilir
    return katsayilar


   
#birden fazla polinom için bulunan katsayıları sözlük yapısında alır.
#en iyi korelasyonu ve kaçıncı polinom olduğunu yazdırır
def test_et(sayi_dizisi,katsayilar_sozlugu):
    en_fazla_korelasyon_polinom=0
    en_fazla_korelasyon=0
    en_fazla_korelasyon_katsayi=0
    y_ortalama=sum(sayi_dizisi)/len(sayi_dizisi)
    for polinomlar in range(len(katsayilar_sozlugu)):#verilen katsayılar sözlüğündeki her polinom için bulunan değerler üzerinde işlem yapar
        katsayilar = katsayilar_sozlugu[polinomlar+1]
        Sr=0 #hataların karelerinin toplamı
        for x in range(len(sayi_dizisi)): # tüm elemanlar için hatanın karesi toplanır
            hata=sayi_dizisi[x]
            for i in range(len(katsayilar)):#y-a0-a1*x..... işlemi
                hata -= katsayilar[i]*x**i
            Sr += hata**2#bulunan hatanın karesi eklenir
        St=0
        for i in range(len(sayi_dizisi)):
            St += (sayi_dizisi[i]-y_ortalama)**2
        korelasyon = sqrt(mutlak_deger((St-Sr)/St))
        if(korelasyon > en_fazla_korelasyon):#bulunan korelasyonu en fazla olanla karşılaştır
            en_fazla_korelasyon = korelasyon
            en_fazla_korelasyon_polinom = polinomlar+1
            en_fazla_korelasyon_katsayi=katsayilar
    #tüm polinomlar için işlem yapıldıktan sonra bulunan en iyi değerler yazdırılır
    print("en iyi korelasyon katsayısı "+str(en_fazla_korelasyon)+" ile "+str(en_fazla_korelasyon_polinom)+".polinom")
    return en_fazla_korelasyon_katsayi
    
def mutlak_deger(x):
    if x<0:
        return -x
    else:
        return x


def en_az_hata_bul(sayilar):
    #veriler için çağrım yapılır
    katsayilar={}
    for i in range(6):#kullanılacak elemanlar boş dizi haline getirilir
        katsayilar[i+1]=[]
    for i in range(6):#1'den 6'ya tüm yaklaştırma denemeleri yapılır
        katsayilar[i+1]=yaklastir(sayilar,i+1)
    katsayilar = test_et(sayilar,katsayilar)
    return katsayilar


#Yukarıdaki fonksiyonlar 1.sorunun cevabını bulurlar. Alttaki iki fonksiyon ise integral alma işlemini yapar.


def integral_polinom(sayilar,katsayilar):
    def f(x):
        polinom=0
        for i in range(len(katsayilar)):
            polinom += katsayilar[i] * x**i
        return polinom
    
    a=9 #180401039
    b=len(sayilar) #sayilar dizisinin uzunluğu satır sayısı kadar
    integral=0
    deltax=0.001
    n = int((b-a)/deltax)
    for i in range(n):
        integral += deltax * (f(a)+f(a+deltax))/2
        a += deltax
    print("En iyi polinomun sayısal integrali: "+str(integral))


def integral_sayilar(sayilar):
    def f(x):
        return sayilar[x]
    a=9 #180401039
    b=len(sayilar) #sayilar dizisinin uzunluğu satır sayısı kadar
    integral=0
    deltax=1
    n=int((b-a)/deltax)
    for i in range(n-1):
        integral += deltax * (f(a)+f(a+deltax))/2
        a += deltax
    print("Gerçek integral: "+str(integral))

#main
#veriler.txt okunur
oku=open("veriler.txt","r")
sayilar=[]
c=0
for i in oku:# \n atılır ve int dizisi haline getirilir
    sayilar.append(i.rstrip('\n'))
    sayilar[c]=int(sayilar[c])
    c+=1
oku.close()


katsayilar = en_az_hata_bul(sayilar)

integral_polinom(sayilar,katsayilar)

integral_sayilar(sayilar)
