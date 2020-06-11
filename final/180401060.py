#Deniz Can Tüfekçi - 180401060
from sympy import Symbol


def notPoly_integrating(a, b, inDatas):
    integral = 0
    deltax = 1
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral += deltax * (inDatas[a] + inDatas[a+deltax])/2
        a += deltax
    return integral


def desired_poly_integrating(PolyCoefficients,a,b):
    x = Symbol('x')
    poly = 0
    for i in range(len(PolyCoefficients)):
        poly += PolyCoefficients[i] * (x ** i)
    integral = 0
    deltax = 1
    n = int((b-a)/deltax)
    for i in range(n):
        integral += deltax * (poly.subs({x: a}) + poly.subs({x: a+deltax}))/2
        a += deltax
    return integral
    

def eligible_poly_degree(c1, c2, c3, c4, c5, c6):
    CorrelationCoefficients = [c1, c2, c3, c4, c5, c6]
    maxElement = max(CorrelationCoefficients)
    poly_degree = 0
    for case in range(len(CorrelationCoefficients)):
        if maxElement == CorrelationCoefficients[case]:
            poly_degree = case
    return poly_degree


def poly_interpolation(degree, inDatas):
    matrix = []
    base = 0

    for i in range(degree+1):
        row = []
        for j in range(degree+1):
            Sum = 0
            for k in range(1, len(inDatas)+1):
                Sum += k**base
            row.append(Sum)
            base += 1
        matrix.append(row)
        base -= degree

    result = []
    for i in range(degree+1):
        Sum = 0
        for j in range(len(inDatas)):
            Sum += inDatas[j]*(j+1)**i
        result.append(Sum)

    for i in range(degree+1):  # lower triangular with gaussian elimination
        factor = matrix[i][i]
        for j in range(i+1, degree+1):
            ratio = factor/matrix[j][i]
            result[j] = result[j]*ratio-result[i]
            for k in range(degree+1):
                matrix[j][k] = matrix[j][k]*ratio-matrix[i][k]

    for i in range(degree, -1, -1):  # upper triangular with gaussian elimination
        factor = matrix[i][i]
        for j in range(i-1, -1, -1):
            ratio = factor/matrix[j][i]
            result[j] = result[j]*ratio-result[i]
            for k in range(degree+1):
                matrix[j][k] = matrix[j][k]*ratio-matrix[i][k]

    for i in range(degree+1):
        result[i] = result[i]/matrix[i][i]

    sum_y = 0
    for i in range(len(inDatas)):
        sum_y += inDatas[i]
    y_avg = sum_y/len(inDatas)

    sum_t, sum_r = 0, 0
    for i in range(len(inDatas)):
        element = inDatas[i]
        sum_t += (inDatas[i]-y_avg)**2
        for j in range(len(result)):
            element -= result[j]*(i+1)**j
        element = element**2
        sum_r += element
    correlation = ((sum_t-sum_r)/sum_t)**(1/2)
    return result, correlation


source = open("veriler.txt", "r")
datas = source.readlines()
value_of_a = 10 # 180401060 --> a = 10
value_of_b = len(datas)
for i in range(len(datas)):
    datas[i] = int(datas[i])
polyns, errors = [0] * 6, [0] * 6
for index in range(0, 6):
    polyns[index], errors[index] = poly_interpolation(index+1, datas)
source.close()

desPolyDegree = eligible_poly_degree(errors[0], errors[1], errors[2], errors[3], errors[4], errors[5])
desPoly_integral_value = desired_poly_integrating(polyns[desPolyDegree], value_of_a, value_of_b)
notPoly_integral_value = notPoly_integrating(value_of_a, value_of_b, datas)
print("İnterpolasyon sonucu ", desPolyDegree+1, ". dereceden polinomda en düşük korelasyon olduğu hesaplanmıştır.")
print(desPolyDegree+1, ". dereceden polinom kullanılarak alınan integral değeri: ", desPoly_integral_value)
print("Polinom kullanılmadan alınan integral değeri: ", notPoly_integral_value)

receiver = open("180401060_yorum.txt", "w", encoding="utf-8")
receiver.write("İnterpolasyon sonucu " + str(desPolyDegree+1) + ". dereceden polinomda en düşük korelasyon olduğu hesaplanmıştır.\n")
receiver.write("Polinom kullanılarak alınan integral değeri: " + str(desPoly_integral_value) + "\n")
receiver.write("Polinom kullanılmadan alınan integral değeri: " + str(notPoly_integral_value) + "\n\n\n")
receiver.write("""Yamuk yöntemi kullanarak elde ettiğimiz iki integral değerinin de 
mutlak doğru alan sonuçları olmayacağı çok rahat bir şekilde belirtilebilir. 
(Çünkü deltaX'i daha da küçülterek daha ayrıntılı sonuçlara ulaşabiliriz.)

2. sorumuzda polinom ile yamuk yöntemi kullanılarak elde edilen ilk integrali hesaplarken, 
veriler.txt'deki veriler ile interpolasyon yapılarak 6. dereceden bir polinomun en iyi 
(1'e en yakın) korelasyon katsayısına sahip olduğu anlaşılmış, interpolasyon sonrasındaki 
katsayılarla elde edilen polinomun integrali alınmış ve sonucunda ise 
yaklaşık olarak 164138 değeri elde edilmiştir.

3. sorumuzda veriler.txt dosyasında verilen değerler yani orjinal polinomun değer kümesinin 
elemanları ile yamuk yöntemi kullanılarak elde ettiğimiz ikinci integrali hesaplarken bu 
veri kümesi işlenmiş ve yaklaşık olarak 162714 değeri elde edilmiştir. 

Elde edilen bu verilerden hareketle:
İki integral değerinin de birbirine çok yakın olduğu görülmüştür. Fakat her ne kadar sonuçlar 
birbirine yakın olsa da sonuçların aynı olmaması, 6. dereceden polinomun ancak belirli bir 
korelasyon ile orjinal polinoma yakınsamasından kaynaklanmaktadır. Korelasyon katsayısı 1 olan
en uygun polinom elde edilseydi, ancak o zaman birbiri ile örtüşen sonuçlar alınabilinirdi.""")
receiver.close()
