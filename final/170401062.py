__dosya__ = "veriler.txt"


# 170401062 Yiğit
# Dosya çalıştığında aşağıdaki main() fonskiyonu çalışır.

def main():
    cevaplar = list()
    veriler = verileriOku()

    print('Soru 1e geçiliyor...')
    yaklastir(1, veriler, cevaplar)
    yaklastir(2, veriler, cevaplar)
    yaklastir(3, veriler, cevaplar)
    yaklastir(4, veriler, cevaplar)
    yaklastir(5, veriler, cevaplar)
    yaklastir(6, veriler, cevaplar)
    endusuk(cevaplar)

    print('\nSoru 2ye geçiliyor...')
    a = int('170401062'[8])
    b = len(veriler)
    denklem = yaklastir(endusuk(cevaplar, noprint=True), veriler, cevaplar, noprint=True)
    integralHesabi(denklem, a, b)

    print('\nSoru 3e geçiliyor...')
    polinomsuzIntegral(veriler, a, b)

    print('\nSoru 4 yorumu dosyaya yazdırılıyor...')
    yazdirBeni()


def verileriOku():
    dosya = open(__dosya__, 'r')
    veriler = dosya.readlines()
    for i in range(len(veriler)):
        veriler[i] = int(veriler[i])
    dosya.close()
    if len(veriler) == 0:
        raise ValueError('Dosyaları okurken hata oluştu')
    return veriler


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


def denklemHesabi(x, denklem):
    toplam = 0.0
    for i in range(len(denklem)):
        toplam += denklem[i] * (x ** i)
    return toplam


def integralHesabi(denklem, a, b):
    integral = 0
    deltax = 0.01
    n = int((b - a) / deltax)
    print('Seçilen Denklem: ')
    for i in range(len(denklem)):
        print('{}x**{} + '.format(denklem[i], i))
    for i in range(n):
        integral += deltax * (denklemHesabi(a, denklem) + denklemHesabi(a + deltax, denklem)) / 2
        a += deltax
    print("Polinomlu sonuc:", integral)


def polinomsuzIntegral(degerler, a, b):
    integral = 0
    deltax = 1
    n = int((b - a) / deltax)
    for i in range(n - 1):
        integral += deltax * (degerler[a] + degerler[a + deltax]) / 2
        a += deltax
    print("Polinomsuz İntegral Değeri: ", integral)


def yazdirBeni():
    dosya = open('170401062_yorum.txt', 'w')
    txt = '170401062 Yiğit\n'
    txt += 'Polinomlu ve polinomsuz olarak hesapladığımız integralin farklı sonuç döndürmesinin nedeni'
    txt += 'deltax için belirlediğimiz değerin uzunluğundan kaynaklanmaktadır.\nDeltax değerini ne kadar küçük değer alırsak hesaplanması.'
    txt += 'gereken alan sayısı artacaktır. \nBundan dolayı hata azalacaktır ve hesapladığımız değer gerçek değerini çok yaklaşacaktır.'
    dosya.write(txt)
    dosya.close()


if __name__ == '__main__':
    main()
