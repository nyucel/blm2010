# -*- coding: utf-8 -*-

#170401009 ATAKAN TÜRKAY
#python3 ile kodlandı.


import decimal

veriler_x=[[]]
veriler_y=[[]]
katsayilar_matrisi = []

def dosya_oku(dosya="veriler.txt",veriler_x=veriler_x,veriler_y=veriler_y): #içerisine bir dosya ve boş bir dizi alır.
    with open('veriler.txt', 'r') as f: 
        veriler_y[0].extend(map(int,f.read().splitlines()))  #\n göstermeden dosyanın içindeki satırları dizinin içerisine aktarıyor ve integer yapıyor.
    for i in range(len(veriler_y[0])):
        veriler_x[0].append(i+1)
    

def matris_olustur(satir_uzunlugu,sutun_uzunlugu,datas):
    vandermonde=[]
    for k in range (0,satir_uzunlugu):
        vandermonde.append([])
    for i in range (satir_uzunlugu):
        for j in range (sutun_uzunlugu+1):
            vandermonde[i].append(datas[i][0]**(j))
    return vandermonde


def matris_transpose(matris):
    transposem = []
    sutun_uzunlugu = len(matris)
    satir_uzunlugu = len(matris[0])
    for k in range(satir_uzunlugu):
        transposem.append([])
    for n in range(satir_uzunlugu):
        for m in range(sutun_uzunlugu):
            transposem[n].append(matris[m][n])
    return transposem


def matris_carpimi(firstmatris, secondmatris):
    result = []
    for i in range (len(firstmatris)):
        result.append([])
        for j in range (len(secondmatris[0])):
            total = 0
            for k in range(len(secondmatris)):
                total += firstmatris[i][k]*int(secondmatris[k][j])
            result[i].append(total)
    return result


def matris_ters(old_matris):
    matris = old_matris
    Imatris = [] #Birim Matris
    for i in range(len(matris)): #Matris ile boyutu aynı birim matris oluşturma
        Imatris.append([])
        for j in range(len(matris)):
            if(i == j):
                Imatris[i].append(1)
            else:
                Imatris[i].append(0)

    for i in range(len(matris)):
        bolen = matris[i][i]
        for j in range(len(matris)):
            matris[i][j] = matris[i][j]/bolen
            Imatris[i][j] = Imatris[i][j]/bolen
        for k,z in zip(matris[i+1:],Imatris[i+1:]):
            carpan = k[i]
            for m in range(len(k)):
                k[m] = k[m]-matris[i][m]*carpan
                z[m] = z[m]-Imatris[i][m]*carpan  

    for i in range(len(matris)-1,-1,-1):
        for j in range(i-1,-1,-1):
            carpan = matris[j][i] / matris[i][i]
            for k in range(len(matris)):
                matris[j][k] -= carpan*matris[i][k]
                Imatris[j][k] -= carpan*Imatris[i][k]
    return Imatris 



def olustur(katsayilar_matrisi=katsayilar_matrisi,veriler_x=veriler_x,veriler_y=veriler_y):
    for degree in range(1,7):
        katsayilar_matrisi.append([])
        vandermondematris = matris_olustur(len(veriler_x),degree,veriler_x)
        transpose = matris_transpose(vandermondematris)
        product = matris_carpimi(transpose,vandermondematris)
        mult = matris_carpimi(matris_ters(product),transpose)
        sonuc = matris_carpimi(mult,veriler_y)
        for m in range(len(sonuc)):
            katsayilar_matrisi[degree-1].append(sonuc[m])
    f=open('sonuc.txt', 'w')
    f.write("----- Elde Edilen Katsayilar(a0 a1 a2) -----\n")
    f.close()
    for i in range(6):
        with open('sonuc.txt','a') as f:
            f.write(f"{i+1}. derece polinomun katsayıları:{katsayilar_matrisi[i]}\n")





