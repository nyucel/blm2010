
# Fikret ÇAKIRLI 140401099

def yorum_yap():
    f = open("yorum.txt","w",encoding="UTF-8")
    f.write("""   
# Fikret ÇAKIRLI 140401099
 Polinom kullanırsak adım aralığının bir önemi yoktur. Hata oranı terim sayısına bağlı artacaktır.
Polinom kullanmazsak h çok küçük olmalıdır ki türeve daha yakın bir değer bulabilelim.
Kullanılan data ne kadar fazla olursa gerçek değere daha çok yaklaşılır.
Bu nedenle hata değeri gerçeğine göre daha düşük olacaktır. """)
    f.close()

##asal sayıların dosyasını oluşturma 
# def asal_yaz(asal):
#     dosya = open('asallar.txt','a+')
#     dosya.write(str(asal)+'\n')
# for num in range(2, 600 + 1):
    
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             asal_yaz(num)
#polinom denkemine x"in değeri atamak fonk.
def f(denklem,x_degeri):
    top=0  
    top+=denklem[0]+sum([denklem[i+1]*pow(x_degeri,i+1) for i in range(len(denklem)-1)])
    return top

def turev_bul_polinom(poli_denklem):
    x0=99 #140401099
    h=0.01
    turev=(f(poli_denklem,(x0+h))-f(poli_denklem,x0))/h
    return turev

def turev_bul_polinomsuz():
    a = 99   #140401099
    h = 1
    turev = (degerler[a+h]-degerler[a])/h
    return turev

import numpy as np 

# dosya okuma 
file=open("asallar.txt")
degerler = []
for line in file.readlines():
    line=line.rstrip('\n')
    degerler.append(line)
file.close()    

#list`in degerleri stringten integere cevirme 
for i in range(0,len(degerler)):
    degerler[i] = int(degerler[i])
#------------------------------------------------
n= len(degerler)
x_2_t ,x_3_t,x_4_t = 0,0,0
x_5_t ,x_6_t,x_mult_y_sum= 0,0,0
x2_mult_y_sum ,x3_mult_y_sum,x_t=0,0,0

#--------------------------- 
xler = [i+1 for i in range(n)]
x_t=sum(xler)
x_ort = np.mean(xler)
y_t= sum(degerler)
y_ort = np.mean(degerler)
y_2_t= sum([pow(degerler[i],2) for i in range(n)])
x_2_t= sum([pow(i+1,2) for i in range(n)])
x_3_t= sum([pow(i+1,3) for i in range(n)])
x_4_t= sum([pow(i+1,4) for i in range(n)])
x_5_t= sum([pow(i+1,5) for i in range(n)])
x_6_t= sum([pow(i+1,6) for i in range(n)])

x_mult_y_sum= sum([(i+1)*degerler[i] for i in range(n)])
x2_mult_y_sum = sum([pow(i+1,2)*degerler[i] for i in range(n)])
x3_mult_y_sum = sum([pow(i+1,3)*degerler[i] for i in range(n)])
mtrx= [[n,x_t,x_2_t, x_3_t],
          [x_t,x_2_t,x_3_t,x_4_t],
          [x_2_t,x_3_t,x_4_t,x_5_t],
          [x_3_t,x_4_t,x_5_t,x_6_t]]

det = np.linalg.det(mtrx) 
mtrx_tmp = [i[:] for i in mtrx]
mtrx[0][0],mtrx[1][0],mtrx[2][0],mtrx[3][0]= y_t,x_mult_y_sum,x2_mult_y_sum,x3_mult_y_sum 
det1 = np.linalg.det(mtrx) 
mtrx= [i[:] for i in mtrx_tmp]
mtrx[0][1],mtrx[1][1],mtrx[2][1],mtrx[3][1]= y_t,x_mult_y_sum,x2_mult_y_sum,x3_mult_y_sum 
det2 = np.linalg.det(mtrx) 
mtrx= [i[:] for i in mtrx_tmp]
mtrx[0][2],mtrx[1][2],mtrx[2][2],mtrx[3][2]= y_t,x_mult_y_sum,x2_mult_y_sum,x3_mult_y_sum 
det3 = np.linalg.det(mtrx) 
mtrx= [i[:] for i in mtrx_tmp]
mtrx[0][3],mtrx[1][3],mtrx[2][3],mtrx[3][3]= y_t,x_mult_y_sum,x2_mult_y_sum,x3_mult_y_sum 
det4 = np.linalg.det(mtrx) 

a30,a31,a32,a33=(det1/det),(det2/det),(det3/det),(det4/det)
denk=[]
denk.append(a30)
denk.append(a31)
denk.append(a32)
denk.append(a33)
turev= turev_bul_polinom(denk)
turev2= turev_bul_polinomsuz()
print("\n-üçüncü dereceden polinom denklemi=\n",a30,"x^0",a31,"x^1",a32,"x^2",a33,"x^3") 
print("\n-polinom denklemi kullanarak truevi",turev)
print("\n-polinom denklemi kullanmadan truevi",turev2)
yorum_yap()
