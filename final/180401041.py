# Emre Ekinci 180401041


__dosya__ = "veriler.txt"  # sizdeki veriler

def main():
    sonuçlar = list()
    veriler = verileriOku()

    print("Soru 1 başlangıcı !")

    yaklastir(1, veriler, sonuçlar)
    yaklastir(2, veriler, sonuçlar)
    yaklastir(3, veriler, sonuçlar)
    yaklastir(4, veriler, sonuçlar)
    yaklastir(5, veriler, sonuçlar)
    yaklastir(6, veriler, sonuçlar)
    endusuk(sonuçlar)

    print('\nSoru 2ye geçiliyor...')
    a = 1    # Bu şekilde  de olur : int('180401041'[1])
    b = len(veriler)
    denklem = yaklastir(endusuk(sonuçlar, noprint=True), veriler, sonuçlar, noprint=True)
    integralHesabi(denklem, a, b)

    print('\nSoru 3 e geçiliyor..')
    polinomsuzIntegral(veriler, a, b)

    print('\nSoru 4 yorum !')
    yazdir()

def yaklastir(mertebe, veri, sonuclar, noprint=False):
    matrix = list()
    konum = 0

    for _ in range(mertebe + 1):
        sutun = list()
        for j in range(mertebe + 1):
            hepsi = 0
            for m in range(1, len(veri) + 1):
                hepsi += m ** konum
            sutun.append(hepsi)
            konum += 1
        matrix.append(sutun)
        konum = konum - mertebe

    cevap = list()
    for i in range(mertebe + 1):
        hepsi = 0
        for j in range(len(veri)):
            hepsi += veri[j] * (j + 1) ** i
        cevap.append(hepsi)

    for i in range(mertebe + 1):  # Alt üçgensel matris
        kiyan = matrix[i][i]
        for j in range(i + 1, mertebe + 1):
            kalan = kiyan / matrix[j][i]
            cevap[j] = cevap[j] * kalan - cevap[i]
            for k in range(mertebe + 1):
                matrix[j][k] = matrix[j][k] * kalan - matrix[i][k]

    for i in range(mertebe, -1, -1):  # Üst üçgensel matris
        kiyan = matrix[i][i]
        for j in range(i - 1, -1, -1):
            kalan = kiyan / matrix[j][i]
            cevap[j] = cevap[j] * kalan - cevap[i]
            for s in range(mertebe + 1):
                matrix[j][s] = matrix[j][s] * kalan - matrix[i][s]

    for c in range(mertebe + 1):
        cevap[c] = cevap[c] / matrix[c][c]

    ytoplami = 0
    for i in range(len(veri)):
        ytoplami += veri[i]
    orty = ytoplami / len(veri)

    tler = 0
    rler = 0
    for i in range(len(veri)):
        a = veri[i]
        tler += (veri[i] - orty) ** 2
        for j in range(len(cevap)):
            a = a - (cevap[j] * (i + 1) ** j)
        a = a ** 2
        rler = rler + a
    korelasyon = ((tler - rler) / tler) ** (1 / 2)
    sonuclar.append((cevap, korelasyon))
    if not noprint:
        print('{} mertebeden polinoma yaklaştırıldı!'.format(mertebe))
    return cevap

def denklemHesabi(x, denklem):
    toplam = 0.0
    for i in range(len(denklem)):
        toplam += denklem[i] * (x ** i)
    return toplam

def endusuk(liste, noprint=False):
    endusuk = liste[0][1]
    index = 0
    for i, item in enumerate(liste):
        if item[1] >= endusuk:
            endusuk = item[1]
            index = i
    if not noprint:
        print('En düşük hata: {} ile {}.polinom'.format(endusuk, index + 1))
    return index + 1

def integralHesabi(denklem, a, b):
    integral = 0
    deltax = 1.2 #Değeri 0.120 ardından da 0.2 girdiğimde polinomlu ve polinomsuz integral arasındaki fark açılıyor
    n = int((b - a) / deltax)
    print('Seçilen Denklem: ')
    for i in range(len(denklem)):
        print('{}x**{} + '.format(denklem[i], i))
    for i in range(n):
        integral += deltax * (denklemHesabi(a, denklem) + denklemHesabi(a + deltax, denklem)) / 2
        a += deltax
    print("Polinomlu sonuc:", integral)
    a=integral

def polinomsuzIntegral(degerler, a, b):
    integral = 0   # Başlangıç değeri integralimizin sıfır.
    deltax = 1     # Bu değerin limiti 0'a yaklaştığı sürece doğruluk payı o kadar artar
    n = int((b - a) / deltax)
    for i in range(n - 1):
        integral += deltax * (degerler[a] + degerler[a + deltax]) / 2
        a += deltax
    print("Polinomsuz İntegral Değeri: ", integral)
    b=integral

def verileriOku():
    dosya = open(__dosya__, 'r')
    veriler = dosya.readlines()
    for i in range(len(veriler)):
        veriler[i] = int(veriler[i])
    dosya.close()
       #if len(veriler) == 0:
       #raise ValueError('Dosyaları okurken hata oluştu')  gerek yok!!!
    return veriler

def yazdir():
    dosya = open('180401041_yorum.txt', 'w')
    txt = 'Ad Soyad: Emre Ekinci No:180401041 \n\n'
    txt += 'Polinomsuz hesaplamada integral üzerinde alabildiğimiz alanlar sınırlıdır , polinomlu hesaplamada ise daha esnek hareket edebiliriz. \n'
    txt += 'İntegral hesabı yaparken polinomlu hesapta denklem bilindiğinden istediğimiz kadar küçük değerlerle işlem yapabiliyoruz.\n'
    txt += 'Bu iki yöntemin sonuçlarının farklı çıkma nedeni budur. Bunu daha iyi anlamak için integral yönteminde deltax değeri, polinomlu \n'
    txt += 've polinomsuz hesaplamada aynı değer verilse bile sonuçlar arasında farklar oluşuyor. Bu eğrilere uydurulan 1 den 6. dereceye kadar \n'
    txt += 'olan polinomlar arasındanen uygun polinom seçilmiş olmasına rağmen sonuçları aynı değildir ve yaklaaşma uzaklaşma durumlarını da vereceğimiz değerler belirlemektedir.\n'

    dosya.write(txt)
    dosya.close()


if __name__ == '__main__':
    main()