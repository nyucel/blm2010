#Ahmet Doğan KAYIŞ / 170401065

import math
import numpy as np

file=open("veriler.txt")
veriler=[]
veriler_temp = []
korelasyonlar=[]
for sira in file.readlines():
    sira=sira.rstrip('\n')
    veriler.append(sira)
    veriler_temp.append(sira)
file.close()    

n= len(veriler)
x_2,x_3,x_4 = 0,0,0
x_5 ,x_6, x_7= 0,0,0
x_8 ,x_9 ,x_10= 0,0,0
x_11 ,x_12,x_y= 0,0,0
x2_y_ ,x3_y_,x4_y_=0,0,0
x5_y_ ,x6_y_,x_top=0,0,0

for i in range(0,len(veriler)):
    veriler[i] = int(veriler[i])
    veriler_temp[i] = int(veriler_temp[i])

def dolas(deg1,deg2,veriler):
    dizi1=[]
    for i in range(deg1,deg2):
        dizi1.append(veriler[i])
    return dizi1

x_deg = [i+1 for i in range(n)]
x_top=sum(x_deg)
x_deg_ortalama = np.mean(x_deg)
y_top= sum(veriler)
y_ort  = np.mean(veriler)
y_2_top= sum([pow(veriler[i],2) for i in range(n)])
x_deg_2_top= sum([pow(i+1,2) for i in range(n)])
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

x_y= sum([(i+1)*veriler[i] for i in range(n)])
x2_y_ = sum([pow(i+1,2)*veriler[i] for i in range(n)])
x3_y_ = sum([pow(i+1,3)*veriler[i] for i in range(n)])
x4_y_=sum([pow(i+1,4)*veriler[i] for i in range(n)])
x5_y_=sum([pow(i+1,5)*veriler[i] for i in range(n)])
x6_y_=sum([pow(i+1,6)*veriler[i] for i in range(n)])

def yazdirma(yaklasikSonuc,katsayilar,derece,KORELASYON,standart_tahmini_hata,baslangic,son):
    dosya = open('sonuc.txt','a+')
    dosya.write('\n('+str(derece)+'). Dereceden Denklem\n')
    dosya.write('baginti_katsayisi:  '+str(KORELASYON)+'\n')
    dosya.write('Standart tahmini hata = '+str(standart_tahmini_hata)+'\n')
    dosya.write('denklem:\n'+ katsayilar)
    dosya.write('\n\n')
    dosya.write('['+str(baslangic)+'-'+str(son)+']'+'arasindaki veriler:'+'\n''\ngercek veriler  ,       yaklasik veriler   ,                           Hata(E)\n')
    for i in range(len(veriler)):
        dosya.write(str(veriler[i])+'\t\t\t'+str(yaklasikSonuc[i])+'\t\t\t'+str(veriler[i]-yaklasikSonuc[i])+'\n')
    dosya.write('\n')


#----birinci dereceden denklem----
A1=(((n*x_y)-(x_top*y_top))/(n*x_deg_2_top-(pow(x_top,2))))
A0= ((y_top/n) - A1*(x_top/n))
Korelasyon_katsayisi1 = (((n*x_y)-(x_top*y_top))/math.sqrt((n*x_deg_2_top-(pow(x_top,2)))*(n*y_2_top-(pow(y_top,2)))))

t1=sum([abs(i-x_deg_ortalama) for i in range(n)])
ts=math.sqrt(pow(t1,2)/(n-1))
standart_tahmini_hata1= (ts/(math.sqrt(n)))
print("*Standart Tahmini Hata:",standart_tahmini_hata1,"\n")
print("*kararlilik_katsayisi:",Korelasyon_katsayisi1,"\n")                        
print("-birinci dereceden denklemi ","y =",A0,A1,"x")
denk_1=str(A0)+" "+str(A1)+'x'
birinci_der_denk_sonuc=[A0+A1*i for i in range(len(x_deg))]
yazdirma(birinci_der_denk_sonuc,denk_1,1,Korelasyon_katsayisi1,standart_tahmini_hata1,1,len(veriler))

#-----ikinci dereceden denklem----
M2= [[n,x_top,x_deg_2_top],
     [x_top,x_deg_2_top,x_3],
     [x_deg_2_top,x_3,x_4]]

det = np.linalg.det(M2) 
M_temp = [i[:] for i in M2]
M2[0][0],M2[1][0],M2[2][0]= y_top,x_y,x2_y_
det1 = np.linalg.det(M2) 
M2= [i[:] for i in M_temp]
M_temp = [i[:] for i in M2] 
M_temp[0][1],M_temp[1][1],M_temp[2][1]= y_top,x_y,x2_y_
det2 = np.linalg.det(M_temp) 
M_temp = [i[:] for i in M2] 
M_temp[0][2],M_temp[1][2],M_temp[2][2]= y_top,x_y,x2_y_
det3 = np.linalg.det(M_temp) 
 
a20,a21,a22=(det1/det),(det2/det),(det3/det)
print("\n-ikinci dereceden polinom denklemi=\n",a20,"x^0",a21,"x^1",a22,"x^2") 
denk_2=str(a20)+"x^0 "+str(a21)+'x '+str(a22)+'x^2'
ikinci_der_denk_sonuc =[a20+(a21*i)+(a22*pow(i,2)) for i in range(len(x_deg))]
tr2=sum([pow(abs(veriler[i]-a20-a21-a22),2) for i in range(n)])
txy2=math.sqrt(tr2/(n-3))
St2=sum([pow((veriler[i]-y_top),2) for i in range(n)])
Korelasyon_katsayisi2=((St2-tr2)/St2)
yazdirma(ikinci_der_denk_sonuc,denk_2,2,Korelasyon_katsayisi2,tr2,1,len(veriler))

#----- üçüncü dereceden denklem----
M3= [[n,x_top,x_deg_2_top, x_3],
          [x_top,x_deg_2_top,x_3,x_4],
          [x_deg_2_top,x_3,x_4,x_5],
          [x_3,x_4,x_5,x_6]]

det = np.linalg.det(M3) 
M_temp = [i[:] for i in M3]
M3[0][0],M3[1][0],M3[2][0],M3[3][0]= y_top,x_y,x2_y_,x3_y_ 
det1 = np.linalg.det(M3) 
M3= [i[:] for i in M_temp]
M3[0][1],M3[1][1],M3[2][1],M3[3][1]= y_top,x_y,x2_y_,x3_y_ 
det2 = np.linalg.det(M3) 
M3= [i[:] for i in M_temp]
M3[0][2],M3[1][2],M3[2][2],M3[3][2]= y_top,x_y,x2_y_,x3_y_ 
det3 = np.linalg.det(M3) 
M3= [i[:] for i in M_temp]
M3[0][3],M3[1][3],M3[2][3],M3[3][3]= y_top,x_y,x2_y_,x3_y_ 
det4 = np.linalg.det(M3) 

a30,a31,a32,a33=(det1/det),(det2/det),(det3/det),(det4/det)
print("\n-üçüncü dereceden polinom denklemi=\n",a30,"x^0",a31,"x^1",a32,"x^2",a33,"x^3") 
denk_3=str(a30)+"x^0 "+str(a31)+'x '+str(a32)+'x^2 '+str(a33)+'x^3 '
ücüncü_der_den_sonuc =[a30+(a31*i)+(a32*pow(i,2))+(a33*pow(i,3)) for i in range(len(x_deg))]
tr3=sum([pow(abs(veriler[i]-a30-a31-a32-a33),2) for i in range(n)])
Syx3=math.sqrt(tr3/(n-4))
St3=sum([pow((veriler[i]-y_top),2) for i in range(n)])
Korelasyon_katsayisi3=((St3-tr3)/St3)
yazdirma(ikinci_der_denk_sonuc,denk_3,3,Korelasyon_katsayisi3,tr3,1,len(veriler))

