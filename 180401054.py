#Ceyda Kamalı 180401054
def rbulma(r1,r2,r3,r4,r5,r6,file):
    file.write("polinomlarda elde ettigimiz r degerini kiyaslayip hangisi 1 e yakınsa onu seciyoruz"+"\n")
    file.write("r1 = "+str(r1)+" r2 = "+str(r2)+" r 3 = "+str(r3)+"r4 = "+str(r4)+" r5 = "+str(r5)+" r6 = "+str(r6)+"\n")
    file.write("bulunan r degerlerini bir diziye aktarip kiyaslama yapiyoruz...."+"\n")
    dizi = [r1,r2,r3,r4,r5,r6]
    for i in range(len(dizi)):
        if dizi[i] == max(dizi):
            file.write("r="+str(dizi[i])+" "+str(i+1)+". polinom\n")
def polinom(derece,event):##derece=kacinci dereceden polinoma yaklaşcaksa o değer, event= listem
    m=[]
    x=0
    for i in range(derece+1):
        mn=[]
        for j in range(derece+1):
            top=0
            for k in range(1,len(event)+1):
                top += k**l
            mn.append(top)
            x += 1
        m.append(mn)
        x -=derece
    matr=[]
    for i in range(derece+1):
        top=0
        for j in range(len(event)):
            top += event[j]*(j+1)**i
        matr.append(top)
    for i in range(derece+1):
        b=m[i][i]
        for j in range(i+1,derece+1):
            o=b/m[j][i]
            matr[j]=matr[j]*o-matr[i]
            for k in range(derece+1):
                m[j][k] = m[j][k]*o-m[i][k]
    for i in range(derece,-1,-1):
        b = m[i][i]
        for j in range(i-1,-1,-1):
            o=b/m[j][i]
            matr[j] = matr[j]*o-matr[i]
            for k in range(derece+1):
                m[j][k]= m[j][k]*o-m[i][k]
    for i in range(derece+1):
        matr[i]=matr[i]/m[i][i]
    y=0
    for i in range (len(event)):
        y+= event[i]
    y= y/len(event)
    St=0
    Sr=0
    for i in range(len(event)):
        x =event[i]
        St +=(event[i]-y_ort)**2
        for j in range(len(matr)):
            x -= matr[j]*(i+1)**j
        x=x**2
        Sr += x
    r=((St-Sr)/St)**(1/2)
    return matr,r
def multiple(pol1,pol2,pol3,pol4,pol5,pol6,file):
    file.write("polinomların katsayıları bulundu....."+"\n")
    file.write("1.derece a0 = "+str(pol1[0]) + " a1 = " + str(pol1[1])+"\n"+"2.derece a0 = "+str(pol2[0]) + " a1 = " + str(pol2[1]) + " a2 =" + str(pol2[2]) + "\n"+"3.derece a0 = "+str(pol3[0]) + " a1 = " + str(pol3[1]) + " a2 =" + str(pol3[2]) + " a3 = " + str(pol3[3]) + "\n"+"4.derece a0 = "+str(pol4[0]) + " a1 = " + str(pol4[1]) + " a2 =" + str(pol4[2]) + " a3 = " + str(pol4[3]) + " a4 = " + str(pol4[4]) + "\n"+"5.derece a0 = "+str(pol5[0]) + " a1 = " + str(pol5[1]) + " a2 =" + str(pol5[2]) + " a3 = " + str(pol5[3]) + " a4 = " + str(pol5[4]) + " a5 = "+ str(pol5[5])+"\n"+"6.derece a0 = "+str(pol6[0]) + " a1 = " + str(pol6[1]) + " a2 =" + str(pol6[2]) + " a3 = " + str(pol6[3]) + " a4 = " + str(pol6[4]) + "a5="+str(pol6[5])+"a6="+str(pol6[6])+"\n")
my_file = open("veriler.txt","r")
event = my_file.readlines()
for i in range(len(event)):
    event[i]=int(event[i])
pol1,r1=polinom(1,event)
pol2,r2=polinom(2,event)
pol3,r3=polinom(3,event)
pol4,r4=polinom(4,event)
pol5,r5=polinom(5,event)
pol6,r6=polinom(6,event)
my_file.close()
file= open("sonuc.txt","w")
multiple(pol1,pol2,pol3,pol4,pol5,pol6,file)
r_bulma(r1,r2,r3,r4,r5,r6,file)
for i in range(len(event)//10):
    grup=[]
    for j in range(10):
        grup.append(event[10*i+j])
    pol1,r1=polinom(1,grup)
    pol2,r2=polinom(2,grup)
    pol3,r3=polinom(3,grup)
    pol4,r4=polinom(4,grup)
    pol5,r5=polinom(5,grup)
    pol6,r6=polinom(6,grup)
    multiple(pol1,pol2,pol3,pol4,pol5,pol6,file)
    r_bulma(r1,r2,r3,r4,r5,r6,file)
file.close()

