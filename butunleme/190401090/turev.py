#Selahattin Ahmed Ataşoğlu  -- 190401090

import sympy as sym

sym.init_printing()                                 #Polinom denklemini de göstermek istediğim için,
x = sym.Symbol('x')                                 #günlük hayattaki yazım şekliyle x'e sembol tanımlaması yapıyoruz.
                                                    #Polinom denklemleri yazdırılırken kullanacağız.
asalDiziDegerler = []

def readFile():

    file = open('asallar.txt', 'r')                 # asallar.txt dosyasından değerler satır satır çekilir.
    for row in file:
        asalDiziDegerler.append(int(row))           # Değerler int olarak diziye aktarılır.
    file.close()


xi = [0 for h in range(7)]                          #xi değerleri toplamları

yi = [0 for c in range(4)]                          #yi değerleri toplamları

coefficients = [0 for p in range(4)]                #katsayılarının bulunduğu dizi


def createMatrix():                                 #4'e 4'lük bir matris oluşturulur.

    matrix = [[0 for p in range(4)] for r in range(4)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            matrix[i][j] = xi[i + j]

    return matrix


def matrixWithGauss():                              #Gauss yöntemiyle matris hesaplaması yapılır.

    matrix = createMatrix()

    row = len(matrix)
    column = len(matrix[0])

    for b in range(row):
        for c in range(b + 1, row):
            u = - matrix[c][b] / matrix[b][b]

            for t in range(b, column):
                if t == b:
                    matrix[c][t] = 0.0
                else:
                    matrix[c][t] += u * matrix[b][t]

            yi[c] += u * yi[b]


    for l in range(row - 1, -1, -1):

        coefficients[l] = yi[l] / matrix[l][l]

        for j in range(l - 1, -1, -1):
            yi[j] -= coefficients[l] * matrix[j][l]
                                                        #Hesaplanan katsayı değerleri ekrana yazdırılır.
    print("Katsayılar (3 --> 0):", (coefficients[3], coefficients[2], coefficients[1], coefficients[0]))


def writePolynomEquation(x):            #Üçüncü dereceden polinom denklemini oluşturan ve yazdıran fonksiyon.

    equation = coefficients[0] + coefficients[1] * x + coefficients[2] * x ** 2 + coefficients[3] * x ** 3

    print("\nPolinom denklemi sonucu: ")
    sym.pprint(equation)        #Katsayılardan biri tam olarak sığmadığı için kalan kısmı aşağıya kayıyor olabilir.
                                #Günlük hayatta kullandığımız şekilde ekrana yazdırıyoruz.

def selectRowGetValue(row, rowValue):   #Seçilen satır değerine göre o satırdaki asal sayı değeriyle katsayı değerleri gauss yardımıyla bulunur.

    if row != 0:                        # row değeri 0 oluncaya kadar bu işlem devam eder.
        for p in range(len(xi)):
            xi[p] += (row) ** p

        for t in range(len(yi)):
            yi[t] += rowValue * ((row) ** t)

        selectRowGetValue(row - 1, asalDiziDegerler[row - 2])

    else:
        matrixWithGauss()               # row değeri 0 olduğunda gauss ile katsayı hesaplaması yapılır.


def function(x):  # Üçüncü dereceden polinom için tanımlanan fonksiyon.

    return (coefficients[0] + coefficients[1] * x + coefficients[2] * x ** 2 + coefficients[3] * x ** 3)


def derivativeWithPolynom():                # Polinomla beraber yapılan türev sonucu.

    a = 90  # 190401090(90)    # a = 90
    h = 0.01
    xprime = (function(a + h) - function(a - h)) / (2 * h)    #Merkezi Farklar ile Birinci Dereceden Sayısal Türev Alma Denklemi

    print("\na = 90 noktasındaki Polinomlu Türev Sonucu: ", xprime)


def derivativeWithOutPolynom():         # Polinomsuz bir şekilde yapılan türev sonucu.

    a = 90 - 1                          # dizimiz index[0]'dan başladığı için bir eksiğini almamız gerekir.
    h = 1                               # h değeri polinomsuz hesaplama olduğu için en az 1 alınabilir.
    xprime = (asalDiziDegerler[a + h] - asalDiziDegerler[a - h]) / (2 * h)  #Merkezi Farklar ile Birinci Dereceden Sayısal Türev Alma Denklemi
    print("a = 90 noktasındaki Polinomsuz Türev Sonucu: ", xprime)


def comments():                        # Polinomlu ve polinomsuz arasındaki farkın yorumlarla dosyaya yazılması.

    file = open('yorum.txt', 'w', encoding='UTF8')
    file.write('Yapmış olduğumuz hesaplamalarda polinomlu ve polinomsuz olarak hesaplanan türev değerlerinin farklı\n')
    file.write('olduğunu gördük. Bu farkın sebeplerinden birisi, polinomsuz bir şekilde yapmış olduğumuz türev hesabında\n')
    file.write('hesaplama yaparken aldığımız aralık en iyi ihtimalle h=1 değeri olabildiğinden dolayı tam olarak istediğimiz\n')
    file.write('sonuca yakın bir sonuç vermeyebilir. Fakat polinomlu bir şekilde yapmış olduğumuz türev hesaplamasında ise\n')
    file.write('aralığı elimizdeki polinoma göre daha da daraltarak aradığımız gerçek sonuca daha yakın bir sonuç buluruz.\n')
    file.write('Bu farka sebep olan ikincil bir durum ise, kullandığımız polinom ile üzerinde işlem yapmış olduğumuz\n')
    file.write('asal sayı değerlerini birebir olarak vermediği için yaptığımız türev hesaplamaları sonuçlarının birbirinden\n')
    file.write('farklı olmasına neden olmaktadır.\n')
    file.close()


readFile()                                      # asallar.txt dosyasından veriler okunur ve değerler çekilerek diziye aktarılır.
selectRowGetValue(109, asalDiziDegerler[108])   # seçilen satır sayısı ve satırda bulunan asal sayı değeriyle işlemler yapılır. Katsayı değerleri bulunur.
writePolynomEquation(x)                         # polinom denklemi ekrana yazdırılır.
derivativeWithPolynom()                         # polinomlu türev değeri hesaplanıp ekrana yazdırılır.
derivativeWithOutPolynom()                      # polinomsuz türev değeri hesaplanıp ekrana yazdırılır.
comments()                                      # yorum.txt dosyası oluşturularak yorum satırları buraya yazdırılır.