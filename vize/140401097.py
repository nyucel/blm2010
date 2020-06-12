#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BARAA MASRI 140401097 
def git_oraya_kadar(nerden,nereye,degerler):
    yeni_dizi=[]
    for i in range(nerden,nereye):
        yeni_dizi.append(degerler[i])
    return yeni_dizi


# In[2]:


def yazdir2(buldugumSonuclar,Denklemin_katSayilari,derece,KORELASYON,StandartError,baslangic,son):
    dosya = open('sonuc.txt','a+')
    dosya.write('\n---------denklem ('+str(derece)+') derece---------\n')
    dosya.write('KORELASYON DEGERI:  '+str(KORELASYON)+'\n')
    dosya.write('Standart hata = '+str(StandartError)+'\n')
    dosya.write('denklemi:\n'+ Denklemin_katSayilari)
    dosya.write('\n\n')
    dosya.write('['+str(baslangic)+'-'+str(son)+']'+'arasindaki verileri'+'\n')
    dosya.write('\ngercek degerler  ,   buldugum degerler ,  (E=y-a0-a1x-a2x^2..am x^m)\n')
    for i in range(len(degerler)):
        dosya.write(str(degerler[i])+'\t\t\t'+str(buldugumSonuclar[i])+'\t\t\t'+str(degerler[i]-buldugumSonuclar[i])+'\n')
    dosya.write('\n')




# In[6]:


import math
import numpy as np 
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

#----birinci dereceden denklemi------------------------------------------------------
A1=(((n*x_y_carpim_toplami)-(Xler_toplami*Yler_toplami))/(n*xlerin_karelerin_toplami-(pow(Xler_toplami,2))))
A0= ((Yler_toplami/n) - A1*(Xler_toplami/n))
Korelasyon_katsayisi1 = (((n*x_y_carpim_toplami)-(Xler_toplami*Yler_toplami))/math.sqrt((n*xlerin_karelerin_toplami-(pow(Xler_toplami,2)))*(n*Yler_karelerin_toplami-(pow(Yler_toplami,2)))))

P=sum([abs(i-xler_ortalama) for i in range(n)])
S=math.sqrt(pow(P,2)/(n-1))
StandartError1= (S/(math.sqrt(n)))
print("*Standart Hata:",StandartError1,"\n")
print("*Korelasyon_katsayısı:",Korelasyon_katsayisi1,"\n")                        
print("-birinci dereceden denklemi ","y =",A0,A1,"x")
denk_1=str(A0)+" "+str(A1)+'x'
birinci_denkleminin_buldugum_sonuclari=[A0+A1*i for i in range(len(xler))]
yazdir2(birinci_denkleminin_buldugum_sonuclari,denk_1,1,Korelasyon_katsayisi1,StandartError1,1,len(degerler))

#-----ikinci dereceden denklem---------------------------------------------------------------
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
print("\n-ikinci dereceden polinom denklemi=\n",a20,"x^0",a21,"x^1",a22,"x^2") 
denk_2=str(a20)+"x^0 "+str(a21)+'x '+str(a22)+'x^2'
ikinci_denkleminin_buldugum_sonuclari =[a20+(a21*i)+(a22*pow(i,2)) for i in range(len(xler))]
Sr2=sum([pow(abs(degerler[i]-a20-a21-a22),2) for i in range(n)])
Syx2=math.sqrt(Sr2/(n-3))
St2=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
Korelasyon_katsayisi2=((St2-Sr2)/St2)
yazdir2(ikinci_denkleminin_buldugum_sonuclari,denk_2,2,Korelasyon_katsayisi2,Sr2,1,len(degerler))

#----- üçüncü dereceden denklem--------------------------------------------------------------
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
print("\n-üçüncü dereceden polinom denklemi=\n",a30,"x^0",a31,"x^1",a32,"x^2",a33,"x^3") 
denk_3=str(a30)+"x^0 "+str(a31)+'x '+str(a32)+'x^2 '+str(a33)+'x^3 '
ucuncu_denkleminin_buldugum_sonuclari =[a30+(a31*i)+(a32*pow(i,2))+(a33*pow(i,3)) for i in range(len(xler))]
Sr3=sum([pow(abs(degerler[i]-a30-a31-a32-a33),2) for i in range(n)])
Syx3=math.sqrt(Sr3/(n-4))
St3=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
Korelasyon_katsayisi3=((St3-Sr3)/St3)
yazdir2(ikinci_denkleminin_buldugum_sonuclari,denk_3,3,Korelasyon_katsayisi3,Sr3,1,len(degerler))

#----- dörtüncü dereceden denklem--------------------------------------------------------------
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
print("\n-dörtüncü dereceden polinom denklemi=\n",a40,"x^0",a41,"x^1",a42,"x^2",a43,"x^3",a44,"x^4") 
denk_4=str(a40)+"x^0 "+str(a41)+'x '+str(a42)+'x^2 '+str(a43)+'x^3 '+str(a44)+'x^4 '
dortucu_denkleminin_buldugum_sonuclari=[a40+(a41*i)+(a42*pow(i,2))+(a43*pow(i,3))+(a44*pow(i,4)) for i in range(len(xler))]
Sr4=sum([pow(abs(degerler[i]-a40-a41-a42-a43-a44),2) for i in range(n)])
Syx4=math.sqrt(Sr4/(n-5))
St4=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
Korelasyon_katsayisi4=((St4-Sr4)/St4)
yazdir2(dortucu_denkleminin_buldugum_sonuclari,denk_4,4,Korelasyon_katsayisi4,Sr4,1,len(degerler))

#----- beşinci dereceden denklem--------------------------------------------------------------
Matrix5= [[n,Xler_toplami,xlerin_karelerin_toplami, xlerin_kupulerin_toplami, xlerin_4d_toplami,xlerin_5d_toplami],
          [Xler_toplami,xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami],
          [xlerin_karelerin_toplami,xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami],
          [xlerin_kupulerin_toplami,xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami],
          [xlerin_4d_toplami,xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami,xlerin_9d_toplami],
         [xlerin_5d_toplami,xlerin_6d_toplami,xlerin_7d_toplami,xlerin_8d_toplami,xlerin_9d_toplami,xlerin_10d_toplami]]

det = np.linalg.det(Matrix5) 
Matrix_temp = [i[:] for i in Matrix5]
Matrix5[0][0],Matrix5[1][0],Matrix5[2][0],Matrix5[3][0],Matrix5[4][0],Matrix5[5][0]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami,x5d_y_carpim_toplami
det1 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in Matrix_temp]
Matrix5[0][1],Matrix5[1][1],Matrix5[2][1],Matrix5[3][1],Matrix5[4][1],Matrix5[5][1]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami,x5d_y_carpim_toplami
det2 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in Matrix_temp]
Matrix5[0][2],Matrix5[1][2],Matrix5[2][2],Matrix5[3][2],Matrix5[4][2],Matrix5[5][2]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami,x5d_y_carpim_toplami
det3 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in Matrix_temp]
Matrix5[0][3],Matrix5[1][3],Matrix5[2][3],Matrix5[3][3],Matrix5[4][3],Matrix5[5][3]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami,x5d_y_carpim_toplami
det4 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in Matrix_temp]
Matrix5[0][4],Matrix5[1][4],Matrix5[2][4],Matrix5[3][4],Matrix5[4][4],Matrix5[5][4]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami,x5d_y_carpim_toplami
det5 = np.linalg.det(Matrix5) 
Matrix5= [i[:] for i in Matrix_temp]
Matrix5[0][5],Matrix5[1][5],Matrix5[2][5],Matrix5[3][5],Matrix5[4][5],Matrix5[5][5]= Yler_toplami,x_y_carpim_toplami,x_kare_y_carpim_toplami,x_kupu_y_carpim_toplami,x4d_y_carpim_toplami,x5d_y_carpim_toplami
det6 = np.linalg.det(Matrix5) 

