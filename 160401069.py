#Adem YILMAZ-160401069

def formulUygula(derece, liste):  #vizede kullandigim formul
    mat = []
    xDeg = 0
    for i in range(derece + 1):
        mat1 = []
        for j in range(derece + 1):
            gecici = 0
            for k in range(1, len(liste) + 1):
                gecici += k ** xDeg
            mat1.append(gecici)
            xDeg += 1
        mat.append(mat1)
        xDeg -= derece
    mat2 = []
    for i in range(derece + 1):
        gecici = 0
        for j in range(len(liste)):
            gecici += liste[j] * (j + 1) ** i
        mat2.append(gecici)
    for i in range(derece + 1):
        gecici1 = mat[i][i]
        for j in range(i + 1, derece + 1):
            ort = gecici1 / mat[j][i]
            mat2[j] = mat2[j] * ort - mat2[i]
            for k in range(derece + 1):
                mat[j][k] = mat[j][k] * ort - mat[i][k]
    for i in range(derece, -1, -1):
        gecici1 = mat[i][i]
        for j in range(i - 1, -1, -1):
            ort = gecici1 / mat[j][i]
            mat2[j] = mat2[j] * ort - mat2[i]
            for k in range(derece + 1):
                mat[j][k] = mat[j][k] * ort - mat[i][k]
    for i in range(derece + 1):
        mat2[i] = mat2[i] / mat[i][i]
    yDeg = 0
    for i in range(len(liste)):
        yDeg += liste[i]
    yDeg = yDeg / len(liste)
    stn = 0
    str = 0
    for i in range(len(liste)):
        xDeg = liste[i]
        stn += (liste[i] - yDeg) ** 2
        for j in range(len(mat2)):
            xDeg -= mat2[j] * (i + 1) ** j
        xDeg = xDeg ** 2
        str += xDeg
    a = ((stn - str) / stn) ** (1 / 2)
    return mat2, a

def polinom_eniyi(pol,r):
    rEniyi=0
    polEniyi=0
    for i in range(len(r)):
        if (r[i]>rEniyi):
            rEniyi=r[i]
            polEniyi=pol[i]
    return polEniyi

def fonkPol(p,x):
    top=0
    for i in range(len(p)):
        top += p[i]*(x**i)
    return top

def polinomlu(eniyiP,liste):
    num=9        #160401069
    delta_x= 0.0001
    gecici= int((liste-num)/delta_x)
    toplam=0
    for i in range(1,gecici):
        toplam += fonkPol(eniyiP,num+i*delta_x)
    sonuc=(delta_x/2)*(fonkPol(eniyiP,num)+fonkPol(eniyiP,liste)+2*toplam)
    return sonuc

def polinomsuz(veriler,liste):
    num=9

    delta_x=1
    sonuc2=veriler[num-1]
    while(num<liste):
        sonuc2 = sonuc2 + (veriler[num-1]+veriler[num+delta_x-1])*delta_x/2
        num += delta_x
    return sonuc2


dosya = open("veriler.txt", "r")
liste = dosya.readlines()
for i in range(len(liste)):
    liste[i]=int(liste[i])

pol_1,r1=formulUygula(1,liste)
pol_2,r2=formulUygula(2,liste)
pol_3,r3=formulUygula(3,liste)
pol_4,r4=formulUygula(4,liste)
pol_5,r5=formulUygula(5,liste)
pol_6,r6=formulUygula(6,liste)
dosya.close()

rList=[r1,r2,r3,r4,r5,r6]
polList=[pol_1,pol_2,pol_3,pol_4,pol_5,pol_6]

eniyiPol=polinom_eniyi(polList,rList)
print("Polinomlu integral sonucu= ",polinomlu(eniyiPol,len(liste)))
print("Polinomsuz integral sonucu= ",polinomsuz(liste,len(liste)))

dosya2= open("160401069_yorum.txt","w", encoding='utf8')
dosya2.write("Adem YILMAZ - 160401069 \n"
             "Sonuclarin farkli cikmasinin nedeni: Polinomlu hesaplamada(yamuk yöntemi),\n"
             "polinoma uydurarak yapildigindan gercek polinom degeri olmadigi icin bu kadar farklı cikiyor ve,\n"
             "Polinomluda delta_x'i kucuk secebiliyoruz\n"
             "Polinomsuzda delta_x 1 seciyoruz\n"
             "Bu yuzden polinomluda daha hassas sekilde integrali hesaplayabiliyoruz fakat polinomsuzda daha hassas hesaplayamıyoruz" )
dosya2.close()