#----- dörtüncü dereceden denklem----
Matrix4= [[n,x_top,x_deg_2_top, x_3, x_4],
          [x_top,x_deg_2_top,x_3,x_4,x_5],
          [x_deg_2_top,x_3,x_4,x_5,x_6],
          [x_3,x_4,x_5,x_6,x_7],
          [x_4,x_5,x_6,x_7,x_8]]

det = np.linalg.det(Matrix4) 
M_temp = [i[:] for i in Matrix4]
Matrix4[0][0],Matrix4[1][0],Matrix4[2][0],Matrix4[3][0],Matrix4[4][0]= y_top,x_y,x2_y_,x3_y_,x4_y_
det1 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in M_temp]
Matrix4[0][1],Matrix4[1][1],Matrix4[2][1],Matrix4[3][1],Matrix4[4][1]= y_top,x_y,x2_y_,x3_y_,x4_y_ 
det2 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in M_temp]
Matrix4[0][2],Matrix4[1][2],Matrix4[2][2],Matrix4[3][2],Matrix4[4][2]= y_top,x_y,x2_y_,x3_y_,x4_y_
det3 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in M_temp]
Matrix4[0][3],Matrix4[1][3],Matrix4[2][3],Matrix4[3][3],Matrix4[4][3]= y_top,x_y,x2_y_,x3_y_,x4_y_
det4 = np.linalg.det(Matrix4) 
Matrix4= [i[:] for i in M_temp]
Matrix4[0][4],Matrix4[1][4],Matrix4[2][4],Matrix4[3][4],Matrix4[4][4]= y_top,x_y,x2_y_,x3_y_,x4_y_
det5 = np.linalg.det(Matrix4) 

a40,a41,a42,a43,a44=(det1/det),(det2/det),(det3/det),(det4/det),(det5/det)
print("\n-dörtüncü dereceden polinom denklemi=\n",a40,"x^0",a41,"x^1",a42,"x^2",a43,"x^3",a44,"x^4") 
denk_4=str(a40)+"x^0 "+str(a41)+'x '+str(a42)+'x^2 '+str(a43)+'x^3 '+str(a44)+'x^4 '
dorduncu_der_denk_sonuc=[a40+(a41*i)+(a42*pow(i,2))+(a43*pow(i,3))+(a44*pow(i,4)) for i in range(len(x_deg))]
tr4=sum([pow(abs(veriler[i]-a40-a41-a42-a43-a44),2) for i in range(n)])
Syx4=math.sqrt(tr4/(n-5))
St4=sum([pow((veriler[i]-y_top),2) for i in range(n)])
Korelasyon_katsayisi4=((St4-tr4)/St4)
yazdirma(dorduncu_der_denk_sonuc,denk_4,4,Korelasyon_katsayisi4,tr4,1,len(veriler))

#----- beşinci dereceden denklem----
Matrix5= [[n,x_top,x_deg_2_top, x_3, x_4,x_5],
          [x_top,x_deg_2_top,x_3,x_4,x_5,x_6],
          [x_deg_2_top,x_3,x_4,x_5,x_6,x_7],
          [x_3,x_4,x_5,x_6,x_7,x_8],
          [x_4,x_5,x_6,x_7,x_8,x_9],
         [x_5,x_6,x_7,x_8,x_9,x_10]]

