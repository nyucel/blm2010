# -*- coding: utf-8 -*-

#Barış KOL 180401073

from math import sqrt 
def orderedList(data):#i değeri için sıralı dizi oluşturuluyor.
    i = []
    for dataNumber in range(len(data)):
        i.append(dataNumber+1)
    return i    
with open("veriler.txt") as f: #Veriler okunup satır satır ayrılıyor ve yi dizisi oluşturuluyor.
    yi = f.read().split("\n")
    if yi[-1] == '':
        yi.pop()
def Matrix(xi,yi,degree): #Xi değerleri ve #Xi(ve üsleri) ve Yi çarpımları için matrislerin oluşturulduğu Fonksiyon
    xiMatrix = [] #Xi 'lerin katsayılarının toplamlarının olduğu matris
    zeroMatrix = [] # Cholesky Metodu için gerekli olan 0 matrisi
    ResultMatrix = [] #Xi(ve üsleri) ve Yi çarpımlarının olduğu sonuç Matrisi
    n = len(xi)
    for i in range(degree+1):
        xiMatrix.append([]) #2. Boyut ekleniyor
        zeroMatrix.append([])
        SumXiandYi = 0 #Xi ve Yi çarpımları her bir satır için sıfırlanıyor.
        for j in range(degree+1):
            if(i == 0 and j == 0):
                xiMatrix[i].append(n) #matrisin 1.Satır 1. Sütununa n eklendi
                zeroMatrix[i].append(0)
            else:
                counter = 0
                for k in xi:
                    counter += k**(i+j) 
                xiMatrix[i].append(counter) #xi matrisinin diğer elemanları eklendi.
                zeroMatrix[i].append(0)
        for l in range(len(xi)):
            SumXiandYi += float(yi[l]) * (xi[l]**i)
        ResultMatrix.append(SumXiandYi) #Xi(ve üsleri) ve Yi çarpımları sonuçlar diziye ekleniyor
    return xiMatrix,ResultMatrix,zeroMatrix
def transposeMatrix(inMtx): 
    """
        Karekök ( Cholesky ) yönteminde bulunan I değerlerinin alt üçgensel matris
        ile sonuç matrisini eşitleyip elde edilen sonuç ile üst üçgensel 
        matris eşitlenir. Bunun sonucunda elimizde olan veriler aradığımız sonucu verir.
        Bu nedenle transpoze matris gerekmektedir.
    """
    tMtx = []
    for row in range(0, len(inMtx[0])):
      tRow = []
      for col in range(0, len(inMtx)):
        ele = inMtx[col][row]
        tRow.append(ele)
      tMtx.append(tRow)
    return(tMtx)
def Cholesky(matrix,zeroMatrix):
    """
        Katsayıların oluşturduğu matris bir kare matris ve simetrik.
        Değerler de pozitif tanımlı olduğu için en pratik olacağını düşündüğüm yöntem
        Karekök (Cholesky) Yöntemidir.
        Ondalıklı Sayılarda çalıştığım için örnek: A*ATranspoze = KatsayılarMatrisi
        vermesi gerektiğinden test ettim. 2. dereceden denkleme yaklaştırdığımda katsayılar;
        [[59, 1770, 70210], [1770, 70210, 3132900], [70210, 3132900, 149111998]] oluyorken cholesky
        metodunu kullanarak alt üçgensel matris oluşturduktan sonra transpozesi ile çarptığımda sonuç;
        [[58.99999999999999, 1770.0000000000002, 70210.00000000001], [1770.0000000000002, 70210.0, 3132900.0], [70210.00000000001, 3132900.0, 149111998.0]] bu olmaktaydı. 
    """
    for i in range(len(matrix)):
       for j in range(i+1):
           IkareToplami = sum(zeroMatrix[j][k]**2 for k in range(j))
           if (i == j):
               zeroMatrix[i][i] = sqrt(matrix[i][i] - IkareToplami)
           else:
               ICarpimToplami = sum(zeroMatrix[i][k] * zeroMatrix[j][k] for k in range (j))
               zeroMatrix[i][j] = (1.0 / zeroMatrix[j][j])*(matrix[i][j]-ICarpimToplami)
    return zeroMatrix
