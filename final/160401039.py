
# 160401039 Belkız Kuş
# Sayısal Yöntemler

def polyfit(arrX, arrY, deg):
    xMatris = createXmatris(arrX, deg)
    yMatris = createYmatris(arrY)
    xTranspoz = matrisTranspoz(xMatris)
    kareMatris = matrisCarpimi(xTranspoz, xMatris)
    inverseKareMatris = getMatrisInverse(kareMatris)
    yCarpim = matrisCarpimi(xTranspoz, yMatris)
    katsayilarMatrisi = matrisCarpimi(inverseKareMatris, yCarpim)
    return katsayilarMatrisi


def createXmatris(arrX, deg):
    n = len(arrX)
    xMatris = []
    for i in range(n):
        xMatris.append([])
        for j in range(deg + 1):
            xMatris[i].append(arrX[i] ** j)
    return xMatris


def createYmatris(arrY):
    n = len(arrY)
    yMatris = []
    for i in range(n):
        yMatris.append([])
        yMatris[i].append(arrY[i])
    return yMatris


def matrisTranspoz(arr):
    transpozMatris = []
    for i in range(len(arr[0])):
        transpozMatris.append([])
        for j in range(len(arr)):
            transpozMatris[i].append(arr[j][i])
    return transpozMatris


def matrisCarpimi(m1, m2):
    r, m = [], []
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            toplam = 0
            for k in range(len(m2)):
                toplam += (m1[i][k] * m2[k][j])
            r.append(toplam)
        m.append(r)
        r = []
    return m


# matris tersini alma fonksiyonları
def getMatrisMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrisDeternminant(m):
    # 2x2 matris:
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrisDeternminant(getMatrisMinor(m, 0, c))
    return determinant


def getMatrisInverse(m):
    determinant = getMatrisDeternminant(m)
    #2x2 matris:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # matris kofaktörü:
    kofaktorler = []
    for r in range(len(m)):
        kofaktor_satir = []
        for c in range(len(m)):
            minor = getMatrisMinor(m, r, c)
            kofaktor_satir.append(((-1) ** (r + c)) * getMatrisDeternminant(minor))
        kofaktorler.append(kofaktor_satir)
    kofaktorler = matrisTranspoz(kofaktorler)
    for r in range(len(kofaktorler)):
        for c in range(len(kofaktorler)):
            kofaktorler[r][c] = kofaktorler[r][c] / determinant
    return kofaktorler

def listeyap(a):
    b = []
    for i in range (len(a)):
        b.append(a[i][0])
    return b


def korelasyonHesapla(veriler,katsayi):
    ortx = 0
    for i in range (len(veriler)):
        ortx += veriler[i]

    ortx= (ortx/len(veriler))

    tempx= 0
    tempy= 0

    for i in range (len(veriler)):
        x=veriler[i]
        tempx += ((veriler[i]-ortx)**2)
        for k in range(len(katsayi)):
	        x -= katsayi[k]*(i+1)**k
        x=x**2
        tempy += x
    korelasyon = ((tempx-tempy)/tempx)**(1/2)
    return korelasyon

def enUygun(r_list):
    temp = 0
    for i in r_list:
        if(i>temp):
            temp = i
    return temp

# en uygun polinom kullanılarak bulunan interal
def polinomluİntegral(liste,katsayi):

    def f(x, p=katsayi):
        return (p[0] + p[1] * x + p[2] * x ** 2 + p[3] * x ** 3 + p[4] * x ** 4 + p[5] * x ** 5 + p[6] * x ** 6)
    a=9   #160401039
    b=len(liste)
    deltax = 0.1
    integral = 0
    n = int((b - a)/deltax)
    for i in range(n):
        integral += deltax * (f(a) + f(a+ deltax)) / 2
        a += deltax
    return integral

# veriler.txt dosyasındaki veriler kullanılarak bulunan integral
def polinomsuzİntegral(liste):
    a=9    #160401039
    b=len(liste)
    deltax=1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n-1):
        integral += deltax * (liste[a] + liste[a + deltax]) / 2
        a += deltax
    return integral

def main():
    arrY = []
    # dosyadan veri okuma
    dosya = open('veriler.txt', 'r')
    for satir in dosya:
        arrY.append(int(satir))
    dosya.close()
    arrX = [i + 1 for i in range(len(arrY))]

    c = []  #katsayiları bulunduracak liste
    r_deger = []  #bütün korelasyon r değerleri

    for i in range(1, 7):
        katsayilarMatrisi = polyfit(arrX, arrY, i)
        katsayi_liste = listeyap(katsayilarMatrisi)
        r = korelasyonHesapla(arrY, katsayi_liste)
        r_deger.append(r)
        c.append(katsayi_liste)

    r_uygun = enUygun(r_deger)   #uygun r değeri
    pol_derece = (r_deger.index(r_uygun))+1   #uygun polinom derecesi
    print("Tüm veriler için korelasyona göre en uygun polinom {}. polinomdur. Korelasyon: {} \n".format((r_deger.index(r_uygun))+1,enUygun(r_deger)))
    print("Polinomlu integral:", polinomluİntegral(arrY,c[pol_derece-1]))
    print("Polinomsuz integral:", polinomsuzİntegral(arrY))

    with open("160401039_yorum.txt", "a") as f:
        f.write("Polinom kullanılarak hesaplanan integral ile polinomsuz hesaplanan integral değeri birbirinden farklıdır.\n\n"
                "Polinom ile hesaplanan integralde veriler.txt dosyasındaki veriler sırasıyla 1.,2.,3.,4.,5.,6. dereceden polinomlara\n"
                "yaklaştırılmış ve korelasyon değerlerine göre en uygun polinom bulunmuştur. Bu polinom Yamuk Yöntemi kullanılarak\n"
                "a=9 b=82 aralığında yüksekliği 0.1 olan yamuklara bölünmüştür.Bu yamukların alanlarının toplanmasıyla integral\n"
                "değeri bulunur. Gerçeğe en yakın sonucun bulanabilmesi, yani daha az taşma ve daha az hata için deltax(yamukların\n"
                "yüksekliği)'e sıfıra yakın değer verilir.\n\n"
                "Polinomsuz hesaplanan integralde ise veriler.txt dosyasındaki veriler direkt kullanılarak integral hesaplanmıştır.\n"
                "Elimizde ara değerler olmadığı için deltax 1 olarak alınmıştır.\n\n"
                "Bu iki integral değerinin farklı olmasının sebebi ise polinom ile hesaplanan integralde gerçek değerlerle değil\n"
                "verilerle yakınlaştırılmış ve korelasyon değerine göre en az hata ile uyan değerlerle oluşturulmuş polinomu\n"
                "kullanmamızdır. Bu nedenle her iki deltax'i eşit aldığımızda bile sonuçların farklı çıktığı görülmüştür.\n")


if __name__ == "__main__":
    main()

