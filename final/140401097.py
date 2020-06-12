#!/usr/bin/env python
# coding: utf-8

# In[1]:



#BARAA MASRI 140401097 

import numpy as np 

#cıkacağı en uygun denklemının derecesile denklemi alıp kullanabilmektedir
def denklemi_getir(derece):
        if(derece==1):
            return denk_1
        elif(derece==2):
            return denk_2
        elif(derece==3):
            return denk_3
        elif(derece==4):
            return denk_4
        elif(derece==5):
            return denk_5
        elif(derece==6):
            return denk_6


# f( list olarack gelen denkeminin elemanları , xin değeri )
def f(denklem,x_degeri):
    top=0
    #burda xi olmayan elemani cikartip diger elemanlarinin toplami sirasila ai+x^i bulmaktir 
    #i+1 0 olmasin ayrica denklemin 2 elemandan baslasin
    
    top+=denklem[0]+sum([denklem[i+1]*pow(x_degeri,i+1) for i in range(len(denklem)-1)])
    return top

def polinomu_kullanarak_integral(denklemi):

    a,b=7,len(degerler) #14040109(7)
    Delta_x = 0.1
    integral = 0
    # Burada a integralin alt sınır değeri, b üst sınır değeri ve n dilim sayısıdır.Eğer D`X dilim kalınlığı biliniyorsa n dilim sayısı 
    n = int((b - a)/Delta_x) 
    for i in range(n):
        integral += Delta_x * (f(denklemi,a) + f(denklemi,a + Delta_x)) / 2
        a += Delta_x
    return integral

def polinomu_kullanmadan_integral(degerler):
    a,b=7,len(degerler)   #14040109(7)
    Delta_x,integral = 1,0
    n = int((b - a) / Delta_x)
    for i in range(n-1):
        integral += Delta_x * (degerler[a] + degerler[a + Delta_x]) / 2
        a += Delta_x
    return integral

def en_iyi_korelasyonu_Bul(R_Kare_listesi):   
    r,derece=abs(1-R_Kare_listesi[0]),0
    for i in range(1,len(R_Kare_listesi)):
        if(abs(1-R_Kare_listesi[i]) < r):
            r,derece=R_Kare_listesi[i],i
    return (r,derece+1)

def yorum_olustur():
    dosya = open('yorum_140401097.txt','w',encoding='UTF8')
    dosya.write('İntegral Hesaplama yaparken, verilen polinomu küçük dikdörtgenlere bölerek' )
    dosya.write('ve alanlarını toplayarak hesaplamaya çalışırız. Aldığımız dikdörtgenlerin')
    dosya.write('genişliği ne kadar küçükse, o kadar çok dikdörtgen alan hesapladık ve istediğimiz ')
    dosya.write('değeri o kadar çok elde ettik.Deltax dediğimiz dikdörtgenlerimizin en iyisi.')
    dosya.write('Bu dikdörtgenlerin genişliği ne kadar küçük olursa, o kadar fazla alan hesaplar ve ')
    dosya.write('integrale o kadar yaklaşırız.Dettax\'ı Polinom 0.1 ile aldığımızda, 2 sayı arasındaki N')
    dosya.write('dikdörtgen alanını hesaplıyoruz.Polinom hesaplama dediğimiz şey aslında deltax 1 almak')
    dosya.write('ve verilerle integrali hesaplamaktır.Polinom kısmında daha fazla alan hesaplandığından,')
    dosya.write('polinom ile karşılaştırıldığında farklı sonuçlar vermesi doğaldır.')
    dosya.write('Polinom integralinin sonucu istediğimiz sonuca polinomdan daha yakın bir sonuç verir.')
    dosya.write('Delta x arttıkça, hesaplanacak dikdörtgen artacağından işlem daha uzun sürer.')
     
    dosya.close()


# dosya okuma 
file=open("veriler.txt")
degerler = []
degerler_temp = []
korelasyonlar=[]
for line in file.readlines():
    line=line.rstrip('\n')
    degerler.append(line)
    degerler_temp.append(line)
file.close()    

#list`in degerleri stringten integere cevirme 
for i in range(0,len(degerler)):
    degerler[i] = int(degerler[i])
    degerler_temp[i] = int(degerler_temp[i])
