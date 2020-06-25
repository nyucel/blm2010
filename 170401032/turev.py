#!/usr/bin/env python
# coding: utf-8

# In[1]:


#600'den küçük asal sayılar;
primeNumbers=[]
for num in range(2,600):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        primeNumbers.append(num)
print(primeNumbers)


# In[2]:


file=open('asallar.txt', 'w')
for i in range(len(primeNumbers)):
    satir=str(primeNumbers[i])
    file.write(satir)
    file.write("\n")


# In[3]:


with open("asallar.txt","r",encoding='utf-8') as file: #dosyadan verileri okuma yapıyorum
    primes = [] 
    for i in file.read().split():
        primes.append(int(i))


# In[4]:


def gaussYontemi(matris):
    n = len(matris)
    for i in range(0, n):
        max = abs(matris[i][i])
        maxSatir = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) > max:
                max = abs(matris[k][i])
                maxSatir = k
        for k in range(i, n + 1):
            tmp = matris[maxSatir][k]
            matris[maxSatir][k] = matris[i][k]
            matris[i][k] = tmp
        for k in range(i + 1, n):
            c = -matris[k][i] / matris[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matris[k][j] = 0
                else:
                    matris[k][j] += c * matris[i][j]
    sonuc = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        sonuc[i] = matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * sonuc[i]
    return sonuc


# In[5]:


def xi(uzunluk):
    xkare=[]
    xkare.append(uzunluk)
    for i in range(1,7): #2m=3*2=6
        deger=0
        for j in range(uzunluk):
            deger += (j + 1) ** i
        xkare.append(deger)
    return xkare
print(xi(len(primes)))


# In[6]:


def xiyi(uzunluk,primes):
    xiyi=[]
    xiyi.append(sum(primes))
    for i in range(1,4,1): #formulde xiyinin derecesi m ile bitiyor.
        q=0
        for j in range(uzunluk):
            q+=(j+1)**i*primes[j]
        xiyi.append(q)
    return xiyi
print(xiyi(len(primes),primes))


# In[7]:


def matris(uzunluk,primes,sayac):
    x=xi(uzunluk)
    y=xiyi(uzunluk,primes)
    matris=[]
    satir=0
    for i in range(0,sayac):
        newsatir=[]
        for i in range(satir,sayac+satir):
            newsatir.append(x[i])
        newsatir.append(y[satir])
        satir+=1
        matris.append(newsatir)
    return matris


# In[8]:


#Gauss Yöntemi ile çözülmüş asıl matrisim
def matrisOlustur(primes):
    matrix=[]
    matrix.append(gaussYontemi(matris(len(primes),primes,4)))
    return matrix


# In[9]:


m=matrisOlustur(primes) 
a0=m[0][0]
a1=m[0][1]
a2=m[0][2]
a3=m[0][3]
print("a0 =",a0,"\na1=",a1,"\na2=",a2,"\na3=",a3)
mm=[] #Tek boyutlu diziye indirgedim
mm.append(a0)
mm.append(a1)
mm.append(a2)
mm.append(a3)
mm


# In[10]:


def korelasyon(matris,primes,uzunluk):#asıl değerler ile bizim bulduklarımızı bu fonksiyona sokup hata değeri hesaplatıyoruz
    st,sr=0,0
    yi=sum(primes) #asal sayılar toplamı
    yort=yi/uzunluk #asallar ortalama
    sizeofmatris=len(matris) #matrisin uzunluğu
    for i in range(uzunluk):
        gecici=0
        for j in range(sizeofmatris):
            if j==0:
                gecici+=matris[j]
            else:
                gecici+=matris[j]*(i+1)**j
        sr+=(primes[i]-gecici)**2
        st +=(primes[i]-yi)**2
    r=((st-sr)/st)**(1/2)
    return r


# In[11]:


correlation=korelasyon(mm,primes,len(primes))
print(correlation)


# In[12]:


a=32 #170401032/ Son iki basamak kullanıldı.
def f(x):
    return (a0+a1*x+a2*(x**2)+a3*(x**3))
print(f(32))


# In[13]:


#Geri Sonlu Farklar Yöntemini kullandım
def turev(a):
    x0=a 
    h=0.001
    xprime=(f(x0)-f(x0-h))/h
    print("Polinomun x=32 noktasında türevi: ",xprime)
print(turev(a))


# In[14]:


def turev2(a):
    x0 = a - 1
    h = 1
    xprime = (primeNumbers[x0+h]-primeNumbers[x0])/h
    print("Polinomsuz x=32 noktasında türevi: ",xprime)
print(turev2(a))


# In[15]:


def yorum():
    f = open("yorum.txt","w",encoding="UTF-8")
    f.write("""AD: Gökçe Nur\nSOYAD: Sarıcı""")
    f.write("""\nNUMARA:170401032\n""")
    f.write("""\nPolinomlu ile Polinomsuz Türev Fonksiyonlarının Farklı Sonuçlar Vermesinin Sebebi:""")
    f.write("""\n\nPolinomlu Sayısal Türev: Aralığı istediğimiz ölçüde azaltabiliriz.Daha hassas bir ölçüm yaparız. Bu sebeple gerçek sonuca daha yakın bir sonuc elde edebiliyoruz.""")
    f.write("""\n\nPolinomsuz Sayısal Türev: Aralığı istediğimiz değerlerde tutamıyoruz.Mühim olan h değil değerdir. Bu yuzden Polinomlu Sayısal Türevden farklı bir sonuç elde ediyoruz.""")
    f.close()


# In[16]:


yorum()


# In[ ]:




