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
    #bulunan katsayılar yazdırılır
    yazdir.write(str(m)+". dereceden polinom için katsayılar : ")
    c=0
    for i in katsayilar_polinom:
        yazdir.write("a"+str(c)+"="+str(i)+" ")
        c+=1
    yazdir.write("\n")
    return katsayilar_polinom

#verilen matrisi çözerek bulduğu katsayıları döndürür
def denklem_sistemi_coz(a,sabit_terim):
    katsayilar=[]
    #len(a)->satır,sütun sayısı
    for t in range(1,len(a)):
        for i in range(t,len(a)):
            if(a[t-1][t-1]!=0):#payda 0 değilken işlem yap.
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
        if(a[i][i]!=0):#payda 0 değilken işlem yap.
            katsayilar.append(sabit_terim[i] / a[i][i])#sabit terim/katsayının yanındaki değerler
        else:#payda 0 ise katsayı =0
            katsayilar.append(0)
    katsayilar.reverse()#katsayılar tersine doğru bulunduğu için dizi ters çevirilir
    return katsayilar
   
#birden fazla polinom için bulunan katsayıları sözlük yapısında alır.
#korelasyonları ve en iyi korelasyonu yazdırır
#tahmini hataları ve en az tahmini hatayı yazdırır
def test_et(sayi_dizisi,katsayilar_sozlugu):
    en_fazla_korelasyon_polinom=0
    en_fazla_korelasyon=0
    en_az_hata=100000000000
    en_az_hata_polinom=0
    y_ortalama=sum(sayi_dizisi)/len(sayi_dizisi)
    for polinomlar in range(len(katsayilar_sozlugu)):#verilen katsayılar sözlüğündeki her polinom için bulunan değerler üzerinde işlem yapar
        tahmini_hata=-1#payda 0 ise hata -1 olarak kalır
        katsayilar = katsayilar_sozlugu[polinomlar+1]
        Sr=0 #hataların karelerinin toplamı
        for x in range(len(sayi_dizisi)): # tüm elemanlar için hatanın karesi toplanır
            hata=sayi_dizisi[x]
            for i in range(len(katsayilar)):#y-a0-a1*x..... işlemi
                hata -= katsayilar[i]*x**i
            Sr += hata**2#bulunan hatanın karesi eklenir
        if(len(sayi_dizisi)-len(katsayilar)!=0):#payda 0 değilse
            tahmini_hata=sqrt(mutlak_deger(Sr/(len(sayi_dizisi)-len(katsayilar))))
            yazdir.write(str(polinomlar+1)+". polinom için standart tahmini hata = "+str(tahmini_hata)+"\n")
        else:#son onluk için payda 0 olma durumu
            yazdir.write(str(polinomlar+1)+". polinom için standart tahmini hata bulunamaz(payda 0)\n")
        St=0
        for i in range(len(sayi_dizisi)):
            St += (sayi_dizisi[i]-y_ortalama)**2
        korelasyon = sqrt(mutlak_deger((St-Sr)/St))
        yazdir.write(str(polinomlar+1)+". polinomun korelasyon katsayısı: "+str(korelasyon)+"\n")
        if(korelasyon > en_fazla_korelasyon):#bulunan korelasyonu en fazla olanla karşılaştır
            en_fazla_korelasyon = korelasyon
            en_fazla_korelasyon_polinom = polinomlar+1
        if(tahmini_hata !=-1 and tahmini_hata < en_az_hata):#bulunan tahmini hatayı en az olanla karşılaştır(-1 -> atanmamış)
            en_az_hata = tahmini_hata
            en_az_hata_polinom = polinomlar+1
    #tüm polinomlar için işlem yapıldıktan sonra bulunan en iyi değerler yazdırılır
    yazdir.write("en iyi korelasyon katsayısı "+str(en_fazla_korelasyon)+" ile "+str(en_fazla_korelasyon_polinom)+".polinom\n")
    yazdir.write("en az standart tahmini hata "+str(en_az_hata)+" ile "+str(en_az_hata_polinom)+".polinom\n\n")
    
def mutlak_deger(x):
    if x<0:
        return -x
    else:
        return x
    
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

yazdir=open("sonuc.txt","w")
yazdir.write("Tüm değerler için\n\n")

#tüm veriler için çağrım yapılır
katsayilar={}
for i in range(6):#kullanılacak elemanlar boş dizi haline getirilir
    katsayilar[i+1]=[]
for i in range(6):#1'den 6'ya tüm yaklaştırma denemeleri yapılır
    katsayilar[i+1]=yaklastir(sayilar,i+1)#(1.soru)
test_et(sayilar,katsayilar)#(2.soru)

#onluk halindeki veriler için çağrımlar yapılır
katsayilar={}
for onluk in range((len(sayilar)-1)//10 +1):#(3.soru) 0,1,2... gibi kaç onluk varsa oraya kadar döner
    #51 52 53...ve 60 için range(6)   10'a kalansız bölünen sayılar için -1 yapıldı
    if onluk!=len(sayilar)//10:
        yazdir.write(str(onluk*10)+" ve "+str(onluk*10+9)+" Değerleri arası\n\n")
    else:#son onluk için
        yazdir.write(str(onluk*10)+" ve "+str(onluk*10+len(sayilar)%10-1)+" Değerleri arası\n\n")
    
    for g in range(6):#kullanılacak elemanlar boş dizi haline getirilir
        katsayilar[g+1]=[]
    for j in range(6):#1'den 6'ya tüm onlu yaklaştırma denemeleri yapılır
        if onluk!=len(sayilar)//10:#son onluk olmadığı sürece
            katsayilar[j+1]=yaklastir(sayilar[onluk*10:onluk*10+10],j+1)
        else:#son onluk için onluğun tamamı yerine son elemana kadar gönder
            katsayilar[j+1]=yaklastir(sayilar[onluk*10:onluk*10+len(sayilar)%10],j+1)
    
    if onluk!=len(sayilar)//10:#test etmek için verileri onluklar olarak gönder
        test_et(sayilar[onluk*10:onluk*10+10],katsayilar)
    else:#son onluk için onluğun tamamı yerine son elemana kadar gönder
        test_et(sayilar[onluk*10:onluk*10+len(sayilar)%10],katsayilar)
yazdir.close()
