# PELİN AKGÜN 180401050
# data = [1,1,5,6,18,47,98,191,359,670,947,1236,1529,1872,2433,3629,5698,7402,9217,10827,13531,15679,18315,20921,23934,27069,30217,34109,38226]
dosya = open("veriler.txt", "r")
data = []

for i in dosya.read().split():
    data.append(int(i))

n = len(data)
x0_sum = 0
x_sum = 0
y_sum = sum(data)
x2_sum = 0
x3_sum = 0
x4_sum = 0
x5_sum = 0
x6_sum = 0
x7_sum = 0
x8_sum = 0
x9_sum = 0
x10_sum = 0
x11_sum = 0
x12_sum = 0
x0y_sum = 0
xy_sum = 0
x2y_sum = 0
x3y_sum = 0
x4y_sum = 0
x5y_sum = 0
x6y_sum = 0
for i in range(n):
    x0_sum += (i + 1) ** 0
    x_sum += i + 1
    x2_sum += (i + 1) ** 2
    x3_sum += (i + 1) ** 3
    x4_sum += (i + 1) ** 4
    x5_sum += (i + 1) ** 5
    x6_sum += (i + 1) ** 6
    x7_sum += (i + 1) ** 7
    x8_sum += (i + 1) ** 8
    x9_sum += (i + 1) ** 9
    x10_sum += (i + 1) ** 10
    x11_sum += (i + 1) ** 11
    x12_sum += (i + 1) ** 12
    x0y_sum += data[i]
    xy_sum += (i + 1) * data[i]
    x2y_sum += (i + 1) * (i + 1) * data[i]
    x3y_sum += (i + 1)*(i + 1)*(i + 1) * data[i]
    x4y_sum += ((i + 1) ** 4)*data[i]
    x5y_sum += ((i + 1) ** 5) * data[i]
    x6y_sum += ((i + 1) ** 6) * data[i]


kullanilacak_x = [x0_sum, x_sum, x2_sum, x3_sum, x4_sum, x5_sum, x6_sum, x7_sum, x8_sum, x9_sum, x10_sum, x11_sum,
                  x12_sum]
x_sums = [n, x0_sum, x_sum, x2_sum, x3_sum, x4_sum, x5_sum, x6_sum, x7_sum, x8_sum, x9_sum, x10_sum, x11_sum, x12_sum]
xy_sums = [y_sum, x0y_sum, xy_sum, x2y_sum, x3y_sum, x4y_sum, x5y_sum, x6y_sum]
xy_degerleri = [x0y_sum, xy_sum, x2y_sum, x3y_sum, x4y_sum, x5y_sum, x6y_sum]
yi = sum(data)


def gauss(matris):
    n = len(matris)
    for i in range(0, n):
        maxEl = abs(matris[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) > maxEl:
                maxEl = abs(matris[k][i])
                maxRow = k

        for k in range(i, n + 1):
            tmp = matris[maxRow][k]
            matris[maxRow][k] = matris[i][k]
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

# result=[]
# print(cozumlerilistele([1,2,3,4,5,6,7,8,9,10]))

def korelasyonsrstdegerleri(a, data, n, yi):
    sr = 0
    yort = yi / n
    st = 0
    for i in range(n):
        islem = 0
        islem += a[0]
        for j in range(1, len(a)):
            islem += a[j] * (i + 1) ** j
        sr += (data[i] - islem) ** 2
        st += (data[i] - yort) ** 2

    return ((st - sr) / st) ** (1 / 2)


def korelasyondegerlerilistesi(korelasyoncozumleri, data, n, yi):
    r_degerler = []
    for i in korelasyoncozumleri:
        r_degerler.append(korelasyonsrstdegerleri(i, data, n, yi))
    return r_degerler


def enuygunpolinom(korelasyondegerleri, data, n, yi):
    p = korelasyondegerlerilistesi(korelasyondegerleri, data, n, yi)
    tut = 1000
    uygunpolderecesi = 0
    for i in range(len(p)):
        kor = abs(1 - p[i])
        if kor < tut:
            tut = kor
            uygunpolderecesi = i+1
    return uygunpolderecesi

def polinomkatsayilistesi():
    katsayilistesi = []
    for i in range(2, 8):
        x_lervey_lerlistesi = []
        for j in range(i):
            x_lervey_lerlistesi.append([])
            for k in range(i):
                x_lervey_lerlistesi[j].append(kullanilacak_x[k + j])
            x_lervey_lerlistesi[j].append(xy_degerleri[j])
            if j == i - 1:
                katsayilistesi.append(gauss(x_lervey_lerlistesi))
                x_lervey_lerlistesi.clear()
    return katsayilistesi

with open("180401050_yorum.txt", "w", encoding='UTF8') as f:
    f.write("Polinomlu integral ve polinomsuz hesaplanan integral arasındaki farkın sebebi deltax dir.Polinomsuz olanda deltax i 1 aldığımız için gerçeğe daha uzak sonuç verir.")


def f(x):
    fx = 0
    z = 0
    p = enuygunpolinom(polinomkatsayilistesi(), data, n, yi)
    for k in polinomkatsayilistesi():
        if len(k) == p + 1:
            for i in range(p + 1):
                fx = fx + k[z]*(x ** i)
                z += 1
            # print(fx)
            return (fx)


def yazdirma():
    print("Polinom =", enuygunpolinom(polinomkatsayilistesi(), data, n, yi),
          ". derecedendir.")


yazdirma()


def polinomlu_integral():
    a = 10 # okul numaramın son rakamı 0 olduğu için (180401050) 10 aldım
    b = len(data)
    deltax = 0.1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n):
        integral += deltax * (f(a) + f(a + deltax)) / 2
        a += deltax
    print("Polinomlu Integral Değeri : ", integral)


polinomlu_integral()


def polinomsuz_integral():
    a = 10  #okul numaramın son rakamı 0 olduğu için (180401050) 10 aldım
    b = len(data)
    deltax = 1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n-1):
        integral = integral + deltax * ((data[a]) + (data[a + deltax])) / 2
        a = a + deltax
    print("Polinomsuz Integral Değeri : ", integral)


polinomsuz_integral()
