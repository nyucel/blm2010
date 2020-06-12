
# coding: utf-8

# In[65]:


#cemre doğan 170401017
with open("veriler.txt","r",encoding='utf-8') as file: #dosya okuma
    vaka_liste = [] 
    for i in file.read().split():
        vaka_liste.append(int(i))
        
#print(vaka_liste)
uzunluk=len(vaka_liste)
ytoplam=sum(vaka_liste)
#print(uzunluk)
#print(ytoplam)

import math
def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


#dereceye göre x toplamları hesabı 
def xitoplam(uzunluk):
    xkaretoplam=[]
    xkaretoplam.append(uzunluk)
    for i in range(1,13):
        a=0
        for j in range(uzunluk):
            a+=(j+1)**i
        xkaretoplam.append(a)
    return xkaretoplam
  
#dereceye göre xiyi toplam hesabı
def xiyitoplam(derece,liste):
    xiyi = []
    xiyi.append(sum(liste))
    for i in range(1,7,1):
        a=0
        for j in range(derece):
            a+=(j+1)**i*liste[j]
        xiyi.append(a)
    return xiyi
#polinom derecesine göre matris oluştur
def make_matrix(derece,liste,m):
    
    x_=xitoplam(derece)
    y_=xiyitoplam(derece,liste)
    matris=[]
    row=0
    for i in range(0,m):
        newrow=[]
        for i in range(row,m+row):
            newrow.append(x_[i])
        newrow.append(y_[row])
        row+=1
        matris.append(newrow)
    return matris
#g=gauss(matrisOlustur(4,vaka_liste))
#print(g)
def matrix_(liste):
    m=[]
    for i in range(2,8): 
        m.append(gauss(make_matrix(len(vaka_liste),vaka_liste,i)))
    return m

matrix=matrix_(vaka_liste)
#print(matrix)
def Kolerasyon(x,liste,n):
    sr = 0
    st = 0
    yToplam=sum(liste)
    y = yToplam/n
    size = len(x)
    for i in range(n):
        temp = 0
        for j in range(size):
            if j == 0:
                temp +=x[j]
            else:
                temp += x[j]*(i+1)**j
        sr +=(liste[i]-temp)**2
        st +=(liste[i]-y)**2
    r = ((st-sr)/st)**(1/2)
    return r
dizi=[]
for i in range(0,6):
    x=Kolerasyon(matrix[i],vaka_liste,uzunluk)
    dizi.append(x)
    
#print(dizi)

def eniyikolerasyon(kolerasyon):
    enuyumlu=max(kolerasyon)
    i=1
    while(enuyumlu!=kolerasyon[i-1]):
        i+=1
    return i
#uyumlu=eniyikolerasyon(dizi)
#print(uyumlu)


#polinomlu integral hesabı
import math
from sympy import Symbol
for i in range(1):
    x=Symbol('x')
    
    pol=matrix[eniyikolerasyon(dizi)-1]
    denklem=(pol[0] + pol[1]*x + pol[2]*x**2 + pol[3]*x**3 + pol[4]*x**4 + pol[5]*x**5 + pol[6]*x**6)
    print("Polinom denklemi",denklem)
    

    a,b=7,len(vaka_liste) #17040101 7
    integral = 0
    deltax = 0.1
    n = int((b-a)/deltax)
    for j in range(n):
        integral += deltax * (denklem.subs({x: a}) + denklem.subs({x: a+deltax}))/2
        a += deltax
    print ("Polinomlu integral sonucu:",integral)
    
def polinomsuz_integral(vaka_liste):
    a=7
    b=len(vaka_liste)
    deltax=1
    integral = 0
    n = int((b - a) / deltax)
    for i in range(n-1):
        integral += deltax * (vaka_liste[a] + vaka_liste[a + deltax]) / 2
        a += deltax
    return integral
print("Polinomsuz integral sonucu : ",polinomsuz_integral(vaka_liste))





       


# In[66]:



dosya = open('170401017_yorum.txt','w',encoding='UTF8')
dosya.write('İntegral alınırken dikdörtgenlerin eninin küçük olması onunla ters orantılı olarak o kadar fazla dikdörtgen alanı hesabını arttırır.\n')
dosya.write('Deltax burada en görevini görür ona verdiğimiz sayısal değerlerin değişimi yani 0.1 ve 1 farklı dikdörtgensel alan hesaplarına neden olur.\n')
dosya.write('Deltax değerini küçültürsek daha az hata payı veren veriler elde ederiz.Çünkü polinomlu yaklaşım vardır ve hata payını azalttığı için istenilen sonuca yaklaşırız.\n')
dosya.write('Aynı zamanda daha çok alan hesabı yapar ve sonuçlar farklı çıkar.')
dosya.write('\n CEMRE DOĞAN 170401017')

dosya.close()