#------------------------------------------------
n= len(degerler)
xlerin_karelerin_toplami ,xlerin_kupulerin_toplami,xlerin_4d_toplami = 0,0,0
xlerin_5d_toplami ,xlerin_6d_toplami, xlerin_7d_toplami= 0,0,0
xlerin_8d_toplami ,xlerin_9d_toplami ,xlerin_10d_toplami= 0,0,0
xlerin_11d_toplami ,xlerin_12d_toplami,x_y_carpim_toplami= 0,0,0
x_kare_y_carpim_toplami ,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami=0,0,0
x5d_y_carpim_toplami ,x6d_y_carpim_toplami,Xler_toplami=0,0,0
#--------------------------- 
xler = [i+1 for i in range(n)]
Xler_toplami=sum(xler)
xler_ortalama = np.mean(xler)
Yler_toplami= sum(degerler)
Yler_ortalama  = np.mean(degerler)
Yler_karelerin_toplami= sum([pow(degerler[i],2) for i in range(n)])
xlerin_karelerin_toplami= sum([pow(i+1,2) for i in range(n)])
xlerin_kupulerin_toplami= sum([pow(i+1,3) for i in range(n)])
xlerin_4d_toplami= sum([pow(i+1,4) for i in range(n)])
xlerin_5d_toplami= sum([pow(i+1,5) for i in range(n)])
xlerin_6d_toplami= sum([pow(i+1,6) for i in range(n)])
xlerin_7d_toplami= sum([pow(i+1,7) for i in range(n)])
xlerin_8d_toplami= sum([pow(i+1,8) for i in range(n)])
xlerin_9d_toplami= sum([pow(i+1,9) for i in range(n)])
xlerin_10d_toplami= sum([pow(i+1,10) for i in range(n)])
xlerin_11d_toplami= sum([pow(i+1,11) for i in range(n)])
xlerin_12d_toplami= sum([pow(i+1,12) for i in range(n)])

x_y_carpim_toplami= sum([(i+1)*degerler[i] for i in range(n)])
x_kare_y_carpim_toplami = sum([pow(i+1,2)*degerler[i] for i in range(n)])
x_kupu_y_carpim_toplami = sum([pow(i+1,3)*degerler[i] for i in range(n)])
x4d_y_carpim_toplami=sum([pow(i+1,4)*degerler[i] for i in range(n)])
x5d_y_carpim_toplami=sum([pow(i+1,5)*degerler[i] for i in range(n)])
x6d_y_carpim_toplami=sum([pow(i+1,6)*degerler[i] for i in range(n)])

#korelasyonu bulmak
def Sr(degerler,buldugumDegerler):
    Sr=0
    for i in range(0,len(degerler)):
        Sr+=(degerler[i]-buldugumDegerler[i])**2
    return Sr

def St(degerler):
    St=0
    for y in degerler:
        St+=(y-Yler_ortalama)**2
    return St

def R_Kare(degerler,buldugumDegerler):
    return ((abs((St(degerler)-Sr(degerler,buldugumDegerler)))/St(degerler)))**(1/2)

#----birinci dereceden denklemi------------------------------------------------------
denk_1=[]
A1=(((n*x_y_carpim_toplami)-(Xler_toplami*Yler_toplami))/(n*xlerin_karelerin_toplami-(pow(Xler_toplami,2))))
A0= ((Yler_toplami/n) - A1*(Xler_toplami/n))          
denk_1.append(A0)
denk_1.append(A1)
birinci_denkleminin_buldugum_sonuclari=[A0+A1*i for i in range(len(xler))]
R1=R_Kare(degerler,birinci_denkleminin_buldugum_sonuclari)
korelasyonlar.append(R1)
print("*birinci dereceden denklemi ","y =",A0,A1,"x","\n","korelasyon =",R1)

#-----ikinci dereceden denklem---------------------------------------------------------------
denk_2=[]
Matrix2= [[n,Xler_toplami,xlerin_karelerin_toplami],
          [Xler_toplami,xlerin_karelerin_toplami,xlerin_kupulerin_toplami],
          [xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami]]
