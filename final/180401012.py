#FATİH CİHAN TASKİN 180401012
katsayi_list=[]
ideal_katsayilar=[]
def matris_olustur(size):
    matris=[]

    for k in range(0,size+1):
        matris.append(x_sums[k:k+size+1])    
        matris[k].append(xy_sums[k])

    x_sums.clear
    xy_sums.clear
    return matris
    
def matris_coz(matris):
    boyut=len(matris)
    for n in range(boyut):
        kat = int(matris[n][n])
        for m in range(boyut+1):
            matris[n][m]=int(matris[n][m])/kat
        for p in range(1,boyut-n):
            kat = float(matris[n+p][n])
            for q in range(boyut+1):
                matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))

    return matris,boyut-1

def katsayilar():   
    if(size==2):
        a2=matris[2][3]
        a1=matris[1][3]- matris[1][2]*a2
        a0=matris[0][3]- matris[0][2]*a2 - matris[0][1]*a1    
        
     
        katsayilar1=[a0,a1,a2]
   
        katsayi_list.append(katsayilar1)
        
        for i in range(n):
            Sr_list.append((data[i] - (int(a0 + a1*(i+1) +a2*(i+1)**2)))**2)
            St_list.append((data[i] - y_ust)**2)
        
    if(size==3):
        a3=matris[3][4]
        a2=matris[2][4]-matris[2][3]*a3
        a1=matris[1][4]-matris[1][3]*a3-matris[1][2]*a2
        a0=matris[0][4]-matris[0][3]*a3-matris[0][2]*a2 - matris[0][1]*a1


        katsayilar2=[a0,a1,a2,a3]

        katsayi_list.append(katsayilar2)
        
        for i in range(n):
            Sr_list.append((data[i] - int(a0 + a1*(i+1) +a2*(i+1)**2 + a3*(i+1)**3))**2)
            St_list.append((data[i] - y_ust)**2)        
        
    if(size==4):
        a4=matris[4][5]
        a3=matris[3][5]-matris[3][4]*a4
        a2=matris[2][5]-matris[2][4]*a4- matris[2][3]*a3
        a1=matris[1][5]- matris[1][4]*a4- matris[1][3]*a3 - matris[1][2]*a2
        a0=matris[0][5]- matris[0][4]*a4 - matris[0][3]*a3 - matris[0][2]*a2 - matris[0][1]*a1
 
    
        katsayilar3=[a0,a1,a2,a3,a4]

        katsayi_list.append(katsayilar3)
        for i in range(n):
            Sr_list.append((data[i]- int(a0 + a1*(i+1) + a2*(i+1)**2 +a3*(i+1)**3 + a4*(i+1)**4))**2)
            St_list.append((data[i] - y_ust)**2)   

    if(size==5):
        a5=matris[5][6]
        a4=matris[4][6]- matris[4][5]*a5
        a3=matris[3][6]- matris[3][5]*a5 - matris[3][4]*a4
        a2=matris[2][6] - matris[2][5]*a5 - matris[2][4]*a4 - matris[2][3]*a3 
        a1=matris[1][6] - matris[1][5]*a5 - matris[1][4]*a4 - matris[1][3]*a3 - matris[1][2]*a2
        a0=matris[0][6] - matris[0][5]*a5 - matris[0][4]*a4 - matris[0][3]*a3 - matris[0][2]*a2 - matris[0][1]*a1
        
        
        katsayilar4=[a0,a1,a2,a3,a4,a5]

        katsayi_list.append(katsayilar4)
        for i in range(n):
            Sr_list.append((data[i]- int(a0 + a1*(i+1) + a2*(i+1)**2 +a3*(i+1)**3 + a4*(i+1)**4 + a5*(i+1)**5))**2)
            St_list.append((data[i] - y_ust)**2)         
           
    if(size==6):
        a6=matris[6][7]
        a5=matris[5][7] - matris[5][6]*a6
        a4=matris[4][7] - matris[4][6]*a6 - matris[4][5]*a5
        a3=matris[3][7] - matris[3][6]*a6 - matris[3][5]*a5 - matris[3][4]*a4
        a2=matris[2][7] - matris[2][6]*a6 - matris[2][5]*a5 - matris[2][4]*a4 - matris[2][3]*a3
        a1=matris[1][7] - matris[1][6]*a6 - matris[1][5]*a5 - matris[1][4]*a4 - matris[1][3]*a3 - matris[1][2]*a2 
        a0=matris[0][7] - matris[0][6]*a6 - matris[0][5]*a5 - matris[0][4]*a4 - matris[0][3]*a3 - matris[0][2]*a2 - matris[0][1]*a1
        
        
        katsayilar5=[a0,a1,a2,a3,a4,a5,a6]

        katsayi_list.append(katsayilar5)
        for i in range(n):
            Sr_list.append((data[i]- int(a0 + a1*(i+1) + a2*(i+1)**2 +a3*(i+1)**3 + a4*(i+1)**4 + a5*(i+1)**5 + a6*(i+1)**6))**2)
            St_list.append((data[i] - y_ust)**2)        
        
    
    Sr=(sum(Sr_list))
    St=(sum(St_list))
    Sr_list.clear()
    St_list.clear()
    r.append(((St - Sr)/St)**(1/2))
        

