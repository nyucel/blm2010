#Yeşim Şekerciler - 140401067

import math



def gauss(r):
  
  lenrow = len(r)   
  lencol = len(r[0]) 
  m = lenrow-1
  k = 0
  z = 0
  for j in range(lenrow):
    m = lenrow-1
    k = j
    z = j
    for i1 in range(lenrow-1):
      if (r[j][k]==0):
        continue
      coeff = r[m][z] / r[j][k]
      for i in range(lencol):
            x = r[j][i]
            if x == r[m][i]:
              continue
            r[m][i] -= coeff*x
      m-=1
    k +=1
    z +=1
  for i in range(1,lenrow):
    if (r[0][i]==0):
      continue
    coeff = r[i][i]/r[0][i]
    for j in range(lencol):
      r[0][j] -=  (r[i][j]/coeff)
  for i in range(lenrow-1,-1,-1):
    for j in range(lencol-1,-1,-1):
      if j != lencol-1:
        r[i][j] = int(r[i][j]/r[i][i])
        continue
      r[i][j] /= r[i][i] 

  a = []
  for i in range(lenrow):
    a.append(r[i][lencol-1])
  return a


def polinom(y,derece):
  sumy = 0
  list1 = y
  n = len(list1)
  
  for i in list1:
    sumy += float(i)
  
  x_list = [0 for i in range(derece*2+1)]
  xi = 0
  for i in range(derece*2+1):
    for j in range(0,n):
        xi += pow(j,i) 
    x_list[i] = xi
    xi = 0
  
  a = [[0 for i in range(derece+1)] for i in range(derece+1)] #ax = b tipindeki denklemin x değerlerini içeren matris
  c = [0 for i in range(derece+1)] #ax = b tipindeki denklemin b değerleri
  
 
  for i in range(0,derece+1):
    for j in range(1,n):
      c[i] += pow(j,i)*float(list1[j]) #int(x_list[i]*sumy)
  
  for i in range(derece+1):
    for j in range(derece+1):
      a[i][j] = float(x_list[j+i])
    a[i].append(c[i])

  return gauss(a)


def err(y,polinom):
  for i in range(len(y)):
    y[i] = float(y[i])
  y_ = sum(y) / len(y)
  val_y = 0
  for i in range(len(y)):
    val_y += pow(y[i]-y_,2)
  err_ = 0
   
  for i in range(0,len(y)):
    err_ = y[i]-polinom[i%len(polinom)]
    for j in range(1,len(polinom)):
      err_ -= polinom[j]*pow(i,j)
  return math.sqrt(abs(val_y-abs(err_))/val_y)  



def f(x):
  f1 = open('veriler.txt','r')
  y = []
  for data in f1.readlines():
    y.append(data)
  f1.close()
  err1 = [err(y,polinom(y,i)) for i in range(1,7)]
  
  poly = polinom(y,err1.index(max(err1))+1)
  
  val = poly[0] 
  for i in range(1,len(poly)):
    val += poly[i]*pow(x,i)
  return val

def poly_integrate():
  f2 = open('veriler.txt','r')
  y = []
  for data in f2.readlines():
    y.append(data)
  f2.close()
  a = 7
  b = len(y)
  deltax = 0.5
  integral = 0
  n = int((b-a)/deltax)
  for i in range(n-1):
    integral += deltax*(f(a)+f(a+deltax))/2
    a += deltax

  return(integral)
  
def integrate():
  f1 = open('veriler.txt','r')
  y = f1.readlines()
 
  
  for i in range(0,len(y)):
    y[i] = float(y[i])
    
  f1.close()
  a = 7
  b = len(y)
  deltax = 1
  integral = 0

  n = int((b-a)/deltax)

  for i in range(n-1):
    integral += deltax*(y[a]+y[a+deltax])/2
    a += deltax

  return(integral)



print("Polinomun integral değeri:{0}".format(poly_integrate()))
print("Verilerin İntegral Değeri:{0}".format(integrate()))



f1 = open('140401067_yorum.txt','w')
f1.write("""Dikdörtgen yönteminde, DeltaX noktasından da x eksenine paralel doğru çizilerek ikinci dikdörtgen dilim elde edilir.\n Bu şekilde devam edilerek her noktadan x eksenine paralel doğrular çizilir ve dikdörtgen dilimler elde edilir.\n Yani, DeltaX ne kadar küçültülürse, işleme katılacak alan sayısı artar ve gerçeğe daha yakın değerler elde edilir ama işlem süresi uzar.\n Polinomla yapılan işlemler yakınsama yoluyla yapıldığından sonuçlar farklı çıkmaktadır.""")
f1.close()
