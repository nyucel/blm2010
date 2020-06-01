
# coding: utf-8

# In[18]:


#cemre doğan 170401017
with open("veriler.txt","r",encoding='utf-8') as file: #dosya okuma
    vaka_liste = [] 
    for i in file.read().split():
        vaka_liste.append(int(i))
        
#print(vaka_liste)

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
def xitoplam(derece,liste):
    xi=[len(liste)]
    for i in range(1,2*derece+1):
        xitoplam=0
        for j in range(1,len(liste)+1):
            xitoplam+=(j)**i
        xi.append(xitoplam)
    return xi
#dereceye göre xiyi toplam hesabı
def xiyitoplam(derece,liste):
    xiyi = []
    for j in range(derece+1):
        xiyitoplam=0
        for i in range(len(liste)):
            xiyitoplam +=  (liste[i]*((i+1)**j))
        xiyi.append(xiyitoplam)
    return xiyi
#polinom derecesine göre matris oluştur
def make_matrix(derece,liste):
    derece+=1
    x_=xitoplam(derece,liste)
    y_=xiyitoplam(derece,liste)
    matris=[]
    row=0
    for i in range(0,derece):
        newrow=[]
        for i in range(row,derece+row):
            newrow.append(x_[i])
        newrow.append(y_[row])
        row+=1
        matris.append(newrow)
    return matris
#g=gauss(matrisOlustur(4,vaka_liste))
#print(g)
dosya = open("sonuc.txt","a+",encoding="UTF8",errors="ignore")
dosya.write("İLK SORUNUN CEVABI"+"\n")  
for i in range (7):
    
    if i==1:
        a=gauss(make_matrix(1,vaka_liste))
        #print(a)
        dosya.write("1.dereceden yaklaşım:")
        dosya.write(str(a)+"\n")
    if i==2:
        b=gauss(make_matrix(2,vaka_liste))
        print(b)
        #dosya.write("2.dereceden yaklaşım:")
        dosya.write(str(b)+"\n")
    if i==3:
        c=gauss(make_matrix(3,vaka_liste))
        #print(c)
        dosya.write("3.dereceden yaklaşım:")
        dosya.write(str(c)+"\n")
    if i==4:
        d=gauss(make_matrix(4,vaka_liste))
        #print(d)
        dosya.write("4.dereceden yaklaşım:")
        dosya.write(str(d)+"\n")
    if i==5:
        e=gauss(make_matrix(5,vaka_liste))
        #print(e)
        dosya.write("5.dereceden yaklaşım:")
        dosya.write(str(e)+"\n")
    if i==6:
        f=gauss(make_matrix(6,vaka_liste))
        #print(f)
        dosya.write("6.dereceden yaklaşım:")
        dosya.write(str(f))
        

#korelizasyon işlemi ile yakınsama 

def ortalamaBul(veriler):
    toplam=0
    for i in veriler:
        toplam+=i
        return toplam
    return toplam/len(veriler)
def stop(veriler):
    sd = 0 
    
    for i in range(0,len(veriler)):
        sd += (i - ortalamaBul(veriler)) ** 2
    
    return sd

def standart(veriler):
    sd = 0 
    
    for i in range(0,len(veriler)):
        sd += (i - ortalamaBul(veriler)) ** 0.5
    
    return sd

def korelasyonBul(veriler):
    return ((abs((stop(veriler)-standart(veriler)))/stop(veriler)))**(1/2)

aa=korelasyonBul(a)
#print(aa)
dosya.write("\nİKİNCİ SORUNUN CEVABI\n")
dosya.write("1.derece korelasyon yaklaşımı"+str(aa)+"\n")
bb=korelasyonBul(b)
dosya.write("2.derece korelasyon yaklaşımı"+str(bb)+"\n")
#print(bb)
cc=korelasyonBul(c)
dosya.write("3.derce korelasyon yaklaşımı"+str(cc)+"\n")
#print(cc)
dd=korelasyonBul(d)
dosya.write("4.derece korelasyon yaklaşımı"+str(dd)+"\n")
#print(dd)
ee=korelasyonBul(e)
dosya.write("5.derece korelasyon yaklaşımı"+str(ee)+"\n")
#print(ee)
ff=korelasyonBul(f)
dosya.write("6.derece korelasyon yaklaşımı"+str(ff)+"\n")
#print(ff)

#en uyumlu korelasyon
uyumlu=[]
uyumlu.append(aa)
uyumlu.append(bb)
uyumlu.append(cc)
uyumlu.append(dd)
uyumlu.append(ee)
uyumlu.append(ff)
#print(uyumlu)
enyakın=max(uyumlu)
dosya.write("en uyumlu polinom:"+str(enyakın)+"\n")
#print(enyakın)
if enyakın==aa:
    dosya.write("1.derece")
if enyakın==bb:
    dosya.write("2.derece")
if enyakın==cc:
    dosya.write("3.derece")
if enyakın==dd:
    dosya.write("4.derece")
if enyakın==ee:
    dosya.write("5.derece")
if enyakın==ee:
    dosya.write("6.derece")

dosya.write("\nÜÇÜNCÜ SORU\n")
#onlu grup döngüsü açtım
bas = 0
son = 10    
while(son<len(vaka_liste)): 
    xx=vaka_liste[bas:son]
    bas = bas+10
    son = son+10
    #print(xx)
    for j in range(1):

        onlugrupk=korelasyonBul(xx) #korelizasyon hesabı

        dosya.write("korelasyon değeri onlu grup")
        dosya.write(str(onlugrupk))
        enuyumluk=[]
        enuyumluk.append(onlugrupk)
        #print("***************",enuyumluk)
        enuyumlupolonlu=max(enuyumluk)
        #print(enuyumlupolonlu)
        dosya.write("onlu grubun en uyumlu pol="+str(enuyumlupolonlu))


        #print(onlugrup)
    for k in range(1):    #polinoma yaklaştırma
        onlugrupp=gauss(make_matrix(1,xx))
        dosya.write("1.derece polinom onlu grup")
        dosya.write(str(onlugrupp))
        #print(onlugrupp)
        onlugrupp=gauss(make_matrix(1,xx))
        dosya.write("2.derece polinom onlu grup")
        dosya.write(str(onlugrupp))
        onlugrupp=gauss(make_matrix(1,xx))
        dosya.write("3.derece polinom onlu grup")
        dosya.write(str(onlugrupp))
        onlugrupp=gauss(make_matrix(1,xx))
        dosya.write("4.derece polinom onlu grup")
        dosya.write(str(onlugrupp))
        onlugrupp=gauss(make_matrix(1,xx))
        dosya.write("5.derece polinom onlu grup")
        dosya.write(str(onlugrupp))
        onlugrupp=gauss(make_matrix(1,xx))
        dosya.write("6.derece polinom onlu grup")
        dosya.write(str(onlugrupp))
dosya.close()
