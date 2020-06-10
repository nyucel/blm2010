import numpy as np

## 160401092 MEHMET TAHIR TAS  - SAYISAL YONTEMLER ODEVI ##

def fitPolynomeThroughOrigin(x, y, nthDegree):
    # Kaynak: https://stackoverflow.com/questions/17930473/how-to-make-my-pylab-poly1dfit-pass-through-zero
    # Bu fonksiyon uretilecek polinomun sabitinin 0 olmasini garantiliyor. Ornek sifirlanmis 2. derecen polinom: y = x^2 + x + 0
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
########################################################################################################################
# verileri dosyadan okuma
infile = open('veriler.txt', 'r')
data_arr = []
for line in infile:
    data_arr.append(int(line))
infile.close()

# for i in range (len(data_arr)):
# print (data_arr[i], end=" ")

# Veriler test amacli hard code edilmistir
# data_arr = [1,5,6,18,47,98,191,359,670,947,1236,1529,1872,2433,3629,5698,7402,9217,10827,13531,15679,18315,20921,23934,27069,30217,34109,38226,42282,47029,52167,56956,61049,65111,69392,74193,78546,82329,86306,90980,95591,98674,101790,104912,107773,110130,112261,114653,117589,120204,122392,124375,126045,127659,129491,131744,133721,135569,137115]
mse_arr = []
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
    # print(f"Hata Payi: {hataPayi}\n")
    # Her bir dereceden polinom icin hesaplanmis hata paylari sonradan dosyaya yazdirilmak uzere mse_arr'de tutulur
    mse_arr.append(hataPayi)
    # grafik ve dosyaya yazmak icin polinom etiketi uretelim
    label = polynomialToString(polynomialDegree, fx.coef);
    # sonuclari dosyaya yazalim
    outfile.write(f"{label}\n")

outfile.write("\nHATA PAYLARI: \n")
for i in range(0, 6):
    outfile.write(f"{i+1}. dereceden polinomun hata payi: {mse_arr[i]} \n")

minimum_error = min(mse_arr)
minimum_error_index = mse_arr.index(minimum_error) + 1
outfile.write(f"\nEn uygun polinom en kucuk hata payi ({minimum_error}) olan {minimum_error_index}. dereceden polinomdur. \n\n")
outfile.write("####################################################################################################\n")
########################################################################################################################
# # 3. SORU: # #
hata_payi_arr = []
for i in range(0, len(data_arr), 10):
    outfile.write(f"{i} - {i + 9} araligindaki veri kumesi icin hesaplama yapiliyor. \n")
    outfile.write("POLINOMLAR: \n")
    sliced_array = data_arr[i:i + 10]
    x_val = range(i, (i + len(sliced_array)))
    for polynomialDegree in range(1, 7):
        fx = convertDataToPolynomial(sliced_array, polynomialDegree)
        ornekSonuc = fx(x_val)
        hataPayi = calculateMeanSquaredError(sliced_array, ornekSonuc)
        hata_payi_arr.append(hataPayi)
        label = polynomialToString(polynomialDegree, fx.coef);
        outfile.write(f"{label}\n")

    outfile.write("HATA PAYLARI: \n")
    for k in range(0, 6):
        outfile.write(f"{k + 1}. dereceden polinomun hata payi: {hata_payi_arr[k]} \n")
    min_err = min(hata_payi_arr)
    min_err_index = hata_payi_arr.index(min_err) + 1
    outfile.write(f"\nEn uygun polinom en kucuk hata payi ({min_err}) olan {min_err_index}. dereceden polinomdur. \n")
    sliced_array = []  # cleaning the sliced_array
    hata_payi_arr = []  # cleaning the hata_payi_arr
    outfile.write("####################################################################################################\n")
# sonuc.txt dosyasini kapatiyoruz
outfile.close()


