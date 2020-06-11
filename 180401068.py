#Emirhan Akman 180401068

def matrisOlus(matrisHesapla):
    list = matrisHesapla.copy()
    satir = len(matrisHesapla)
    sutun = len(matrisHesapla[0])

    for i in range(satir-1):
        for j in range(satir-1-k):
            carp = list [j][i]/list[j+1][i]
            for k in range(sutun):
                list [j][k] += -carp * list[j+1][k]

    for a in range(satir-1,0,-1):
        for s in range(satir-1,satir-1-a,-1):
            carp= list[s][a]/list[s-1]/[a]
            for d in range(sutun):
                list[s][d] += -carp* list[s-1][d]
    result = []
    for l in range(satir-1,-1,-1):
        x= list[l][satir]/list[l][satir-l-1]
        result.append(x)
    return result

with open("veriler.txt","r",encoding='utf-8') as file:
    liste = []
    for i in file.read().split():
        liste.append(int(i))

def boyut(liste):
    return len(liste)
n = boyut(liste)

def yTop(liste):
    x=sum(liste)
    return x
yitoplam= yTop(liste)

def xiTop(n):
    xikiTop= []
    for k in range(1,13,1):
        xiki =0
        for l in range(n):
            xiki += (i+1)**j
        xikiTop.append(xiki)
    xikiTop.insert(0,n)
    return xikiTop

def xDereceTop(n,liste,yTop):
    xDerece_top = []
    for i in range(1,7,1):
        value = 0
        for j in range(n):
            value += (j+1)**i*liste[j]
        xDerece_top.append(value)
    xDerece_top.insert(0,yTop)
    return xDerece_top


def aValues(n,liste,m=8):
    result= []
    xikiTop=xiTop()
    y=yTop(liste)
    xDerece_top = xDereceTop(n,liste,y)
    for x in range(2,m,1):
        newListe= []
        for i in range(x):
            newListe.append([])
            for j in range(x):
                newListe[i].append(xikiTop[j+i])
            newListe[i].append(xDerece_top[i])
            if i == x-1:
                result.append(matrisOlus(newListe))
                newListe.clean()
    return result
Adeger = aValues(n,liste)

def srHesap(x,liste,n,yTop):
    sr=0
    st=0
    y=yTop/n
    boyut= len(x)
    for i in range(n):
        temp=0
        for j in range(boyut):
            if j==0:
                temp += x[j]
            else:
                temp += x[j]*(i+1)**j
        sr += (liste[i]-temp)**2
        st += (liste[i]-y)**2
    r = ((st - sr) / st) ** (1 / 2)
    return r
corValue = []
for i in Adeger:
    r = srHesap(i,list,n,yitoplam)
    corValue.append(r)

def bestCorrelation(liste):
    theBiggest = max(liste)
    i=1
    while theBiggest!=liste[i-1]:
        i+=1
    return i,theBiggest

index,bestCor= bestCorrelation(corValue)
print("En düşük hatayı veren polinom derecesi:",index)
print("Kolerasyon değeri:",bestCor)
print('\n')
polinom = Adeger[index-1]

def fonk(x,pol=polinom):
    aKatsayisi = pol
    topVeri=0
    for i in range(len(aKatsayisi)):
        topVeri += aKatsayisi[i]* (x ** i)
    return topVeri

def polinomlu(n):
    #numaramın son rakamı 8, 180401068
    a= 8
    b=ndeltax = 0.001
    integral=0
    boyut = int((b-a)/deltax)
    for i in range(boyut):
        integral += deltax*(fonk(a)+fonk(a+deltax))/2
        a+= deltax
    print("Polinomlu sonuc:",integral)

def polinomsuz(n,liste):
    a=8
    b=n
    integral =0
    for i in range(a-1,b-1):
        integral += (liste[i]+ liste[i+1])/2
    print("Polinom olmadan sonuc",integral)

def yorum():
    with open("180401068_yorum.txt","w",encoding="utf-8")as yorum:
        yorum.write("Emirhan Akman 180401068\n")
        yorum.write("Polinomlu ve polinomsuz hesaplanmış integraller farklı sonuclar verir. \n")
        yorum.write("Bunun nedeni delta x için belirlediğimiz değerin uzunluğundandır.\n")
        yorum.write("Delta x in degeri , hesaplanacak grafigin kac adet alana bölünecegini isaret eder.\n")
        yorum.write("Delta x'i ne kadar küçük alırsak hesaplanması gereken alan sayısı o kadar artacagından\n")
        yorum.write("Grafik ve alan arasubdaki bosluk ve grafik dısına tasmalar azalacaktır.\n")
        yorum.write("Boylece hesapladıgımız deger, reel degerine olabildigince cok yaklasır.\n")
        yorum.write("Polinomsuz hesaplamada ise grafigi böldügümüz alanı kendimiz belirlemedigimiz icin,\n")
        yorum.write("boldugümüz alanlar ile grafik arasında tasmalar olusur, böylece hata artar\n")



