#Ahmet Doğan KAYIŞ 170401065

import numpy as np 

file=open("veriler.txt")
deg1 = []
deg1_list = []
baglanti_deg=[]
for k in file.readlines():
    k=k.rstrip('\n')
    deg1.append(k)
    deg1_list.append(k)
file.close()    

def f(denk,x_deg):
    top=0
    top+=denk[0]+sum([denk[i+1]*pow(x_deg,i+1) for i in range(len(denk)-1)])
    return top

def fonk1(deg1,sonuc):
    fonk1=0
    for i in range(0,len(deg1)):
        fonk1+=(deg1[i]-sonuc[i])**2
    return fonk1

def fonk2(deg1):
    fonk2=0
    for y in deg1:
        fonk2+=(y-y_ort)**2
    return fonk2

def fonk3(deg1,sonuc):
    return ((abs((fonk2(deg1)-fonk1(deg1,sonuc)))/fonk2(deg1)))**(1/2)

def denk(deg):
        if(deg==1):
            return denk_1
        elif(deg==2):
            return denk_2
        elif(deg==3):
            return denk_3
        elif(deg==4):
            return denk_4
        elif(deg==5):
            return denk_5
        elif(deg==6):
            return denk_6


def polinomlu_integral(d1):

    a,b=5,len(deg1)
    Delta_x = 0.1
    integral = 0
    n = int((b - a)/Delta_x) 
    for i in range(n):
        integral += Delta_x * (f(d1,a) + f(d1,a + Delta_x)) / 2
        a += Delta_x
    return integral

def polinomsuz_integral(deg1):
    a,b=5,len(deg1)  
    Delta_x,integral = 1,0
    n = int((b - a) / Delta_x)
    for a in range(n-1):
        integral += Delta_x * (deg1[a] + deg1[a + Delta_x]) / 2
        a += Delta_x
    return integral

def en_iyi_bul(deg2):   
    r,deg=abs(1-deg2[0]),0
    for i in range(1,len(deg2)):
        if(abs(1-deg2[i]) < r):
            r,deg=deg2[i],i
    return (r,deg+1)

for i in range(0,len(deg1)):
    deg1[i] = int(deg1[i])
    deg1_list[i] = int(deg1_list[i])

n= len(deg1)
x_2 ,x_3,x_4 = 0,0,0
x_5 ,x_6, x_7= 0,0,0
x_8 ,x_9 ,x_10= 0,0,0
x_11 ,x_12,x_y= 0,0,0
x2_y_  ,x3_y_,x4_y_=0,0,0
x5_y_ ,x6_y_,x_top=0,0,0

 
x_deg1 = [i+1 for i in range(n)]
x_top=sum(x_deg1)
x_ort = np.mean(x_deg1)
y_top= sum(deg1)
y_ort  = np.mean(deg1)
y2_top= sum([pow(deg1[i],2) for i in range(n)])
x_2= sum([pow(i+1,2) for i in range(n)])
x_3= sum([pow(i+1,3) for i in range(n)])
x_4= sum([pow(i+1,4) for i in range(n)])
x_5= sum([pow(i+1,5) for i in range(n)])
x_6= sum([pow(i+1,6) for i in range(n)])
x_7= sum([pow(i+1,7) for i in range(n)])
x_8= sum([pow(i+1,8) for i in range(n)])
x_9= sum([pow(i+1,9) for i in range(n)])
x_10= sum([pow(i+1,10) for i in range(n)])
x_11= sum([pow(i+1,11) for i in range(n)])
x_12= sum([pow(i+1,12) for i in range(n)])

x_y= sum([(i+1)*deg1[i] for i in range(n)])
x2_y_  = sum([pow(i+1,2)*deg1[i] for i in range(n)])
x3_y_ = sum([pow(i+1,3)*deg1[i] for i in range(n)])
x4_y_=sum([pow(i+1,4)*deg1[i] for i in range(n)])
x5_y_=sum([pow(i+1,5)*deg1[i] for i in range(n)])
x6_y_=sum([pow(i+1,6)*deg1[i] for i in range(n)])


denk_1=[]
A1=(((n*x_y)-(x_top*y_top))/(n*x_2-(pow(x_top,2))))
A0= ((y_top/n) - A1*(x_top/n))          
denk_1.append(A0)
denk_1.append(A1)
der1=[A0+A1*i for i in range(len(x_deg1))]
R1=fonk3(deg1,der1)
baglanti_deg.append(R1)