det = np.linalg.det(Matrix2) 
Matrix_temp = [i[:] for i in Matrix2]
Matrix2[0][0],Matrix2[1][0],Matrix2[2][0]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami
det1 = np.linalg.det(Matrix2) 
Matrix2= [i[:] for i in Matrix_temp]
Matrix_temp = [i[:] for i in Matrix2] 
Matrix_temp[0][1],Matrix_temp[1][1],Matrix_temp[2][1]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami
det2 = np.linalg.det(Matrix_temp) 
Matrix_temp = [i[:] for i in Matrix2] 
Matrix_temp[0][2],Matrix_temp[1][2],Matrix_temp[2][2]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami
det3 = np.linalg.det(Matrix_temp) 
a20,a21,a22=(det1/det),(det2/det),(det3/det)
denk_2.append(a20)
denk_2.append(a21)
denk_2.append(a22)
ikinci_denkleminin_buldugum_sonuclari =[a20+(a21*i)+(a22*pow(i,2)) for i in range(len(xler))]
R2=R_Kare(degerler,ikinci_denkleminin_buldugum_sonuclari)
print("\n*ikinci dereceden polinom denklemi=\n",a20,"x^0",a21,"x^1",a22,"x^2","\n","korelasyon =",R2) 
korelasyonlar.append(R2)


#----- üçüncü dereceden denklem--------------------------------------------------------------
denk_3=[]
Matrix3= [[n,Xler_toplami,xlerin_karelerin_toplami, xlerin_kupulerin_toplami],
          [Xler_toplami,xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami],
          [xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami],
          [xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami]]
det = np.linalg.det(Matrix3) 
Matrix_temp = [i[:] for i in Matrix3]
Matrix3[0][0],Matrix3[1][0],Matrix3[2][0],Matrix3[3][0]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami 
det1 = np.linalg.det(Matrix3) 
Matrix3= [i[:] for i in Matrix_temp]
Matrix3[0][1],Matrix3[1][1],Matrix3[2][1],Matrix3[3][1]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami 
det2 = np.linalg.det(Matrix3) 
Matrix3= [i[:] for i in Matrix_temp]
Matrix3[0][2],Matrix3[1][2],Matrix3[2][2],Matrix3[3][2]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami 
det3 = np.linalg.det(Matrix3) 
Matrix3= [i[:] for i in Matrix_temp]
Matrix3[0][3],Matrix3[1][3],Matrix3[2][3],Matrix3[3][3]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami 
det4 = np.linalg.det(Matrix3) 
a30,a31,a32,a33=(det1/det),(det2/det),(det3/det),(det4/det)
ucuncu_denkleminin_buldugum_sonuclari =[a30+(a31*i)+(a32*pow(i,2))+(a33*pow(i,3)) for i in range(len(xler))]
R3=R_Kare(degerler,ucuncu_denkleminin_buldugum_sonuclari)
print("\n*üçüncü dereceden polinom denklemi=\n",a30,"x^0",a31,"x^1",a32,"x^2",a33,"x^3","\n","korelasyon =",R3) 
korelasyonlar.append(R3)
denk_3.append(a30)
denk_3.append(a31)
denk_3.append(a32)
denk_3.append(a33)
#----- dörtüncü dereceden denklem--------------------------------------------------------------
denk_4=[]
Matrix4= [[n,Xler_toplami,xlerin_karelerin_toplami, xlerin_kupulerin_toplami, xlerin_4d_toplami],
          [Xler_toplami,xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami],
          [xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami],
          [xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami],
          [xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami]]
det = np.linalg.det(Matrix4) 
Matrix_temp = [i[:] for i in Matrix4]
Matrix4[0][0],Matrix4[1][0],Matrix4[2][0],Matrix4[3][0],Matrix4[4][0]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami
det1 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in Matrix_temp]
Matrix4[0][1],Matrix4[1][1],Matrix4[2][1],Matrix4[3][1],Matrix4[4][1]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami 
det2 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in Matrix_temp]
Matrix4[0][2],Matrix4[1][2],Matrix4[2][2],Matrix4[3][2],Matrix4[4][2]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami
det3 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in Matrix_temp]
Matrix4[0][3],Matrix4[1][3],Matrix4[2][3],Matrix4[3][3],Matrix4[4][3]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami
det4 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in Matrix_temp]
Matrix4[0][4],Matrix4[1][4],Matrix4[2][4],Matrix4[3][4],Matrix4[4][4]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami
det5 = np.linalg.det(Matrix4) 
a40,a41,a42,a43,a44=(det1/det),(det2/det),(det3/det),(det4/det),(det5/det)
dortucu_denkleminin_buldugum_sonuclari=[a40+(a41*i)+(a42*pow(i,2))+(a43*pow(i,3))+(a44*pow(i,4)) for i in range(len(xler))]
R4=R_Kare(degerler,dortucu_denkleminin_buldugum_sonuclari)
print("\n*dörtüncü dereceden polinom denklemi=\n",a40,"x^0",a41,"x^1",a42,"x^2",a43,"x^3",a44,"x^4","\n","korelasyon =",R4)
korelasyonlar.append(R4)
denk_4.append(a40)
denk_4.append(a41)
denk_4.append(a42)
denk_4.append(a43)
denk_4.append(a44)