a50,a51,a52,a53,a54,a55=(det1/det),(det2/det),(det3/det),(det4/det),(det5/det),(det6/det)
print("\n-beşinci dereceden polinom denklemi=\n",a50,"x^0",a51,"x^1",a52,"x^2",a53,"x^3",a54,"x^4",a55,"x^5")
denk_5=str(a50)+"x^0 "+str(a51)+'x '+str(a52)+'x^2 '+str(a53)+'x^3 '+str(a54)+'x^4 '+str(a55)+'x^5 '
besinci_denkleminin_buldugum_sonuclari=[a50+(a51*i)+(a52*pow(i,2))+(a53*pow(i,3))+(a54*pow(i,4))+(a55*pow(i,5)) for i in range(len(xler))]
Sr5=sum([pow(abs(degerler[i]-a50-a51-a52-a53-a54-a55),2) for i in range(n)])
Syx5=math.sqrt(Sr5/(n-6))
St5=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
Korelasyon_katsayisi5=((St5-Sr5)/St5)
yazdir2(besinci_denkleminin_buldugum_sonuclari,denk_5,5,Korelasyon_katsayisi5,Sr5,1,len(degerler))

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
print("\n-altıncı dereceden polinom denklemi=\n",a60,"x^0",a61,"x^1",a62,"x^2",a63,"x^3",a64,"x^4",a65,"x^5",a66,"x^6")
Sr6=sum([pow(abs(degerler[i]-a60-a61-a62-a63-a64-a65-a66),2) for i in range(n)])
Syx6=math.sqrt(Sr6/(n-7))
St6=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
Korelasyon_katsayisi6=((St6-Sr6)/St6)
altinci_denkleminin_buldugum_sonuclari=[a60+(a61*i)+(a62*pow(i,2))+(a63*pow(i,3))+(a64*pow(i,4))+(a65*pow(i,5))+(a66*pow(i,6)) for i in range(len(xler))]
denk_6='y= '+str(a60)+'x^0 '+str(a61)+'x^1 '+str(a62)+'x^2 '+str(a63)+'x^3 '+str(a64)+'x^4 '+str(a65)+'x^5 '+str(a66)+'x^6'+'\n'
yazdir2(altinci_denkleminin_buldugum_sonuclari,denk_6,6,Korelasyon_katsayisi6,Sr6,1,len(degerler))


# In[9]:


