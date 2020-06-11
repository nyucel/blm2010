
# 160401039 Belkız Kuş
# Sayısal Yöntemler

# formül => w(katsayılar matrisi) = ((X(t)*X)**-1)*X(t)*Y
# formül için kaynak: https://www.youtube.com/watch?v=nGcMl03LPC0

def polyfit(arrX, arrY, deg):
    xMatris = createXmatris(arrX, deg)
    yMatris = createYmatrix(arrY)
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


def createYmatrix(arrY):
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
def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixDeternminant(m):
    # 2x2 matris:
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


def getMatrisInverse(m):
    determinant = getMatrixDeternminant(m)
    #2x2 matris:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # matris kofaktörü:
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = matrisTranspoz(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def hataHesapla(arrX, arrY, katsayilarMatrisi):
    hataPayı = 0
    for i in range(len(arrX)):
        estimatedY = 0
        for j in range(len(katsayilarMatrisi)):
            estimatedY += katsayilarMatrisi[j][0] * arrX[i] ** j
        hataPayı += abs(estimatedY - arrY[i])
    return hataPayı  # toplam hata payını döndürür


def grupOlustur(liste):
    grupListe = []
    x = int(len(liste) / 10)
    a, b = 0, 0
    for i in range(x):
        a = (i + 1) * 10
        b = i * 10
        temp = []
        for j in range(b, a, 1):
            temp.append(liste[j])
        grupListe.append(temp)
    return grupListe


def main():
    arrY = []
    # dosyadan veri okuma
    dosya = open('Veriler.txt', 'r')
    for satir in dosya:
        arrY.append(int(satir))
    dosya.close()
    arrX = [i + 1 for i in range(len(arrY))]

    hataPayıDict = {}
    for i in range(1, 7):
        katsayilarMatrisi = polyfit(arrX, arrY, i)
        with open("sonuc.txt", "a") as f:
            f.write("{}. derece polinomun katsayıları: \n{}\n\n".format(i,katsayilarMatrisi))
        hataPayı = hataHesapla(arrX, arrY, katsayilarMatrisi)
        hataPayıDict[i] = hataPayı

    minPolinom = min(hataPayıDict, key=lambda k: hataPayıDict[k])
    with open("sonuc.txt", "a") as f:
        f.write("Tüm veriler için en az hata payı olan polinom {}. polinomdur. Hata payı: {} \n\n".format(minPolinom,hataPayıDict[minPolinom]))


    # 10 lu veri grupları için
    grup = grupOlustur(arrY)
    for i in range(len(grup)):
        hataPayıGrup = {}
        newArrX = []
        newArrY = []
        for j in range(len(grup[i])):
            newArrX.append((i * 10) + j + 1)
            newArrY.append(grup[i][j])
        for d in range(1, 7):
            katsayılar = polyfit(newArrX, newArrY, d)
            hata = hataHesapla(newArrX, newArrY, katsayılar)
            hataPayıGrup[d] = hata
        minPolinomGrup = min(hataPayıGrup, key=lambda k: hataPayıGrup[k])
        with open("sonuc.txt", "a") as f:
            f.write("{} - {} arasındaki veriler için uygun polinom derecesi = {}\nHata payı: {}\n\n".format(newArrX[0],newArrX[-1],minPolinomGrup,hataPayıGrup[minPolinomGrup]))


if __name__ == "__main__":
    main()

