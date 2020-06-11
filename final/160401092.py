# 160401092 MEHMET TAHIR TAS  - SAYISAL YONTEMLER FINAL ODEVI #

import numpy as np


# from numpy import trapz
# import scipy
# from scipy.integrate import quad


def fitPolynomeThroughOrigin(x, y, nthDegree):
    # Kaynak: https://stackoverflow.com/questions/17930473/how-to-make-my-pylab-poly1dfit-pass-through-zero
    # Bu fonksiyon uretilecek polinomun sabitinin 0 olmasini garantiliyor.
    # Ornek sifirlanmis 2. derecen polinom: y = x^2 + x + 0
    x = np.asarray(x);
    a = x[:, np.newaxis] ** np.arange(1, nthDegree + 1)
    coefficients = np.linalg.lstsq(a, y)[0]

    return np.polynomial.Polynomial(np.concatenate(([0], coefficients)))


def convertDataToPolynomial(data, polynomialDegree):
    y = data
    x = range(
        len(y))  # Her veri noktasi bir gune ait diye dusunursek, x ekseni kacinci gun oldugunu gosteriyor 0,1,2,3,..vs

    # Normalde direk polyfit() fonksiyonunu kullanirdik ama sonuclar (0,0) noktasindan gecmiyor o durumda
    # return np.poly1d(np.polyfit(x, y, polynomialDegree))

    # Dolayisiyla, (0,0) noktasindan gecmesini zorlayarak polinomu uretelim
    return fitPolynomeThroughOrigin(x, y, polynomialDegree)


def polynomialToString(polynomialDegree, coefficients):
    # Katsayilarin okunakli olmasi icin yuvarlayalim
    coefficients = np.round(coefficients, 5)

    res = str(polynomialDegree) + '. derece: y ='
    first_pow = len(coefficients) - 1
    i = 0
    for coef in reversed(coefficients):  # katsayilar sondan basa oldugu icin ters cevirmemiz lazim array'i
        power = first_pow - i

        if coef:
            if i == 0:
                sign = ' '
            elif coef < 0:
                sign, coef = (' - ' if res else '- '), -coef
            elif coef > 0:
                sign = (' + ' if res else '')

            str_coef = '' if coef == 1 and power != 0 else str(coef)

            if power == 0:
                str_power = ''
            elif power == 1:
                str_power = 'x'
            else:
                str_power = 'x' + '^' + str(power)

            res += sign + str_coef + str_power
            i += 1
    return res


# Hata payi hesaplama
# Kaynak: https://www.geeksforgeeks.org/python-mean-squared-error/
def calculateMeanSquaredError(y_true, y_pred):
    mse = np.square(np.subtract(y_true, y_pred)).mean()
    return mse


# integral icin kaynak: https://www.geeksforgeeks.org/trapezoidal-rule-for-approximate-value-of-definite-integral/
# En az hata ureten polinom (en iyi polinom) kullanilarak yapilan integral hesabi
def integrationWithPolynomial(a, b, n, p1):
    # Grid spacing
    h = (b - a) / n

    # Computing sum of first and last terms
    # in above formula
    s = (p1(a) + p1(b))

    # Adding middle terms in above formula
    i = 1
    while i < n:
        s += 2 * p1(a + i * h)
        i += 1

    # h/2 indicates (b-a)/2n.
    # Multiplying h/2 with s.
    return (h / 2) * s


# integral icin kaynak: https://www.geeksforgeeks.org/trapezoidal-rule-for-approximate-value-of-definite-integral/
# veriler.txt dosyasindaki veriler kullanilarak integral hesabi
def integrationWithDataArr(a, b, n, dataArr):
    # Grid spacing
    h = (b - a) / n

    # Computing sum of first and last terms
    # in above formula
    s = (dataArr[a] + dataArr[b - 1])

    # Adding middle terms in above formula
    i = 1
    while i < n:
        index = int(a + i * h)
        s += 2 * dataArr[index]
        i += 1

    # h/2 indicates (b-a)/2n.
    # Multiplying h/2 with s.
    return (h / 2) * s


########################################################################################################################
# verileri dosyadan okuma
infile = open('veriler.txt', 'r')
data_arr = []
for line in infile:
    data_arr.append(int(line))
infile.close()

mse_arr = []
polynomial_arr = []

# sonuc.txt dosyasi olusturulur
outfile = open('sonuc.txt', 'w')
outfile.write("POLINOMLAR: \n")

# 1'den 6'ya kadar her dereceden hesaplama yapalim
for polynomialDegree in range(1, 7):
    # Verileri kullanarak tahmini polinom'u uretelim
    fx = convertDataToPolynomial(data_arr, polynomialDegree)
    # 'x' verilerini polinom fonksiyonumuzdan gecirip y sonuclarini alalim
    x = range(len(data_arr))
    ornekSonuc = fx(x)  # Her bir x degeri icin polinomumuzun urettigi y'leri array olarak dondurur
    # Hata payi hesaplama
    hataPayi = calculateMeanSquaredError(data_arr, ornekSonuc)
    # Her bir dereceden polinom icin hesaplanmis hata paylari sonradan dosyaya yazdirilmak uzere mse_arr'de tutulur
    mse_arr.append(hataPayi)
    polynomial_arr.append(fx)
    # Dosyaya yazmak icin polinom etiketi uretelim
    label = polynomialToString(polynomialDegree, fx.coef);
    # Polinomlari dosyaya yazalim
    outfile.write(f"{label}\n")

