# Mert BAYGIN 180401104

# nxm matris hespalama
def nnMatris(matrisHesapla):
    list = matrisHesapla.copy()
    satir = len(matrisHesapla)
    sutun = len(matrisHesapla[0])
    
#Sol üçgensel matris
    for k in range(satir-1):                            
        for i in range(satir-1-k):                      
            carpan = list[i][k]/list[i+1][k]
            for j in range(sutun):                     
                list[i][j] += -carpan * list[i+1][j]

#köşegen matris               
    for r in range(satir-1, 0, -1):
        for t in range(satir-1, satir-1-r, -1):
            carpan = list[t][r]/list[t-1][r]
            for h in range(sutun):
                list[t][h] += -carpan * list[t-1][h]
    result = []
    for s in range(satir-1, -1, -1):
        x = list[s][satir] / list[s][satir-s-1]
        result.append(x)
    return result

with open("veriler.txt","r",encoding='utf-8') as file:
    liste = [] 
    for i in file.read().split():
        liste.append(int(i))

def size(liste):
    return len(liste)
n = size(liste)
def yToplam(liste):
    x= sum(liste)
    return x
yitoplam = yToplam(liste)


#x^12 e kadar olan bütün xi toplamları tutan dizi
def xiToplam(n):
    xKareToplam = []
    for j in range(1,13,1):
        xKare = 0
        for i in range(n):
            xKare += (i+1)**j
        xKareToplam.append(xKare)
    xKareToplam.insert(0,n)
    return xKareToplam

#Polinomun 2.derecesinden itibaren bütün x^(*derece)yi tutan dizi
def xiyiToplam(n,liste,yToplam):
    xDerece_yi_toplam = []
    for j in range(1,7,1):
        value = 0
        for k in range(n):
            value +=(k+1)**j*liste[k]
        xDerece_yi_toplam.append(value)
    xDerece_yi_toplam.insert(0,yToplam)
    return xDerece_yi_toplam


def aDegerleri(n,liste,m = 8):
    result = []
    xKareToplam = xiToplam(n)
    y=yToplam(liste)
    xDerece_yi_toplam = xiyiToplam(n,liste,y)
    for x in range(2,m,1):
        newListe = []
        for i in range(x):
            newListe.append([])
            for j in range(x):
                newListe[i].append(xKareToplam[j+i])
            newListe[i].append(xDerece_yi_toplam[i])
            if i == x-1:
                result.append(nnMatris(newListe))
                newListe.clear()
    return result
# Adeger Dizisi => ?.derece polinomun a değerlerini bir dizi olarak tutar
Adeger = aDegerleri(n,liste)


#kolerasyon değeri hesaplama
def srHesapla(x,liste,n,yToplam):
    sr = 0
    st = 0
    y = yToplam/n
    size = len(x)
    for i in range(n):
        temp = 0
        for j in range(size):
            if j == 0:
                temp +=x[j]
            else:
                temp += x[j]*(i+1)**j
        sr +=(liste[i]-temp)**2
        st +=(liste[i]-y)**2
    r = ((st-sr)/st)**(1/2)
    return r

# bütün kolerasyon değerlerimizi bir dizi içerisinde tutalım    
kolDeger = []
for i in Adeger:
    r= srHesapla(i,liste,n,yitoplam)
    kolDeger.append(r)

# 1'e En yakın olan kolerasyon değerini döndürür
def bestKolerasyon(liste):
    enBuyuk = max(liste)
    i=1
    while enBuyuk!=liste[i-1]:
        i+=1
    return i,enBuyuk 
index,bestKol = bestKolerasyon(kolDeger)
print("En düşük hatayı veren polinom derecesi:",index)
print("Kolerasyon değeri:",bestKol)
print('\n')
polinom = Adeger[index-1]


def f(x,pol=polinom):
    aKatsayisi = pol
    toplamVeri = 0
    for i in range(len(aKatsayisi)):
        toplamVeri += aKatsayisi[i] * (x ** i)
    return toplamVeri


def polinomlu(n):
    # okul numaramın son rakamı 4
    a= 4
    b = n
    deltax = 0.001
    integral = 0
    size = int((b-a)/deltax)
    for i in range(size):
        integral += deltax*(f(a)+f(a+deltax))/2
        a +=deltax
    print("Polinomlu sonuc:",integral)


def polinomsuz(n,liste):
    # 180401104 (4)
    a = 4
    b = n
    integral = 0
    for i in range(a-1,b-1):
            integral += (liste[i]+ liste[i+1])/2
    print("Polinomsuz sonuc:",integral)

def coment():
    with open("180401104_yorum.txt","w",encoding="utf-8") as coment:
        coment.write("Mert BAYGIN  180401104\n")
        coment.write("Polinomlu ve polinomsuz olarak hesapladığımız integralin farklı sonuç döndürmesinin nedeni, \n")
        coment.write("deltax için belirlediğimiz değerin uzunluğundan kaynaklanmaktadır. Burada deltax değeri hesaplanacak grafiğin \n")
        coment.write("kaç adet alana bölünmesine denk gelir. Deltax değerini ne kadar küçük değer alırsak hesaplanması gereken\n")
        coment.write("alan sayısı artacağından grafik ile alanlar arasındaki boşluklar ve grafiğin dışına taşmalar oldukça azalıcaktır. \n")
        coment.write("Bundan dolayı hesapladığımız değer gerçek değerini çok yaklaşacaktır.\n")
        coment.write("Polinomsuz hesaplama işleminde ise grafiği istediğimiz sayıda alana bölemediğimiz için böldüğümüz alanlar ile\n")
        coment.write("grafik arasında boşluklar ve grafikte taşmalar meydana geliyor bu sebepden dolayı hata oranı artıyor.\n")
        coment.write("Son olarak hesaplamalamarımda'yamuk' metodu kullandım.")

polinomlu(n)
polinomsuz(n,liste)
coment()




