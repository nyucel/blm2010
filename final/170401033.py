#Göksel AKTAŞ 170401033

import sympy as sym
import math

x = sym.Symbol('x')
values = []
korelasyonlar = []

def veriokuma():
    with open("veriler.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            values.append(int(line))



def Gauss(A):                             
    size = len(A)
    for i in range(0, size):
        maxCol = abs(A[i][i])
        maxRow = i
        for j in range(i + 1, size):
            if abs(A[j][i]) > maxCol:
                maxCol = abs(A[j][i])
                maxRow = j
        for k in range(i, size + 1):
            temp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = temp
        for t in range(i + 1, size):
            c = -A[t][i] / A[i][i]
            for j in range(i, size + 1):
                if i == j:
                    A[t][j] = 0
                else:
                    A[t][j] += c * A[i][j]

    matrix = [0 for i in range(size)]

    for i in range(size - 1, -1, -1):
        matrix[i] = A[i][size] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][size] -= A[k][i] * matrix[i]
    return matrix

def korelasyon(myLastResults, first, last):
    n = last - first
    yi = 0
    for i in range(first, last):
        yi += values[i]
    y_ussu = yi / n
    Sr = 0
    for i in range(first, last):
        Sr = (myLastResults[i - first] - values[i]) ** 2 + Sr
    St = 0
    for i in range(first, last):
        St = St + (values[i] - y_ussu) ** 2
    rSquare = abs((St - Sr) / St)
    r = math.sqrt(rSquare)
    return r



def degerbul(first, last):  
    arrayForValues = []
    n = last - first
    for derece in range(1, 7):
        xdegerleri = []
        for i in range(n):
            xdegerleri.append(i + 1)
        matrix = [[0 for i in range(derece + 1)] for j in range(derece + 1)]
        size = len(matrix)
        for i in range(size):
            for j in range(size):
                xSums = 0
                for k in range(n):
                    matrix[0][0] = len(xdegerleri)
                    xSums = xdegerleri[k] ** (i + j) + xSums
                    matrix[i][j] = xSums

        xyResults = []
        for i in range(size):
            sum = 0
            for j in range(first, last):
                sum = sum + (values[j] * (xdegerleri[j - first] ** i))
            xyResults.append(sum)           
        k = 0
        for i in matrix:
            i.append(xyResults[k])
            k = k + 1
        katsayilar = Gauss(matrix)
        myResultsArray = []
        for i in range(n):
            sum = 0
            for j in range(len(katsayilar)):
                sum = sum + katsayilar[j] * ((i + 1) ** j)
                if j == derece:
                    myResultsArray.append(int(sum))
        r = korelasyon(myResultsArray, first, last)
        arrayForValues.append(r)
    best = 100
    index = 0
    for i in range(len(arrayForValues)):
        temp = abs(1 - arrayForValues[i])

        if temp < best:
            best = temp
            index = i + 1
    print("En uygun dereceli polinomun derecesi:  ", index) 
    polinomlu(index, 0, len(values))

def polinomlu(derece, first, last):
    n = last - first
    xdegerleri = []
    for i in range(n):
        xdegerleri.append(i + 1)

    matrix = [[0 for i in range(derece + 1)] for j in range(derece + 1)]
    size = len(matrix)

    for i in range(size):
        for j in range(size):
            xSums = 0
            for k in range(n):
                matrix[0][0] = len(xdegerleri)
                xSums = xdegerleri[k] ** (i + j) + xSums
                matrix[i][j] = xSums

    xyResults = []
    for i in range(size):
        sum = 0
        for j in range(first, last):
            sum = sum + (values[j] * (xdegerleri[j - first] ** i))
        xyResults.append(sum)

    k = 0
    for i in matrix:
        i.append(xyResults[k])
        k = k + 1
    katsayilar = Gauss(matrix)
    if len(katsayilar) < 7:
        while len(katsayilar) != 7:
            katsayilar.append(0)

    print("Polinom Denklemi Sonucu: \n")               
    equation = katsayilar[6] * x ** 6 + katsayilar[5] * x ** 5 + katsayilar[4] * x ** 4 + \
               katsayilar[3] * x ** 3 + katsayilar[2] * x ** 2 + \
               katsayilar[1] * x + katsayilar[0]

    print(equation)
    
    integral = 0
    a = 3 #170401033 
    b = len(values)
    deltax = 0.1
    n = int((b - a) / deltax)
    for i in range(n):
        integral += deltax * (equation.subs({x: a}) + equation.subs({x: a + deltax})) / 2
        a += deltax
    print("Integral Sonucu : ", integral)


def polinomsuz():
    integral = 0
    a = 3  #170401033
    b = len(values)
    deltax = 1
    n = int((b - a) / deltax)
    for i in range(n - 1):
        integral += deltax * (values[a] + values[a + deltax]) / 2
        a += deltax
    print("Polinomsuz Integral Sonucu: ", integral)


with open("170401033_yorum.txt","w") as f:
    f.write(" Göksel AKTAŞ 170401033\n")
    f.write("Polinomlu ve polinomsuz integral hesaplamalarında birbirinden farklı sonuçlar almamızın nedeni\n")
    f.write("delta x için belirlenen değerin uzunluğu ve elimizdeki verilerin belirlenen derecelerdeki polinoma %100 uygun olmadığından kaynaklanmaktadır.\n")
    f.write("Eğer elimizdeli veriler hatasız bir şekilde polinomumuza uysaydı ve 2 integral hesabında da deltaxi 1 alsaydık aynı sonuca ulaşabilirdik.\n")

veriokuma()
degerbul(0, len(values))
polinomsuz()