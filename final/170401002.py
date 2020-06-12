#Ahmet Furkan Kurt 170401002


import math

def create_matrix(a,b,c,d):
    matrix=[]
    for i in range(d+1):
        row=[]
        for j in range(d+1):
            if(i==0 and j==0):
                row.append(c)
            else:
                suma = 0
                for a_eleman in a:
                    suma += a_eleman**(i+j)
                row.append(suma)
        sum_= 0
        for eleman in range(c):
            sum_ += (a[eleman]**i)*b[eleman]
        row.append(sum_)
        matrix.append(row)
    return matrix

def gauss_eleme(A):
    boyut = len(A)
    for i in range(0, boyut):
        maxSutun = abs(A[i][i])
        maxSatir = i
        for j in range(i + 1, boyut):
            if abs(A[j][i]) > maxSutun:
                maxSutun = abs(A[j][i])
                maxSatir = j
        for k in range(i, boyut + 1):
            temp = A[maxSatir][k]
            A[maxSatir][k] = A[i][k]
            A[i][k] = temp
            
        for l in range(i + 1, boyut):
            c = -A[l][i] / A[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    A[l][j] = 0
                else:
                    A[l][j] += c * A[i][j]

    matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        matris[i] = A[i][boyut] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][boyut] -= A[k][i] * matris[i]
    return matris

def yaklasma(x,y):
    r =[]
    polinom_katsayilari = []
    for i in range(1,7):
        katsayilar = gauss_eleme(create_matrix(x,y,len(y),i))
        r.append(correlation(x,y,len(y),katsayilar,i))
        polinom_katsayilari.append(katsayilar)
    max_= r[0]
    gecici = 0
    for z in range(len(r)):
        if(r[z]> max_):
            max_ = r[z]
            gecici = z+1  #170401002
    print("En büyük korelasyon : "+str(max_))
    print("En düşük hatalı polinom "+str(gecici)+". dereceden")
    return polinom_katsayilari[gecici-1]


def correlation(a,b,c,katsayilar,m):
    Sr,St,y_= 0,0,0
    for i in b:
        y_+= i
    y_ /= len(b)
    for i in range(c):
        Sr_1=0
        St += (b[i]-y_)**2
        Sr_1 += b[i]-katsayilar[0]
        for j in range(1,m+1):
            Sr_1 -= katsayilar[j]*(a[i]**j)
        Sr_1 = Sr_1**2
        Sr+=Sr_1
    k = math.sqrt(abs((St-Sr)/St)) 
    return k




def u(katsayilar,x):
    y=0
    for i in range(len(katsayilar)):
        y+=katsayilar[i]*(x**i) #170401002
    return y


    
 
def polinomu_kullanmadan_integral(degree):
    a,b=9,len(degree)  
    Delta_x,integral = 1,0
    n = int((b - a) / Delta_x)
    for i in range(n-1):
        integral += Delta_x * (degree[a] + degree[a + Delta_x]) / 2
        a += Delta_x
    print("Polinomsuz integralin sonucu = ",integral)


def polinom_kullanarak_integral(b,katsayilar):
    a=1 
    deltax = 0.1
    integral=0
    
    n = int((b-a)/deltax)
    for i in range(n):
        integral +=  deltax*(u(katsayilar,a)+u(katsayilar,a+deltax))/2
        a+=deltax
    print("Polinomlu integralin sonucu = ",integral)        


with open("170401002_yorum.txt","w",encoding='utf-8') as file:
    file.write("Ahmet Furkan Kurt 170401002 \n")
    file.write("Polinomlu integral gerçeğe daha yakın bir sonuç verir. \n")
    file.write("Çünkü polinomlu integralde deltax'i değerini değiştirebiliyoruz. \n")
    file.write("deltax'i küçültürsek hesaplayacağımız alan artacağı için hesapladığımız değer gerçeğe daha yakın olur.\n")
    file.write("Ancak polinomsuz integralde istediğimiz parçaya bölemediğimiz için hata oranı daha yüksektir.\n")
    
    
def oku():
    dosya = open("veriler.txt")
    y = dosya.readlines()
    x=[]
    for i in range(len(y)):
        y[i]=int(y[i])
        x.append(i)
    return x,y

x,y = oku()
polinom_katsayilari = yaklasma(x,y)
polinom_kullanarak_integral(len(y),polinom_katsayilari)
polinomu_kullanmadan_integral(y)
