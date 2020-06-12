#!/usr/bin/env python
# coding: utf-8

# In[38]:


#GÖKÇE NUR SARICI
#170401032

with open("veriler.txt","r",encoding='utf-8') as file: #dosyadan verileri okuma yapıyorum
    vakalar = [] 
    for i in file.read().split():
        vakalar.append(int(i))
    print(vakalar)


# In[53]:


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


# In[54]:


def xi(derece): #Günlerin toplamı gibi düşünebiliriz
    xkare=[]
    xkare.append(derece)
    for i in range(1,13): #formul x^2m ile bitiyor 6*2=12
        q=0 #her satır için sıfırlıyor denklemleri oluşturmak adına
        for j in range(derece):
            q+=(j+1)**i
        xkare.append(q)
    return xkare
    


# In[55]:


def xiyi(vakalar,derece):
    xiyi=[]
    xiyi.append(sum(vakalar))
    for i in range(1,7,1): #formulde xiyinin derecesi m ile bitiyor.
        q=0
        for j in range(derece):
            q+=(j+1)**i*vakalar[j]
        xiyi.append(q)
    return xiyi


# In[59]:


def matris(derece,vakalar,sayac):
    x=xi(derece)
    y=xiyi(vakalar,derece)
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


# In[60]:


def matrisOlustur(vakalar): #Katsayılar matrisini gauss ile çözdürüp asıl matrisimi oluşturdum
    matrix=[]
    for i in range(2,8):
        matrix.append(gaussYontemi(matris(len(vakalar),vakalar,i)))
    return matrix


# In[110]:


m=matrisOlustur(vakalar) #Derecelere yakınlaştırıp elde ettiğim katsayılar matrisi
#print(m)


# In[111]:


def korelasyon(matris,vakalar,uzunluk):#asıl değerler ile bizim bulduklarımızı bu fonksiyona sokup hata değeri hesaplatıyoruz
    st,sr=0,0
    yi=sum(vakalar) #vakalar toplamı
    yort=yi/uzunluk #vakalar ortalama
    sizeofmatris=len(matris) #matrisin uzunluğu
    for i in range(uzunluk):
        gecici=0
        for j in range(sizeofmatris):
            if j==0:
                gecici+=matris[j]
            else:
                gecici+=matris[j]*(i+1)**j
        sr+=(vakalar[i]-gecici)**2
        st +=(vakalar[i]-yi)**2
    r=((st-sr)/st)**(1/2)
    return r

liste=[]
for i in range(0,6): #6.dereceye kadar pol
    correlation=korelasyon(m[i],vakalar,len(vakalar))#Herbir hata payını listeye attık ki en uygun korelasyonu seçelim
    liste.append(correlation)
print(liste)
            
    


# In[120]:


def enIyiKorelasyon(correlation): #1'e en yakın olanı almalıyız.
    correlationMax=max(correlation)
    i=1
    while(correlationMax!=correlation[i-1]):
        i+=1
    return i


# In[121]:


eniyi=enIyiKorelasyon(liste)
print(eniyi)


# In[127]:


pol=m[enIyiKorelasyon(liste)-1]
def f(x,pol):
    return(pol[0] + pol[1]*x + pol[2]*x**2 + pol[3]*x**3 + pol[4]*x**4 + pol[5]*x**5 + pol[6]*x**6)


# In[123]:


a=2 #170401032
b=len(vakalar)


# In[134]:


def withPolynomial(a,b,pol):
    deltax=0.1
    integral=0
    n=int((b-a)/deltax)
    for i in range(n):
        integral=deltax*(f(a,pol)+f(a+deltax,pol)) / 2+integral
        a+=deltax
    return integral


# In[137]:


def withoutPolynomial(a,b,vakalar):
    deltax=1
    integral=0
    n=int((b-a)/deltax)
    for i in range(n-1):
        integral+=deltax*(vakalar[a]+vakalar[a+deltax])/2
        a+=deltax
    return integral


# In[138]:


print("Polinomlu integral sonucu  : ",withPolynomial(a,b,pol))
print("Polinomsuz integral sonucu : ",withoutPolynomial(a,b,vakalar))


# In[146]:


with open("170401032_yorum.txt","w",encoding='utf-8') as file:
    file.write("***********Gökçe Nur Sarıcı*********** 170401032 \n\n\n")
    file.write("Polinomlu ve Polinomsuz İntegralin farklı çıkmasının nedenleri: \n\n")
    file.write("integrali hesaplarken eğrinin altında kalan alanı küçük diktorgenlere ayırıp alanlarının hesaplarını toplarız. \n")
    file.write("Dikdörtgen sayısı küçüldükçe gerçek değere daha çok yaklaşmış oluruz.\n")
    file.write("Böldüğümüz dikdörtgenlerin eni deltax'tir.")
    file.write("Dikdörtgenlerin eni küçüldükçe dikdörtgen sayısı artacak doğru orantılı olarak hassasiyette artacaktır.")          
    file.write("\nPolinomlu da deltax değeri ile oynayabiliyoruz fakat polinomsuzda deltax'i 1 olarak alıyoruz.\nYani istediğimiz kadar dikdörtgene bölemiyoruz.\n")
    file.write("Bu sebepten Polinomlu ile Polinomsuz İntegralın sonuçları farklı değerlerdir.\n")
    file.write("Bu bilgiler doğrultusunda POLİNOM İNTEGRALİnin sonucu beklenen sonuca daha yakın olur.")


# In[ ]:




