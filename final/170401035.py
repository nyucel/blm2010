#Hasan Avcı 170401035
from sympy import Symbol,pprint


file = open("veriler.txt", "r")
data = file.readlines()
for i in range(len(data)):
    data[i] = int(data[i])

def detectPolynominal(m1, m2, m3, m4, m5, m6):
    if m1 > m6 and m1 > m5 and m1 > m4 and m1 > m3 and m1 > m2:
        print(str(m1) + " en uygun 1. polinom. \n")
        return 1

    elif m2 > m6 and m2 > m5 and m2 > m4 and m2 > m3:
        print(str(m2) + " en uygun 2.polinom. \n")
        return 2

    elif m3 > m6 and m3 > m5 and m3 > m4:

        print(str(m3) + " en uygun 3.polinom. \n")
        return 3

    elif m4 > m6 and m4 > m5:

        print(str(m4) + " en uygun 4.polinom. \n")
        return 4

    elif m5 > m6:

        print(str(m5) + " en uygun 5.polinom. \n")

        return 5
    else:

        print(str(m6) + " en uygun 6.polinom. \n")
        return 6




def wrtieEquationAndIntegral(polynominal1, polynominal2, polynominal3, polynominal4, polynominal5, polynominal6,a):
    x = Symbol('x')
    if(a==1):
        denklem =polynominal1[1] * x + polynominal1[0]
        pprint(denklem)
    elif(a==2):
        denklem =  polynominal2[2] * x ** 2 + polynominal2[1] * x + polynominal2[0]
        pprint(denklem)
    elif (a == 3):
        denklem = polynominal3[3] * x ** 3 + polynominal3[2] * x ** 2 + polynominal3[1] * x + polynominal3[0]
        pprint(denklem)
    elif(a==4):
        denklem = polynominal4[4] * x ** 4 + polynominal4[3] * x ** 3 + polynominal4[2] * x ** 2 \
                  + polynominal4[1] * x  + polynominal4[0]
        pprint(denklem)
    elif(a==5):
        denklem = polynominal5[5] * x ** 5 + polynominal5[4] * x ** 4 + polynominal5[3] * x ** 3\
                  + polynominal5[2] * x ** 2 +polynominal5[1] * x + polynominal5[0]
        pprint(denklem)
    else:
        denklem = polynominal6[6] * x ** 6 + polynominal6[5] * x ** 5 + polynominal6[4] * x ** 4 \
                  + polynominal6[3] * x ** 3  +polynominal6[2] * x ** 2 + polynominal6[1] * x +polynominal6[0]
        pprint(denklem)
    a = 5 #170401035
    b = len(data)
    deltax = 1

    integral = 0

    n = int((b - a) / deltax)

    for i in range(n):
        integral += deltax * ((denklem.subs({x: a})) + (denklem.subs({x: a + deltax})) )/ 2
        a += deltax

    print("Polinom kullanılarak bulunan integral değeri : ",integral)


def interpolation(factor, data):
    matrix = []
    result = []
    a = 0

    for i in range(factor + 1):
        line = []

        for j in range(factor + 1):
            total = 0

            for k in range(1, len(data) + 1):
                total += k ** a

            line.append(total)

            a += 1

        matrix.append(line)

        a -= factor

    for i in range(factor + 1):
        total = 0

        for j in range(len(data)):
            total += data[j] * (j + 1) ** i

        result.append(total)

    for i in range(factor, -1, -1):
        simile = matrix[i][i]

        for j in range(i - 1, -1, -1):
            rate = simile / matrix[j][i]
            result[j] = result[j] * rate - result[i]

            for k in range(factor + 1):
                matrix[j][k] = matrix[j][k] * rate - matrix[i][k]

    for i in range(factor + 1):
        simile = matrix[i][i]

        for j in range(i + 1, factor + 1):
            rate = simile / matrix[j][i]
            result[j] = result[j] * rate - result[i]

            for k in range(factor + 1):
                matrix[j][k] = matrix[j][k] * rate - matrix[i][k]

    for i in range(factor + 1):
        result[i] = result[i] / matrix[i][i]

    y_r = 0

    for i in range(len(data)):
        y_r += data[i]

    y_r = y_r / len(data)
    y_rp, y_rr = 0, 0

    for i in range(len(data)):
        z = data[i]
        y_rp += (data[i] - y_r) ** 2

        for j in range(len(result)):
            z -= result[j] * (i + 1) ** j

        z = z ** 2
        y_rr += z

    m = ((y_rp - y_rr) / y_rp) ** (1 / 2)
    return result, m

def polinomsuzIntegral():
    a = 5  # 170401035
    b = len(data)
    deltax = 1

    integral = 0

    n = int((b - a) / deltax)

    for i in range(n-1):
        integral += deltax * (data[a] + data[a+1]) / 2
        a += deltax
    print("Polinom kullanmadan bulunan integral değeri : ", integral)


polynominal1, m1 = interpolation(1, data)
polynominal2, m2 = interpolation(2, data)
polynominal3, m3 = interpolation(3, data)
polynominal4, m4 = interpolation(4, data)
polynominal5, m5 = interpolation(5, data)
polynominal6, m6 = interpolation(6, data)


z=detectPolynominal(m1, m2, m3, m4, m5, m6 )

wrtieEquationAndIntegral(polynominal1, polynominal2, polynominal3, polynominal4, polynominal5, polynominal6,z)

polinomsuzIntegral()

dosya = open('170401035_yorum.txt', 'w')

dosya.write("""Sonuçların farklı çıkmasının sebebi deltax'e verilen değerlerden kaynaklanıyor.Çünkü deltax'e 
ne kadar küçük değer verirsek grafiğin altındaki alanı daha fazla parçaya böleriz ve bu parçaların grafikten 
taşan ya da grafik ile arasında kalan boş alanlar daha az olur.Böylece gerçeğe daha yakın bir değer elde ederiz.
Polinom kullanmadan ,sadece verileri kullanırken deltax 1 oluyor ama polinomu kullanırken deltax'e 1'den daha küçük 
bir değer atayabiliriz.Bu yüzdende polinom ile çözülen integral polinomsuza göre gerçeğe daha yakındır.
""")

