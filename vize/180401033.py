#Kerem Kecel 180401033

"""""İnterpolasyon:Polinomlar kullanarak, dataların bilindiği noktalardan yeni dataların üretilmesini sağlayan bir eğri uydurma metodudur.
Kolerasyon: Korelasyon iki ya da daha fazla değişken arasındaki doğrusal ilişkiyi gösterir.
Gaus Eleme Yöntemi:Bu yöntem genel bir n denklemli ve n bilinmeyenli lineer sistemin çözümüne bir yaklaşım getirmektedir.Bu sistemde  n x  bilinmiyeninden başlayarak geriye doğru yerine koyma işlemi ile bilinmeyenler bulunur.
Alt Üçgen,Üst Üçgen:Köşegen üstündeki bütün elemanları sıfır olan kare matris,Köşegen altındaki bütün elemanları sıfır olan kare matris
En uygun polinom korelan katsayısı 1 e en yakın olandır.1 e doğru gidildikçe ilişki artar."""""

def interpolasyon(derece, veri):          #eğriye uydurma işlemi
    matrix = []
    b = 0

    for i in range(derece+1):
        satir= []
        for j in range(derece + 1):
            toplam = 0
            for k in range(1, len(veri)+1):
                toplam += k**b
            satir.append(toplam)
            b += 1
        matrix.append(satir)
        b -= derece

    sonuç = []
    for i in range(derece+1):
        toplam = 0
        for j in range(len(veri)):
            toplam += veri[j]*(j+1)**i
        sonuç.append(toplam)

    for i in range(derece+1):  # Alt üçgensel matris
        bölen = matrix[i][i]
        for j in range(i+1, derece+1):
            bölüm = bölen/matrix[j][i]
            sonuç[j] = sonuç[j]*bölüm-sonuç[i]
            for k in range(derece+1):
                matrix[j][k] = matrix[j][k]*bölüm-matrix[i][k]

    for i in range(derece, -1, -1):  # Üst üçgensel matris 
        bölen = matrix[i][i]
        for j in range(i-1, -1, -1):
            bölüm = bölen/matrix[j][i]
            sonuç[j] = sonuç[j]*bölüm-sonuç[i]
            for k in range(derece+1):
                matrix[j][k] = matrix[j][k]*bölüm-matrix[i][k]

    for i in range(derece+1):
        sonuç[i] = sonuç[i]/matrix[i][i]

    toplam_y = 0
    for i in range(len(veri)):
        toplam_y += veri[i]
    y_ortalama = toplam_y/len(veri)

    toplam_t, toplam_r = 0, 0
    for i in range(len(veri)):
        e = veri[i]
        toplam_t += (veri[i]-y_ortalama)**2
        for j in range(len(sonuç)):
            e -= sonuç[j]*(i+1)**j
        e = e**2
        toplam_r += e
    korelasyon = ((toplam_t-toplam_r)/toplam_t)**(1/2)
    return sonuç, korelasyon


#Elemental satır işlemi uyguladığımız matristeki katsayıları çekip a değerlerini buluyoruz.
def KatsayıÇek(p1, p2, p3, p4, p5, p6, k_dosya):
    k_dosya.write("n.dereceden polinomun n+1 sayida birbirinden farkli a değeri olur. \n")
    k_dosya.write("Polinomlarimizin  Katsayilari  \n")
    k_dosya.write("1.dereceden  a0 = "+str(p1[0]) + " a1 = " + str(p1[1]) + "\n")
    k_dosya.write("2.dereceden  a0 = "+str(p2[0]) + " a1 = " + str(p2[1]) + " a2 =" + str(p2[2]) + "\n")
    k_dosya.write("3.dereceden  a0 = "+str(p3[0]) + " a1 = " + str(p3[1]) + " a2 =" + str(p3[2]) + " a3 = " + str(p3[3]) + "\n")
    k_dosya.write("4.dereceden  a0 = "+str(p4[0]) + " a1 = " + str(p4[1]) + " a2 =" + str(p4[2]) + " a3 = " + str(p4[3]) + " a4 = " + str(p4[4]) + "\n")
    k_dosya.write("5.dereceden  a0 = "+str(p5[0]) + " a1 = " + str(p5[1]) + " a2 =" + str(p5[2]) + " a3 = " + str(p5[3]) + " a4 = " + str(p5[4]) + " a5 = "+ str(p5[5])+ "\n")
    k_dosya.write("6.dereceden  a0 = "+str(p6[0]) + " a1 = " + str(p6[1]) + " a2 =" + str(p6[2]) + " a3 = " + str(p6[3]) + " a4 = " + str(p6[4]) + " a5 = "+ str(p6[5])+" a6 = "+str(p6[6])+ "\n")

def Uygun_Polinom(c1, c2, c3, c4, c5, c6, k_dosya2):
    k_dosya2.write("Korelasyon Katsayıları"+
                   "\n1. dereceden polinomun korelasyon katsayisi: "+str(c1) +
                   "\n2. dereceden polinomun korelasyon katsayisi: "+str(c2) +
                   "\n3. dereceden polinomun korelasyon katsayisi: "+str(c3) +
                   "\n4. dereceden polinomun korelasyon katsayisi: "+str(c4) +
                   "\n5. dereceden polinomun korelasyon katsayisi: "+str(c5) +
                   "\n6. dereceden polinomun korelasyon katsayisi: "+str(c6)+"\n")
    Korelasyon_Katsayisi = [c1, c2, c3, c4, c5, c6]
    maxE = max(Korelasyon_Katsayisi)
    for i in range(len(Korelasyon_Katsayisi)):
        if maxE == Korelasyon_Katsayisi[i]:
            k_dosya2.write("  "+str(Korelasyon_Katsayisi[i])+"  ile "+str(i+1)+". dereceden polinom en uygun polinomdur.\n")

kaynaklar = open("veriler.txt", "r")
veriler = kaynaklar.readlines()
for i in range(len(veriler)):
    veriler[i] = int(veriler[i])
polinom, h = [0] * 6, [0] * 6
for index in range(0,6):
    polinom[index], h[index] = interpolasyon(index+1, veriler)
kaynaklar.close()


r = open("sonuc.txt", "w")
r.write(" Kaynağimizdan Aldiğimiz Veri\n")
KatsayıÇek(polinom[0], polinom[1], polinom[2], polinom[3], polinom[4], polinom[5], r)
Uygun_Polinom(h[0], h[1], h[2], h[3], h[4], h[5], r)
for Range in range(len(veriler) - 9):
    r.write("\n 10lu  gruplandirdik. ("+str(Range+1)+","+str(Range+10)+") \n")
    e_liste = veriler[Range:Range+10]
    for i in range(6):
        polinom[i], h[i] = interpolasyon(i+1, e_liste)
    KatsayıÇek(polinom[0], polinom[1], polinom[2], polinom[3], polinom[4], polinom[5], r)
    Uygun_Polinom(h[0], h[1], h[2], h[3], h[4], h[5], r)
r.close()
