#Rahmi Buğra Ünal
veri=[]

def veriAl():
    dosya = open(r"C:\Users\ABRA\Desktop\veriler.txt","a+")
    veri = dosya.read()
    for i in range(len(veri)):
        veri[i] = int(veri[i])
    print(veri) #kontrol

    dosya.close()


def gauss(matris):
    boyut = len(matris)
    for i in range(0, boyut):
        maksSutun = abs(matris[i][i])
        maksSatir = i
        for j in range(i + 1, boyut):
            if abs(matris[j][i]) > maksSutun:
                maksSutun = abs(matris[j][i])
                maksSatir = j
        for k in range(i, boyut + 1):
            temp = matris[maksSatir][k]
            matris[maksSatir][k] = matris[i][k]
            matris[i][k] = temp
        for l in range(i + 1, boyut):
            c = -matris[l][i] / matris[i][i]
            for j in range(i, boyut + 1):
                if i == j:
                    matris[l][j] = 0
                else:
                    matris[l][j] += c * matris[i][j]
    mat1 = [0 for i in range(boyut)]
    for i in range(boyut - 1, -1, -1):
        mat1[i] = matris[i][boyut] / matris[i][i]
        for k in range(i - 1, -1, -1):
            matris[k][boyut] -= matris[k][i] * mat1[i]
    return mat1


def korelasyon(sonuclar,ilk,son):
    n = son - ilk
    yi = 0
    for i in range(ilk,son):
        yi += veri[i]
    y_ust = yi/n
    Sr = 0
    for j in range(ilk,son):
        Sr = (sonuclar[j-ilk] - veri[j])**2 + Sr
    St = 0
    for k in range(ilk,son):
        St = St + (veri[k] - y_ust)**2
    s =  abs((St-Sr)/St)**2
    return s

def veriIslem(ilk,son):
    dizi = []
    n= son - ilk
    for derece in range(1,7):
        xdeger = []
        for i in range(n):
            xdeger.append(i+1)
        matris = [[0 for i in range(derece+1)] for j in range(derece+1)]
        boyut = len(matris)
        for i in range(boyut):
            for j in range(boyut):
                xtoplam = 0
                for m in range(n):
                    matris[0][0] = len(xdeger)
                    xtoplam = xdeger[m] ** (i+j) + xtoplam
                    matris[i][j] = xtoplam
        xytoplam = []
        for i in range(boyut):
            toplam = 0
            for j in range(ilk,son):
                toplam = toplam + (veri[j]*(xdeger[j-ilk]**i))
            xytoplam.append(toplam)
        l=0
        for i in matris:
            i.append(xytoplam[l])
            l=l+1
        katsayi=gauss(matris)
        sonuc=[]
        for i in range(n):
            toplam=0
            for j in range(len(katsayi)):
                toplam= toplam+katsayi[j]* ((i+1)**j)
                if j==derece:
                    sonuc.append(int(toplam))
        s= korelasyon(sonuc,ilk,son)
        dizi.append(s)
        yaz = open("sonuc.txt", "a+",encoding="UTF8" )
        yaz.write("*-*-*-*-"+str(ilk)+" - "+str(son-1)+"arası için "+str(derece)+". dereceden yaklaşım \n\n")
        yaz.write("korelasyon :  "+str(s)+"\n")
        yaz.write("Katsayılar: ")
        for i in katsayi:
            yaz.write(str(i))
            yaz.write(" \\ ")
        yaz.write("\n")
        eniyi = 100
        nm = 0
        for i in range(len(dizi)):
            temp = abs(1 - dizi[i])
            if temp < eniyi:
                eniyi = temp
                nm = i + 1
        yaz.write("Gerçek veri \ Bulduğumuz sonuç:")
        yaz.write("\n")
        for i in range(ilk,son):
            yaz.write(str(veri[i]))
            yaz.write("  \\  ")
            yaz.write(str(sonuclar[i-ilk]))
            yaz.write("*-*-*-*-*- \n")
        yaz.write(str(ilk)+"-"+str(son-1)+" arası için en uygun olan polinom: "+str(nm)+"\n\n")
        yaz.write("*-*-*-*-")
        yaz.close()



veriAl()
veriIslem(0,len(veri))

########3.soru
ilkIndex = 0
ucuncuSoru = 10
while(ucuncuSoru < len(veriler)):
   findData (ilkIndex,son)
   ilkIndex = ilkIndex+10
   ucuncuSoru = ucuncuSoru+10
