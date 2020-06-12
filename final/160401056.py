import math
def yorumyap():
    with open ("160401056_yorum.txt","w") as dosya:
        dosya.write("Batuhan Şahin 160401056.\n")
        dosya.write("3. ve 4. maddelerde farklı sonuç çıkma sebebi deltax değeridir.Deltax parçaladığımız parçaların enini ifade eder.\n")
        dosya.write("Deltax azaldığı zaman parçaların alanı artıyor\n")
        dosya.write("Polinomlu integral hesabında deltax az olduğu zaman alan artıyor ve bulduğumuz değer gerçek değerine yakınlaşıyor\n")
        dosya.write("Polinomsuz integral hesabında deltax değeri değişmiyor alan değerimiz aynı kalıyor bu nedenle hata payı artıyor\n ")

file=open("veriler.txt","r",encoding='utf-8')
veriler_=[]
for i in file.read().split():
    veriler_.append(int(i))
file.close()
length = len(veriler_)
bsum = sum(veriler_)
yorumyap()



def xdegerleritoplam(length):
    xüssü2toplam = []
    xüssü2toplam.append(length)
    for x in range(1, 13):
        i = 0
        for j in range(length):
            i += (j + 1) ** x
        xüssü2toplam.append(i)
    return xüssü2toplam



def xydegerlertoplami(a, b):
    xydeğerleri = []
    xydeğerleri.append(sum(b))
    for i in range(1, 7, 1):
        k = 0
        for j in range(a):
            k += (j + 1) ** i * b[j]
        xydeğerleri.append(k)
    return xydeğerleri



def matris_olustur(a, b, x):
    a_ = xdegerleritoplam(a)
    b_ = xydegerlertoplami(a, b)
    matrix = []
    degistir = 0
    for i in range(0, x):
        olusan = []
        for i in range(degistir, x + degistir):
            olusan.append(a_[i])
        olusan.append(b_[degistir])
        degistir += 1
        matrix.append(olusan)
    return matrix



def gausyöntemi(G):
    t = len(G)

    for i in range(0, t):

        for q in range(i + 1, t):
            A = -G[q][i] / G[i][i]
            for w in range(i, t + 1):
                if i == w:
                    G[q][w] = 0
                else:
                    G[q][w] += A * G[i][w]

        eniyi = abs(G[i][i])
        eniyirow = i
        for q in range(i, t + 1):
            tut = G[eniyirow][q]
            G[eniyirow][q] = G[i][q]
            G[i][q] = tut

        for q in range(i + 1, t):
            if abs(G[q][i]) > eniyi:
                eniyi = abs(G[q][i])
                eniyirow = q



    m = [0 for i in range(t)]
    for i in range(t - 1, -1, -1):
        m[i] = G[i][t] / G[i][i]
        for q in range(i - 1, -1, -1):
            G[q][t] -= G[q][i] * m[i]
    return m



def matris(liste):
    matriss = []
    for i in range(2, 8):
        matriss.append(gausyöntemi(matris_olustur(len(veriler_), veriler_, i)))
    return matriss


matrix = matris(veriler_)



def Kolerasyon(x, liste, n):
    sr = 0
    st = 0
    yToplam = sum(liste)
    y = yToplam / n
    size = len(x)
    for i in range(n):
        temp = 0
        for j in range(size):
            if j == 0:
                temp += x[j]
            else:
                temp += x[j] * (i + 1) ** j
        sr += (liste[i] - temp) ** 2
        st += (liste[i] - y) ** 2
    r = ((st - sr) / st) ** (1 / 2)
    return r


dizi = []
for i in range(0, 6):
    x = Kolerasyon(matrix[i], veriler_, length)
    dizi.append(x)




def Kolerasyon_(r):
    a = max(r)
    i = 1
    while (a != r[i - 1]):
        i += 1
    return i


import math
from sympy import Symbol

for i in range(1):
    x = Symbol('x')

    pol = matrix[Kolerasyon_(dizi) - 1]
    denklem = (pol[0] + pol[1] * x + pol[2] * x ** 2 + pol[3] * x ** 3 + pol[4] * x ** 4 + pol[5] * x ** 5 + pol[
        6] * x ** 6)
    print("Polinom denklemi", denklem)

    a, b = 7, len(veriler_)
    integral = 0
    x = 0.1
    n = int((b - a) / x)
    for j in range(n):
        integral += x * (denklem.subs({x: a}) + denklem.subs({x: a + x})) / 2
        a += x
    print("Polinomlu integral sonucu:", integral)


def integrall(verilerr):
    a = 7
    b = len(verilerr)
    x = 1
    inte = 0
    n = int((b - a) / x)
    for i in range(n - 1):
        inte += x * (verilerr[a] + verilerr[a + x]) / 2
        a += x
    return inte

print("integral sonucu : ", integrall(veriler_))