# Her bir polinom icin hata paylarini dosyaya yazdirma
outfile.write("HATA PAYLARI: \n")
for i in range(0, 6):
    outfile.write(f"{i + 1}. dereceden polinomun hata payi: {mse_arr[i]} \n")

########################################################################################################################
# EN  UYGUN POLINOMUN BULUNMASI & DOSYAYA YAZDIRILMASI#
minimum_error = min(mse_arr)
best_index = mse_arr.index(minimum_error)
minimum_error_index = best_index + 1
best_label = polynomialToString(minimum_error_index, polynomial_arr[best_index].coef)

outfile.write(
    f"\nEn uygun polinom en kucuk hata payi ({minimum_error}) olan {minimum_error_index}. dereceden polinomdur. \n")
outfile.write(f"{best_label}")

########################################################################################################################
# INTEGRAL HESAPLAMALARI #

# a- b: Integralin sinirlari. Integral bu a ve b degerleri arasinda tanimlidir
a = 2  # 160401092 => son rakam: 2
b = len(data_arr)  # dosyanin satir sayisi
# n: Dikdortgen sayisi. n sayisi ne kadar buyuk ise, dogruluk payimiz o kadar artar.
n = 100000
outfile.write(
    f"\nPolinom kullanilarak hesaplanan integral degeri:  {integrationWithPolynomial(a, b, n, polynomial_arr[best_index])} \n")
outfile.write(
    f"Veriler kullanilarak hesaplanan integral degeri:  {integrationWithDataArr(a, b, n, data_arr)} \n")

# sonuc.txt dosyasini kapatiyoruz
outfile.close()

# print("Value of integral with polynomial is ", "%.4f" % integrationWithPolynomial(a, b, n, polynomial_arr[best_index]))
# print("Value of integral with data is ", "%.4f" % integrationWithDataArr(a, b, n, data_arr))

# HESAPLADIGIMIZ DEGERLERI HAZIR KUTUPHANE FONKSIYONLARININ HESAPLADIGI DEGERLERLE TEST ETMEK ICIN:
# NUMPY & SCIPY
# print(f"Polinomlu - Hazir kutuphane fonk ile hesaplanan deger: { quad(polynomial_arr[best_index], a, b) }")
# print(f"Verili - Hazir kutuphane fonk ile hesaplanan deger: { trapz(data_arr) }")

# sonuc.txt dosyasi olusturulur
out_file = open('160401092_yorum.txt', 'w')
out_file.write(f"POLINOM KULLANARAK YAPILAN INTEGRAL HESABI ILE VERILER.TXT DOSYASINDAKI VERILER \n"
               f"KULLANILARAK YAPILAN INTEGRAL HESABININ FARKLI OLMASININ SEBEPLERI: \n\n"
               f"Integral, x=a ve x=b sınırları arasında f(x) fonksiyonu altında kalan alanin hesaplanması ile elde edilir.\n"
               f"Öncelikle a, b aralığı daha alt aralıklara bölünür bu alt bölmelerin alanı (yaklaşık dikdörtgen şekilli) \n"
               f"hesaplanır ve bunlar toplanmak suretiyle toplam alan yaklaşık olarak hesaplanır. \n\n"
               f"Integrali alınacak fonksiyon polinom formunda olabileceği gibi deneysel verileri olan farklı noktalarda \n"
               f"x ve f(x) degerlerinin olduğu tablo seklinde bir fonksiyon da olabilir. (Biz de sorunun 2. adımında polinom \n"
               f"ile 3. adımında da veriler.txt dosyasındaki verileri kullanarak 2 farklı sekilde hesapladık.) \n\n"
               f"Sayısal integrallemede orjinal f(x) fonksiyonu yerine, interpolasyon fonksiyonu (n. mertebeden bir polinom)\n"
               f"olan g(x) fonksiyonunu yerlestirerek integrali kolayca hesaplayabiliyoruz. Sayısal integrallemenin sonucunun doğruluğu\n"
               f"bu yeni fonksiyonun orijinal fonksiyonu ne kadar iyi temsil ettiğine bağlıdır. Buyuzden hata oranı en düşük,\n"
               f"en uygun polinomu kullanarak integral hesabi yapmak, en doğru sonuca daha da yaklasmamizi sağlayacaktır.\n\n"
               f"*******************************\n"
               f"Polinom ile Veri kullanarak yapılan iki hesaplamanın farklı sonuclar üretmesi doğaldır. Polinom kullanarak \n"
               f"yaptigimiz hesaplamadaki alt bölmelerin alanları gercege daha yakin bir sonuc üretmektedir. (Daha hassas bir \n"
               f"hesaplama yaptigimiz icin daha fazla alanı hesaplamaya dahil edip, daha az veri kaybı yasamış oluyoruz. \n"
               f"Bu sebeple; hata payı, veri kullanarak yaptigimiz integral hesabında  daha fazla oluyor. [a,b] aralığıni \n"
               f"çok sayıda alt aralığa bolerek duyarlıligi artirip iyileştirmeler yapabiliriz.  Ne kadar çok alt bölme alırsak \n"
               f"her bir bölmedeki hata o oranda küçüklecektir. Ancak  alt bölme sayisini artirdigimizda da daha fazla hesaplama \n"
               f"yaptigimize icin programın calışma suresi uzamaktadır.  Bu sebeple alt bölme sayisini belirlerken programimizin \n"
               f"performansını da göz önünde bulundurmamız gerekir.\n"
               f"*******************************\n\n"
               f"Sayısal integrallemeleri yaparken tercih ettigimiz yöntem: Trapez Kuralidir. (Yamuk Yontemi)")
out_file.close()