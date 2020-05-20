## Batuhan Şahin 160401056

dosya=open("veriler.txt","r")
data = dosya.read().split()
for i in range(len(data)):
    data[i]=int(data[i])
dosya.close()
uzunluk = len(data)
yToplam=sum(data)

def matrisOlustur(length,list,k):
    x,y=adegerler(length),abdegerler(length,list)
    matrix,line=[],0
    for i in range(0,k):
        addline=[]
        for i in range(line,k+line):
            addline.append(x[i])
        addline.append(y[line])
        line+=1
        matrix.append(addline)
    return matrix

def adegerler(length):
    atoplam=[]
    atoplam.append(length)
    for j in range(1,13):
        sonuc=0
        for i in range(length):
            sonuc += (i + 1) ** j
        atoplam.append(sonuc)
    return atoplam



def abdegerler(length,list):
    abdegerler_ = []
    abdegerler_.append(sum(list))
    for i in range(1, 7):
        sonuc=0
        for j in range(length):
            sonuc += (j + 1) ** i * list[j]
        abdegerler_.append(sonuc)
    return abdegerler_


def poli(matrix):## gauss yöntemi ile verileri istenilen derecedeki polinoma yakınlastırıyorum
    q = len(matrix)
    for i in range(0, q):
        max = abs(matrix[i][i])
        maxline = i
        for k in range(i + 1, q):
            if abs(matrix[k][i]) > max:##sayi negatif çıkmaması için abs()kullandım.
                max = abs(matrix[k][i])
                maxline = k
        for k in range(i, q + 1):
            tmp = matrix[maxline][k]
            matrix[maxline][k] = matrix[i][k]
            matrix[i][k] = tmp
        for k in range(i + 1, q):
            c = -matrix[k][i] / matrix[i][i]
            for j in range(i, q + 1):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]
    sonuc = [0 for i in range(q)]
    for i in range(q - 1, -1, -1):
        sonuc[i] = matrix[i][q] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            matrix[k][q] -= matrix[k][i] * sonuc[i]
    return sonuc

def cagir(list):
    data_1 = []
    for i in range(2,8):

        data_1.append(poli(matrisOlustur(len(list),list,i)))
    return data_1
matrix=cagir(data)


def degery(q):
    y=0
    for i in range(len(q)):
        y+=(q[i])
    x=y/len(q)
    return x

degery_=degery(data)

def st(y,n):
    x=0
    for i in range(len(n)):
        x+=((n[i]-y)**2)
    return x

s_t=st(degery_,data)

def Kolerasyon(matris,n):
    sr=0
    for i in range(len(n)):
        tmp=0
        for j in range(len(matris)):
            if(j==0):
                tmp+=matris[j]
            else:
                tmp+=matris[j]*(i+1)**j
        sr +=(n[i]-tmp)**2
    r=abs((s_t-sr)/s_t)**(1/2)
    return r



sr=[]
for i in range(len(matrix)):
    sr.append(Kolerasyon(matrix[i],data ))

sr_sirali=sorted(sr,reverse=True)
lastArray = sorted(sr)


file=open("sonuc.txt","a")
counter=1
file.write('\n')
for j in matrix:
    x= len(j)
    file.write(str(counter)+".grup"+'\n')
    for y in range(x):
        file.write(str(j[y])+'\n')
    counter +=1
    file.write('\n')
file.close()


dosya=open("sonuc.txt","a+")
for i in range(len(matrix)):
    dosya.write("************************************************")
    dosya.write(str(i+1)+"derece polinom hatası="+str(sr[i])+"\n")
dosya.write("**************polinomlar kıyaslandı*************")
dosya.write("kiyaslanan polinomlarda en uygun hata degeri="+str(sr_sirali[0])+"\n")
dosya.write("en uygun hata degerine sahip polinomun derecesi="+str(sr.index(sr_sirali[0])+1)+"\n")
dosya.write("\n\n")
dosya.write("Batuhan Şahin 160401056")
dosya.close()
