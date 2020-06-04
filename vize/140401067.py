#Yeşim Şekerciler-140401067
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
    sumy += int(i)
  
  x_list = [0 for i in range(derece*2+1)]
  xi = 0
  for i in range(derece*2+1):
    for j in range(n):
      xi += pow(j+1,i)
    x_list[i] = xi
    xi = 0
  a = [[0 for i in range(derece+1)] for i in range(derece+1)] #ax = b tipindeki denklemin x değerlerini içeren matris
  c = [0 for i in range(derece+1)] #ax = b tipindeki denklemin b değerleri
  c[0] = sumy
  for i in range(1,derece+1):
    c[i] = int(x_list[i] * sumy)

  for i in range(derece+1):
    for j in range(derece+1):
      a[i][j] = int(x_list[j+i])
    a[i].append(c[i])
  return gauss(a)


def err(y,polinom):
  for i in range(len(y)):
    y[i] = float(y[i])

  err = []
  err_ = 0
  hata = []
  for i in range(len(y)):
    err_ = polinom[0]
    for j in range(1,len(polinom)):
      err_ += pow(polinom[j],j)
    err.append(err_)

  for i in range(len(y)):
    hata.append(abs((abs(err[i])-y[i])/err[i]))  
  
  return (sum(hata)/len(y))

  



with open('veriler.txt','r') as f:
  y = f.readlines()


err1 = [err(y,polinom(y,i)) for i in range(1,7)]


with open('sonuc.txt','w') as f1:
  for i in range(1,7):
    f1.writelines("%s. dereceden polinom\n" % i)
    f1.writelines("{0}\n".format(polinom(y,i)))
    f1.writelines("{0}. dereceden polinomun r değeri:{1}\n\n".format( i , err(y,polinom(y,i))))
    
  f1.writelines("\n")
  f1.writelines("En uygun polinom:{0}. dereceden polinom\nr değeri:{1}\n".format(err1.index(max(err1))+1,max(err1)))
  for j in range(0,len(y),10):
    for i in range(1,7):
      f1.writelines(("{0}. dereceden polinom {1} ile {2} verileri arası\n").format(i,j,j+10))
      f1.writelines("{0}\n".format(polinom(y[j:j+10],i)))
      f1.writelines("{0} ile {1} verileri arası {2}. dereceden polinomun r değeri:{3}\n\n".format( j,j+10,i , err(y[j:j+10],polinom(y[j:j+10],i))))




