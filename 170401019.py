# -*- coding: utf-8 -*-
"""
Created on Thu Jun 6 01:20:25 2020

@author: LEGION
"""

#Cengiz Ermis - 170401019 

with open("veriler.txt", "r", encoding='utf-8') as file:
    array = []
    for i in file.read().split():
        array.append(int(i))
uz = len(array)
yToplam = sum(array)


def xitoplam(uz):

    xKareToplam = []
    xKareToplam.append(uz)
    for i in range(1,13):
        value = 0
        for j in range(uz):
            value = value + ((j + 1) ** i)
        xKareToplam.append(value)
    return xKareToplam

def xiyiToplam(uz,array):

    xi_yi_toplam = []
    xi_yi_toplam.append(sum(array))
    for i in range(1 ,7 ,1):
        value = 0
        for j in range(uz):
            value = value + ((j + 1) ** i * array[j])
        xi_yi_toplam.append(value)
    return xi_yi_toplam

#Elementer satır islemleri icin gerekli fonksiyon.

def gaussElimination(mx):

    s = len(mx)
    for i in range(0 ,s):
        max = abs(mx[i][i])
        maxRow = i
        for t in range(i + 1 ,s):
            if (abs(mx[t][i]) > max):
                max = abs(mx[t][i])
                maxRow = t
        for t in range(i ,s + 1):
            temp = mx[maxRow][t]
            mx[maxRow][k] = mx[i][t]
            mx[i][t] = temp
        for t in range(i + 1 ,s):
            c = -mx[t][i] / mx[i][i]
            for j in range(i ,n + 1):
                if i == j:
                    mx[t][j] = 0
                else:
                    mx[t][j] = mx[t][j] + (c * mx[i][j])
    result = [0 for i in range(s)]
    for i in range(s-1 ,-1 ,-1):
        result[i] = mx[i][s] / mx[i][i]
        for t in range(i-1 ,-1 ,-1):
            mx[t][s] = mx[t][s] - (mx[t][i] * result[i])
    return result

#Matrisi olusturma.

def createMx(uz ,array ,m):

    x , y = xitoplam(uz) , xiyiToplam(uz ,array)
    mx , row = [] , 0
    for i in range(0,m):
        eklenecekSatir=[]
        for i in range(row ,m+row):
            eklenecekSatir.append(x[i])
        eklenecekSatir.append(y[row])
        row += 1
        mx.append(eklenecekSatir)
    return mx


#Matrisi cagırma ve ekleme yapma.

def call(array):

    x = []
    for i in range(2,8):
        x.append(gaussElimination(createMx(len(array),array,i)))
    return x
mx = call(array)


def calculateCorrelation(x ,array ,n):

    sr = 0
    st = 0
    yToplam=sum(array)
    y = yToplam / n
    size = len(x)
    for i in range(n):
        temp = 0
        for j in range(size):
            if j == 0:
                temp = temp + x[j]
            else:
                temp = temp + (x[j]*(i+1)**j)
        sr = sr + ((array[i]-temp)**2)
        st = st + ((array[i]-y)**2)
    result = ((st-sr)/st)**(1/2)
    return result


array = []
for i in range(0,6):
    x = calculateCorrelation(mx[i],array,uz)
    array.append(x)
lastArray = sorted(array)


def bestCorrelation(correlation):
    supreme = max(correlation)
    counter = 1
    while(supreme!=correlation[counter - 1]):
        counter = counter + 1
    return counter

pol = mx[bestCorrelation(array) - 1]
def f(x,pol):
    return(pol[0] + pol[1]*x + pol[2]*x**2 + pol[3]*x**3 + pol[4]*x**4 + pol[5]*x**5 + pol[6]*x**6)


def polinomluIntegral(array):

    a=9
    b=len(array)
    deltax = 0.1
    integral = 0
    n = int((b - a)/deltax)
    for i in range(n):
        integral = deltax * (f(a) + f(a+deltax)) / 2+integral
        a = a + deltax
    return integral

def polinomsuzIntegral(array):
    a = 9
    b = len(array)
    deltax = 1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n-1):
        integral += deltax * (array[a] + array[a + deltax]) / 2
        a = a + deltax
    return integral
print("Polinomlu integral : ",polinomluIntegral(array))
print("Polinomsuz integral : ",polinomsuzIntegral(array))


with open("170401019_yorum.txt","w",encoding='utf-8') as file:
    file.write("Cengiz Ermis 170401019 \n")
    file.write("İntegral sonuçlarının farklı çıkma sebebi deltax'e verilen değerden kaynaklanır.\n" )
    file.write("Eğer deltax'i küçültürsek hesaplanan alan artacaktır bu sebeple hesaplanan değer gerçeğe daha yakınlaşmış olur.\n")
    file.write("Bu yüzden polinomlu integral gerçeğe daha yakın bir sonuç verir. \n")
    file.write("Polinomsuz hesaplamada istediğimiz kadar parçaya bölemediğimiz için  hata oranı daha fazladır.\n")

