def polinom(derece, liste):
    matris1 = []
    x = 0
    for i in range(derece + 1):
        matris_deger = []
        for j in range(derece + 1):
            top = 0
            for k in range(1, len(liste) + 1):
                top += k ** x
            matris_deger.append(top)
            x += 1
        matris1.append(matris_deger)
        x -= derece
    matris2 = []
    for i in range(derece + 1):
        top = 0
        for j in range(len(liste)):
            top += liste[j] * (j + 1) ** i
        matris2.append(top)
    for i in range(derece + 1):
        sayi1 = matris1[i][i]
        for j in range(i + 1, derece + 1):
            ortalama = sayi1 / matris1[j][i]
            matris2[j] = matris2[j] * ortalama - matris2[i]
            for k in range(derece + 1):
                matris1[j][k] = matris1[j][k] * ortalama - matris1[i][k]
    for i in range(derece, -1, -1):
        sayi1 = matris1[i][i]
        for j in range(i - 1, -1, -1):
            ortalama = sayi1 / matris1[j][i]
            matris2[j] = matris2[j] * ortalama - matris2[i]
            for k in range(derece + 1):
                matris1[j][k] = matris1[j][k] * ortalama - matris1[i][k]
    for i in range(derece + 1):
        matris2[i] = matris2[i] / matris1[i][i]
    y = 0
    for i in range(len(liste)):
        y += liste[i]
    y = y / len(liste)
    sutun = 0
    satir = 0
    for i in range(len(liste)):
        x = liste[i]
        sutun += (liste[i] - y) ** 2
        for j in range(len(matris2)):
            x -= matris2[j] * (i + 1) ** j
        x = x ** 2
        satir += x
    r = ((sutun - satir) / sutun) ** (1 / 2)
    return matris2, r


def regres(r1, r2, r3, r4, r5, r6, file):
    file.write("r1 = " + str(r1) + " r2 = " + str(r2) + " r 3 = " + str(r3) + "r4 = " + str(r4) + " r5 = " + str(
        r5) + " r6 = " + str(r6) + "\n")

    dizi = [r1, r2, r3, r4, r5, r6]
    for i in range(len(dizi)):
        if dizi[i] == max(dizi):
            file.write("r=" + str(dizi[i]) + " " + str(i + 1) + ". polinom\n")


def file_write(pol1, pol2, pol3, pol4, pol5, pol6, file, n1, n2):


    file.write(" \n" + " \n" + " \n" + "polinomlarin katsayilari     " + str(n1) + " ---- " + str(n2) + " \n")
    n1 = n1 + 10
    n2 = n2 + 10
    file.write("1.derece a0 = " + str(pol1[0]) + " a1 = " + str(pol1[1]) + "\n" + "2.derece a0 = " + str(
        pol2[0]) + " a1 = " + str(pol2[1]) + " a2 =" + str(pol2[2]) + "\n" + "3.derece a0 = " + str(
        pol3[0]) + " a1 = " + str(pol3[1]) + " a2 =" + str(pol3[2]) + " a3 = " + str(
        pol3[3]) + "\n" + "4.derece a0 = " + str(pol4[0]) + " a1 = " + str(pol4[1]) + " a2 =" + str(
        pol4[2]) + " a3 = " + str(pol4[3]) + " a4 = " + str(pol4[4]) + "\n" + "5.derece a0 = " + str(
        pol5[0]) + " a1 = " + str(pol5[1]) + " a2 =" + str(pol5[2]) + " a3 = " + str(pol5[3]) + " a4 = " + str(
        pol5[4]) + " a5 = " + str(pol5[5]) + "\n" + "6.derece a0 = " + str(pol6[0]) + " a1 = " + str(
        pol6[1]) + " a2 =" + str(pol6[2]) + " a3 = " + str(pol6[3]) + " a4 = " + str(pol6[4]) + "a5=" + str(
        pol6[5]) + "a6=" + str(pol6[6]) + "\n")
    return n1,n2


n1=1
n2=10
my_file = open("veriler.txt", "r")
liste = my_file.readlines()
for i in range(len(liste)):
    liste[i] = int(liste[i])
pol_1, r1 = polinom(1, liste)
pol_2, r2 = polinom(2, liste)
pol_3, r3 = polinom(3, liste)
pol_4, r4 = polinom(4, liste)
pol_5, r5 = polinom(5, liste)
pol_6, r6 = polinom(6, liste)
my_file.close()
file = open("sonuc.txt", "w")
n1,n2=file_write(pol_1, pol_2, pol_3, pol_4, pol_5, pol_6, file, n1, n2)
regres(r1, r2, r3, r4, r5, r6, file)

for i in range(len(liste) // 10):
    grup = []
    for j in range(10):
        grup.append(liste[10 * i + j])
    pol_1, r1 = polinom(1, grup)
    pol_2, r2 = polinom(2, grup)
    pol_3, r3 = polinom(3, grup)
    pol_4, r4 = polinom(4, grup)
    pol_5, r5 = polinom(5, grup)
    pol_6, r6 = polinom(6, grup)
    n1,n2=file_write(pol_1, pol_2, pol_3, pol_4, pol_5, pol_6, file, n1, n2)
    regres(r1, r2, r3, r4, r5, r6, file)
file.close()
