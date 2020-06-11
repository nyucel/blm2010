#PELİN AKGÜN 180401050
#1
#data = [1,1,5,6,18,47,98,191,359,670,947,1236,1529,1872,2433,3629,5698,7402,9217,10827,13531,15679,18315,20921,23934,27069,30217,34109,38226]
dosya=open("D://veriler.txt","r")
data=[]

for i in dosya.read().split():
    data.append(int(i))

n=len(data)
x0_sum=0
x_sum=0
y_sum=sum(data)
x2_sum=0
x3_sum=0
x4_sum=0
x5_sum=0
x6_sum=0
x7_sum=0
x8_sum=0
x9_sum=0
x10_sum=0
x11_sum=0
x12_sum=0
x0y_sum=0
xy_sum=0
x2y_sum=0
x3y_sum=0
x4y_sum=0
x5y_sum=0
x6y_sum=0
for i in range(n):
    x0_sum +=(i+1)**0
    x_sum += i+1
    x2_sum += (i+1)**2
    x3_sum += (i+1)**3
    x4_sum += (i+1)**4
    x5_sum += (i+1)**5
    x6_sum += (i+1)**6
    x7_sum += (i+1)**7
    x8_sum += (i+1)**8
    x9_sum += (i+1)**9
    x10_sum += (i+1)**10
    x11_sum += (i+1)**11
    x12_sum += (i+1)**12
    x0y_sum += data[i]
    xy_sum += (i+1)*data[i]
    x2y_sum += (i+1)*(i+1)*data[i]
    x3y_sum += (i+1)*(i+1)*(i+1)*data[i]
    x4y_sum += ((i+1)**4)* data[i]
    x5y_sum += ((i+1)**5)*data[i]
    x6y_sum += ((i+1)**6)*data[i]
xy_degerleri=[]
kullanılacak_x=[]
kullanılacak_x=[x0_sum,x_sum,x2_sum,x3_sum,x4_sum,x5_sum,x6_sum,x7_sum,x8_sum,x9_sum,x10_sum,x11_sum,x12_sum]
x_sums=[n,x0_sum,x_sum,x2_sum,x3_sum,x4_sum,x5_sum,x6_sum,x7_sum,x8_sum,x9_sum,x10_sum,x11_sum,x12_sum]
xy_sums=[y_sum,x0y_sum,xy_sum,x2y_sum,x3y_sum,x4y_sum,x5y_sum,x6y_sum]
xy_degerleri=[x0y_sum,xy_sum,x2y_sum,x3y_sum,x4y_sum,x5y_sum,x6y_sum]

def gauss(matris):
    n = len(matris)
    for i in range(0, n):
        maxEl = abs(matris[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(matris[k][i]) > maxEl:
                maxEl = abs(matris[k][i])
                maxRow = k

        for k in range(i, n + 1):
            tmp = matris[maxRow][k]
            matris[maxRow][k] = matris[i][k]
            matris[i][k] = tmp

        for k in range(i + 1, n):
            c = -matris[k][i] / matris[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matris[k][j] = 0
                else:
                    matris[k][j] += c * matris[i][j]

 
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] =matris[i][n] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][n] -= matris[k][i] * x[i]
    return x
def cozumlerilistele(list):
    cozum = []
    for i in range(2, 8):
        degerlerlistesi = []
        for j in range(i):
            degerlerlistesi.append([])
            for k in range(i):
                 degerlerlistesi[j].append(kullanılacak_x[k + j])
            degerlerlistesi[j].append(xy_degerleri[j])
            if j == i - 1:
                cozum.append(gauss(degerlerlistesi))
                degerlerlistesi.clear()
    return cozum
#result=[]
print(cozumlerilistele([1,2,3,4,5,6,7,8,9,10]))
#result=(cozumlerilistele([1,2,3,4,5,6,7,8,9,10]) 


with open("sonuclar.txt", "a+") as f:
  for i in cozumlerilistele(data):
          f.write(str(i))
   

