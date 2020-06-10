#Ömer Çiçek 170401047
x=open('veriler.txt','r')
veriler=[0]
for i in x:
    veriler.append(int(i))
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

def main():
    r_list=[0]
    for i in range(1,7):
        cozumlu_matris=denklem_olusturma(i,veriler)
        katsayi_listesi=katsayi_bulma(cozumlu_matris,i)
    return katsayi_listesi
    uygun_polinom(r_list)

def f(x,listem):
    #print(listem)
    return((listem[0] + listem[1] * x + listem[2] *x**2 + listem[3]* x**3 + listem[4]*x**4 + listem[5]*x**5 + listem[6]*x**6))

def polinomlu(veriler):
    listem=[]
    listem=main()
    a = 7
    b = len(veriler)-1
    deltax = 1
    integral = 0
    n = int((b-a)/deltax)
    for i in range(n):
        integral += deltax*(f(a,listem)+f(a+deltax,listem))/2
        a += deltax
    return(integral)

def polinomsuz(veriler):
    a = 7
    b = len(veriler)-1
    deltax = 1
    integral = 0
    n = int((b-a)/deltax)
    for i in range(n):
        integral += deltax*(veriler[a]+veriler[a+deltax])/2
        a += deltax
    return (integral)

print("Polinom kullanılarak integral değeri:",polinomlu(veriler))
print("Polinom kullanmadan integral değeri:" ,polinomsuz(veriler))
f=open("170401047_yorum.txt",'w')
f.write("Ömer Çiçek 170401047 \n")
f.write("Verileri, 6. dereceden polinoma 0.9626337181923464 korelasyon değeri ile uyarladığımızda çok yakın değerler bulabiliyoruz.\n ")
f.write("Elde ettiğimiz bu polinomu yamuk yöntemiyle deltax değerini ne kadar küçültürsek o kadar yakın değerde belirtilen aralıkta integral alabiliriz.\n")
f.write("Polinom kullanmadan gerçek veriler üzerinden yaptığımızda arada az bir fark oluşuyor.\n")
f.write("Bunun en büyük sebebi polinomlu yöntemde çizilen polinomun daha lineer artışlara veya azalışlara sahip olmasıdır.\n")
f.write("Bu sayede hesaba katılmayan alan parçaları az oluyor.Fazla etki etmesede diğer bir sebebi ise delta x in 1 olma zorunluluğudur.\n")