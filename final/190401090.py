import sympy as sym
import math

sym.init_printing()
x = sym.Symbol('x')                                 #Günlük hayattaki yazım şekli için x'e sembol tanımlaması yapıyoruz.
values = []                                         #Polinom denklemleri yazdırılırken kullancağız.
correlations = []                                   #Değerler ve koreleasyonlar için dizi tanımlamaları.


def readFile():

    file = open('veriler.txt', 'r')                 #veriler.txt dosyasından değerler satır satır çekilir.
    for row in file:
        values.append(int(row))
    file.close()


def correlation(myLastResults, ilk, son):

    n = son - ilk
    yi = 0

    for i in range(ilk, son):
        yi += values[i]

    y_exponent = yi / n
    Sr = 0

    for i in range(ilk, son):
        Sr = (myLastResults[i - ilk] - values[i]) ** 2 + Sr

    St = 0

    for i in range(ilk, son):
        St = St + (values[i] - y_exponent) ** 2

    rSquare = abs((St - Sr) / St)
    r = math.sqrt(rSquare)

    return r


def matrixWithGauss(Z):                             #Gauss yöntemiyle matrisle hesaplama.

    size = len(Z)

    for i in range(0, size):

        maxColumn = abs(Z[i][i])
        maxRow = i

        for j in range(i + 1, size):
            if abs(Z[j][i]) > maxColumn:
                maxColumn = abs(Z[j][i])
                maxRow = j

        for k in range(i, size + 1):
            temp = Z[maxRow][k]
            Z[maxRow][k] = Z[i][k]
            Z[i][k] = temp

        for t in range(i + 1, size):
            c = -Z[t][i] / Z[i][i]

            for j in range(i, size + 1):

                if i == j:
                    Z[t][j] = 0
                else:
                    Z[t][j] += c * Z[i][j]

    matrix = [0 for i in range(size)]

    for i in range(size - 1, -1, -1):
        matrix[i] = Z[i][size] / Z[i][i]

        for k in range(i - 1, -1, -1):
            Z[k][size] -= Z[k][i] * matrix[i]

    return matrix


def findValues(ilk, son):  #6. dereceye kadar her derece hesaplanır ve en iyi derece bunların arasından seçilir.

    arrayForValues = []
    n = son - ilk

    for degree in range(1, 7):
        xValues = []

        for i in range(n):
            xValues.append(i + 1)

        matrix = [[0 for i in range(degree + 1)] for j in range(degree + 1)]        #Matris oluşturulur.
        size = len(matrix)

        for i in range(size):
            for j in range(size):

                xSums = 0

                for k in range(n):

                    matrix[0][0] = len(xValues)
                    xSums = xValues[k] ** (i + j) + xSums
                    matrix[i][j] = xSums         # y*x , y*x^2 vb. x'in üssü artacak şekilde diğer değerler de bulunur.

        xyResults = []

        for i in range(size):
            sum = 0
            for j in range(ilk, son):
                sum = sum + (values[j] * (xValues[j - ilk] ** i))
            xyResults.append(sum)           # Sonuçlar, oluşturduğumuz matrisin en son sütünlarına atılır.

        k = 0

        for i in matrix:
            i.append(xyResults[k])
            k = k + 1

        coefficients = matrixWithGauss(matrix)
        myResultsArray = []

        for i in range(n):
            sum = 0

            for j in range(len(coefficients)):
                sum = sum + coefficients[j] * ((i + 1) ** j)

                if j == degree:
                    myResultsArray.append(int(sum))

        r = correlation(myResultsArray, ilk, son)
        arrayForValues.append(r)

    best = 100
    index = 0

    for i in range(len(arrayForValues)):
        temp = abs(1 - arrayForValues[i])

        if temp < best:
            best = temp
            index = i + 1

    print("Polinomlar arasında en iyi dereceli polinom:  ", index) #Hesaplanan polinomlar arasındaki değeri en iyi olan derecedeki polinom'un hangisi olduğu yazdırılır.
    wroteBestIntegralAndPolynom(index, 0, len(values))