denk_2=[]
m_2= [[n,x_top,x_2],[x_top,x_2,x_3],[x_2,x_3,x_4]]
det = np.linalg.det(m_2) 
m_deg = [i[:] for i in m_2]
m_2[0][0],m_2[1][0],m_2[2][0]= y_top,x_y,x2_y_ 
det1 = np.linalg.det(m_2) 
m_2= [i[:] for i in m_deg]
m_deg = [i[:] for i in m_2] 
m_deg[0][1],m_deg[1][1],m_deg[2][1]= y_top,x_y,x2_y_ 
det2 = np.linalg.det(m_deg) 
m_deg = [i[:] for i in m_2] 
m_deg[0][2],m_deg[1][2],m_deg[2][2]= y_top,x_y,x2_y_ 
det3 = np.linalg.det(m_deg) 
a20,a21,a22=(det1/det),(det2/det),(det3/det)
denk_2.append(a20)
denk_2.append(a21)
denk_2.append(a22)
der2 =[a20+(a21*i)+(a22*pow(i,2)) for i in range(len(x_deg1))]
R2=fonk3(deg1,der2)
baglanti_deg.append(R2)


denk_3=[]
m_3= [[n,x_top,x_2, x_3],[x_top,x_2,x_3,x_4],[x_2,x_3,x_4,x_5],[x_3,x_4,x_5,x_6]]
det = np.linalg.det(m_3) 
m_deg = [i[:] for i in m_3]
m_3[0][0],m_3[1][0],m_3[2][0],m_3[3][0]= y_top,x_y,x2_y_ ,x3_y_ 
det1 = np.linalg.det(m_3) 
m_3= [i[:] for i in m_deg]
m_3[0][1],m_3[1][1],m_3[2][1],m_3[3][1]= y_top,x_y,x2_y_ ,x3_y_ 
det2 = np.linalg.det(m_3) 
m_3= [i[:] for i in m_deg]
m_3[0][2],m_3[1][2],m_3[2][2],m_3[3][2]= y_top,x_y,x2_y_ ,x3_y_ 
det3 = np.linalg.det(m_3) 
m_3= [i[:] for i in m_deg]
m_3[0][3],m_3[1][3],m_3[2][3],m_3[3][3]= y_top,x_y,x2_y_ ,x3_y_ 
det4 = np.linalg.det(m_3) 
a30,a31,a32,a33=(det1/det),(det2/det),(det3/det),(det4/det)
der3 =[a30+(a31*i)+(a32*pow(i,2))+(a33*pow(i,3)) for i in range(len(x_deg1))]
R3=fonk3(deg1,der3)
baglanti_deg.append(R3)
denk_3.append(a30)
denk_3.append(a31)
denk_3.append(a32)
denk_3.append(a33)

denk_4=[]
m_4= [[n,x_top,x_2, x_3, x_4],[x_top,x_2,x_3,x_4,x_5],[x_2,x_3,x_4,x_5,x_6],[x_3,x_4,x_5,x_6,x_7],[x_4,x_5,x_6,x_7,x_8]]
det = np.linalg.det(m_4) 
m_deg = [i[:] for i in m_4]
m_4[0][0],m_4[1][0],m_4[2][0],m_4[3][0],m_4[4][0]= y_top,x_y,x2_y_ ,x3_y_,x4_y_
det1 = np.linalg.det(m_4) 
m_4= [i[:] for i in m_deg]
m_4[0][1],m_4[1][1],m_4[2][1],m_4[3][1],m_4[4][1]= y_top,x_y,x2_y_ ,x3_y_,x4_y_ 
det2 = np.linalg.det(m_4) 
m_4= [i[:] for i in m_deg]
m_4[0][2],m_4[1][2],m_4[2][2],m_4[3][2],m_4[4][2]= y_top,x_y,x2_y_ ,x3_y_,x4_y_
det3 = np.linalg.det(m_4) 
m_4= [i[:] for i in m_deg]
m_4[0][3],m_4[1][3],m_4[2][3],m_4[3][3],m_4[4][3]= y_top,x_y,x2_y_ ,x3_y_,x4_y_
det4 = np.linalg.det(m_4) 
m_4= [i[:] for i in m_deg]
m_4[0][4],m_4[1][4],m_4[2][4],m_4[3][4],m_4[4][4]= y_top,x_y,x2_y_ ,x3_y_,x4_y_
det5 = np.linalg.det(m_4) 
a40,a41,a42,a43,a44=(det1/det),(det2/det),(det3/det),(det4/det),(det5/det)
der4=[a40+(a41*i)+(a42*pow(i,2))+(a43*pow(i,3))+(a44*pow(i,4)) for i in range(len(x_deg1))]
R4=fonk3(deg1,der4)
baglanti_deg.append(R4)
denk_4.append(a40)
denk_4.append(a41)
denk_4.append(a42)
denk_4.append(a43)
denk_4.append(a44)

