#Oğulcan Demirbilek 180401061
import numpy as np
from math import sqrt
with open('veriler.txt', 'r') as r: 
        y = r.read().split('\n') 
if y[-1]=='':y.pop()
for i in range(len(y)):
    y[i] = int(y[i])

def echelon(arr,n):
        for col in range(n): 
            if arr[col][col] == 0:
                for lower_cells in range(col+1,n):
                    if arr[lower_cells][col] != 0: 
                        arr[col] = arr[col] + arr[lower_cells]
                        break
                    
            for row in range(col+1,n): 
                elim_ratio = arr[row][col] / arr[col][col] 
                arr[row] = arr[row] - elim_ratio * arr[col]
                
    
def reducedEchelon(arr,n):
        echelon(arr,n)
        for col in reversed(range(n)):
            if arr[col][col] == 0:
                for upper_cells in reversed(range(col+1,0)):
                    if arr[upper_cells][col] != 0:
                        arr[col] = arr[col] + arr[upper_cells]
                        break
                               
            for row in reversed(range(col)): 
                elim_ratio = arr[row][col] / arr[col][col] 
                arr[row] = arr[row] - elim_ratio * arr[col]

    
def solveSystem(arr):
        n = len(arr)
        reducedEchelon(arr,n)
        for idx, row in enumerate(arr):
            yield row[-1]/row[idx] 
        return arr

def ekle(cr,r,n,c,i):
    top=0
    if(r==i-1):
        for t in range(n):
             top += y[t]*((t+1)**c)
        return top
    else:
        if(cr==0):
            return n
        for t in range(n):
             top += (t+1)**cr  
        return top

def polinom(y):
    s=[]
    yortalama = sum(y)/len(y)
    der=0
    for i in range(1,7):
        top = 0
        a=[] 
        x = np.zeros(shape=(i+1,i+2),dtype='float64')
        for col in range(len(x)):
             for row in range(i+2):
                 x[col][row] = ekle(col+row,row,len(y),col,i+2)

        for val in solveSystem(x):
             a.append(val)
       
        for b in range(len(y)):
             shatatahmini = y[b]
             for c in range(i+1):
                 shatatahmini += -(a[c]*((b+1)**c)) 
             top += shatatahmini**2
        top = top/(len(y)-(i+1))
        top = sqrt(top)
        s.append(top)
        if(i==1):
            uygun = s[i-1]
        else:
            if(s[i-1]<uygun):
                uygun = s[i-1]
    for r in range(6):
        if(s[r]==uygun):
            der = r+1
    return der

def polinomKatsayisi(der,y):
    a=[]
    x = np.zeros(shape=(der+1,der+2),dtype='float64')
    for col in range(len(x)):
         for row in range(der+2):
             x[col][row] = ekle(col+row,row,len(y),col,der+2)
      
    for val in solveSystem(x):
         a.append(val)
    return a
 
def f(x,der,a):
    topf = 0
    for i in range(der+1):
        topf += a[i]*(x**i)
    return(topf)

def f1(x):
    return(y[x-1])

der = polinom(y)
katsayilar = polinomKatsayisi(der,y)
a = 1
b = len(y)
deltax = 0.001
integral = 0
n = int((b-a)/deltax)
for i in range(n):
    integral += deltax*(f(a,der,katsayilar)+f(a+deltax,der,katsayilar))/2
    a += deltax
print("Polinom kullanarak alınan integral sonucu : "+str(integral))

x0 = 1
x1 = len(y)
h = 1
y0 = y[0]
while(x0<x1):
    y0 += (f1(x0)+f1(x0+h))*h/2
    x0 += h
print("Polinom kullanmadan verileri kullanarak alınan integral sonucu : "+str(y0))

with open('180401061_yorum.txt','a') as w:
                w.write("Bulduğumuz iki integral sonucunun farklı çıkmasının sebebi;\n")
                w.write("Polinom fonk. kullanarak aldığımız integralin daha az hata payı ile değer döndürmesi.\n")
                w.write("Bunun nedeni ise, deltax(dikdörtgenin eni)'i küçük bi sayı aldığımız için alanını hesaplayacağımız dikdörtgenler de çoğalmış olur ve yüksek hassasiyet ile değer döndürür.\n")
                w.write("Polinom fonk. kullanmadan alınan integral de deltax'i 1 belirlediğimiz için alanı daha az parçaya böler ve daha az hassasiyet ile değer döndürür.\n")
                w.write("Polinom fonk. kullanmadan alınan integral de deltax'i 1 almamızın nedeni ise verilerin birer birer artması ara bir değeri almamasıdır.")
