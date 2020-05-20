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
