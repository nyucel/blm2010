#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lara Betül Arslantaş-180401024
def polinoma_cevirme(derece,veriler): 
    matris = []
    a = 0
    for i in range(derece+1): 
        satir = []
        for j in range(derece+1):
            toplam = 0
            for k in range(1,len(veriler)+1):
                toplam += k**a
            satir.append(toplam)
            a += 1
        matris.append(satir)
        a -= derece
    sonuc = []
    for i in range(derece+1):
        toplam = 0
        for j in range(len(veriler)):
            toplam += veriler[j]*(j+1)**i
        sonuc.append(toplam)
    for i in range(derece+1):
        b = matris[i][i]
        for j in range(i+1,derece+1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]  
    for i in range(derece,-1,-1):
        b = matris[i][i]
        for j in range(i-1,-1,-1):
            bolum = b/matris[j][i]
            sonuc[j] = sonuc[j]*bolum-sonuc[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*bolum-matris[i][k]
    for i in range(derece+1):
        sonuc[i] = sonuc[i]/matris[i][i]
    y_ort=0
    for i in range (len(veriler)):
        y_ort += veriler[i]
    y_ort = y_ort/len(veriler)
    St=0
    Sr=0
    for i in range(len(veriler)):
        x = veriler[i]
        St +=(veriler[i]-y_ort)**2
        for j in range(len(sonuc)):
            x -= sonuc[j]*(i+1)**j
        x=x**2
        Sr += x
    korelasyon = ((St-Sr)/St)**(1/2)
    return sonuc,korelasyon

def en_uygun_polinom(k1,k2,k3,k4,k5,k6,dosya):
    dosya2.write("katsayi1 = "+str(k1)+" katsayi2 = "+str(k2)+" katsayi 3 = "+str(k3)+" katsayi4 = "+str(k4)+" katsayi5 = "+str(k5)+" katsayi6 = "+str(k6)+"\n")
    degerler = [k1,k2,k3,k4,k5,k6]
    for i in range(len(degerler)):
        if degerler[i] == max(degerler):
             dosya2.write("En uygun olan "+str(i+1)+". polinomdur.\n")

def polinom_katsayilari(p1,p2,p3,p4,p5,p6,dosya):
    dosya2.write("1.dereceden polinom : a0 = "+str(p1[0]) + " a1 = " + str(1[1])+"\n" )
    dosya2.write("2.dereceden polinom : a0 = "+str(p2[0]) + " a1 = " + str(p2[1]) + " a2 =" + str(p2[2]) + "\n")
    dosya2.write("3.dereceden polinom : a0 = "+str(p3[0]) + " a1 = " + str(p3[1]) + " a2 =" + str(p3[2]) + " a3 = " + str(p3[3]) + "\n")
    dosya2.write("4.dereceden polinom : a0 = "+str(p4[0]) + " a1 = " + str(p4[1]) + " a2 =" + str(p4[2]) + " a3 = " + str(p4[3]) + " a4 = " + str(p4[4]) + "\n")
    dosya2.write("5.dereceden polinom : a0 = "+str(p5[0]) + " a1 = " + str(p5[1]) + " a2 =" + str(p5[2]) + " a3 = " + str(p5[3]) + " a4 = " + str(p5[4]) + " a5 = "+ str(5[5])+ "\n")
    dosya2.write("6.dereceden polinom : a0 = "+str(p6[0]) + " a1 = " + str(p6[1]) + " a2 =" + str(p6[2]) + " a3 = " + str(p6[3]) + " a4 = " + str(p6[4]) + " a5 = "+ str(p6[5])+" a6 = "+str(p6[6])+ "\n")

dosya = open("veriler.txt","r")
veriler = dosya.readlines()
for i in range(len(veriler)):
    veriler[i]=int(veriler[i])



p1,k1=polinoma_cevirme(1,veriler)
p2,k2=polinoma_cevirme(2,veriler)
p3,k3=polinoma_cevirme(3,veriler)   
p4,k4=polinoma_cevirme(4,veriler)
p5,k5=polinoma_cevirme(5,veriler)
p6,k6=polinoma_cevirme(6,veriler)

dosya.close()
dosya2 = open("sonuc.txt","w")
polinom_katsayilari(p1,p2,p3,p4,p5,p6,dosya2)
en_uygun_polinom(k1,k2,k3,k4,k5,k6,dosya2)
for i in range(len(veriler)//10):
    dosya2.write("\n"+str(i+1)+". 10'lu grup : \n")
    onluGruplar=[]
    for j in range(10):
        onluGruplar.append(veriler[10*i+j])

    p1,k1=polinoma_cevirme(1,onluGruplar)
    p2,k2=polinoma_cevirme(2,onluGruplar)
    p3,k3=polinoma_cevirme(3,onluGruplar)
    p4,k4=polinoma_cevirme(4,onluGruplar)
    p5,k5=polinoma_cevirme(5,onluGruplar)
    p6,k6=polinoma_cevirme(6,onluGruplar)
    polinom_katsayilari(p1,p2,p3,p4,p5,p6,dosya2)
    en_uygun_polinom(k1,k2,k3,k4,k5,k6,dosya2)
dosya2.close()


# In[ ]:




