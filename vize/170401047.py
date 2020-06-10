#Ömer Çiçek 170401047
x=open('veriler.txt','r')
veriler=[0]
for i in x:
    veriler.append(int(i))

def main():
    f = open('sonuc.txt', "w")
    f.write("----------------1. dereceden polinom katsayilari-------------")
    f.write('\n')
    r_list=[0]
    for i in range(1,7):
        f = open('sonuc.txt', "a")
        if(i<6):
            f.write("-------------------" + str(i + 1) + "." + "dereceden polinom katsayilari----------------------")
        f.write('\n')
        cozumlu_matris=denklem_olusturma(i,veriler)
        katsayi_listesi=katsayi_bulma(cozumlu_matris,i)
        yazdirma(katsayi_listesi)
        r_list=hata_bulma(veriler, katsayi_listesi, i,r_list)
    uygun_polinom(r_list)


def yazdirma(list):     #Katsayı değerlerini yazdırır...
    f = open('sonuc.txt', "a")
    for i in range(len(list)):
        string=str(list[i])
        f.write("a" + str(i) + "=")
        f.write(string)
        f.write('\n')
    f.write('\n')

def uygun_polinom(list):    #Korelasyon değerine göre uygun polinomu önerir...
    f = open('sonuc.txt', "a")
    for i in range(1,len(list)):
        string=str(list[i])
        f.write(str(i) + ". dereceden polinom korelasyon degeri=")
        f.write(string)
        f.write('\n')
    f.write('\n')
    f.write("6.derece polinomdan yaklasmak bize en yakin sonuclari verir.Korelasyon degeri--> " + str(list[6]))
    f.write('\n')


def uygun_polinom_2(list,veriler,b):   #10 lu veri grupları için korelasyon değerine göre uygun polinomu önerir...
    f = open('sonuc.txt', "a")
    f.write('\n')
    f.write('----------------------------' + str(1 + b) + "-" + str(10 + b) + ' indeks arasi korelasyon degerleri---------------------- ')
    f.write('\n')
    for i in range(1,len(list)):
        string=str(list[i])
        f.write(str(i) + ". dereceden polinom korelasyon degeri=")
        f.write(string)
        f.write('\n')
    f.write('\n')
    f.write("6.derece polinomdan yaklasmak bize en yakin sonuclari verir.Korelasyon degeri--> " + str(list[6]))
    f.write('\n')


def denklem_olusturma(derece,veriler):  #1,2,3,4,5 ve 6. derece için denklemler oluşturur...
    matris=[]
    if(derece==1):
        n=len(veriler)-1
        x_toplam=0
        x_2_toplam=0
        y_toplam=0
        x_y_toplam=0
        for i in range(1,len(veriler)):
            x_toplam=x_toplam+i
            x_2_toplam=x_2_toplam+i**2
            y_toplam=y_toplam+veriler[i]
            x_y_toplam=x_y_toplam+i*veriler[i]
        matris.append([n,x_toplam,y_toplam])
        matris.append([x_toplam,x_2_toplam,x_y_toplam])
        cozumlu_matris=matris_coz(matris)
        return cozumlu_matris
    if(derece==2):
        for i in range(0,3):
            a,b,c,d=0,0,0,0
            for x in range(1,len(veriler)):
                a=x**i + a
                b=x**(i+1) + b
                c=x**(i+2) + c
                d=x**i * veriler[x] + d
            matris.append([a,b,c,d])
        cozumlu_matris=matris_coz(matris)
        return cozumlu_matris
    if(derece==3):
        for i in range(0,4):
            a,b,c,d,e=0,0,0,0,0
            for x in range(1,len(veriler)):
                a = x ** i + a
                b = x ** (i + 1) + b
                c = x ** (i + 2) + c
                d = x ** (i + 3) + d
                e = x **(i) * veriler[x] + e
            matris.append([a,b,c,d,e])
        cozumlu_matris=matris_coz(matris)
        return cozumlu_matris
    if(derece==4):
        for i in range(0,5):
            a,b,c,d,e,f=0,0,0,0,0,0
            for x in range(1,len(veriler)):
                a = x ** i + a
                b = x ** (i + 1) + b
                c = x ** (i + 2) + c
                d = x ** (i + 3) + d
                e = x ** (i + 4) + e
                f = x **(i) * veriler[x] + f
            matris.append([a, b, c, d, e, f])
        cozumlu_matris=matris_coz(matris)
        return cozumlu_matris
    if(derece==5):
        for i in range(0,6):
            a,b,c,d,e,f,g=0,0,0,0,0,0,0
            for x in range(1,len(veriler)):
                a = x ** i + a
                b = x ** (i + 1) + b
                c = x ** (i + 2) + c
                d = x ** (i + 3) + d
                e = x ** (i + 4) + e
                f = x ** (i + 5) + f
                g = x **(i) * veriler[x] + g
            matris.append([a, b, c, d, e, f, g])
        cozumlu_matris=matris_coz(matris)
        return cozumlu_matris
    if(derece==6):
        for i in range(0,7):
            a,b,c,d,e,f,g,h=0,0,0,0,0,0,0,0
            for x in range(1,len(veriler)):
                a = x ** i + a
                b = x ** (i + 1) + b
                c = x ** (i + 2) + c
                d = x ** (i + 3) + d
                e = x ** (i + 4) + e
                f = x ** (i + 5) + f
                g = x ** (i + 6) + g
                h = x **(i) * veriler[x] + h
            matris.append([a, b, c, d, e, f, g, h])
        cozumlu_matris=matris_coz(matris)
        return cozumlu_matris
