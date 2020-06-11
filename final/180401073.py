# -*- coding: utf-8 -*-
# Barış KOL - 180401073
from math import sqrt
from sympy import Symbol
x = Symbol('x')
def orderedList(data):#i değeri için sıralı dizi oluşturuluyor.
    i = []
    for dataNumber in range(len(data)):
        i.append(dataNumber+1)
    return i    
with open("veriler.txt") as f: #Veriler okunup satır satır ayrılıyor ve yi dizisi oluşturuluyor.
    yi = f.read().split("\n")
    if yi[-1] == '':
        yi.pop()
def IntData(data):
    for i in range(len(data)):
        data[i] = int(data[i]) 
    return data
def Matrix(xi,yi,degree): #Xi değerleri ve #Xi(ve üsleri) ve Yi çarpımları için matrislerin oluşturulduğu Fonksiyon
    xiMatrix = [] #Xi 'lerin katsayılarının toplamlarının olduğu matris
    zeroMatrix = [] # Cholesky Metodu için gerekli olan 0 matrisi
    ResultMatrix = [] #Xi(ve üsleri) ve Yi çarpımlarının olduğu sonuç Matrisi
    n = len(xi)
    for i in range(degree+1):
        xiMatrix.append([]) #2. Boyut ekleniyor
        zeroMatrix.append([])
        SumXiandYi = 0 #Xi ve Yi çarpımları her bir satır için sıfırlanıyor.
        for j in range(degree+1):
            if(i == 0 and j == 0):
                xiMatrix[i].append(n) #matrisin 1.Satır 1. Sütununa n eklendi
                zeroMatrix[i].append(0)
            else:
                counter = 0
                for k in xi:
                    counter += k**(i+j) 
                xiMatrix[i].append(counter) #xi matrisinin diğer elemanları eklendi.
                zeroMatrix[i].append(0)
        for l in range(len(xi)):
            SumXiandYi += float(yi[l]) * (xi[l]**i)
        ResultMatrix.append(SumXiandYi) #Xi(ve üsleri) ve Yi çarpımları sonuçlar diziye ekleniyor
    return xiMatrix,ResultMatrix,zeroMatrix
def transposeMatrix(inMtx): 
    tMtx = []
    for row in range(0, len(inMtx[0])):
      tRow = []
      for col in range(0, len(inMtx)):
        ele = inMtx[col][row]
        tRow.append(ele)
      tMtx.append(tRow)
    return(tMtx)
def Cholesky(matrix,zeroMatrix):
    for i in range(len(matrix)):
       for j in range(i+1):
           IkareToplami = sum(zeroMatrix[j][k]**2 for k in range(j))
           if (i == j):
               zeroMatrix[i][i] = sqrt(matrix[i][i] - IkareToplami)
           else:
               ICarpimToplami = sum(zeroMatrix[i][k] * zeroMatrix[j][k] for k in range (j))
               zeroMatrix[i][j] = (1.0 / zeroMatrix[j][j])*(matrix[i][j]-ICarpimToplami)
    return zeroMatrix
def Result(bottomTriangular,resultMatrix):
    columnMatris = [0 for i in range(len(bottomTriangular))]
    result = [0 for i in range(len(resultMatrix))]
    for i in range(len(bottomTriangular)): 
        if(i == 0):
            columnMatris[i] = resultMatrix[i] / bottomTriangular[i][i]
        else:
            totals = sum(bottomTriangular[i][j] * columnMatris[j] for j in range(i))
            columnMatris[i] = ((resultMatrix[i])- totals)/(bottomTriangular[i][i])
    topTriangular = transposeMatrix(bottomTriangular)
    n = len(topTriangular)
    for i in range(n-1,-1,-1):
        if(i == n-1):
            result[i] = columnMatris[i] / topTriangular[i][i]
        else:
            total = sum(topTriangular[i][j] * result[j] for j in range(i,n)) 
            result[i] = (columnMatris[i]-total)/topTriangular[i][i]
    return result
def resultant(data): # Bulunan Katsayılara göre bizim bulacağımız sonuçlar
    result = []
    for i in range(len(yi)):
        totals = 0
        for j in range(len(data)):
            totals += data[j]*((i+1)**j)
        result.append(totals)
    return result
def E(lastData,firstData): # kolerasyon değerinin hesaplandığı fonksiyon
    totalY = 0
    Sr = 0
    St = 0
    EHata = 0
    n = len(firstData)
    for i in range(n):
        totalY += int(firstData[i])
    averageY = totalY / n # yi'lerin ortalaması
    for j in range(n):
        Sr += (int(firstData[j]) - lastData[j])**2 # Hataların Kareleri Toplamı
        St += (int(firstData[j]) - averageY) ** 2
        EHata += abs(lastData[j] - int(firstData[j]))
    r = sqrt((St - Sr)/St)
    return r 
