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
            m[j] = [int(m[j][k]) - int(m[i][k]) * int(m[j][i]) / int(m[i][i]) for k in range(n + 1)]

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


def standartEstimateError(x, y, n, coefficients, d):
    total = 0
    temp = 0
    k = 0
    for i in y:
        temp += i
    temp = temp / len(y)
    for i in range(n):
        seeVal = 0
        k += (y[i] - temp) ** 2
        seeVal += y[i] - coefficients[0]
        for j in range(1, d + 1):
            seeVal = seeVal - coefficients[j] * (x[i] ** j)
        total += seeVal ** 2
    val = abs((k - total) / k) ** .5
    return val


def createEquationForAllDegrees(x, y, n, m):
    arr = []
    for i in range(m + 1):
        line = []
        for j in range(m + 1):
            if i == 0 and j == 0:
                line.append(n)
            else:
                xSum = 0
                for k in x:
                    xSum += k ** (i + j)
                line.append(xSum)
        total = 0
        for l in range(n):
            total += (x[l] ** i) * y[l]
        line.append(total)
        arr.append(line)
    return arr


def getOptimalValue(list):
    return min(range(len(list)), key=list.__getitem__)


def fx(coefficients, x):
    y = 0
    for i in range(len(coefficients)):
        y += coefficients[i] * (x ** i)
    return y


def withPolynomial(b, coefficients):
    a = 5  # 150401075
    deltax = 0.1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n):
        integral += (deltax * (fx(coefficients, a) + fx(coefficients, a + deltax)) / 2)
        a += deltax
    return integral


def withoutPolynomial(y):
    a = 5
    b = len(y)
    deltax = 1
    integral = 0

    n = int((b - a) / deltax)
    for i in range(n - 1):
        integral += deltax * (y[a] + y[a + deltax]) / 2
        a += deltax
    return integral


def main():
    data = readFile("veriler.txt")
    n = len(data)

    equationList = [x for x in range(6)]
    for i in range(1, 7):
        equationList[i - 1] = createEquationForAllDegrees(list(range(0, n)), data, n, i)

    solutions = [x for x in range(6)]
    for i in range(len(solutions)):
        solutions[i] = gaussElimination(equationList[i])

    ratios = [x for x in range(1, 7)]
    for o in range(6):
        ratios[o] = standartEstimateError(list(range(0, n)), data, n, solutions[o], o)

    minIndex = getOptimalValue(ratios)

    print(f"En düşük hata oranına sahip {minIndex + 1}. derece polinomdur, "
          f"hata miktari:"
          f" {ratios[minIndex]}")

    print("Polinom ile elde edilen sonuç", withPolynomial(len(data), solutions[minIndex]))
    print("Polinomsuz elde edilen sonuç", withoutPolynomial(data))


if __name__ == "__main__":
    main()
