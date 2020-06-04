#Deniz Can Tüfekçi - 180401060


def GetCoefficients(p1, p2, p3, p4, p5, p6, MainFile):
    MainFile.write("|------------------------------------------------ Polinom Katsayıları / Polynomial Coefficients ------------------------------------------------|\n")
    MainFile.write("|-----------------------------------------------------------------------------------------------------------------------------------------------|\n")
    MainFile.write("|     1. degreeden 	|     2. degreeden 	|     3. degreeden 	|     4. degreeden 	|     5. degreeden 	|     6. degreeden 	|\n")
    MainFile.write("|        Polinom   	|        Polinom   	|        Polinom   	|        Polinom   	|        Polinom   	|        Polinom   	|\n")
    MainFile.write("|      Katsayıları 	|      Katsayıları 	|      Katsayıları 	|      Katsayıları 	|      Katsayıları 	|      Katsayıları 	|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|\n")
    MainFile.write("|a0=" + str(round(p1[0],15)) + "\t|a0=" + str(round(p2[0],15)) + "\t|a0=" + str(round(p3[0],15)) + "\t|a0=" + str(round(p4[0],15)) + "\t|a0=" + str(round(p5[0],15)) + "\t|a0=" + str(round(p6[0],15)) + "\t|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|\n")
    MainFile.write("|a1=" + str(round(p1[1],15)) + "\t|a1=" + str(round(p2[1],15)) + "\t|a1=" + str(round(p3[1],15)) + "\t|a1=" + str(round(p4[1],15)) + "\t|a1=" + str(round(p5[1],15)) + "\t|a1=" + str(round(p6[1],15)) + "\t|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|\n")
    MainFile.write("|-----------------------|a2=" + str(round(p2[2],15)) + "\t|a2=" + str(round(p3[2],15)) + "\t|a2=" + str(round(p4[2],15)) + "\t|a2=" + str(round(p5[2],15)) + "\t|a2=" + str(round(p6[2],15)) + "\t|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|\n")
    MainFile.write("|-----------------------|-----------------------|a3=" + str(round(p3[3],15)) + "\t|a3=" + str(round(p4[3],15)) + "\t|a3=" + str(round(p5[3],15)) + "\t|a3=" + str(round(p6[3],15)) + "\t|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|a4=" + str(round(p4[4],15)) + "\t|a4=" + str(round(p5[4],15)) + "\t|a4=" + str(round(p6[4],15)) + "\t|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|a5=" + str(round(p5[5],15)) + "\t|a5=" + str(round(p6[5],15)) + "\t|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|\n")
    MainFile.write("|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|a6=" + str(round(p6[6],15)) + "\t|\n")
    MainFile.write("|-----------------------------------------------------------------------------------------------------------------------------------------------|\n")


def eligible_poly(c1, c2, c3, c4, c5, c6, TextFile):
    TextFile.write("------ Korelasyon Katsayıları / Correlation Coefficients ------" +
                   "\n1. degreeden polinomun korelasyon katsayısı: "+str(c1) +
                   "\n2. degreeden polinomun korelasyon katsayısı: "+str(c2) +
                   "\n3. degreeden polinomun korelasyon katsayısı: "+str(c3) +
                   "\n4. degreeden polinomun korelasyon katsayısı: "+str(c4) +
                   "\n5. degreeden polinomun korelasyon katsayısı: "+str(c5) +
                   "\n6. degreeden polinomun korelasyon katsayısı: "+str(c6)+"\n")
    CorrelationCoefficients = [c1, c2, c3, c4, c5, c6]
    maxElement = max(CorrelationCoefficients)
    for case in range(len(CorrelationCoefficients)):
        if maxElement == CorrelationCoefficients[case]:
            TextFile.write("Belirtilen aralıkta en uygun polinom: "+str(CorrelationCoefficients[case])+" değeri ile "+str(case+1)+". degreeden polinomdur.\n")


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
for i in range(len(datas)):
    datas[i] = int(datas[i])
polyns, errors = [0] * 6, [0] * 6
for index in range(0,6):
    polyns[index], errors[index] = poly_interpolation(index+1, datas)
source.close()


receiver = open("sonuc.txt", "w")
receiver.write("************************************************** Veri Setimizin Tamamının Baz Alındığı Durum **************************************************\n")
GetCoefficients(polyns[0], polyns[1], polyns[2], polyns[3], polyns[4], polyns[5], receiver)
eligible_poly(errors[0], errors[1], errors[2], errors[3], errors[4], errors[5], receiver)
for Range in range(len(datas) - 9):
    receiver.write("\n************************************************ Sıralı 10'lu veri grubu ("+str(Range+1)+","+str(Range+10)+") günlerinde iken: ************************************************\n")
    element_list = datas[Range:Range+10]
    for i in range(6):
        polyns[i], errors[i] = poly_interpolation(i+1, element_list)
    GetCoefficients(polyns[0], polyns[1], polyns[2], polyns[3], polyns[4], polyns[5], receiver)
    eligible_poly(errors[0], errors[1], errors[2], errors[3], errors[4], errors[5], receiver)
receiver.close()

"""
Korelasyon, iki değişken arasında doğrusal bir ilişkiyi ifade eder.
Korelasyon katsayısı ise değişkenler arasındaki ilişkiyi göstermek için kullanılan bir değerdir.
Korelasyon katsayısı; 
    +1,00′e yaklaştıkça iki değişken arasında aynı yöndeki ilişki artar.Değişkenlerden biri artarken diğeri de artar.
    -1,00′e yaklaştıkça iki değişen arasında ters yönde ilişki artar. Değişkenlerden biri artarken diğeri azalır.
    0,00’a yaklaştıkça iki değişken arasındaki ilişki azalır.
Biz bu ödevde aynı yönde artan veriler üzerinde ilgileceğimiz için korelasyon katsayısı 1'e en yakın olan 
polinomu, en uygun polinom olarak kabul edeceğiz.
"""