def FindPolynomial(coefficients,r):
    if len(coefficients) < 7:
            while len(coefficients)!=7:
                coefficients.append(0)
    print(r," kolerasyon değeri ile en uygun polinom denklemi:\n")       
    equation=coefficients[6]*x**6 + coefficients[5]*x**5 + coefficients[4]*x**4 + coefficients[3]*x**3 + coefficients[2]*x**2 + coefficients[1]*x + coefficients[0]
    print(equation,"\n")
    return equation
def PolynomialIntegral(equation):
    a,b=3,len(yi) #180401073 
    deltax = 0.1
    integral = 0
    n = int((b - a) / deltax)
    for _ in range(n):
        integral += deltax * (equation.subs({x:a}) + equation.subs({x:a+deltax})) / 2
        a += deltax
    return integral
def Integral(data):
    a , b = 180401073 % 10 ,len(data) 
    deltaX = 1
    integral = 0
    n = int((b - a) / deltaX)
    for _ in range(n-1):
        integral += deltaX * (data[a] + data[a+deltaX]) / 2
        a += deltaX
    return integral
def main():
    xi = orderedList(yi)
    lastData = [] # Yakınlaştırılma sonucunda elde edilen sonuçların tutulacağı liste
    flaw = [] # 1,2,3,....,6 dereceden polinomlar için hata değerlerinin tutulduğu dizi
    res = [] # Katsayıların tutulduğu dizi
    for i in range(6):
        XilerinToplamı, SonuclarinToplami,zeroMatrix = Matrix(xi, yi, i+1)
        bottomTriangular=Cholesky(XilerinToplamı,zeroMatrix)
        res.append(Result(bottomTriangular,SonuclarinToplami))
    for j in range(6):
        lastData.append(resultant(res[j]))
        flaw.append(E(lastData[j],yi))
        print(j+1,". Dereceden Polinom Kolerasyon Değeri: ",flaw[j])
    flawData,polinom = max((value, index) for index, value in enumerate(flaw))
    print("\nBulunan Sonuçlar için ",polinom+1,". Dereceden Polinom En Uygun Polinomdur.\n")
    equation = FindPolynomial(res[polinom],flawData)
    PolyIntegral = PolynomialIntegral(equation)
    integral = Integral(IntData(yi))
    print(polinom+1,". Dereceden Polinomun 3 ve ",len(yi)," Aralığında Belirli Olan İntegrali :",PolyIntegral)
    print("veriler.txt Dosyasında Bulunan Verilerin 3 ve",len(yi)," Aralığında Belirli Olan İntegrali :",integral)
    f=open('180401073_yorum.txt','w')
    f.write("-----------------------------------------------------\n")
    f.close()
    with open('180401073_yorum.txt','a') as f:
            f.write(f"{polinom+1}. Dereceden Polinomun 3 ve {len(yi)} Aralığında Belirli Olan İntegrali :{str(PolyIntegral)}\n")
            f.write(f"veriler.txt Dosyasında Bulunan Verilerin 3 ve {len(yi)} Aralığında Belirli Olan İntegrali : {integral}\n")
            f.write("-----------------------------------------------------\n")
            f.write("İntegral kısaca belli bir aralıktaki toplam değişimi, ya da biriken değişim miktarını ifade etmek için kullanılır\n")
            f.write("Bu uygulamada 2 farklı işlem ile verilerin integralleri alınmıştır. Birinci işlem verilerin, 1. dereceden\n")
            f.write("6. dereceye kadar olan polinomlara yaklaştırılıp kolerasyon değeri en fazla olan polinomun integrali alınmıştır.\n")
            f.write("Bu işlem yapılırken polinom dikdörtgenlere bölünmüştür. Bu bölünen dikdörtgenlerin alan toplamı integralin\n")
            f.write("Alanını bize vermektedir. Ne kadar az genişliğe sahip dikdörtgenler seçersek doğru sonuca o kadar fazla yaklaşmış\n")
            f.write("olunmaktadır. Burada Ne kadar az genişlik denilen kısım DeltaX ile ifade edilen kısımdır. DeltaX ne kadar 0'a yakın\n")
            f.write("seçilirse sonuç o kadar hassas olur, hesaba katılan dikdörtgenler o kadar fazla olur,taşmalar ve eksiklikler o kadar az olur.\n")
            f.write("Ancak polinomlar yerine veriler kullanılarak hesaplama yapıldığında DeltaX olarak verebileceğimiz değer en az 1 olmaktadır\n")
            f.write("Yani hesaplamayı yaparken bir veriden, bir sonraki veriye hesaplama yapabilmekteyiz.Bu sebeple oluşturulan parçaların\n")
            f.write("taşma veya boşluklar olarak adlandırdığımız doğru sonuçtan uzaklaşmalar daha çok yaşanmaktadır. Bu sebeplerden dolayı\n")
            f.write("iki işlem arasında farklılıklar oluşmaktadır.")
            f.close()
if __name__ == main():
    main()
