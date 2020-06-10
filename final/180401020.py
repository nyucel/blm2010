
# BETÜL İNCE - 180401020

with open("veriler.txt", "r+") as data:
    cases = []
    for line in data:
        cases.append(int(line))
size = len(cases)
sum_cases = sum(cases)
#print(size)

def polynominal(d):
    x_list = []
    size = d + 1
    matrix = [[0 for i in range(d + 1)] for j in range(d + 1)]
    for i in range(len(cases)):
        x_list.append(i + 1)
    for i in range(size):
        for j in range(size):
            for x in x_list:
                matrix[i][j] += pow(x, i + j)
    for i in range(size):
        sum_of_xy = 0
        for j in x_list:
            sum_of_xy += cases[j - 1] * pow(j, i)
        matrix[i].append(sum_of_xy)
    return matrix

def solution_with_gauss(matrix):
    n = len(matrix)
    for i in range(0, n):
        maxCol = abs(matrix[i][i])
        maxRow = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > maxCol:
                maxCol = abs(matrix[j][i])
                maxRow = j
        for j in range(i, n + 1):
            temp = matrix[maxRow][j]
            matrix[maxRow][j] = matrix[i][j]
            matrix[i][j] = temp
        for j in range(i + 1, n):
            c = -matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                if i == k:
                    matrix[j][k] = 0
                else:
                    matrix[j][k] += c * matrix[i][k]
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][n] -= matrix[j][i] * x[i]
    return x

def correlation(comp_list):
    sr = 0
    st = 0
    yavg = sum_cases / size
    for i in range(size):
        sr += (cases[i] - comp_list[i]) ** 2
    for i in range(size):
        st += (cases[i] - yavg) ** 2
    square_r = ((st - sr) / st)
    r = square_r ** (0.5)
    return r

def found_values():
    correlation_values = []
    x_list = []
    coef_list = []
    for i in range(len(cases)):
        x_list.append(i + 1)
    #print(x_list)
    for i in range(1, 7): #1den 6ya kadar polinomlara yaklaştıracak
        comp_list = []
        matrix = polynominal(i) #kaçıncı dereceye yaklaştırıyorsa onun için uygun olan polinom matrisini oluşturuyor
        coef = solution_with_gauss(matrix) #bu matrisi çözümleyip katsayıları buluyor
        coef_list.append(coef)
        sum = 0
        for i in x_list:
            for j in range(len(coef)):
                sum += coef[j] * (i ** j)
            comp_list.append(sum)
            sum = 0
        correlation_values.append(correlation(comp_list))
    # best_correlation'ı şu şekilde bulmayı deneyelim:
    best = correlation_values[0]
    temp = 0
    for i in range(len(correlation_values)):
        if(correlation_values[i] > best):
            best = correlation_values[i]
            temp = i+1
    print("best correlation value is: "+str(best))
    print("optimal polynom is:"+str(temp)+"th order")
    print("coefficients of {}th order polynom : ".format(str(temp)),end = " ")
    return coef_list[temp-1]

coef_of_polynom = found_values()
print(coef_of_polynom) #her polinom için bulunan korelasyon değerlerini bastırır
#best_correlation=sorted(found_values)[-1] #en iyi korelasyon değerini bulur,en düşük hata ile uyan polinomun korelasyon değeri
#print(best_correlation)

def function(coefficients,x):
    func = 0
    for i in range(len(coefficients)):
        func += coefficients[i]*(x**i) #0.katsayı+1.kaysatı*x+2.katsayı*x**2+3.katsayı*x**3+...+6.katsayı*x**6
    return func

a = 10 #18040102(0) --> a = 10
b = len(cases)
def integratingPolynomial(a,b,coef_of_polynom):
    deltax = 10
    integral = 0
    n = int((b-a)/deltax)
    for i in range(n):
        integral += deltax * (function(coef_of_polynom,a)+function(coef_of_polynom,a+deltax))/2 #küçük dikdörtgenler ve büyük dikdörtgenlerin ortasındaki değere göre hesap yapılır
        a += deltax
    print("integral(with polynom) : ",integral)

integratingPolynomial(a,b,coef_of_polynom)

def integratingCases(a,b,cases):
    deltax = 1
    integral = 0
    n = int((b-a)/deltax)
    for i in range(n-1):
        integral += deltax*(cases[a] + cases[a+deltax])/2
        a += deltax
    print("integral(without polynom) : ",integral)

integratingCases(a,b,cases)

with open("180401020_yorum.txt", "w" , encoding="utf-8") as file:
    file.write("    İşlenen verilerin en düşük hata ile uyduğu polinomu ve verileri kullanarak yaptığımız integral hesaplarının birbirinden farklı çıkmasının nedeni: ")
    file.write
    file.write("""
    Yamuk yöntemi(küçük dikdörtgenler ve büyük dikdörtgenlerin ortasındaki değere göre) kullanılarak integral hesabı yapılırken deltax(dikdörtgenin eni) 
    değerini ne kadar küçültürsek küçültelim eğrinin altındaki alanı hiçbir zaman tam olarak bulamayız ama gerçeğe daha yakın bir değer bulmuş oluruz.
    Fakat iki integral arasındaki farkın sebebi deltax değerlerini farklı almamız değil çünkü deltax değerlerini aynı verdiğimde de integral sonucu farklı çıkıyor.
    Dolayısıyla bu farkın asıl sebebi polinoma yaklaştırarak elde edilen değerlerle oluşturulan fonksiyonun integrali alınırken 
    polinomu belirli bir korelasyon değerine göre yakınsatmış olmamızdır.Yani polinom fonksiyonunu kullanarak aldığımız integral daha az hata payı ile değer döndürür.
    """)
