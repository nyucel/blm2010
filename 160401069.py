def formulUygula(derece, liste):
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


def katsayi(r1, r2, r3, r4, r5, r6, dosya2):
   dosya2.write("<----------------------------------------->\n")
   dosya2.write("r1 = " + str(r1) + " r2 = " + str(r2) + " r 3 = " + str(r3) + "r4 = " + str(r4) + " r5 = " + str(
        r5) + " r6 = " + str(r6) + "\n")

   dizi = [r1, r2, r3, r4, r5, r6]
   for i in range(len(dizi)):
       if dizi[i] == max(dizi):
           dosya2.write("r=" + str(dizi[i]) + " " + str(i + 1) + ".\n")


def katsayiHes(pol1, pol2, pol3, pol4, pol5, pol6, dosya2, a1, a2):


    
    dosya2.write(" \n" + " \n" + " \n" + "polinomlarin katsayilari     " + str(a1) + " ---- " + str(a2) + " \n")
    a1 = a1 + 10
    a2 = a2 + 10
    dosya2.write("1.dereceden katsayilar \nk1 = " + str(pol1[0]) + " k1 = " + str(pol1[1]) + "\n")
    dosya2.write(
        "2.dereceden katsayilar \nk0 = " + str(pol2[0]) + " k1 = " + str(pol2[1]) + " k2 =" + str(pol2[2]) + "\n")
    dosya2.write("3.dereceden katsayilar \nk0 = " + str(pol3[0]) + " k1 = " + str(pol3[1]) + " k2 =" + str(
        pol3[2]) + " k3 = " + str(pol3[3]) + "\n")
    dosya2.write("4.dereceden katsayilar \nk0 = " + str(pol4[0]) + " k1 = " + str(pol4[1]) + " k2 =" + str(
        pol4[2]) + " k3 = " + str(pol4[3]) + " k4 = " + str(pol4[4]) + "\n")
    dosya2.write("5.dereceden katsayilar \nk0 = " + str(pol5[0]) + " k1 = " + str(pol5[1]) + " k2 =" + str(
        pol5[2]) + " k3 = " + str(pol5[3]) + " k4 = " + str(pol5[4]) + " k5 = " + str(pol5[5]) + "\n")
    dosya2.write("6.dereceden katsayilar \nk0 = " + str(pol6[0]) + " k1 = " + str(pol6[1]) + " k2 =" + str(
        pol6[2]) + " k3 = " + str(pol6[3]) + " k4 = " + str(pol6[4]) + " k5 = " + str(pol6[5]) + " k6 = " + str(
        pol6[6]) + "\n")
    return a1,a2


a1=1
a2=10
dosya = open("veriler.txt", "r")
liste = dosya.readlines()
for i in range(len(liste)):
    liste[i] = int(liste[i])
pol_1, r1 = formulUygula(1, liste)
pol_2, r2 = formulUygula(2, liste)
pol_3, r3 = formulUygula(3, liste)
pol_4, r4 = formulUygula(4, liste)
pol_5, r5 = formulUygula(5, liste)
pol_6, r6 = formulUygula(6, liste)
dosya.close()
dosya2 = open("sonuc.txt", "w")
a1,a2=katsayiHes(pol_1, pol_2, pol_3, pol_4, pol_5, pol_6, dosya2, a1, a2)
katsayi(r1, r2, r3, r4, r5, r6, dosya2)

for i in range(len(liste) // 10):
    onlu = []
    for j in range(10):
        onlu.append(liste[10 * i + j])
    pol_1, r1 = formulUygula(1, onlu)
    pol_2, r2 = formulUygula(2, onlu)
    pol_3, r3 = formulUygula(3, onlu)
    pol_4, r4 = formulUygula(4, onlu)
    pol_5, r5 = formulUygula(5, onlu)
    pol_6, r6 = formulUygula(6, onlu)
    a1,a2=katsayiHes(pol_1, pol_2, pol_3, pol_4, pol_5, pol_6, dosya2, a1, a2)
    katsayi(r1, r2, r3, r4, r5, r6, dosya2)
dosya2.close()