det = np.linalg.det(Matrix5) 
M_temp = [i[:] for i in Matrix5]
Matrix5[0][0],Matrix5[1][0],Matrix5[2][0],Matrix5[3][0],Matrix5[4][0],Matrix5[5][0]= y_top,x_y,x2_y_,x3_y_,x4_y_,x5_y_
det1 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in M_temp]
Matrix5[0][1],Matrix5[1][1],Matrix5[2][1],Matrix5[3][1],Matrix5[4][1],Matrix5[5][1]= y_top,x_y,x2_y_,x3_y_,x4_y_,x5_y_
det2 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in M_temp]
Matrix5[0][2],Matrix5[1][2],Matrix5[2][2],Matrix5[3][2],Matrix5[4][2],Matrix5[5][2]= y_top,x_y,x2_y_,x3_y_,x4_y_,x5_y_
det3 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in M_temp]
Matrix5[0][3],Matrix5[1][3],Matrix5[2][3],Matrix5[3][3],Matrix5[4][3],Matrix5[5][3]= y_top,x_y,x2_y_,x3_y_,x4_y_,x5_y_
det4 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in M_temp]
Matrix5[0][4],Matrix5[1][4],Matrix5[2][4],Matrix5[3][4],Matrix5[4][4],Matrix5[5][4]= y_top,x_y,x2_y_,x3_y_,x4_y_,x5_y_
det5 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in M_temp]
Matrix5[0][5],Matrix5[1][5],Matrix5[2][5],Matrix5[3][5],Matrix5[4][5],Matrix5[5][5]= y_top,x_y,x2_y_,x3_y_,x4_y_,x5_y_
det6 = np.linalg.det(Matrix5) 

a50,a51,a52,a53,a54,a55=(det1/det),(det2/det),(det3/det),(det4/det),(det5/det),(det6/det)
print("\n-beşinci dereceden polinom denklemi=\n",a50,"x^0",a51,"x^1",a52,"x^2",a53,"x^3",a54,"x^4",a55,"x^5")
denk_5=str(a50)+"x^0 "+str(a51)+'x '+str(a52)+'x^2 '+str(a53)+'x^3 '+str(a54)+'x^4 '+str(a55)+'x^5 '
besinci_der_denk_sonuc=[a50+(a51*i)+(a52*pow(i,2))+(a53*pow(i,3))+(a54*pow(i,4))+(a55*pow(i,5)) for i in range(len(x_deg))]
tr5=sum([pow(abs(veriler[i]-a50-a51-a52-a53-a54-a55),2) for i in range(n)])
Syx5=math.sqrt(tr5/(n-6))
St5=sum([pow((veriler[i]-y_top),2) for i in range(n)])
Korelasyon_katsayisi5=((St5-tr5)/St5)
yazdirma(besinci_der_denk_sonuc,denk_5,5,Korelasyon_katsayisi5,tr5,1,len(veriler))

Matrix6=[[n,x_top,x_deg_2_top, x_3, x_4,x_5,x_6],
            [x_top,x_deg_2_top,x_3,x_4,x_5,x_6,x_7],
            [x_deg_2_top,x_3,x_4,x_5,x_6,x_7,x_8],
            [x_3,x_4,x_5,x_6,x_7,x_8,x_9],
            [x_4,x_5,x_6,x_7,x_8,x_9,x_10],
            [x_5,x_6,x_7,x_8,x_9,x_10,x_11],
            [x_6,x_7,x_8,x_9,x_10,x_11,x_12]]  

a6=np.polyfit(x_deg,veriler,6)
denk6=[a6[i] for i in range(len(a6))]
a60=denk6[6]
a61=denk6[5]
a62=denk6[4]
a63=denk6[3]
a64=denk6[2]
a65=denk6[1]
a66=denk6[0]
print("\n-altıncı dereceden polinom denklemi=\n",a60,"x^0",a61,"x^1",a62,"x^2",a63,"x^3",a64,"x^4",a65,"x^5",a66,"x^6")
tr6=sum([pow(abs(veriler[i]-a60-a61-a62-a63-a64-a65-a66),2) for i in range(n)])
Syx6=math.sqrt(tr6/(n-7))
St6=sum([pow((veriler[i]-y_top),2) for i in range(n)])
Korelasyon_katsayisi6=((St6-tr6)/St6)
altinci_der_denk_sonuc=[a60+(a61*i)+(a62*pow(i,2))+(a63*pow(i,3))+(a64*pow(i,4))+(a65*pow(i,5))+(a66*pow(i,6)) for i in range(len(x_deg))]
denk_6='y= '+str(a60)+'x^0 '+str(a61)+'x^1 '+str(a62)+'x^2 '+str(a63)+'x^3 '+str(a64)+'x^4 '+str(a65)+'x^5 '+str(a66)+'x^6'+'\n'
yazdirma(altinci_der_denk_sonuc,denk_6,6,Korelasyon_katsayisi6,tr6,1,len(veriler))


