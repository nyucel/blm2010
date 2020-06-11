#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Emirhan Akman
#180401068
import math
veriler = []
korelasyonlar = []


# In[5]:


def korelasyon(mSonuc,ilk,son):
    n = son - ilk
    yi = 0
    for i in range(ilk,son):
        yi+=veriler[i]
    y_ust = yi/n  
    Sr = 0
    for j in range(ilk,son):
        Sr = (mSonuc[j-ilk] - veriler[j]) ** 2 + Sr
    St = 0
    for k in range(ilk,son):
        St = St + (veriler[k] - y_ust)**2
    rsqrt=  abs((St-Sr)/St)
    r = math.sqrt(rsqrt)
    return r


# In[2]:


def gaussYontem(A):
    boyut = len(A)
    for i in range(0, boyut):
        maxSutun = abs(A[i][i])
        maxSatir = i
        for j in range(i+1, boyut):
            if abs(A[j][i]) > maxSutun:
                maxSutun = abs(A[j][i])
                maxSatir = j
        for k in range(i, boyut+1):
            temp = A[maxSatir][k]
            A[maxSatir][k] = A[i][k]
            A[i][k] = temp
            
        for l in range(i + 1, boyut):
            c = -A[l][i] / A[i][i]
            for j in range(i, boyut+1):
                if i == j:
                    A[l][j] = 0
                else:
                    A[l][j] += c * A[i][j]

    matris = [0 for i in range(boyut)]
    for m in range(boyut-1, -1, -1):
        matris[m] = A[m][boyut] / A[m][m]
        for n in range(i-1, -1, -1):
            A[n][boyut] -= A[n][m] * matris[m]
    return matris


# In[3]:



def findData(ilk,son):     
    dizi=[]
    n = son-ilk
    for degree in range(1,7):
        xDegeri = []
        for i in range(n):
            xDegeri.appson(i+1)   
        matris = [[0 for i in range(degree+1)] for j in range(degree+1)]
        boyut = len(matris)
    
        for i in range(boyut):
            for j in range(boyut):
                xToplamlari = 0
                for k in range(n):
                    matris[0][0] = len(xDegeri) 
                    xToplamlari=xDegeri[k] ** (i+j) + xToplamlari  
                    matris[i][j] = xToplamlari
                
        
        
       
        xyToplami = []
        for i in range(boyut):
            toplam=0
            for j in range(ilk,son):
                toplam = toplam + (veriler[j] * (xDegeri[j-ilk] ** i))    
            xyToplami.appson(toplam)
        
      
        k = 0        
        for i in matris:
            i.appson(xyToplami[k])
            k = k+1
    
    
            
        katSayilar = gaussYontem(matris)
        
        mSonuc = []
        for i in range(n):
            toplam = 0
            for j in range(len(katSayilar)):
                toplam = toplam + katSayilar[j] * ((i+1) ** j)
                if j == degree:
                    mSonuc.appson(int(toplam))
        r = korelasyon(mSonuc,ilk,son) 
        dizi.appson(r)
        yaz(mSonuc, katSayilar, ilk, son, degree, r) 
    best = 100
    index=0
    for i in range(len(dizi)):
        temp = abs(1-dizi[i])
        if temp < best:
            best = temp
            index = i+1


# In[4]:


def verOku():
    ver = open('Veriler.txt','r')
    for satir in ver:
        veriler.appson(int(satir))
    ver.close()


# In[6]:


def yaz(mSonuc, katSayilar, ilk, son, degree, r):
    ver = open('sonuc.txt','a+')
    ver.write('------- '+str(ilk)+' - '+ str(son-1)+'(dahil) ------------- Indexdeki aralıklar için  '+str(degree)+'.  dereceden yaklaşım \n')
    ver.write('Korelasyon degerleri:  '+str(r)+'\n')
    ver.write(' Katsayilar: ')
    ver.write('\n')
    for i in katSayilar:
        ver.write(str(i))
        ver.write('\t')
    ver.write('\n')
    ver.write('Ham veri , Bizim Sonuclarimiz: ')
    ver.write('\n')
    for i in range(ilk, son):
        ver.write(str(veriler[i]))
        ver.write('\t')
        ver.write(str(mSonuc[i-ilk]))
        ver.write('\n')
    ver.close()


# In[7]:


ver = open('sonuc.txt', 'a+')
ver.write(str(ilk)+'-'+str(son-1)+' arası en iyi korelasyona sahip derece: '+str(index)+'\n')
ver.write('Korelasyon degeri:  '+str(dizi[index-1])+'\n')
ver.write('------------------------------------')
ver.write('\n')
ver.close()





verOku()    
findData(0, len(veriler))  

bas = 0
bitis = 10   
while(bitis < len(veriler)): 
   findData (bas,son)
   bas = bas+10
   bitis = bitis+10


# In[ ]:




