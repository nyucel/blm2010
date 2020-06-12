#Berivan ARAS
#180401037

def polinom_bulma(m1,m2,m3,m4,m5,m6,file):
    
    file.write("m1 = "+str(m1)+" m2 = "+str(m2)+" m3 = "+str(m3)+" m4 = "+str(m4)+" m5 = "+str(m5)+" m6 = "+str(m6)+"\n")
    if m1>m6 and m1>m5 and m1>m4 and m1>m3 and m1>m2:
        file2.write(str(m1) + "en uygun 1. polinom. \n")
        
    elif m2>m6 and m2>m5 and m2>m4 and m2>m3:
        file2.write(str(m2) + "en uygun 2.polinom. \n")
        
    elif m3>m6 and m3>m5 and m3>m4:
        file2.write(str(m3) + " en uygun 3.polinom. \n")
        
    elif m4>m6 and m4>m5:
        file2.write(str(m4) + "en uygun 4.polinom. \n")
        
    elif m5>m6:
        file2.write(str(m5) + "en uygun 5.polinom. \n")
        
    else:
        file2.write(str(m6) + "en uygun 6.polinom. \n")


def katsayılar(pol1,pol2,pol3,pol4,pol5,pol6,file):
    file.write("1.dereceden polinom icin x0 = "+str(pol1[0]) + " x1 = " + str(pol1[1]) + "\n" )
    file.write("2.dereceden polinom icin x0 = "+str(pol2[0]) + " x1 = " + str(pol2[1]) + " x2 =" + str(pol2[2]) + "\n")
    file.write("3.dereceden polinom icin x0 = "+str(pol3[0]) + " x1 = " + str(pol3[1]) + " x2 =" + str(pol3[2]) + " x3 = " + str(pol3[3]) + "\n")
    file.write("4.dereceden polinom icin x0 = "+str(pol4[0]) + " x1 = " + str(pol4[1]) + " x2 =" + str(pol4[2]) + " x3 = " + str(pol4[3]) + " x4 = " + str(pol4[4]) + "\n")
    file.write("5.dereceden polinom icin x0 = "+str(pol5[0]) + " x1 = " + str(pol5[1]) + " x2 =" + str(pol5[2]) + " x3 = " + str(pol5[3]) + " x4 = " + str(pol5[4]) + " x5 = "+ str(pol5[5])+ "\n")
    file.write("6.dereceden polinom icin x0 = "+str(pol6[0]) + " x1 = " + str(pol6[1]) + " x2 =" + str(pol6[2]) + " x3 = " + str(pol6[3]) + " x4 = " + str(pol6[4]) + " x5 = "+ str(pol6[5])+" x6 = "+str(pol6[6])+ "\n")


def interpolasyon(derece,veri):
    matrix=[]
    a=0

    for i in range(derece+1):
        line=[]
        for j in range(derece+1):
            toplam=0
            for k in range(1,len(veri)+1):
                toplam += k**a
            line.append(toplam)
            a += 1
        matrix.append(line)
        a -= derece



    cozum = []
    for i in range(derece+1):
        toplam=0
        for j in range(len(veri)):
            toplam += veri[j]*(j+1)**i
        cozum.append(toplam)


    for i in range(derece,-1,-1):
        simile = matrix[i][i]
        for j in range(i-1,-1,-1):
            rate=simile/matrix[j][i]
            cozum[j] = cozum[j]*rate-cozum[i]
            for k in range(derece+1):
                matrix[j][k]= matrix[j][k]*rate-matrix[i][k]
                
    for i in range(derece+1):
        simile = matrix[i][i]
        for j in range(i+1, derece+1):
            rate = simile/matrix[j][i]
            cozum[j] = cozum[j]*rate-cozum[i]
            for k in range(derece+1):
                matrix[j][k] = matrix[j][k]*rate-matrix[i][k]
                
                

    for i in range(derece+1):
        cozum[i]=cozum[i]/matrix[i][i]
        
    y_ortalama=0
    
    for i in range (len(veri)):
        y_ortalama += veri[i]
    y_ortalama = y_ortalama/len(veri)
    y_ortalama_t, y_ortalama_r = 0,0
    
    
    for i in range(len(veri)):
        z = veri[i]
        y_ortalama_t += (veri[i]-y_ortalama)**2
        for j in range(len(cozum)):
            z -= cozum[j]*(i+1)**j
        z=z**2
        y_ortalama_r += z
    m = ((y_ortalama_t - y_ortalama_r)/y_ortalama_t)**(1/2)
    
    return cozum,m

file = open("veri.txt","r")
veri = file.readlines()
for i in range(len(veri)):
    veri[i]=int(veri[i])



pol1,m1=interpolasyon(1,veri)
pol2,m2=interpolasyon(2,veri)
pol3,m3=interpolasyon(3,veri)
pol4,m4=interpolasyon(4,veri)
pol5,m5=interpolasyon(5,veri)
pol6,m6=interpolasyon(6,veri)

file.close()
file2 = open("sonuc.txt","w")
katsayılar(pol1,pol2,pol3,pol4,pol5,pol6,file2)
polinom_bulma(m1,m2,m3,m4,m5,m6,file2)
for i in range(len(veri)//10):

    file2.write("\n"+str(i+1)+". 10'lu grup icin \n")
    onlu_sıralı=[]
    for j in range(10):
        onlu_sıralı.append(veri[10*i+j])
    pol1,m1=interpolasyon(1,onlu_sıralı)
    pol2,m2=interpolasyon(2,onlu_sıralı)
    pol3,m3=interpolasyon(3,onlu_sıralı)
    pol4,m4=interpolasyon(4,onlu_sıralı)
    pol5,m5=interpolasyon(5,onlu_sıralı)
    pol6,m6=interpolasyon(6,onlu_sıralı)
    katsayılar(pol1,pol2,pol3,pol4,pol5,pol6,file2)
    polinom_bulma(m1,m2,m3,m4,m5,m6,file2)
file2.close()
