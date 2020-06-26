#Oktay Saraçoğlu
#160401083

import numpy as np
def asal(kaca_kadar):
    asallar = [2]
    if kaca_kadar < 2:
        return None
    elif kaca_kadar == 2:
        return asallar
    else:
        for i in range(3,kaca_kadar,2):
            bolundu = False
            # karekökün aşağı yuvarlanma ihtimaline karşı, + 1 ekliyoruz.
            limit = (i ** 0.5) + 1
            for j in asallar:

                if i % j == 0:
                    bolundu=True
                    break
                if j > limit:
                    break
            if bolundu == False:
                asallar.append(i)
    return asallar

asallar = asal(600)

asallartxt = open("asallar.txt","w")

for i in range(len(asallar)):
    asallar[i] = str(asallar[i])
    asallartxt.write(asallar[i]+"\n")


def det(l):
    n=len(l)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0])

train_sample_number = len(asallar)
X_train = []
Y_train = []
for i in range(train_sample_number):
    X_train.append(i+1)
    Y_train.append(float(asallar[i]))

degree = int(input("polinom derecesi : "))
matris = np.full((degree+1,degree+1),0).astype("float")

for i in range(degree+1):

    for j in range(degree+1):

        sum_x = 0
        for k in range(train_sample_number):
            sum_x += X_train[k]**(i+j)
        matris[i][j] = sum_x

sonuc = []
for i in range(degree+1):
    sum = 0
    for j in range(train_sample_number):
        sum = sum +  (Y_train[j]*(X_train[j]**i))
    sonuc.append(sum)

array = np.array(sonuc)
array.reshape(-1,1)

delta = det(matris)
dete = []

x = np.full((degree+1,degree+1),0).astype("float")

for i in range(degree+1):
    for j in range(degree+1):
        for k in range(degree+1):
            x[j][k] = matris[j][k]
    #print(x)
    for j in range(degree+1):
        x[j][i] = array[j]
    #print(det(x))
    dete.append(det(x)/delta)

prediction = float(input("tahmin edilecek değer : "))

sonuc = 0
for i in range(degree+1):
    sonuc = sonuc + dete[i]*(prediction**i)
    print(dete[i])
#print(sonuc)


delta = 1
degree = 4
point = 160401083% 100
fx = 0

def f(degree,fx,dete,point):
    for i in range(degree):
        fx = fx + dete[i] * (point ** i)
    return fx

central_derivation = (f(degree,fx,dete,(point+delta)) - f(degree,fx,dete,(point-delta)))/2*delta
print("Polinom ile türev : ",central_derivation)





def polinomsuzTurev():
    x0 =160401083% 100
    h = 1
    xprime = (float(asallar[x0 - 1 + h]) - float(asallar[x0 - 1 - h])) / (2 * h)
    return xprime

turev2 = polinomsuzTurev()
print("Polinomsuz türev ",turev2)