def lineer_regression():
    
    n=len(data)
    x_sum=0
    y_sum=sum(data)
    xi_yi_sum=0
    x_squared_sum=0
    for i in range (n):
        x_sum += (i+1)
        xi_yi_sum += data[i] * (i+1)
        x_squared_sum += (i+1)*(i+1)
    
    a1 = (n * xi_yi_sum - x_sum * y_sum) / (n * x_squared_sum - (x_sum)**2)
    a0 = (y_sum - a1 * x_sum ) / n
    

    katsayilar=[a0,a1]

    katsayi_list.append(katsayilar)
    for i in range(n):
        Sr_list.append((data[i] - int(a0 + a1*(i+1)))**2)
        St_list.append((data[i] - y_ust)**2)
    

    Sr=(sum(Sr_list))
    St=(sum(St_list))
    Sr_list.clear()
    St_list.clear()
    r.append(((St - Sr)/St)**(1/2))
   
    
data=[]
for satir in open('veriler.txt', 'r'):  # dosyamızdan verileri çektik
    data.append(int(satir))

#dosya=open("katsayilar.txt",'w')
n=len(data)
x_sum=0
y_sum=sum(data)
x2_sum, x3_sum, x4_sum, xy_sum, x2y_sum, x5_sum, x6_sum, x3y_sum, x7_sum, x8_sum, x4y_sum, x9_sum, x10_sum, x5y_sum, x11_sum, x12_sum, x6y_sum=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
y_ust=y_sum/n
for i in range(n):
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
    xy_sum += (i+1) * data[i]
    x2y_sum += ((i+1)**2) * data[i]
    x3y_sum += ((i+1)**3) * data[i]
    x4y_sum += ((i+1)**4) * data[i]
    x5y_sum += ((i+1)**5) * data[i]
    x6y_sum += ((i+1)**6) * data[i]
    
      
x_sums=[n,x_sum,x2_sum,x3_sum,x4_sum,x5_sum,x6_sum,x7_sum,x8_sum,x9_sum,x10_sum,x11_sum,x12_sum]
xy_sums=[y_sum,xy_sum,x2y_sum,x3y_sum,x4y_sum,x5y_sum,x6y_sum] 

Sr_list=[]
St_list=[]
r=[]#korelasyonlar
Sr=0
St=0
r_abs=[]#korelasyonların ideala olan yakınlıgı
best_r=0#en ideal yakınlık

lineer_regression()#1.derece dogruluk icin ayrı hesaplandi
for i in range(2,7):#2.dereceden 6. dereceye yakınlastırıldı
    matris,size=matris_coz(matris_olustur(i))
    katsayilar()
    

for i in range(0,6):
    r_abs.append(abs(1-r[i]))#korelasyon degerlerinin idealligi hesaplanip diziye atandı

best_r=sorted(r_abs)[0]#en ideali saptanıp atandı
#print(best_r)

print("En yakın polinomun derecesi: ",r_abs.index(best_r) +1)

if((r_abs.index(best_r) +1)==1):
    ideal_katsayilar=katsayi_list[0]

elif((r_abs.index(best_r) +1)==2):
    ideal_katsayilar=katsayi_list[1]
    
elif((r_abs.index(best_r) +1)==3):
    ideal_katsayilar=katsayi_list[2]
    
elif((r_abs.index(best_r) +1)==4):
    ideal_katsayilar=katsayi_list[3]
    
elif((r_abs.index(best_r) +1)==5):
    ideal_katsayilar=katsayi_list[4]

elif((r_abs.index(best_r) +1)==6):
    ideal_katsayilar=katsayi_list[5]
    
#print(ideal_katsayilar)



def f(x):
    denklem=0
    for i in range(len(ideal_katsayilar)):
        denklem+=ideal_katsayilar[i]*x**(i)
    return denklem



def pol_integral():
    a=2#alt sınır ogrenci numarasi   
    b=len(data)#üst sınır    
    deltax=1      
    integral=0
    n2=int((b-a)/deltax)      

    for i in range(n2):
        integral +=deltax*(f(a) + f(a+deltax))/2
        a+=deltax    
        
    print(integral)
    
    
    
def not_pol_integral():
    a=2#alt sınır ogrenci numarasi   
    b=len(data)#üst sınır  
    integral =0
    deltax=1
    n2 = int((b-a)/deltax)
    for i in range(n2-1):
        integral += deltax * (data[a] + data[a + deltax])/2
        a+=deltax
    print(integral)

print("Yakinlastirilmis polinom ile hesaplanan integral: ")
pol_integral()
print("Gercek verilerle hesaplanan integral: ")
not_pol_integral()

with open("180401012_yorum.txt","w",encoding='utf-8') as file:
    file.write("Fatih Cihan Taskin 180401012\n")
    file.write("İlk şıkta elimizdeki verilerin grafiğine 'en yakın' polinomu bulmuştuk\n")
    file.write("Daha sonra o polinomun integralini hesaplattık\n")
    file.write("Polinomlu integral hesaplanırken deltax ne kadar küçülürse o kadar yakın sonuç çıkacağını gördük\n")
    file.write("Gerçek verilerle hesaplanan integralde deltax 1 alindi cünkü ara değerlerin karsiligini bilmiyorduk sadece tam degerlerin karsiligina sahiptik\n")
    file.write("Gerçek verilerle hesaplanan integralde deltax 1 alındığı için eşit bir kıyas yapmak amacıyla polinomlu integralde de deltax 1 alındı\n")
    file.write("Eşit koşullarda hesaplanan bu iki integralin arasında fark olmasının asıl nedeni bizim her ne kadar en yakın diye kabul ettiğimiz parabolün\n")
    file.write("gerçek verilerin grafiğine tam olarak uymamasıdır.")
    file.write("Yani biz 1,2,3,4,5,6 derece arasından en yakın polinomu bulduk ama gerçekte bu polinom bizim verilerimize çok yakın olmak zorunda değildir.\n")
    file.write("Eğer korelasyon sayımız 1 olsaydı yani polinomumuz gerçek verilerle tamamen örtüşseydi böyle bir fark olmayacakti.")
    
    
    