degerler_temp[i] = int(degerler_temp[i])
baslangic = 0
son = 10
while(son != len(degerler_temp)+1):
    degerler = git_oraya_kadar(baslangic ,son,degerler_temp)
    xler = [i+1 for i in range(len(degerler_temp))]
    xler = git_oraya_kadar(baslangic,son,xler)
    Xler_toplami=sum(xler)
    x_y_carpim_toplami= sum([(xler[i]*degerler[i]) for i in range(len(degerler))])
    Yler_toplami= sum(degerler)
    baslangic+=1
    son+=1
    hataOrani=[]
    n= len(degerler)
    
    A1=np.polyfit(xler,degerler,1)
    denk1=[A1[i] for i in range(len(A1))]
    a10,a11=denk1[1],denk1[0]
    denk_1='y= '+str(a10)+'x^0 '+str(a11)+'x^1'+'\n'
    birinci_denkleminin_buldugum_sonuclari=[a10+a11*i for i in range(len(xler))]
    Korelasyon_katsayisi1 = (((n*x_y_carpim_toplami)-(Xler_toplami*Yler_toplami))/math.sqrt((n*xlerin_karelerin_toplami-(pow(Xler_toplami,2)))*(n*Yler_karelerin_toplami-(pow(Yler_toplami,2)))))
    P=sum([abs(i-xler_ortalama) for i in range(n)])
    S=math.sqrt(pow(P,2)/(n-1))
    StandartError1= (S/(math.sqrt(n)))
    yazdir2(birinci_denkleminin_buldugum_sonuclari,denk_1,1,Korelasyon_katsayisi1,StandartError1,baslangic,son)
    
    a2=np.polyfit(xler,degerler,2)
    denk2=[a2[i] for i in range(len(a2))]
    a20,a21,a22=denk2[2],denk2[1],denk2[0]
    denk_2='y= '+str(a20)+'x^0 '+str(a21)+'x^1 '+str(a22)+'x^2'+'\n'
    ikinci_denkleminin_buldugum_sonuclari =[a20+(a21*i)+(a22*pow(i,2)) for i in range(len(xler))]
    Sr2=sum([pow(abs(degerler[i]-a20-a21-a22),2) for i in range(n)])
    Syx2=math.sqrt(Sr2/(n-3))
    St2=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
    Korelasyon_katsayisi2=((St2-Sr2)/St2)
    yazdir2(ikinci_denkleminin_buldugum_sonuclari,denk_2,2,Korelasyon_katsayisi2,Sr2,baslangic,son)
    hataOrani.append(Syx2)
    
    a3=np.polyfit(xler,degerler,3)
    denk3=[a3[i] for i in range(len(a3))]
    a30,a31,a32,a33=denk3[3],denk3[2],denk3[1],denk3[0]
    denk_3='y= '+str(a30)+'x^0 '+str(a31)+'x^1 '+str(a32)+'x^2 '+str(a33)+'x^3 '+'\n'
    ucuncu_denkleminin_buldugum_sonuclari =[a30+(a31*i)+(a32*pow(i,2))+(a33*pow(i,3)) for i in range(len(xler))]
    Sr3=sum([pow(abs(degerler[i]-a30-a31-a32-a33),2) for i in range(n)])
    Syx3=math.sqrt(Sr3/(n-4))
    St3=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
    Korelasyon_katsayisi3=((St3-Sr3)/St3)
    yazdir2(ikinci_denkleminin_buldugum_sonuclari,denk_3,3,Korelasyon_katsayisi3,Sr3,baslangic,son)
    hataOrani.append(Syx3)
    
    
    a4=np.polyfit(xler,degerler,4)
    denk4=[a4[i] for i in range(len(a4))]
    a40,a41,a42,a43,a44=denk4[4],denk4[3],denk4[2],denk4[1],denk4[0]
    denk_4='y= '+str(a40)+'x^0 '+str(a41)+'x^1 '+str(a42)+'x^2 '+str(a43)+'x^3 '+str(a44)+'x^4'+'\n'
    dortucu_denkleminin_buldugum_sonuclari=[a40+(a41*i)+(a42*pow(i,2))+(a43*pow(i,3))+(a44*pow(i,4)) for i in range(len(xler))]
    Sr4=sum([pow(abs(degerler[i]-a40-a41-a42-a43-a44),2) for i in range(n)])
    Syx4=math.sqrt(Sr4/(n-5))
    St4=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
    Korelasyon_katsayisi4=((St4-Sr4)/St4)
    yazdir2(dortucu_denkleminin_buldugum_sonuclari,denk_4,4,Korelasyon_katsayisi4,Sr4,baslangic,son)
    hataOrani.append(Syx4)
    
    a5=np.polyfit(xler,degerler,5)
    denk5=[a5[i] for i in range(len(a5))]
    a50,a51,a52,a53,a54,a55=denk5[5],denk5[4],denk5[3],denk5[2],denk5[1],denk5[0]
    denk_5='y= '+str(a50)+'x^0 '+str(a51)+'x^1 '+str(a52)+'x^2 '+str(a53)+'x^3 '+str(a54)+'x^4'+str(a55)+'x^5'+'\n'
    besinci_denkleminin_buldugum_sonuclari=[a50+(a51*i)+(a52*pow(i,2))+(a53*pow(i,3))+(a54*pow(i,4))+(a55*pow(i,5)) for i in range(len(xler))]
    Sr5=sum([pow(abs(degerler[i]-a50-a51-a52-a53-a54-a55),2) for i in range(n)])
    Syx5=math.sqrt(Sr5/(n-6))
    St5=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
    Korelasyon_katsayisi5=((St5-Sr5)/St5)
    yazdir2(besinci_denkleminin_buldugum_sonuclari,denk_5,5,Korelasyon_katsayisi5,Sr5,baslangic,son)
    hataOrani.append(Syx5)
    
    a6=np.polyfit(xler,degerler,6)
    denk6=[a6[i] for i in range(len(a6))]
    a60,a61,a62,a63,a64,a65,a66=denk6[6],denk6[5],denk6[4],denk6[3],denk6[2],denk6[1],denk6[0]
    denk_6='y= '+str(a60)+'x^0 '+str(a61)+'x^1 '+str(a62)+'x^2 '+str(a63)+'x^3 '+str(a64)+'x^4 '+str(a65)+'x^5 '+str(a66)+'x^6'+'\n'
    altinci_denkleminin_buldugum_sonuclari=[a60+(a61*i)+(a62*pow(i,2))+(a63*pow(i,3))+(a64*pow(i,4))+(a65*pow(i,5))+(a66*pow(i,6)) for i in range(len(xler))]
    Sr6=sum([pow(abs(degerler[i]-a60-a61-a62-a63-a64-a65-a66),2) for i in range(n)])
    Syx6=math.sqrt(Sr6/(n-7))
    St6=sum([pow((degerler[i]-Yler_toplami),2) for i in range(n)])
    Korelasyon_katsayisi6=((St6-Sr6)/St6)
    yazdir2(altinci_denkleminin_buldugum_sonuclari,denk_6,6,Korelasyon_katsayisi6,Sr6,baslangic,son)
    hataOrani.append(Syx6)
    min_hata = hataOrani[0]
    for i in hataOrani:
        if (i < min_hata):
            min_hata = i   
        
    print("[",baslangic,"-",son-1,"] aralginida ki ")
    print("en uygun ",(hataOrani.index(min_hata)+1),"denklemi hata degeri",min_hata,"\n")
    hataOrani=[0]


# In[ ]:





# In[ ]:




