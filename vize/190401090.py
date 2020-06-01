def zeros_matrix(rows, cols):  # Sıfır matris oluşturulur.
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A


def createList(n):  # "n" kadar uzunlukta olacak bir sıralı dizi oluşturulur.
    x = [i + 1 for i in range(n)]
    return x


def matrix_multiply(A, B):  # Matrisleri çarpan fonksiyon.
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
        exit()

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C


def createValues(list, values):
    listForValues = []
    for y in range(len(list)):
        lastValue = 0
        for i in range(len(values)):
            lastValue += values[i] * ((y + 1) ** i)
        listForValues.append(round(lastValue, 3))
    return listForValues


def invert_matrix(AM, IM):  # Matrisi ters çeviren fonksiyon.
    for fd in range(len(AM)):
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(len(AM)):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in list(range(len(AM)))[0:fd] + list(range(len(AM)))[fd + 1:]:
            crScaler = AM[i][fd]
            for j in range(len(AM)):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM


def polynomValues(firstArray, secondArray, degree):  # Polinom yakınlaştırma hesabı bu fonksiyonla yapılır.

    n = len(firstArray)

    squareMatrix = []
    lastValuesMatrix = []

    for x in range(degree + 1):
        squareMatrix.append([])

        for y in range(degree + 1):
            if (x == 0 and y == 0):
                squareMatrix[x].append(n)
            else:
                c = 0
                for i in firstArray:
                    c += i ** (x + y)
                squareMatrix[x].append(c)

        arrVal1 = 0
        for i in range(len(firstArray)):
            arrVal1 += (firstArray[i] ** x) * float(secondArray[i])
        lastValuesMatrix.append([arrVal1])
    opst = invert_matrix(squareMatrix, lastValuesMatrix)
    value = matrix_multiply(opst, lastValuesMatrix)

    return value


def inaccuracy(weirdList):  # Listedekileri 1'den 6. dereceden polinoma kadar yakınlaştırır
    # ve hata paylarını toplar.
    inaccuracyList = []

    for i in range(6):
        expectedInaccuracy = 0
        list = createValues(weirdList, polynomValues(createList(len(weirdList)), weirdList, i + 1))

        for j in range(len(list)):
            expectedInaccuracy += round(abs(int(weirdList[j]) - list[j]), 3)
        inaccuracyList.append(round(expectedInaccuracy, 3))

    (curr, i) = min((vlu, i) for i, vlu in enumerate(inaccuracyList))  # hata sayısı en az olanı seçer.

    return (curr, i)


def main():  # MAIN Fonksiyonu

    with open('veriler.txt', 'r') as f:  # Dosyadaki veriler, kullanacağımız diziye aktarılır.
        y = f.read().split('\n')  # Veriler satır satır ayrılır.

    ex1 = createList(len(y))  # y'nin boyu kadar olacak bir dizi ex1'e atanır.

    f = open('sonuc.txt', 'w')
    f.close()

    for i in range(6):
        with open('sonuc.txt', 'a') as f:
            f.write(f"{i + 1}..: {str(polynomValues(ex1, y, i + 1))}\n")

    (curr, i) = inaccuracy(y)
    print(f" {i + 1}.'ci polinoma yakınlaştırma en uygun olandır. Hata sayısı = {curr} kadardır.")
    print("\n----------------------------------------------------------------------------------\n")

    for day in range((len(y) - 9)):
        listForDays = y[day:day + 10]
        (curr, i) = inaccuracy(listForDays)
        print(f"({day + 1},{day + 10}) gün aralığı için {i + 1}. polinoma yakınlaştırma en uygun olandır. Hata sayısı = {curr} kadardır.")


if __name__ == "__main__":
    main()


#Selahattin Ahmed Ataşoğlu - 190401090