#Yiğitcan ÜSTEK - 160401030
import numpy as np
import math



with open('veriler.txt','r') as f:
  y = f.readlines()

for i in range(len(y)):
  y[i] = int(y[i])

y = np.array(y,dtype=int)
xi = np.array([i for i in range(len(y))])
polynom = [np.poly1d(np.polyfit(xi,y,i)) for i in range(1,7)]


def hata(polinom):
  f1 = open('veriler.txt','r')
  y = f1.readlines()
  f1.close()
  for i in range(len(y)):
    y[i] = float(y[i])
  yi_y = 0 
  y_toplam = sum(y)
  y_ort = y_toplam/len(y)
  e_toplam = 0
  for i in range(1,len(y)+1):
    t1 = y[i-1]-y_ort
    yi_y += pow((t1),2)
    e_toplam +=y[i-1]-polinom[0]
    for j in range(1,len(polinom)):
      e_toplam += -polinom[j]*pow(i,j)
    e_toplam = abs(e_toplam)
  r = math.sqrt(abs(yi_y-abs(e_toplam))) / math.sqrt(yi_y)
  return r






def f(x,y):
  err1 = [hata(polynom[i]) for i in range(6)]
  
  poly = polynom[err1.index(max(err1))-1]
 
  val = poly[0]
  
  for i in range(1,len(poly)):
    
    val += poly[i]*(x**i)
  
  return val

def polinom():
  a = 10
  b = len(y)
  deltax = 0.1
  integral = 0
  n = int((b-a)/deltax)
  for i in range(n-1):
      integral += deltax*((f(a,y)+f(a+deltax,y))/2)
      a += deltax
  return (integral)


def w_polinom():
  a = 10
  b = len(y)
  deltax = 1
  integral = 0
  n = int((b-a)/deltax)
  for i in range(n-1):
      integral+=deltax*(y[a]+y[a+deltax])/2
      a += deltax

  return (integral)


print("Polinom Yakınsaması:" + "{0}".format(polinom()))

print("İntegral Yakınsaması:" + "{0}".format(w_polinom()))




yorum = open('160401030_yorum.txt','w')
yorum.writelines("""Polinomla yaklaşımda ve verilerle yaklaşımda sonuçlarının farklı çıkmasının sebebi deltaX'e bağlıdır.\n
Polinomu kullanarak yaklaşım yaptığımızda deltaX'i çok küçük tutabiliriz ve hata payını deltaX'le doğru orantıyla azaltabiliriz; fakat verilerle yaklaşım yapabilmek için deltaX'in en küçük 1 olması gerekli. Verilerle yaklaşımda aralık fazla olduğu için hata payı yüksek olduğundan dolayı hassaslık polinomla yaklaşmamıza göre daha düşüktür. """)
yorum.close()