#170401041 Mehmet Akif Selbi

import math
def dosya_oku():
    dosya = open("veriler.txt")
    y = dosya.readlines()
    x=[]
    for i in range(len(y)):
        y[i]=int(y[i])
        x.append(i)
    return x,y

def matris_olustur(x,y,n,m):
    
    matris=[]
    for i in range(m+1):
        satir=[]
        for j in range(m+1):
            if(i==0 and j==0):
                satir.append(n)
            else:
                x_toplam = 0
                for x_eleman in x:
                    x_toplam += x_eleman**(i+j)
                satir.append(x_toplam)
        sum_= 0
        for eleman in range(n):
            sum_ += (x[eleman]**i)*y[eleman]
        satir.append(sum_)
        matris.append(satir)
    return matris

def matris_coz(matris):#Gauss
    boyut = len(matris)
    for i in range(0, boyut):
        maxSutun = abs(matris[i][i])
        maxSatir = i
        for j in range(i + 1, boyut):
            if abs(matris[j][i]) > maxSutun:
                maxSutun = abs(matris[j][i])
                maxSatir = j
        for k in range(i, boyut + 1):
            temp = matris[maxSatir][k]
            matris[maxSatir][k] = matris[i][k]
            matris[i][k] = temp
            
        for l in range(i + 1, boyut):
            c = -matris[l][i] / matris[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    matris[l][j] = 0
                else:
                    matris[l][j] += c * matris[i][j]

    r_matris = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        r_matris[i] = matris[i][boyut] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][boyut] -= matris[k][i] * r_matris[i]
    return r_matris

def korelasyon_ve_hata(x,y,n,katsayilar,m):
    Sr,St,y_= 0,0,0
    for i in y:
        y_+= i
    y_ /= len(y)
    for i in range(n):
        Sr_1=0
        St += (y[i]-y_)**2
        Sr_1 += y[i]-katsayilar[0]
        for j in range(1,m+1):
            Sr_1 -= katsayilar[j]*(x[i]**j)
        Sr_1 = Sr_1**2
        Sr+=Sr_1
    S_y_x = math.sqrt(abs(Sr/(n-(m+1)))) #Standart tahmini hata
    if(St==0):
        r = "inf"
    else:
        r = math.sqrt(abs((St-Sr)/St)) #korelasyon
    return r,S_y_x

def polinom_yakinlastirma(x,y,dosya):
    r =[]
    dosya.write("       1. Soru             \n-------------------------------------------------------\n\n")
    for i in range(1,7):
        katsayilar = matris_coz(matris_olustur(x,y,len(y),i))
        dosya.write(str(i)+". dereceden polinomun\nsirasiyla katsayilari: "+str(katsayilar)+"\n")
        r.append(korelasyon_ve_hata(x,y,len(y),katsayilar,i))
        dosya.write("korelasyon katsayisi: "+str(r[i-1][0])+"\n")
        dosya.write("Standart Tahmini Hata: "+str(r[i-1][1])+"\n\n\n")
        
    dosya.write("       2. Soru             \n----------------------------------------------------\n\n")
    max_= r[0][0]
    min_ = r[0][1]
    temp = 0
    for z in range(len(r)):
        if(r[z][0] > max_):
            max_ = r[z][0]
            temp = z+1
        if(z < min_):
            min_ = r[z][1]
    dosya.write("en buyuk korelasyon : "+str(max_))
    dosya.write("\nen kucuk standart tahmini hata :"+str(min_)+"\n")
    dosya.write("en uygun polinom: "+str(temp)+". dereceden \n\n\n")

def onlu_gruplama(y,dosya):
    dosya.write("       3. Soru             \n--------------------------------------------------\n\n")
    sayac,son_kaldigi_sayi=1,0
    onlu_liste=[]
    for i in range(len(y)):
        if(sayac==10 or i == len(y)-1):
            if(i==len(y)-1):
                for j in range(len(onlu_liste),10):
                    onlu_liste.append(0)
            x,r = [],[]
            kts = []
            for z in range(len(onlu_liste)):
                x.append(z)
            for z in range(1,7):
                katsayilar = matris_coz(matris_olustur(x,onlu_liste,len(onlu_liste),z))
                r.append(korelasyon_ve_hata(x,onlu_liste,len(onlu_liste),katsayilar,z))
                kts.append(katsayilar)
            max_= r[0][0]
            min_ =r[0][1]
            temp = 0
            for z in range(len(r)):
                if(r[z][0] > max_):
                    max_ = r[z][0]
                    temp = z+1
                if(r[z][1] < min_):
                    min_ = r[z][1]
            if(i==len(y)-1):
                dosya.write(str(son_kaldigi_sayi)+"-"+str(i)+" arasi :\n")
                for l in range(len(kts)):
                    dosya.write("  "+str(l+1)+". dereceden polinomun katsayilari"+str(kts[l])+"\n")
                dosya.write("  en buyuk korelasyon : "+str(max_))
                dosya.write("\n  en kucuk standart tahmini hata :"+str(min_)+"\n")
                dosya.write("  en uygun polinom: "+str(temp)+". dereceden \n\n")
            else:
                dosya.write(str(i-9)+"-"+str(i)+" arasi :\n")
                for l in range(len(kts)):
                    dosya.write("  "+str(l+1)+". dereceden polinomun katsayilari"+str(kts[l])+"\n")
                dosya.write("  en buyuk korelasyon : "+str(max_))
                dosya.write("\n  en kucuk standart tahmini hata :"+str(min_)+"\n")
                dosya.write("  en uygun polinom: "+str(temp)+". dereceden \n\n")
                son_kaldigi_sayi = i+1
            onlu_liste.clear()
            sayac = 0
        onlu_liste.append(y[i])
        sayac += 1
         
x,y = dosya_oku()
dosya = open("sonuc.txt","w")
polinom_yakinlastirma(x,y,dosya)
onlu_gruplama(y,dosya)
dosya.close()


