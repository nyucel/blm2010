5# Fikret ÇAKIRLI 140401099
import numpy as np 
# dosya okuma 
f1=open("veriler.txt")
degree = []
degree_temp = []
std_sp=[]
for line in f1.readlines():
    line=line.rstrip('\n')
    degree.append(line)
    degree_temp.append(line)
f1.close()    

def dg1(degree1):
        if(degree1==1):
            return denklem1
        elif(degree1==2):
            return denklem2
        elif(degree1==3):
            return denklem3
        elif(degree1==4):
            return denklem4
        elif(degree1==5):
            return denklem5
        elif(degree1==6):
            return denklem6

def denk1(denklem,x_degeri):
    top=0    
    top+=denklem[0]+sum([denklem[i+1]*pow(x_degeri,i+1) for i in range(len(denklem)-1)])
    return top
for i in range(0,len(degree)):
    degree[i] = int(degree[i])
    degree_temp[i] = int(degree_temp[i])

def bestSolution(r_kare):   
    r,degree1=abs(1-r_kare[0]),0
    for i in range(1,len(r_kare)):
        if(abs(1-r_kare[i]) < r):
            r,degree1=r_kare[i],i
    return (r,degree1+1)

def polinomu_kullanmadan_integral(degree):
    a,b=9,len(degree)  
    Delta_x,integral = 1,0
    n = int((b - a) / Delta_x)
    for i in range(n-1):
        integral += Delta_x * (degree[a] + degree[a + Delta_x]) / 2
        a += Delta_x
    return integral
def polinomu_kullanarak_integral(denk):

    a,b=9,len(degree)  
    Delta_x = 0.1
    integral = 0
    n = int((b - a)/Delta_x) 
    for i in range(n):
        integral += Delta_x * (denk1(denk,a) + denk1(denk,a + Delta_x)) / 2
        a += Delta_x
    return integral


n= len(degree)
x_kare_top ,x_kup_top,x_4der_top = 0,0,0
x_5der_top ,x_6der_top, x_7der_top= 0,0,0
x_8der_top ,x_9der_top ,x_10der_top= 0,0,0
x_11der_top ,x_12der_top,xy_top= 0,0,0
xy_kare_top ,xy_kup_top,xy_4der_top=0,0,0
xy_5der_top ,xy_6der_top,x_top=0,0,0
#--------------------------- 
X = [i+1 for i in range(n)]
x_top=sum(X)
X_ort = np.mean(X)
Y_top= sum(degree)
Y_ort  = np.mean(degree)
Y_kare_top= sum([pow(degree[i],2) for i in range(n)])
x_kare_top= sum([pow(i+1,2) for i in range(n)])
x_kup_top= sum([pow(i+1,3) for i in range(n)])
x_4der_top= sum([pow(i+1,4) for i in range(n)])
x_5der_top= sum([pow(i+1,5) for i in range(n)])
x_6der_top= sum([pow(i+1,6) for i in range(n)])
x_7der_top= sum([pow(i+1,7) for i in range(n)])
x_8der_top= sum([pow(i+1,8) for i in range(n)])
x_9der_top= sum([pow(i+1,9) for i in range(n)])
x_10der_top= sum([pow(i+1,10) for i in range(n)])
x_11der_top= sum([pow(i+1,11) for i in range(n)])
x_12der_top= sum([pow(i+1,12) for i in range(n)])

xy_top= sum([(i+1)*degree[i] for i in range(n)])
xy_kare_top = sum([pow(i+1,2)*degree[i] for i in range(n)])
xy_kup_top = sum([pow(i+1,3)*degree[i] for i in range(n)])
xy_4der_top=sum([pow(i+1,4)*degree[i] for i in range(n)])
xy_5der_top=sum([pow(i+1,5)*degree[i] for i in range(n)])
xy_6der_top=sum([pow(i+1,6)*degree[i] for i in range(n)])


def std1(degree,find_deg):
    std1=0
    for i in range(0,len(degree)):
        std1+=(degree[i]-find_deg[i])**2
    return std1

def Std2(degree):
    Std2=0
    for y in degree:
        Std2+=(y-Y_ort)**2
    return Std2

def R_Kare(degree,find_deg):
    return ((abs((Std2(degree)-std1(degree,find_deg)))/Std2(degree)))**(1/2)

denklem1=[]
A1=(((n*xy_top)-(x_top*Y_top))/(n*x_kare_top-(pow(x_top,2))))
A0= ((Y_top/n) - A1*(x_top/n))          
denklem1.append(A0)
denklem1.append(A1)
birinci_der_denk_sonuc=[A0+A1*i for i in range(len(X))]
R1=R_Kare(degree,birinci_der_denk_sonuc)
std_sp.append(R1)