denk_5=[]
m_5= [[n,x_top,x_2, x_3, x_4,x_5],[x_top,x_2,x_3,x_4,x_5,x_6],[x_2,x_3,x_4,x_5,x_6,x_7],[x_3,x_4,x_5,x_6,x_7,x_8],[x_4,x_5,x_6,x_7,x_8,x_9],[x_5,x_6,x_7,x_8,x_9,x_10]]
a5=np.polyfit(x_deg1,deg1,5)
denk5=[a5[i] for i in range(len(a5))]
a50=denk5[5]
a51=denk5[4]
a52=denk5[3]
a53=denk5[2]
a54=denk5[1]
a55=denk5[0]
der5=[a50+(a51*i)+(a52*pow(i,2))+(a53*pow(i,3))+(a54*pow(i,4))+(a55*pow(i,5)) for i in range(len(x_deg1))]
R5=fonk3(deg1,der5)
denk_5.append(a50)
denk_5.append(a51)
denk_5.append(a52)
denk_5.append(a53)
denk_5.append(a54)
denk_5.append(a55)
baglanti_deg.append(R5)

denk_6=[]
m_6=[[n,x_top,x_2, x_3, x_4,x_5,x_6],
            [x_top,x_2,x_3,x_4,x_5,x_6,x_7],
            [x_2,x_3,x_4,x_5,x_6,x_7,x_8],
            [x_3,x_4,x_5,x_6,x_7,x_8,x_9],
            [x_4,x_5,x_6,x_7,x_8,x_9,x_10],
            [x_5,x_6,x_7,x_8,x_9,x_10,x_11],
            [x_6,x_7,x_8,x_9,x_10,x_11,x_12]]  
a6=np.polyfit(x_deg1,deg1,6)
denk6=[a6[i] for i in range(len(a6))]
a60=denk6[6]
a61=denk6[5]
a62=denk6[4]
a63=denk6[3]
a64=denk6[2]
a65=denk6[1]
a66=denk6[0]
der6=[a60+(a61*i)+(a62*pow(i,2))+(a63*pow(i,3))+(a64*pow(i,4))+(a65*pow(i,5))+(a66*pow(i,6)) for i in range(len(x_deg1))]
R6=fonk3(deg1,der6)
denk_6.append(a60)
denk_6.append(a61)
denk_6.append(a62)
denk_6.append(a63)
denk_6.append(a64)
denk_6.append(a65)
denk_6.append(a66)
baglanti_deg.append(R6)
baglanti_kat,deg=en_iyi_bul(baglanti_deg)
print("\nen uygun denklem :",deg,".dereceden denklemdir."," baglanti katsayisi:",baglanti_kat)
integral1 =polinomsuz_integral(deg1)
integral2=polinomlu_integral(denk(deg))
print("Polinomlu İntegral Değeri: ",integral1)
print("Polinomsuz İntegral Değeri: ",integral2)

def yorum():
    dosya = open('yorum_170401065.txt','w',encoding='UTF8')
    dosya.write('Polinom ile yapılan integral hesabının polinomsuz integral hesaba göre daha çok alan, deklemin dereceleri üzerinde hesap yapmaktadır.')
    dosya.write('Bu sebeblede polinom ile yapılan integral hesabı gerçek sonuca daha çok yakın bir sonuç çıkarır.')
    dosya.write('2 sonucun farklı olmasının sebebi bundan kaynaklanmaktadır.')
    dosya.close()
yorum()