veriler_temp[i] = int(veriler_temp[i])
baslangic = 0
son = 10
while(son != len(veriler_temp)+1):
    veriler = dolas(baslangic ,son,veriler_temp)
    x_deg = [i+1 for i in range(len(veriler_temp))]
    x_deg = dolas(baslangic,son,x_deg)
    x_top=sum(x_deg)
    x_y= sum([(x_deg[i]*veriler[i]) for i in range(len(veriler))])
    y_top= sum(veriler)
    baslangic+=1
    son+=1
    hataOrani=[]
    n= len(veriler)
    
    A1=np.polyfit(x_deg,veriler,1)
    denk1=[A1[i] for i in range(len(A1))]
    a10,a11=denk1[1],denk1[0]
    denk_1='y= '+str(a10)+'x^0 '+str(a11)+'x^1'+'\n'
    birinci_der_denk_sonuc=[a10+a11*i for i in range(len(x_deg))]
    Korelasyon_katsayisi1 = (((n*x_y)-(x_top*y_top))/math.sqrt((n*x_deg_2_top-(pow(x_top,2)))*(n*y_2_top-(pow(y_top,2)))))
    P=sum([abs(i-x_deg_ortalama) for i in range(n)])
    S=math.sqrt(pow(P,2)/(n-1))
    standart_tahmini_hata1= (S/(math.sqrt(n)))
    yazdirma(birinci_der_denk_sonuc,denk_1,1,Korelasyon_katsayisi1,standart_tahmini_hata1,baslangic,son)
    
    a2=np.polyfit(x_deg,veriler,2)
    denk2=[a2[i] for i in range(len(a2))]
    a20,a21,a22=denk2[2],denk2[1],denk2[0]
    denk_2='y= '+str(a20)+'x^0 '+str(a21)+'x^1 '+str(a22)+'x^2'+'\n'
    ikinci_der_denk_sonuc =[a20+(a21*i)+(a22*pow(i,2)) for i in range(len(x_deg))]
    tr2=sum([pow(abs(veriler[i]-a20-a21-a22),2) for i in range(n)])
    txy2=math.sqrt(tr2/(n-3))
    St2=sum([pow((veriler[i]-y_top),2) for i in range(n)])
    Korelasyon_katsayisi2=((St2-tr2)/St2)
    yazdirma(ikinci_der_denk_sonuc,denk_2,2,Korelasyon_katsayisi2,tr2,baslangic,son)
    hataOrani.append(txy2)
    
    a3=np.polyfit(x_deg,veriler,3)
    denk3=[a3[i] for i in range(len(a3))]
    a30,a31,a32,a33=denk3[3],denk3[2],denk3[1],denk3[0]
    denk_3='y= '+str(a30)+'x^0 '+str(a31)+'x^1 '+str(a32)+'x^2 '+str(a33)+'x^3 '+'\n'
    ücüncü_der_den_sonuc =[a30+(a31*i)+(a32*pow(i,2))+(a33*pow(i,3)) for i in range(len(x_deg))]
    tr3=sum([pow(abs(veriler[i]-a30-a31-a32-a33),2) for i in range(n)])
    Syx3=math.sqrt(tr3/(n-4))
    St3=sum([pow((veriler[i]-y_top),2) for i in range(n)])
    Korelasyon_katsayisi3=((St3-tr3)/St3)
    yazdirma(ikinci_der_denk_sonuc,denk_3,3,Korelasyon_katsayisi3,tr3,baslangic,son)
    hataOrani.append(Syx3)
    
    
    a4=np.polyfit(x_deg,veriler,4)
    denk4=[a4[i] for i in range(len(a4))]
    a40,a41,a42,a43,a44=denk4[4],denk4[3],denk4[2],denk4[1],denk4[0]
    denk_4='y= '+str(a40)+'x^0 '+str(a41)+'x^1 '+str(a42)+'x^2 '+str(a43)+'x^3 '+str(a44)+'x^4'+'\n'
    dorduncu_der_denk_sonuc=[a40+(a41*i)+(a42*pow(i,2))+(a43*pow(i,3))+(a44*pow(i,4)) for i in range(len(x_deg))]
    tr4=sum([pow(abs(veriler[i]-a40-a41-a42-a43-a44),2) for i in range(n)])
    Syx4=math.sqrt(tr4/(n-5))
    St4=sum([pow((veriler[i]-y_top),2) for i in range(n)])
    Korelasyon_katsayisi4=((St4-tr4)/St4)
    yazdirma(dorduncu_der_denk_sonuc,denk_4,4,Korelasyon_katsayisi4,tr4,baslangic,son)
    hataOrani.append(Syx4)
    
    a5=np.polyfit(x_deg,veriler,5)
    denk5=[a5[i] for i in range(len(a5))]
    a50,a51,a52,a53,a54,a55=denk5[5],denk5[4],denk5[3],denk5[2],denk5[1],denk5[0]
    denk_5='y= '+str(a50)+'x^0 '+str(a51)+'x^1 '+str(a52)+'x^2 '+str(a53)+'x^3 '+str(a54)+'x^4'+str(a55)+'x^5'+'\n'
    besinci_der_denk_sonuc=[a50+(a51*i)+(a52*pow(i,2))+(a53*pow(i,3))+(a54*pow(i,4))+(a55*pow(i,5)) for i in range(len(x_deg))]
    tr5=sum([pow(abs(veriler[i]-a50-a51-a52-a53-a54-a55),2) for i in range(n)])
    Syx5=math.sqrt(tr5/(n-6))
    St5=sum([pow((veriler[i]-y_top),2) for i in range(n)])
    Korelasyon_katsayisi5=((St5-tr5)/St5)
    yazdirma(besinci_der_denk_sonuc,denk_5,5,Korelasyon_katsayisi5,tr5,baslangic,son)
    hataOrani.append(Syx5)
    
    a6=np.polyfit(x_deg,veriler,6)
    denk6=[a6[i] for i in range(len(a6))]
    a60,a61,a62,a63,a64,a65,a66=denk6[6],denk6[5],denk6[4],denk6[3],denk6[2],denk6[1],denk6[0]
    denk_6='y= '+str(a60)+'x^0 '+str(a61)+'x^1 '+str(a62)+'x^2 '+str(a63)+'x^3 '+str(a64)+'x^4 '+str(a65)+'x^5 '+str(a66)+'x^6'+'\n'
    altinci_der_denk_sonuc=[a60+(a61*i)+(a62*pow(i,2))+(a63*pow(i,3))+(a64*pow(i,4))+(a65*pow(i,5))+(a66*pow(i,6)) for i in range(len(x_deg))]
    tr6=sum([pow(abs(veriler[i]-a60-a61-a62-a63-a64-a65-a66),2) for i in range(n)])
    Syx6=math.sqrt(tr6/(n-7))
    St6=sum([pow((veriler[i]-y_top),2) for i in range(n)])
    Korelasyon_katsayisi6=((St6-tr6)/St6)
    yazdirma(altinci_der_denk_sonuc,denk_6,6,Korelasyon_katsayisi6,tr6,baslangic,son)
    hataOrani.append(Syx6)
    min_hata = hataOrani[0]
    for i in hataOrani:
        if (i < min_hata):
            min_hata = i   
        
    print("[",baslangic,"-",son-1,"] arasindaki veriler icin: ")
    print("en uygun polinom",(hataOrani.index(min_hata)+1),". dereceden polinomdur","denklemin hata miktari:",min_hata,"\n")
    hataOrani=[0]