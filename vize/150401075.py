# Sefa Karagöz - 150401075

def readFile(filename):
    file = open(filename)
    list = []
    for line in file.readlines():
        line = line.rstrip('\n')
        list.append(float(line))
    file.close()
    return list


def gaussElimination(m):
    n = len(m)
    for i in range(n):
        pivot(m, n, i)
        for j in range(i + 1, n):
            m[j] = [m[j][k] - m[i][k] * m[j][i] / m[i][i] for k in range(n + 1)]

    if m[n - 1][n - 1] == 0: raise ValueError('hatalı format!')

    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(m[i][j] * x[j] for j in range(i, n))
        x[i] = (m[i][n] - s) / m[i][i]
    return x


def pivot(m, n, i):
    max = 0
    for r in range(i, n):
        if max < abs(m[r][i]):
            max_row = r
            max = abs(m[r][i])
    m[i], m[max_row] = m[max_row], m[i]


def getCoefficients(n, data):
    xiList = [[] for y in range(n + 2)]

    for i in range(0, n + 2):
        for k in range(0, n + 2):
            if i == 0:
                xiList[i].append(k + 1)
            else:
                xiList[i].append((k + 1) ** (i + 1))
    return xiList


def getSumCoefficients(data):
    for k in range(len(data)):
        data[k] = sumOfDataLen(data[k])
    return data


def getAllXiYi(n, data, yi, coefficients):
    list = [x for x in range(6)]
    for j in range(n):
        for i in range(6):
            list[i] += data[j] * coefficients[i][j]

    list.insert(0, yi)
    return list


def sumOfDataLen(arr):
    t = 0
    for i in range(10):
        t += arr[i]
    return t


def createEquationForAllDegrees(coefficients, xiyi, n):
    list = [x for x in range(6)]
    w, h = 3, 2

    # tüm dereceler için denklem oluşturalım
    for i in range(6):
        matrix = [[0 for x in range(w)] for y in range(h)]
        for k in range(h):
            for l in range(w):
                if k == 0:
                    if k == 0 and l == 0:
                        matrix[k][l] = n
                    else:
                        for z in range(len(coefficients)):
                            if coefficients[z] in matrix[k]:
                                pass
                            else:
                                matrix[k][l] = coefficients[z]
                                break
                    if l == (w - 1):
                        matrix[k][l] = xiyi[k]
                else:
                    for z in range(len(coefficients)):
                        if coefficients[z] in matrix[k]:
                            pass
                        elif matrix[k - 1][l] == coefficients[z] or matrix[k - 1][l] > coefficients[z]:
                            pass
                        else:
                            if coefficients[z] > matrix[k][l - 1]:
                                matrix[k][l] = coefficients[z]
                                break
                    if l == (w - 1):
                        matrix[k][l] = xiyi[k]

        w += 1
        h += 1
        list[i] = matrix
    return list


def standartEstimateError(data, list):
    arr = []
    val = 0
    for k in range(1, len(list) + 1):
        for i in range(len(data)):
            seeVal= data[i]
            for j in range(k + 1):
                seeVal = seeVal - (list[k - 1][j] * ((i + 1) ** j))
            val += seeVal ** 2
        val = (val / (len(data) - (k + 1))) ** .5
        arr.append(val)
    return (arr)


def getOptimalValue(list):
    return min(range(len(list)), key=list.__getitem__)


def granularData():
    data = readFile("veriler.txt")
    for i in range((len(data) - 9)):
        chunk = data[i:i + 10]

        n = len(chunk)
        yi = sum(chunk)
        rawCoefficients = getCoefficients(n, chunk)
        xiyi = getAllXiYi(n, chunk, yi, rawCoefficients)
        coefficients = getSumCoefficients(rawCoefficients)

        equationList = createEquationForAllDegrees(coefficients, xiyi, n)

        solutions = [x for x in range(6)]
        for j in range(len(solutions)):
            solutions[j] = gaussElimination(equationList[j])

        ratios = standartEstimateError(chunk, solutions)
        minIndex = getOptimalValue(ratios)
        print(f"{i + 1}-{i + 10} aralığındaki veriler için {minIndex + 1}. derece polinom en uygun, hata miktari:"
              f" {ratios[minIndex - 1]}")

        f = open('sonuc.txt', 'a')
        f.write("\n")
        f.write(f"{i + 1}-{i + 10} aralığındaki veriler için {minIndex + 1}. derece polinom en uygun, hata miktari:"
                f" {ratios[minIndex - 1]}")
        f.close()


def main():
    data = readFile("veriler.txt")
    n = len(data)
    yi = sum(data)
    rawCoefficients = getCoefficients(n, data)
    xiyi = getAllXiYi(n, data, yi, rawCoefficients)
    coefficients = getSumCoefficients(rawCoefficients)

    equationList = createEquationForAllDegrees(coefficients, xiyi, n)

    solutions = [x for x in range(6)]
    for i in range(len(solutions)):
        solutions[i] = gaussElimination(equationList[i])

    f = open('sonuc.txt', 'w')
    for j in range(len(solutions)):
        f.write(f"{j + 1}.derece => {str(solutions[j])}\n")
    f.close()

    ratios = standartEstimateError(data, solutions)

    f = open('sonuc.txt', 'a')
    f.write("\n\n")
    for m in range(len(solutions)):
        f.write(f"{m + 1}.derece polinom için standart tahmini hata => {str(ratios[m])}\n")
    f.close()

    minIndex = getOptimalValue(ratios)
    print(f"Tüm veriler için en uygun polinom: {minIndex + 1}. derece polinomdur, hata miktari: {ratios[minIndex - 1]}")

    f = open('sonuc.txt', 'a')
    f.write("\n\n")
    f.write(f"Tüm veriler için en uygun: => {(minIndex + 1)}. derece polinomdur\n")
    f.close()

    granularData()


if __name__ == "__main__":
    main()
