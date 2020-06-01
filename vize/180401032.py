
# Yasemin Arslan
# 180401032

file = open("veriler.txt", "r", encoding="utf-8")
verilerliste = []
for x in file:
    verilerliste.append((int(x)))
len_veriliste = len(verilerliste)
file.close()

def toplamlari(min, max, kuvvet):
    toplam = 0
    for k in range(min, max+1):
        toplam = toplam + (k ** kuvvet)
    return toplam

def gauss(matris):
    n = len(matris)
    for i in range(0, n):
        maxEl = abs(matris[i][i])
        sira = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) > maxEl:
                maxEl = abs(matris[k][i])
                sira = k
        for k in range(i, n + 1):
            tmp = matris[sira][k]
            matris[sira][k] = matris[i][k]
            matris[i][k] = tmp
        for k in range(i + 1, n):
            c = -matris[k][i] / matris[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matris[k][j] = 0
                else:
                    matris[k][j] += c * matris[i][j]
            x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * x[i]
    return x

def xy_toplam(verilerliste, derece, deger):
    toplamxy = 0
    for y in range(0, len(verilerliste)):
        toplamxy = toplamxy + verilerliste[y] * ((y + deger) ** derece)
    return toplamxy

def matris(veri, xbasla):
    kat = []
    basla = 0
    lenx = len(veri)
    for i in range(1, 6):
        matris = []
        for k in range(i + 1):
            satir = []
            for j in range(i + 1):
                if k == 0 and j == 0:
                    satir.append(lenx)
                else:
                    t = lenx - basla
                    satir.append(toplamlari(1, t, j + k))
            satir.append(xy_toplam(veri, k, xbasla))
            matris.append(satir)
        kat.append(gauss(matris))
    return kat


dosya = open('sonuc.txt', 'w')
derece = 1
for i in matris(verilerliste, 1):
    dosya.write(" Derecesi " + str(derece) + " olan polinomun katsayilari" + str(i) + "\n")
    derece = derece + 1


