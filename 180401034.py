#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ezgi Cengiz 180401034
def  Katsayı(p1, p2, p3, p4, p5, p6, katpol):
     katpol.write("1.derece polinom : a0 = "+str(polinom1[0]) + " a1 = " + str(polinom1[1])+"\n" )
     katpol.write("2.derece polinom : a0 = "+str(polinom2[0]) + " a1 = " + str(polinom2[1]) + " a2 =" + str(polinom2[2]) + "\n")
     katpol.write("3.derece polinom : a0 = "+str(polinom3[0]) + " a1 = " + str(polinom3[1]) + " a2 =" + str(polinom3[2]) + " a3 = " + str(polinom3[3]) + "\n")
     katpol.write("4.derece polinom : a0 = "+str(polinom4[0]) + " a1 = " + str(polinom4[1]) + " a2 =" + str(polinom4[2]) + " a3 = " + str(polinom4[3]) + " a4 = " + str(polinom4[4]) + "\n")
     katpol.write("5.derece polinom : a0 = "+str(polinom5[0]) + " a1 = " + str(polinom5[1]) + " a2 =" + str(polinom5[2]) + " a3 = " + str(polinom5[3]) + " a4 = " + str(polinom5[4]) + " a5 = "+ str(polinom5[5])+ "\n")
     katpol.write("6.derece polinom : a0 = "+str(polinom6[0]) + " a1 = " + str(polinom6[1]) + " a2 =" + str(polinom6[2]) + " a3 = " + str(polinom6[3]) + " a4 = " + str(polinom6[4]) + " a5 = "+ str(polinom6[5])+" a6 = "+str(polinom6[6])+ "\n")
    
def En_uygun_polinom(ks1, ks2, ks3, ks4, ks5, ks6,file):
     file.write( "  1.derece polinom katsayısı: "+str(ks1) +
                 "\n2.derece polinom katsayısı: "+str(ks2) +
                 "\n3.derece polinom katsayısı: "+str(ks3) +
                 "\n4.derece polinom katsayısı: "+str(ks4) +
                 "\n5.derece polinom katsayısı: "+str(ks5) +
                 "\n6.derece polinom katsayısı: "+str(ks6)+"\n")
     katsayılar = [c1, c2, c3, c4, c5, c6]
     b = max(katsayılar)
     for i in range(len(katsayılar)):
         if b == katsayılar[i]:
             file.write("En uygun polinom: "+str(katsayılar[i])+" katsayısı olan "+str(i+1)+". derece polinomdur.\n")



def İnterpolasyon(derece,veri):
    matriks = []
    tut = 0

    for i in range(derece+1):
        line = []
        for j in range(derece+1):
            sonuc = 0
            for k in range(1, len(veri)+1):
                sonuc += k**tut
            line.append(sonuc)
            tut += 1
        matriks.append(line)
        tut -= derece

    snc = []
    for i in range(derece+1):
        sonuc = 0
        for j in range(len(veri)):
            sonuc += veri[j]*(j+1)**i
        snc.append(sonuc)

    for i in range(derece+1):  
        comp = matriks[i][i]
        for j in range(i+1, derece+1):
            eps = comp/matriks[j][i]
            snc[j] = snc[j]*eps-snc[i]
            for k in range(derece+1):
                matriks[j][k] = matriks[j][k]*eps-matriks[i][k]

    for i in range(derece, -1, -1):  # gaus
        comp = matriks[i][i]
        for j in range(i-1, -1, -1):
            eps = comp/matriks[j][i]
            snc[j] = snc[j]*eps-snc[i]
            for k in range(derece+1):
                matriks[j][k] = matriks[j][k]*eps-matriks[i][k]

    for i in range(derece+1): 
        snc[i] = snc[i]/matriks[i][i]

    sonucy = 0
    for i in range(len(veri)):
        sonucy += veri[i]
    avg = sonucy/len(veri)

    sonuct, sonucr = 0, 0
    for i in range(len(veri)):
        q = veri[i]
        sonuct += (veri[i]-avg)**2
        for j in range(len(snc)):
            q -= snc[j]*(i+1)**j
        q = q**2
        sonucr += q
    korelasyon = ((sonuct-sonucr)/sonuct)**(1/2)
    return snc, korelasyon



verilerim = open("veriler.txt", "r")
 vaka = verilerim.readlines()
 for i in range(len(vaka)):
     vaka[i] = int(vaka[i])
 pol, hata = [0] * 6, [0] * 6
 for j in range(0,6):
     pol[j], hata[j] = İnterpolasyon(j+1,vaka)
 verilerim.close()


 sonuclarım= open("sonuc.txt", "w")
 sonuclarım.write("bütün veriler\n")
 Katsayı(pol[0], pol[1], pol[2], pol[3], pol[4], pol[5], sonuclarım)
 En_uygun_polinom(hata[0], hata[1], hata[2], hata[3], hata[4], hata[5],sonuclarım)
 for a in range(len(vaka) - 9):
     sonuclarım.write("\n10'lu veri grubu ("+str(a+1)+","+str(a+10)+") ")
     liste= vaka[a:a+10]
     for i in range(6):
         pol[i],hata[i] = İnterpolasyon(i+1, liste)
     Katsayı(pol[0], pol[1], pol[2], pol[3], pol[4], pol[5], sonuclarım)
     En_uygun_polinom(hata[0], hata[1], hata[2], hata[3], hata[4], hata[5],sonuclarım)
 sonuclarım.close()