def matris_coz(matris): #Alt üçgen yöntemiyle verilen matrisi çözer...
    boyut=len(matris)
    for n in range(boyut):
        kat = float(matris[n][n])
        for m in range(boyut + 1):
            matris[n][m] = float(matris[n][m]) / kat
        for p in range(1, boyut - n):
            kat = float(matris[n + p][n])
            for q in range(boyut + 1):
                matris[n + p][q] = float(matris[n + p][q]) - float(matris[n][q]) * (kat / float(matris[n][n]))
    return matris

def katsayi_bulma(matris,derece):   #Çözülen matrisdeki katsayıları bulur...
    katsayi_liste=[]
    if(derece==1):
        a_1=matris[1][2]
        a_0=matris[0][2]-(a_1 * matris[0][1])
        katsayi_liste.append(a_0)
        katsayi_liste.append(a_1)
    if(derece==2):
        a_2=matris[2][3]
        a_1=matris[1][3]-(matris[1][2] * a_2)
        a_0=matris[0][3]-(a_1 * matris[0][1] + a_2 * matris[0][2])
        katsayi_liste.append(a_0)
        katsayi_liste.append(a_1)
        katsayi_liste.append(a_2)
    if(derece==3):
        a_3=matris[3][4]
        a_2=matris[2][4]-(a_3 * matris[2][3])
        a_1=matris[1][4]-(a_2 * matris[1][2] + a_3 * matris[1][3])
        a_0=matris[0][4]-(a_1 * matris[0][1] + a_2 * matris[0][2] + a_3 * matris[0][3])
        katsayi_liste.append(a_0)
        katsayi_liste.append(a_1)
        katsayi_liste.append(a_2)
        katsayi_liste.append(a_3)
    if(derece==4):
        a_4=matris[4][5]
        a_3=matris[3][5]-(a_4 * matris[3][4])
        a_2=matris[2][5]-(a_3 * matris[2][3] + a_4 * matris[2][4])
        a_1=matris[1][5]-(a_2 * matris[1][2] + a_3 * matris[1][3] + a_4 * matris[1][4])
        a_0=matris[0][5]-(a_1 * matris[0][1] + a_2 * matris[0][2] + a_3 * matris[0][3] + a_4 * matris[0][4])
        katsayi_liste.append(a_0)
        katsayi_liste.append(a_1)
        katsayi_liste.append(a_2)
        katsayi_liste.append(a_3)
        katsayi_liste.append(a_4)
    if(derece==5):
        a_5=matris[5][6]
        a_4=matris[4][6]-(a_5 * matris[4][5])
        a_3=matris[3][6]-(a_4 * matris[3][4] + a_5 * matris[3][5])
        a_2=matris[2][6]-(a_3 * matris[2][3] + a_4 * matris[2][4] + a_5 * matris[2][5])
        a_1=matris[1][6]-(a_2 * matris[1][2] + a_3 * matris[1][3] + a_4 * matris[1][4] + a_5 * matris[1][5])
        a_0=matris[0][6]-(a_1 * matris[0][1] + a_2 * matris[0][2] + a_3 * matris[0][3] + a_4 * matris[0][4] + a_5 * matris[0][5])
        katsayi_liste.append(a_0)
        katsayi_liste.append(a_1)
        katsayi_liste.append(a_2)
        katsayi_liste.append(a_3)
        katsayi_liste.append(a_4)
        katsayi_liste.append(a_5)
    if(derece==6):
        a_6=matris[6][7]
        a_5=matris[5][7]-(a_6 * matris[5][6])
        a_4=matris[4][7]-(a_5 * matris[4][5] + a_6 * matris[4][6])
        a_3=matris[3][7]-(a_4 * matris[3][4] + a_5 * matris[3][5] + a_6 * matris[3][6])
        a_2=matris[2][7]-(a_3 * matris[2][3] + a_4 * matris[2][4] + a_5 * matris[2][5] + a_6 * matris[2][6])
        a_1=matris[1][7]-(a_2 * matris[1][2] + a_3 * matris[1][3] + a_4 * matris[1][4] + a_5 * matris[1][5] + a_6 * matris[1][6])
        a_0=matris[0][7]-(a_1 * matris[0][1] + a_2 * matris[0][2] + a_3 * matris[0][3] + a_4 * matris[0][4] + a_5 * matris[0][5] + a_6 * matris[0][6])
        katsayi_liste.append(a_0)
        katsayi_liste.append(a_1)
        katsayi_liste.append(a_2)
        katsayi_liste.append(a_3)
        katsayi_liste.append(a_4)
        katsayi_liste.append(a_5)
        katsayi_liste.append(a_6)
    return katsayi_liste
