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

    
def solveSystem(arr,n):
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
    for i in range(1,7):
        top = 0
        a=[] 
        x = np.zeros(shape=(i+1,i+2),dtype='float32')
        for col in range(len(x)):
             for row in range(i+2):
                 x[col][row] = ekle(col+row,row,len(y),col,i+2)
      
        for val in solveSystem(x,len(x)):
             a.append(val)
       
        with open('sonuc.txt','a') as w:
            w.write(str(i)+". dereceden polinom katsayıları : "+str(a)+"\n")
            
        for b in range(len(y)):
             shatatahmini = 0
             shatatahmini = y[b]
             for c in range(i+1):
                 shatatahmini += -(a[c]*((b+1)**c)) 
             top += shatatahmini**2
        top = top/(len(y)-(i+1))
        top = sqrt(top)
        s.append(top)
        with open('sonuc.txt','a') as w:
            w.write(str(i)+". dereceden polinom hata payı : "+str(top)+"\n")
        if(i==1):
            uygun = s[i-1]
        else:
            if(s[i-1]<uygun):
                uygun = s[i-1]
    for r in range(6):
        if(s[r]==uygun):
            with open('sonuc.txt','a') as w:
                w.write("En uygun polinom "+str(r+1)+". polinomdur.\n")
polinom(y)
k=0
sirali=[]
for i in range(len(y)):
    if((i)%10!=0):
        sirali.append(y[i])
        if(len(y)%10==0 and i == len(y)-1):
            with open('sonuc.txt','a') as w:
                w.write(str(i-9)+"-"+str(i)+" : \n")
            polinom(sirali)
    else:  
        if(i==0):
            sirali.append(y[i])
        else:
            with open('sonuc.txt','a') as w:
                w.write(str(i-10)+"-"+str(i-1)+" : \n")
            polinom(sirali)
            sirali=[]
            sirali.append(y[i])


    