def matrixMultiplication(bottomTriangular,topTriangular):
    """
        Bu fonksiyonu sadece A*ATranspoze = Katsayılar Matrisi için yazdım.
        Sayılar büyük olduğu için test edip görmek istedim
    """
    rowsA = len(bottomTriangular)
    colsA = len(bottomTriangular[0])
    colsB = len(topTriangular[0])
    newZeroMatrix = [[0 for row in range(colsB)]for col in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                newZeroMatrix[i][j] += bottomTriangular[i][k] * topTriangular[k][j]
    return newZeroMatrix
def Result(bottomTriangular,resultMatrix):
    """
        Cholesky yönteminden sonra elde ettiğim alt 
        üçgensel matris ile yaptığım işlemler için 
        hafta5.pdf adlı kaynağınızdan yararlandım. Ancak 43. sayfada
        son satırdaki denklemde hata vardır. Toplam formülünde bulunan
        LjiXj yerine LijXj olması gerekmektedir. Formülümü buna göre düzenleyerek
        sizin verdiğiniz doğruya yaklaştırma örneğindeki a0 ve a1 katsayılarına göre test ettim.
        Sonuç doğru çıkmaktadır.
        
    """
    columnMatris = [0 for i in range(len(bottomTriangular))]
    result = [0 for i in range(len(resultMatrix))]
    """
        Bu kısım;
        [L]{D} = {C} denkleminin {D} Sütun matrisini verir. 
    """
    for i in range(len(bottomTriangular)): 
        if(i == 0):
            columnMatris[i] = resultMatrix[i] / bottomTriangular[i][i]
        else:
            totals = sum(bottomTriangular[i][j] * columnMatris[j] for j in range(i))
            columnMatris[i] = ((resultMatrix[i])- totals)/(bottomTriangular[i][i])
    """
        Bu kısım ise;
        [L]Transpoze{x} = {D} denkleminde yerine koyup {x} istenen çözümü bulduğumuz kısımdır
    """
    topTriangular = transposeMatrix(bottomTriangular)
    n = len(topTriangular)
    for i in range(n-1,-1,-1):
        if(i == n-1):
            result[i] = columnMatris[i] / topTriangular[i][i]
        else:
            total = sum(topTriangular[i][j] * result[j] for j in range(i,n)) 
            result[i] = (columnMatris[i]-total)/topTriangular[i][i]
    return result
def resultant(data): #Bulunan Katsayılara göre bizim bulacağımız sonuçlar
    result = []
    for i in range(len(yi)):
        totals = 0
        for j in range(len(data)):
            totals += data[j]*((i+1)**j)
        result.append(totals)
    return result
def E(lastData,firstData): # kolerasyon değerinin hesaplandığı fonksiyon
    totalY = 0
    Sr = 0
    St = 0
    EHata = 0
    n = len(firstData)
    for i in range(n):
        totalY += int(firstData[i])
    averageY = totalY / n # yi'lerin ortalaması
    for j in range(n):
        Sr += (int(firstData[j]) - lastData[j])**2 # Hataların Kareleri Toplamı
        St += (int(firstData[j]) - averageY) ** 2
        EHata += abs(lastData[j] - int(firstData[j]))
    #r = sqrt((St - Sr)/St) 
    """
        Bu fonksiyonda kolerasyon hesaplaması yapıp uyumluluğu test edip sonucu uyumluluğa göre verdirmek istedim. Bulduğum sonuçların hepsi için veya veriler.txt dosyasındaki verileri elle 
10 adet veri olacak şekilde değiştirdiğimde hiçbir sorun çıkmamaktadır. Ancak verileri 10'lu gruplandırarak bu fonksiyona gönderdiğimde (St-Sr)/St negatif sonuç vermekte ve kökünü alamamaktayım. Soruda istediğiniz gibi sadece gerçek veri - bizim bulduğumuz veri ile hata hesapkaması yapıp çözüme devam ettim.
    
    """
    return EHata
def main():   
    xi = orderedList(yi)
    lastData = [] # Yakınlaştırılma sonucunda elde edilen sonuçların tutulacağı liste
    flaw = [] # 1,2,3,....,6 dereceden polinomlar için hata değerlerinin tutulduğu dizi
    f=open('sonuc.txt','w')
    f.write("Barış KOL 180401073\n\n1,2,3,4,5,6. dereceden polinomlara yakınlaştırılması sonucu elde edilen katsayılar \n\n")
    f.close()
    
    res = [] # Katsayıların tutulduğu dizi
    for i in range(6):
        XilerinToplamı, SonuclarinToplami,zeroMatrix = Matrix(xi, yi, i+1)
        bottomTriangular=Cholesky(XilerinToplamı,zeroMatrix)
        res.append(Result(bottomTriangular,SonuclarinToplami))
        with open('sonuc.txt','a') as f:
            f.write(f"{i+1}. Dereceden Polinomun Katsayıları: {str(res[i])}\n")
            f.close()
    for j in range(6):
        lastData.append(resultant(res[j]))
        flaw.append(E(lastData[j],yi))
    flawData,polinom = min((value, index) for index, value in enumerate(flaw))
    with open('sonuc.txt','a') as f:
        f.write("\n")
        f.close()
    for i in range(len(flaw)):
         with open('sonuc.txt','a') as f:
             f.write(f"Bulunan Sonuçlar İçin {str(i+1)}. Polinoma Yakınlaştırılma Sonunda Toplam Hata: {str(flaw[i])}\n")
             f.close()
    with open('sonuc.txt','a') as f:
        f.write("\n")
        f.write("Bu Hata Toplamlarından Minimum Değer Ve O Hata Değerine Ait Polinom Bizim İçin En Uygun Olan Polinom Olacaktır.")
        f.write("\n")
        f.close()
    with open('sonuc.txt','a') as f:
        f.write("\n")
        f.write(f"Bulunan Sonuçlar İçin {str(polinom+1)}. Polinoma Yakınlaştırmada Daha Sağlıklı Sonuçlar Verdi.\nSonucun Toplam Hata Değeri: {str(flawData)}")
        f.close()
    dataGroup = [] # Bulduğumuz sonuçları 10'lu gruplara ayırmak için oluşturuldu 
    for l in range(len(yi)-9):
        dataGroup.append([])
        for m in range(l,l+10):
            dataGroup[l].append((yi[m]))
    with open('sonuc.txt','a') as f:
            f.write("\n\n10'lu veri grupları için son 10'lu veri gruplarında her dereceden denklem için aynı\nsonuçları verdiğinden dizinin ilk elemanını en küçük hata oranı sayarak 1. polinom yazmaktadır.\n")
            f.close()
    newRes = [] #10'lu Gruplar için katsayıların tutulacağı dizi
    newLastData = [] #10'lu Grupların polinomlara yakınlaştırılması sonucunda elde edilecek sonuçlar listesi
    newFlaw = [] # 10'lu grupların Kolerasyonlarının tutulduğu dizi
    for p in range(len(dataGroup)):
        newXi = orderedList(dataGroup[p])
        newFlaw.append([])
        for r in range(6):
            newXilerinToplamı, newSonuclarinToplami,newZeroMatrix = Matrix(newXi,dataGroup[p],r+1)
            newBottomTriangular=Cholesky(newXilerinToplamı,newZeroMatrix)
            newRes.append(Result(newBottomTriangular,newSonuclarinToplami))
        for s in range(6):
            newLastData.append(resultant(newRes[s]))
            newFlaw[p].append(E(newLastData[s],dataGroup[p]))
       
        newFlawData,newPolinom = min((value, index) for index, value in enumerate(newFlaw[p]))
        
        with open('sonuc.txt','a') as f:
            f.write("\n")
            f.write(f"{p+1} ve {p+10}. Değerler İçin {str(newPolinom+1)}. Polinoma Yakınlaştırmada Daha Sağlıklı Sonuçlar Verdi.\nHata Değeri: {str(newFlawData)}")
            f.close()
        
    
if __name__ == main():
    main()
