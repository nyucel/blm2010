# MERT BAYGIN 180401104


# nxn matris hespalama
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

#Corona günlük veriler            
with open("veriler.txt","r",encoding='utf-8') as file:
    liste = [] 
    for i in file.read().split():
        liste.append(int(i))

n = len(liste) 

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

def bestKolerasyon(liste): # 1'e En yakın olan kolerasyon değerini döndürür
        sirala = sorted(liste)
        enBuyuk = sirala[-1]
        i=1
        while enBuyuk!=liste[i-1]:
            i+=1
        return i,enBuyuk 

# 10 lu gruplar için hesaplama
def grups(liste):
    grupListe=[]
    x = int(len(liste)/10)
    a,b = 0,0
    for i in range(x):
        a = (i+1)*10
        b = i*10
        temp = []
        for j in range(b,a,1):
            temp.append(liste[j])
        grupListe.append(temp)
    return grupListe



with open("sonuc.txt","a",encoding='utf-8') as file2:
    file2.write("Tüm veriler için :"+'\n')
    for i in Adeger:
        file2.write(str(len(i)-1)+".Derece"+"\n")
        for j in i:
            file2.write(str(j)+'\n')
        x = srHesapla(i,liste,n,yitoplam)
        file2.write("Kolerasyon:"+str(x)+'\n')
        file2.write('\n')
    file2.write("Tüm veriler için en uygun Polinom Grafiği  1'e en yakın olan 6. Derece Polinom:"+str(x)+'\n'+'\n')

    #Bu kısımdan itibaren 10lu değerler yazdırılıyor
    grup = grups(liste)
    newVal = 0
    for o in grup:
        Kolerasyons = []
        file2.write(str(newVal*10)+'-'+str((newVal+1)*10-1)+' aralığındaki veriler için:'+'\n')
        yeniDeger = aDegerleri(len(o),o)
        for p in yeniDeger:
            file2.write(str(len(p)-1)+".Derece"+"\n")
            for r in p:
                 file2.write(str(r)+'\n')
            s=srHesapla(p,o,len(o),sum(o))
            Kolerasyons.append(s)
            file2.write("Kolerasyon:"+str(s)+'\n')
            file2.write('\n')
        index,bestKol = bestKolerasyon(Kolerasyons)
        file2.write(str(newVal*10)+'-'+str((newVal+1)*10-1)+" verileri arasında 1'e yakın olan "+str(index)+".Derece Polinom:"+str(bestKol)+'\n'+'\n')    
        newVal +=1