def hata_bulma(veriler,katsayilar,derece,r_list):   #Korelasyon değerini hesaplar....
    hata,y,S_t=0,0,0
    boy=len(veriler)-1
    for j in range(1,len(veriler)):
       y=y+ veriler[j]
    y_= y/boy
    for i in range(1,len(veriler)):
        S_t= S_t + (veriler[i] -y_)**2
    if(derece==1):
        for i in range(1,len(veriler)):
          hata= hata + (veriler[i] - int((katsayilar[0] + katsayilar[1] * i)))**2
    if(derece==2):
        for i in range(1,len(veriler)):
            hata= hata + (veriler[i] - int((katsayilar[0] + katsayilar[1] * i + katsayilar[2] *i**2 )))**2
    if(derece==3):
        for i in range(1,len(veriler)):
            hata= hata + (veriler[i] - int((katsayilar[0] + katsayilar[1] * i + katsayilar[2] *i**2 + katsayilar[3]* i**3)))**2
    if(derece==4):
        for i in range(1,len(veriler)):
            hata= hata + (veriler[i] - int((katsayilar[0] + katsayilar[1] * i + katsayilar[2] *i**2 + katsayilar[3]* i**3 + katsayilar[4]*i**4)))**2
    if(derece==5):
        for i in range(1,len(veriler)):
            hata= hata + (veriler[i] - int((katsayilar[0] + katsayilar[1] * i + katsayilar[2] *i**2 + katsayilar[3]* i**3 + katsayilar[4]*i**4 + katsayilar[5]*i**5)))**2
    if(derece==6):
        for i in range(1,len(veriler)):
            hata= hata + (veriler[i] - int((katsayilar[0] + katsayilar[1] * i + katsayilar[2] *i**2 + katsayilar[3]* i**3 + katsayilar[4]*i**4 + katsayilar[5]*i**5 + katsayilar[6]*i**6)))**2
    r = ((S_t - hata) / S_t) ** (1 / 2)
    r_list.append(r)
    return r_list

def onlu_gruplar(list): #10 lu gruplar için denklemleri oluşturup katsayıları buldurur...
    b=0
    f = open('sonuc.txt', "a")
    while(b<int(len(list)/10)*10):
        listem = [0]
        r_listem_2=[0]
        for i in range(1+b,11+b):
            listem.append(list[i])
        for j in range(1,7):
            x = []
            cozumlu_matris=denklem_olusturma(j,listem)
            katsayi_liste=katsayi_bulma(cozumlu_matris,j)
            x=hata_bulma(listem,katsayi_liste,j,x)
            r_listem_2.append(x[0])
        uygun_polinom_2(r_listem_2,listem,b)
        b=b+10

main()      # main i çağırarak tüm veriler için katsayılar çıkar...
onlu_gruplar(veriler)   #Onlu grupları değerlendirmek için çağırırız...