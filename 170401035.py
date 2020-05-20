def Polynominal(m1, m2, m3, m4, m5, m6, file):
    file.write("m1 --> " + str(m1) + "\n")
    file.write("m2 --> " + str(m2) + "\n")
    file.write("m3 --> " + str(m3) + "\n")
    file.write("m4 --> " + str(m4) + "\n")
    file.write("m5 --> " + str(m5) + "\n")
    file.write("m6 --> " + str(m6) + "\n")
    file.write("--------------------------------------------------------- \n")
    file.write("Result --> ")
    if m1 > m6 and m1 > m5 and m1 > m4 and m1 > m3 and m1 > m2:

        file2.write(str(m1) + " en uygun 1. polinom. \n")

    elif m2 > m6 and m2 > m5 and m2 > m4 and m2 > m3:

        file2.write(str(m2) + " en uygun 2.polinom. \n")

    elif m3 > m6 and m3 > m5 and m3 > m4:
        file2.write(str(m3) + " en uygun 3.polinom. \n")

    elif m4 > m6 and m4 > m5:
        file2.write(str(m4) + " en uygun 4.polinom. \n")

    elif m5 > m6:
        file2.write(str(m5) + " en uygun 5.polinom. \n")

    else:
        file2.write(str(m6) + " en uygun 6.polinom. \n")

    file.write("--------------------------------------------------------- \n")


def findFactors(pol1, pol2, pol3, pol4, pol5, pol6, file):
    file.write("\n\n1.dereceden polinom icin x0 = " + str(pol1[0]) + " x1 = " + str(pol1[1]) + "\n")
    file.write(
        "2.dereceden polinom icin x0 = " + str(pol2[0]) + " x1 = " + str(pol2[1]) + " x2 =" + str(
            pol2[2]) + "\n")
    file.write(
        "3.dereceden polinom icin x0 = " + str(pol3[0]) + " x1 = " + str(pol3[1]) + " x2 =" + str(
            pol3[2]) + " x3 = " + str(pol3[3]) + "\n")
    file.write(
        "4.dereceden polinom icin x0 = " + str(pol4[0]) + " x1 = " + str(pol4[1]) + " x2 =" + str(
            pol4[2]) + " x3 = " + str(pol4[3]) + " x4 = " + str(pol4[4]) + "\n")
    file.write(
        "5.dereceden polinom icin x0 = " + str(pol5[0]) + " x1 = " + str(pol5[1]) + " x2 =" + str(
            pol5[2]) + " x3 = " + str(pol5[3]) + " x4 = " + str(pol5[4]) + " x5 = " + str(
            pol5[5]) + "\n")
    file.write(
        "6.dereceden polinom icin x0 = " + str(pol6[0]) + " x1 = " + str(pol6[1]) + " x2 =" + str(
            pol6[2]) + " x3 = " + str(pol6[3]) + " x4 = " + str(pol6[4]) + " x5 = " + str(
            pol6[5]) + " x6 = " + str(pol6[6]) + "\n")
    file.write("--------------------------------------------------------- \n")


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

    y2 = 0

    for i in range(len(data)):
        y2 += data[i]

    y2 = y2 / len(data)
    y1, y2 = 0, 0

    for i in range(len(data)):
        z = data[i]
        y1 += (data[i] - y2) ** 2

        for j in range(len(result)):
            z -= result[j] * (i + 1) ** j

        z = z ** 2
        y2 += z

    m = ((y1 - y2) / y1) ** (1 / 2)
    return result, m


file = open("veriler.txt", "r")
data = file.readlines()
for i in range(len(data)):
    data[i] = int(data[i])

pol1, m1 = interpolation(1, data)
pol2, m2 = interpolation(2, data)
pol3, m3 = interpolation(3, data)
pol4, m4 = interpolation(4, data)
pol5, m5 = interpolation(5, data)
pol6, m6 = interpolation(6, data)

file.close()
file2 = open("sonuc.txt", "w")
file2.write("********** Hasan AVCI 170401035 **********")
findFactors(pol1, pol2, pol3, pol4, pol5, pol6, file2)
Polynominal(m1, m2, m3, m4, m5, m6, file2)

for i in range(len(data) // 10):
    group = []
    file2.write("\n" + str(i + 1) + ". 10'lu grup icin \n")

    for j in range(10):
        group.append(data[10 * i + j])

    polynominal1, m1 = interpolation(1, group)
    polynominal2, m2 = interpolation(2, group)
    polynominal3, m3 = interpolation(3, group)
    polynominal4, m4 = interpolation(4, group)
    polynominal5, m5 = interpolation(5, group)
    polynominal6, m6 = interpolation(6, group)
    findFactors(polynominal1, polynominal2, polynominal3, polynominal4, polynominal5, polynominal6, file2)
    Polynominal(m1, m2, m3, m4, m5, m6, file2)

file2.close()