def wroteBestIntegralAndPolynom(degree, ilk, son):              #En iyi polinom ve integral değeri burada bulunur.

    n = son - ilk
    xValues = []

    for i in range(n):
        xValues.append(i + 1)

    matrix = [[0 for i in range(degree + 1)] for j in range(degree + 1)]        #Matris oluşturulur.
    size = len(matrix)

    for i in range(size):
        for j in range(size):
            xSums = 0
            for k in range(n):
                matrix[0][0] = len(xValues)
                xSums = xValues[k] ** (i + j) + xSums
                matrix[i][j] = xSums

    xyResults = []
    for i in range(size):
        sum = 0
        for j in range(ilk, son):
            sum = sum + (values[j] * (xValues[j - ilk] ** i))
        xyResults.append(sum)

    k = 0
    for i in matrix:
        i.append(xyResults[k])
        k = k + 1
    coefficients = matrixWithGauss(matrix)
    if len(coefficients) < 7:
        while len(coefficients) != 7:
            coefficients.append(0)

    print("Polinom Denklemi Sonucu: \n")                #Polinomların denklem sonuçları yazdırılır.
    equation = coefficients[6] * x ** 6 + coefficients[5] * x ** 5 + coefficients[4] * x ** 4 + \
               coefficients[3] * x ** 3 + coefficients[2] * x ** 2 + \
               coefficients[1] * x + coefficients[0]

    sym.pprint(equation)                #pprint ile günlük hayattaki yazdığımız gibi yazdırırız.

    integral = 0
    a = 10  # Okul no : 190401090(0)
    b = len(values)
    deltaxValue = 0.01
    n = int((b - a) / deltaxValue)
    for i in range(n):
        integral += deltaxValue * (equation.subs({x: a}) + equation.subs({x: a + deltaxValue})) / 2
        a += deltaxValue

    print("Integral Sonucu : ", integral)       #Integralin sonucu yazdırılır.


def integralWithOutPolynom():                   #Polinomsuz integral hesabı yapılır.

    integral = 0
    a = 10  # Okul no : 190401090(0)
    b = len(values)
    deltaxValue = 1                             #deltax değeri bir önceki fonksiyona göre daha yüksek alınır.
    n = int((b - a) / deltaxValue)

    for i in range(n - 1):
        integral += deltaxValue * (values[a] + values[a + deltaxValue]) / 2
        a += deltaxValue

    print("Polinomsuz Integral Sonucu: ", integral)


file = open('190401090_yorum.txt', 'w', encoding='UTF8')
file.write('Polinomlar aracılığıyla hesaplamak istediğimiz değeri küçük dikdörtgenlere bölüp daha sonra bunların alanlarını toplayarak hesaplamalar yapılır.\n')
file.write('Ele aldığımız dikdörtgenlerin eni ne kadar küçük olursa, yani delta x değeri ne kadar küçük olursa o kadar daha fazla dikdörtgen alanı hesaplamış oluruz.')
file.write('Ve aradığımız sonuca çok daha yakın sonuçları böylelikle elde edebiliriz.\n')
file.write('Deltax olarak ele aldığımız değer aslında bizim dikdörtgenlerimizin en boyudur.\n')
file.write('Delta x değerini 1 alarak yaptığımız integral hesaplama ise polinomsuz hesaplamadır.\n')
file.write('Polinomlu ve polinomsuz alan hesaplamalarında birbirlerinden farklı sonuçlar verir.\n')
file.write('Bunun sebebi polinomlu olup olmamasına bağlı olarak değişen alan hesabının farklı olmasından dolayıdır.')
file.write('Polinomlu integral ile yapılan çözümler polinomsuz integral çözümüne göre aradığımız sonuca daha yakın bir sonuç verir sonucuna net bir şekilde ulaşabiliriz.')
file.write('Delta x değerinin artması durumunda hesaplanacak dikdörtgen sayısı öncekine göre artacağından yapılan işlemler daha fazla zaman alır.\n')
file.write('Delta x değerinin azalması durumunda ise hesaplanacak dikdörtgen sayısı azaldığı için hesaplama hızlı yapılacaktır fakat istenen sonuca yakın sonuç elde etme oranı azalır.')
file.close()

#Selahattin Ahmed Ataşoğlu  -- 190401090

readFile()
findValues(0, len(values))          #Ekrana yazdırılacak veriler. Hesaplamaların yapılması biraz sürüyor.
integralWithOutPolynom()