def hata_hesapla(veriler_x,veriler_y,katsayilar_matrisi):
    hm1,hm2,hm3,hm4,hm5,hm6=[],[],[],[],[],[]
    for i in veriler_x:
         #print((veriler_y[i[0]-1][0],(katsayilar_matrisi[5][0][0]+katsayilar_matrisi[5][1][0]*i[0]+katsayilar_matrisi[5][2][0]*(i[0]**2)+katsayilar_matrisi[5][3][0]*(i[0]**3)+katsayilar_matrisi[5][4][0]*(i[0]**4)+katsayilar_matrisi[5][5][0]*(i[0]**5)+katsayilar_matrisi[5][6][0]*(i[0]**6),veriler_y[i[0]-1][0]-(katsayilar_matrisi[5][0][0]+katsayilar_matrisi[5][1][0]*i[0]+katsayilar_matrisi[5][2][0]*(i[0]**2)+katsayilar_matrisi[5][3][0]*(i[0]**3)+katsayilar_matrisi[5][4][0]*(i[0]**4)+katsayilar_matrisi[5][5][0]*(i[0]**5)+katsayilar_matrisi[5][6][0]*(i[0]**6)))))
        
        #Hata miktarlarını hesaplıyor.

        hm1.append(abs(veriler_y[i[0]-1][0]-(katsayilar_matrisi[0][0][0]+katsayilar_matrisi[0][1][0]*i[0])))
        hm2.append(abs(veriler_y[i[0]-1][0]-(katsayilar_matrisi[1][0][0]+katsayilar_matrisi[1][1][0]*i[0]+katsayilar_matrisi[1][2][0]*(i[0]**2))))
        hm3.append(abs(veriler_y[i[0]-1][0]-(katsayilar_matrisi[2][0][0]+katsayilar_matrisi[2][1][0]*i[0]+katsayilar_matrisi[2][2][0]*(i[0]**2)+katsayilar_matrisi[2][3][0]*(i[0]**3))))
        hm4.append(abs(veriler_y[i[0]-1][0]-(katsayilar_matrisi[3][0][0]+katsayilar_matrisi[3][1][0]*i[0]+katsayilar_matrisi[3][2][0]*(i[0]**2)+katsayilar_matrisi[3][3][0]*(i[0]**3)+katsayilar_matrisi[3][4][0]*(i[0]**4))))
        hm5.append(abs(veriler_y[i[0]-1][0]-(katsayilar_matrisi[4][0][0]+katsayilar_matrisi[4][1][0]*i[0]+katsayilar_matrisi[4][2][0]*(i[0]**2)+katsayilar_matrisi[4][3][0]*(i[0]**3)+katsayilar_matrisi[4][4][0]*(i[0]**4)+katsayilar_matrisi[4][5][0]*(i[0]**5))))
        hm6.append(abs(veriler_y[i[0]-1][0]-(katsayilar_matrisi[5][0][0]+katsayilar_matrisi[5][1][0]*i[0]+katsayilar_matrisi[5][2][0]*(i[0]**2)+katsayilar_matrisi[5][3][0]*(i[0]**3)+katsayilar_matrisi[5][4][0]*(i[0]**4)+katsayilar_matrisi[5][5][0]*(i[0]**5)+katsayilar_matrisi[5][6][0]*(i[0]**6))))
    return hm1,hm2,hm3,hm4,hm5,hm6


def en_az_hata_hesapla(hm):
    en_az=9999999999999999                             #ilk küçük gelende değişmesi için böyle değer verildi.
    indis=0
    for i in range(6):
        if sum(hm[i]) < en_az :
            en_az = sum(hm[i])
            indis = i
    return en_az,indis

def en_az_hata_aralık(hm,x,y):
    en_az=9999999999999999                              #ilk küçük gelende değişmesi için böyle değer verildi.
    indis=0
    for i in range(6):
        if sum(hm[i][x-1:y]) < en_az :
            en_az = sum(hm[i][x-1:y])
            indis = i
    return en_az,indis

print("Program çalışmaya başladı.")

dosya_oku()

veriler_y = matris_transpose(veriler_y)
veriler_x = matris_transpose(veriler_x)

olustur(katsayilar_matrisi,veriler_x,veriler_y)           #katsayıları hesaplıyorum.
print("Katsayılar bulundu...")
print(*katsayilar_matrisi,sep="\n")

hm = hata_hesapla(veriler_x,veriler_y,katsayilar_matrisi) #her derece için ayrı şekilde diziler halinde hesaplanıyor.Hm içinde diziler tutan bir tuple.
print("Hatalar hesaplandı...")
# print(*hm,sep="\n")

enaz,indis=en_az_hata_hesapla(hm)                         #en az miktarda hatayı sağlayan dereceyi buluyor.
# en_az_hata_aralık(hm,1,60)                              #istediğim aralıkta hesaplayabiliyorum  
print("Hata miktarı "+str(round(enaz,2))+" ile en uygun polinom "+str(indis+1)+". dereceden polinom olmuştur...")
f = open('sonuc.txt', 'a')
f.write("\n----- Hata miktarı "+str(round(enaz,2))+" ile en uygun polinom "+str(indis+1)+". dereceden polinom olmuştur -----\n")
f.close()

#Belirli aralıkların hata miktarlarını hesaplayıp karşılaştırıyorum.
f = open('sonuc.txt', 'a')
for i in range(1,len(veriler_x)-9):
    ea,ind=en_az_hata_aralık(hm,i,i+9)
    f.write("----- "+str(i)+" ve "+str(i+9)+" Arasında Hata miktarı "+str(round(ea,2))+" ile en uygun polinom "+str(ind+1)+". dereceden polinom olmuştur -----\n")
f.close()

print("10lu aralıklı hatalar hesaplandı ve dosyaya yazıldı...")
print("Program sonlanacak...")






