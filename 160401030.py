import math


def y_hesap(dataset):       #Verileri y dizisine aktarmaya sağlayan fonksiyon
  y = []
  with open(dataset) as f:  
    for lines in f:
      y.append(float(lines))
  #print( sum(y) / len(y))
  return y



def polynomial(dataset,degree):   #polinom yaklaşımını yapan fonksiyon
  a = []
  x = [0]*((degree*2)+1)
  y = y_hesap(dataset)
  n = len(y)

  c = [0]*(degree+1)
  denklem = [[0]*(degree+1)] * (degree+1)
  x[0] = n

  for j in range(0,degree+1):
    for k in range(0,n):
      c[j] += pow(k,j)*y[k]

  for j in range(1,degree*2+1):
    for k in range(1,n+1):
      x[j] += pow(k,j)
             
  
  for j in range(1,degree+2):
    
    for k in range(0,degree+1):
      a.append(x[k+j-1])
    a.append(c[j-1])  
    denklem[j-1] = a
    a = []
  return gauss(denklem)  


def polynomial1(y,degree):  #Diğer polinom yaklaşımı fonksiyonundan farkı komple veri setini almaması, belirli veri grubunu alması
  a = []
  x = [0]*((degree*2)+1)
 

  n = len(y)

  c = [0]*(degree+1)
  denklem = [[0]*(degree+1)] * (degree+1)
  x[0] = n

  for j in range(0,degree+1):
    for k in range(0,n):
      c[j] += pow(k,j)*y[k]

  for j in range(1,degree*2+1):
    for k in range(1,n+1):
      x[j] += pow(k,j)
             
  
  for j in range(1,degree+2):
    
    for k in range(0,degree+1):
      a.append(x[k+j-1])
    a.append(c[j-1])  
    denklem[j-1] = a
    a = []
  return gauss(denklem)  
 



def gauss(ar):     

  n = len(ar)
  #Alt üçgen matrisi 0'layan kod parçası
  for i in range(0, n):
    for k in range(i + 1, n):
      c = -ar[k][i] / ar[i][i]          
      for j in range(i, n + 1):           
          if i != j:
              ar[k][j] += c * ar[i][j]
   #Üst üçgen matrisi çözüp köşegen matrisi elde ediyoruz
  x = [0 for i in range(n)]
  for i in range(n - 1, -1, -1):
      x[i] = ar[i][n] / ar[i][i]         
      for k in range(i - 1, -1, -1):
          ar[k][n] -= ar[k][i] * x[i]
  return x




def hata(polinom,y):
  #y = y_hesap("veriler.txt")
  #y verisetini alıp bu verisetinde hata payını hesaplayan fonksiyon
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
  r = math.sqrt(abs(yi_y-e_toplam)) / math.sqrt(yi_y)
  return r




def yazdir(n):
  polinom = []
  polinom1 = []
  er = []
  er1 = []
  k = 0
  y = y_hesap('veriler.txt')

  f = open("sonuc.txt","w")

  for i in range(1,n+1):
    polinom.append(polynomial('veriler.txt',i))
    f.writelines("{0}.dereceden polinomun\n".format(i))
    for j in range(0,i+1):
      f.writelines("\t{0}.katsayısı:{1}\n".format(j+1,polinom[i-1][j]))
    
    er.append(hata(polinom[i-1],y_hesap('veriler.txt')))
    f.writelines("r değeri:{0}\n".format(er[i-1]))
    f.writelines("\n")
  
  f.writelines("En uygun polinom\n")
  f.writelines("{0}.dereceden polinom\nr değeri:{1}\n".format(er.index(max(er))+1,max(er)))
  f.writelines("\n")
  j = 1
  while (k*10 < len(y)):
    f.writelines("{0} ile {1} verilerin polinomları\n".format(k*10,(k+1)*10))
    for i in range(1,n+1):
      f.writelines("\t{0}.dereceden polinom\n".format(i))
      polinom1.append(polynomial1(y[k*10:(k+1)*10],i))
      for j in range(0,i+1):
        f.writelines("\t\t{0}.katsayısı:{1}\n".format(j+1,polinom1[i-1][j]))
      f.writelines("\tr değeri:{0}\n".format(hata(polinom1[i-1],y[k*10:(k+1)*10])))
      er1.append(hata(polynomial1(y[k*10:(k+1)*10],i),y[k*10:(k+1)*10]))
      j+=1
    
    f.writelines("\n\n")
    f.writelines("En uygun polinom\n")
    f.writelines("{0}.dereceden polinom\nr değeri:{1}\n".format(er1.index(max(er1))+1,max(er1)))
    f.writelines("\n")
    polinom1.clear()
    er1.clear()
    j=1
    k+=1
  
  f.close()



yazdir(6)