denklem2=[]
Matrix2= [[n,x_top,x_kare_top],[x_top,x_kare_top,x_kup_top],[x_kare_top,x_kup_top,x_4der_top]]
det = np.linalg.det(Matrix2) 
Matrix_temp = [i[:] for i in Matrix2]
Matrix2[0][0],Matrix2[1][0],Matrix2[2][0]= Y_top,xy_top,xy_kare_top
d1 = np.linalg.det(Matrix2) 
Matrix2= [i[:] for i in Matrix_temp]
Matrix_temp = [i[:] for i in Matrix2] 
Matrix_temp[0][1],Matrix_temp[1][1],Matrix_temp[2][1]= Y_top,xy_top,xy_kare_top
det2 = np.linalg.det(Matrix_temp) 
Matrix_temp = [i[:] for i in Matrix2] 
Matrix_temp[0][2],Matrix_temp[1][2],Matrix_temp[2][2]= Y_top,xy_top,xy_kare_top
det3 = np.linalg.det(Matrix_temp) 
a20,a21,a22=(d1/det),(det2/det),(det3/det)
denklem2.append(a20)
denklem2.append(a21)
denklem2.append(a22)
ikinci_der_denk_sonuc =[a20+(a21*i)+(a22*pow(i,2)) for i in range(len(X))]
R2=R_Kare(degree,ikinci_der_denk_sonuc)
std_sp.append(R2)


denklem3=[]
Matrix3= [[n,x_top,x_kare_top, x_kup_top],
          [x_top,x_kare_top,x_kup_top,x_4der_top],
          [x_kare_top,x_kup_top,x_4der_top,x_5der_top],
          [x_kup_top,x_4der_top,x_5der_top,x_6der_top]]
det = np.linalg.det(Matrix3) 
Matrix_temp = [i[:] for i in Matrix3]
Matrix3[0][0],Matrix3[1][0],Matrix3[2][0],Matrix3[3][0]= Y_top,xy_top,xy_kare_top,xy_kup_top 
d1 = np.linalg.det(Matrix3) 
Matrix3= [i[:] for i in Matrix_temp]
Matrix3[0][1],Matrix3[1][1],Matrix3[2][1],Matrix3[3][1]= Y_top,xy_top,xy_kare_top,xy_kup_top 
det2 = np.linalg.det(Matrix3) 
Matrix3= [i[:] for i in Matrix_temp]
Matrix3[0][2],Matrix3[1][2],Matrix3[2][2],Matrix3[3][2]= Y_top,xy_top,xy_kare_top,xy_kup_top 
det3 = np.linalg.det(Matrix3) 
Matrix3= [i[:] for i in Matrix_temp]
Matrix3[0][3],Matrix3[1][3],Matrix3[2][3],Matrix3[3][3]= Y_top,xy_top,xy_kare_top,xy_kup_top 
det4 = np.linalg.det(Matrix3) 
a30,a31,a32,a33=(d1/det),(det2/det),(det3/det),(det4/det)
ucuncu_der_denk_sonuc =[a30+(a31*i)+(a32*pow(i,2))+(a33*pow(i,3)) for i in range(len(X))]
R3=R_Kare(degree,ucuncu_der_denk_sonuc)
std_sp.append(R3)
denklem3.append(a30)
denklem3.append(a31)
denklem3.append(a32)
denklem3.append(a33)

denklem4=[]
Matrix4= [[n,x_top,x_kare_top, x_kup_top, x_4der_top],
          [x_top,x_kare_top,x_kup_top,x_4der_top,x_5der_top],
          [x_kare_top,x_kup_top,x_4der_top,x_5der_top,x_6der_top],
          [x_kup_top,x_4der_top,x_5der_top,x_6der_top,x_7der_top],
          [x_4der_top,x_5der_top,x_6der_top,x_7der_top,x_8der_top]]
det = np.linalg.det(Matrix4) 
Matrix_temp = [i[:] for i in Matrix4]
Matrix4[0][0],Matrix4[1][0],Matrix4[2][0],Matrix4[3][0],Matrix4[4][0]= Y_top,xy_top,xy_kare_top,xy_kup_top,xy_4der_top
d1 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in Matrix_temp]
Matrix4[0][1],Matrix4[1][1],Matrix4[2][1],Matrix4[3][1],Matrix4[4][1]= Y_top,xy_top,xy_kare_top,xy_kup_top,xy_4der_top 
det2 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in Matrix_temp]
Matrix4[0][2],Matrix4[1][2],Matrix4[2][2],Matrix4[3][2],Matrix4[4][2]= Y_top,xy_top,xy_kare_top,xy_kup_top,xy_4der_top
det3 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in Matrix_temp]
Matrix4[0][3],Matrix4[1][3],Matrix4[2][3],Matrix4[3][3],Matrix4[4][3]= Y_top,xy_top,xy_kare_top,xy_kup_top,xy_4der_top
det4 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in Matrix_temp]
Matrix4[0][4],Matrix4[1][4],Matrix4[2][4],Matrix4[3][4],Matrix4[4][4]= Y_top,xy_top,xy_kare_top,xy_kup_top,xy_4der_top
det5 = np.linalg.det(Matrix4) 
a40,a41,a42,a43,a44=(d1/det),(det2/det),(det3/det),(det4/det),(det5/det)
dorduncu_der_denk_sonuc=[a40+(a41*i)+(a42*pow(i,2))+(a43*pow(i,3))+(a44*pow(i,4)) for i in range(len(X))]
R4=R_Kare(degree,dorduncu_der_denk_sonuc)
std_sp.append(R4)
denklem4.append(a40)
denklem4.append(a41)
denklem4.append(a42)
denklem4.append(a43)
denklem4.append(a44)