#----- beşinci dereceden denklem--------------------------------------------------------------
denk_5=[]
Matrix5= [[n,Xler_toplami,xlerin_karelerin_toplami, xlerin_kupulerin_toplami, xlerin_4d_toplami,xlerin_5d_toplami],
          [Xler_toplami,xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami],
          [xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami],
          [xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami],
          [xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami,xlerin_9d_toplami],
         [xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami,xlerin_9d_toplami,xlerin_10d_toplami]]
a5=np.polyfit(xler,degerler,5)
denk5=[a5[i] for i in range(len(a5))]
a50=denk5[5]
a51=denk5[4]
a52=denk5[3]
a53=denk5[2]
a54=denk5[1]
a55=denk5[0]


besinci_denkleminin_buldugum_sonuclari=[a50+(a51*i)+(a52*pow(i,2))+(a53*pow(i,3))+(a54*pow(i,4))+(a55*pow(i,5)) for i in range(len(xler))]
R5=R_Kare(degerler,besinci_denkleminin_buldugum_sonuclari)
print("\n*beşinci dereceden polinom denklemi=\n",a50,"x^0",a51,"x^1",a52,"x^2",a53,"x^3",a54,"x^4",a55,"x^5","\n","korelasyon =",R5)
denk_5.append(a50)
denk_5.append(a51)
denk_5.append(a52)
denk_5.append(a53)
denk_5.append(a54)
denk_5.append(a55)
korelasyonlar.append(R5)
denk_6=[]
Matrix6=[[n,Xler_toplami,xlerin_karelerin_toplami, xlerin_kupulerin_toplami, xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami],
            [Xler_toplami,xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami],
            [xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami],
            [xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami,xlerin_9d_toplami],
            [xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami,xlerin_9d_toplami,xlerin_10d_toplami],
            [xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami,xlerin_9d_toplami,xlerin_10d_toplami,xlerin_11d_toplami],
            [xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami,xlerin_9d_toplami,xlerin_10d_toplami,xlerin_11d_toplami,xlerin_12d_toplami]]  
a6=np.polyfit(xler,degerler,6)
denk6=[a6[i] for i in range(len(a6))]
a60=denk6[6]
a61=denk6[5]
a62=denk6[4]
a63=denk6[3]
a64=denk6[2]
a65=denk6[1]
a66=denk6[0]

altinci_denkleminin_buldugum_sonuclari=[a60+(a61*i)+(a62*pow(i,2))+(a63*pow(i,3))+(a64*pow(i,4))+(a65*pow(i,5))+(a66*pow(i,6)) for i in range(len(xler))]
R6=R_Kare(degerler,altinci_denkleminin_buldugum_sonuclari)
print("\n*altinci dereceden polinom denklemi=\n",a60,"x^0",a61,"x^1",a62,"x^2",a63,"x^3",a64,"x^4",a65,"x^5",a66,"x^6","\n","korelasyon =",R6)
denk_6.append(a60)
denk_6.append(a61)
denk_6.append(a62)
denk_6.append(a63)
denk_6.append(a64)
denk_6.append(a65)
denk_6.append(a66)
korelasyonlar.append(R6)
korelasyonDegeri,derece=en_iyi_korelasyonu_Bul(korelasyonlar)
print("\nen uygun denklem :",derece,"denklemi"," korelasyon Degeri:",korelasyonDegeri)
integral =polinomu_kullanmadan_integral(degerler)
integral1=polinomu_kullanarak_integral(denklemi_getir(derece))
print("Polinomu kullanmadan İntegral Değeri: ",integral)
print("Polinomu kullanarak İntegral Değeri: ",integral1)
yorum_olustur()


# In[ ]:




