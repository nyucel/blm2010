# Kutay KALMAZ  180401025

from sympy import Symbol

def convenientPolyDegree(coefficients):
    max_e = max(coefficients)
    for i in range(len(coefficients)):
        if coefficients[i] == max_e:
            degree = i
    return degree


def findPIntegral(polys,a,b):
    x = Symbol('x')
    p = 0
    for i in range(len(polys)):
        p += polys[i] * (x ** i) 
    integral = 0
    delta_x = 1
    n = int((b-a)/delta_x)
    for j in range(n):
        integral += delta_x * (p.subs({x: a}) + p.subs({x: a+delta_x}))/2
        a += delta_x
    return integral,p


def integrating_withoutPoly(datas):
    a,b=1,len(datas) 
    integral = 0
    delta_x = 1
    n = int((b-a)/delta_x)
    for i in range(n-1):
        integral += delta_x * (datas[a] + datas[a+delta_x])/2
        a += delta_x
    return integral


def interpolation(pdegree,y): 
    matrix = []
    temp = 0
    for i in range(pdegree+1): 
        row = []
        for j in range(pdegree+1):
            sum = 0
            for k in range(1,len(y)+1):
                sum += k**temp
            row.append(sum)
            temp += 1
        matrix.append(row)
        temp -= pdegree
    results = []
    
    for i in range(pdegree+1):
        sum = 0
        for j in range(len(y)):
            sum += y[j]*(j+1)**i
        results.append(sum)
        
    for i in range(pdegree+1): # alt ucgensel
        b = matrix[i][i]
        for j in range(i+1,pdegree+1):
            part = b/matrix[j][i]
            results[j] = results[j]*part-results[i]
            for k in range(pdegree+1):
                matrix[j][k] = matrix[j][k]*part-matrix[i][k]  
                
    for i in range(pdegree,-1,-1): # ust ucgensel
        b = matrix[i][i]
        for j in range(i-1,-1,-1):
            part = b/matrix[j][i]
            results[j] = results[j]*part-results[i]
            for k in range(pdegree+1):
                matrix[j][k] = matrix[j][k]*part-matrix[i][k]
                
    for i in range(pdegree+1):
        results[i] = results[i]/matrix[i][i]
        
    yOrt=0
    for i in range (len(y)):
        yOrt += y[i]
    yOrt = yOrt/len(y)
    sumT, sumR = 0, 0
    for i in range(len(y)):
        x = y[i]
        sumT +=(y[i]-yOrt)**2
        for j in range(len(results)):
            x -= results[j]*(i+1)**j
        x=x**2
        sumR += x
    correlation = ((sumT-sumR)/sumT)**(1/2)
    return results,correlation


file = open("veriler.txt","r")
y = file.readlines()
valueA = 5  # 180401025 --> (5)
valueB = len(y)
for i in range(len(y)):
    y[i]=int(y[i])
polynoms, correlations = [0] * 6, [0] * 6
for indis in range(0, 6):
    polynoms[indis], correlations[indis] = interpolation(indis+1, y)
file.close()

eligiblePolyDegree = convenientPolyDegree(correlations)
print("En uygun polinom derecesi : ",eligiblePolyDegree+1)
IntegralwPoly, polynomial = findPIntegral(polynoms[eligiblePolyDegree],valueA,valueB)
print("\nKullanilan polinom : ", polynomial)
print("\nPolinomlu integral : ",IntegralwPoly)
notPoly_integrating = integrating_withoutPoly(y)
print("\nPolinomsuz integral : ",notPoly_integrating)


def commentFunction(file):
    comment = """Kutay Kalmaz 180401025 \n
Polinom yardımı ile delta_x' i küçülterek alanı genişletebildiğimiz için tarama alanı büyüyor. \n
Yani integral hesabı yapılırken polinom küçük dikdörtgenlere bölünerek alan toplamları hesaplanıyor. \n
Aldığımız dikdörtgenin eni ne kadar küçükse o kadar doğru alan hesabı ve o kadar doğru değer elde etmiş oluyoruz. \n
Bu nedenle polinomlu hesaplama, polinomsuz hesaplamaya göre daha gerçekçi sonuçlar karşımıza çıkarıyor. \n
              """
    with open(file,"w") as commentFile:
        commentFile.write(comment)

    
commentFunction('180401025_yorum.txt')
