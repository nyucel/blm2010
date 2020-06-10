#Berkay Yanýk 180401070

f = open("veriler.txt","r")
liste = []
for i in f.read().split():
    liste.append(int(i))

b = len(liste)

def xitoplam(b):
    xidizi = []
    xidizi.append(b)
    for i in range(1,13):
        xi = 0
        for j in range(b):
            xi = xi+(j+1)**i
        xidizi.append(xi)
    return xidizi

def xiyitoplam(b,liste):
    yitoplam = sum(liste)
    xyidizi = []
    xyidizi.append(yitoplam)
    for i in range(1,7):
        yi = 0
        for j in range(b):
            yi = yi+(j+1)**i*liste[j]
        xyidizi.append(yi)
    return xyidizi

def matrishesaplama(matris):
    n = len(matris)
    for i in range(0, n):
        max = abs(matris[i][i])
        satir = i
        for j in range(i + 1, n):
            if abs(matris[j][i]) > max:
                max = abs(matris[j][i])
                satir = j
        for k in range(i, n + 1):
            tmp = matris[satir][k]
            matris[satir][k] = matris[i][k]
            matris[i][k] = tmp
        for y in range(i + 1, n):
            c = -matris[y][i] / matris[i][i]
            for r in range(i, n + 1):
                if i == j:
                    matris[y][r] = 0
                else:
                    matris[y][r] += c * matris[i][r]
    sonuc = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        sonuc[i] = matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * sonuc[i]
    return sonuc

def matris(b,liste,poliderece):
    x = xitoplam(b)
    y = xiyitoplam(b,liste)
    matris = []
    satir = 0
    for i in range(0,poliderece):
        satirekle=[]
        for i in range(satir,poliderece+satir):
            satirekle.append(x[i])
        satirekle.append(y[satir])
        satir+=1
        matris.append(satirekle)
    return matris


def matriscagir(b,liste):
    x = []
    for i in range(2,8):
        x.append(matrishesaplama(matris(b,liste,i)))
    return x

matris1 = matriscagir(b,liste)

def kolerasyon(matris,liste,n):
    sr = 0
    st = 0
    y = sum(liste)/n
    for i in range(n):
        gecici = 0
        for j in range(len(matris)):
            if j == 0:
                gecici += matris[j]
            else:
                gecici += matris[j]*(i+1)**j
        sr +=(liste[i]-gecici)**2
        st +=(liste[i]-y)**2
    r = ((st-sr)/st)**(1/2)
    return r

hesaplama = []
for i in range(len(matris1)):
    x = kolerasyon(matris1[i],liste,b)
    hesaplama.append(x)
print(hesaplama)

eniyihesap = sorted(hesaplama)
derecehesap = []
x = kolerasyon(matris1[i],liste,b)
for i in range(1,6):
    derecehesap.append(x)
eniyiderece = sorted(derecehesap)

with open("sonuc.txt","a") as file:
    sayac = 1
    for j in matris1:
        x= len(j)
        file.write(str(sayac)+".Derece"+'\n')
        for y in range(x):
            file.write(str(j[y])+'\n')
        file.write("Hata payi:"+str(eniyihesap[sayac-1])+'\n')
        sayac +=1
        file.write('\n')
    file.write("En dusuk hata payli derece:"+str(len(eniyiderece)+1)+'\n')
    file.write("Hepsi icin en iyi hata payi:"+str(eniyihesap[-1])+'\n')
    