denklem5=[]
Matrix5= [[n,x_top,x_kare_top, x_kup_top, x_4der_top,x_5der_top],
          [x_top,x_kare_top,x_kup_top,x_4der_top,x_5der_top,x_6der_top],
          [x_kare_top,x_kup_top,x_4der_top,x_5der_top,x_6der_top,x_7der_top],
          [x_kup_top,x_4der_top,x_5der_top,x_6der_top,x_7der_top,x_8der_top],
          [x_4der_top,x_5der_top,x_6der_top,x_7der_top,x_8der_top,x_9der_top],
         [x_5der_top,x_6der_top,x_7der_top,x_8der_top,x_9der_top,x_10der_top]]
a5=np.polyfit(X,degree,5)
denk5=[a5[i] for i in range(len(a5))]
a50=denk5[5]
a51=denk5[4]
a52=denk5[3]
a53=denk5[2]
a54=denk5[1]
a55=denk5[0]
besinci_der_denk_sonuc=[a50+(a51*i)+(a52*pow(i,2))+(a53*pow(i,3))+(a54*pow(i,4))+(a55*pow(i,5)) for i in range(len(X))]
R5=R_Kare(degree,besinci_der_denk_sonuc)
denklem5.append(a50)
denklem5.append(a51)
denklem5.append(a52)
denklem5.append(a53)
denklem5.append(a54)
denklem5.append(a55)
std_sp.append(R5)
denklem6=[]
Matrix6=[[n,x_top,x_kare_top, x_kup_top, x_4der_top,x_5der_top,x_6der_top],
            [x_top,x_kare_top,x_kup_top,x_4der_top,x_5der_top,x_6der_top,x_7der_top],
            [x_kare_top,x_kup_top,x_4der_top,x_5der_top,x_6der_top,x_7der_top,x_8der_top],
            [x_kup_top,x_4der_top,x_5der_top,x_6der_top,x_7der_top,x_8der_top,x_9der_top],
            [x_4der_top,x_5der_top,x_6der_top,x_7der_top,x_8der_top,x_9der_top,x_10der_top],
            [x_5der_top,x_6der_top,x_7der_top,x_8der_top,x_9der_top,x_10der_top,x_11der_top],
            [x_6der_top,x_7der_top,x_8der_top,x_9der_top,x_10der_top,x_11der_top,x_12der_top]]  
a6=np.polyfit(X,degree,6)
denk6=[a6[i] for i in range(len(a6))]
a60=denk6[6]
a61=denk6[5]
a62=denk6[4]
a63=denk6[3]
a64=denk6[2]
a65=denk6[1]
a66=denk6[0]
altinci_der_denk_sonuc=[a60+(a61*i)+(a62*pow(i,2))+(a63*pow(i,3))+(a64*pow(i,4))+(a65*pow(i,5))+(a66*pow(i,6)) for i in range(len(X))]
R6=R_Kare(degree,altinci_der_denk_sonuc)
denklem6.append(a60)
denklem6.append(a61)
denklem6.append(a62)
denklem6.append(a63)
denklem6.append(a64)
denklem6.append(a65)
denklem6.append(a66)
std_sp.append(R6)
standart_sapma,degree1=bestSolution(std_sp)
print("\nEn iyi cozum :",degree1,". dereceden polinom ile"," Standart Sapma:",standart_sapma)
çikti1 =polinomu_kullanmadan_integral(degree)
çikti2=polinomu_kullanarak_integral(dg1(degree1))
print("Polinomu kullanmadan İntegral Sonucu: ",çikti1)
print("Polinomu kullanarak İntegral Sonucu: ",çikti2)

def yorum_olustur():
    dosya = open('140401099_yorum.txt','w',encoding='UTF8')
    dosya.write('integral hesabında h ı ne kadar küçük alırsak gerçek sonuca çok yaklaşmış oluruz. Polinom ile denklemin derecelerine bakıldığı için,' )
    dosya.write('gerçek sonuca polinomsuz integrale göre daha çok yaklaşılmış olacaktır. Aralarındaki fark bu sebeptendir.')
     
    dosya.close()
yorum_olustur()