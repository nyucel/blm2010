# Süleyman Baltacı 130401064
import numpy as np


def RMSE(pred, target):
    err = np.subtract(target, pred)
    return (np.mean(err ** 2)) ** 0.5


# (1) Dosya okuma, RMSE hesaplama ve en dusuk RMSE'yi veren polinomu bulma

# veri dosyasi acilir
f = open("veriler.txt")

# veriler okunur, varsa bos satirlar silinir
data = f.readlines()
if "\n" in data: data.remove("\n")

# veriler numpy array seklinde y'ye kaydedilir, x 0'dan baslatilir
y = np.array(data, dtype=int)
x = np.array([i for i in range(len(y))], dtype=int)

## Tum veri uzerine tek bir polinom fit edilginde:
RMSE_list = [0] * 6
poly_list = list()

for i in range(6):
    # ip : interpolasyon fonksiyonu
    poly = np.poly1d(np.polyfit(x, y, i + 1))
    # RMSE hesaplanir
    RMSE_list[i] = RMSE(poly(x), y)
    poly_list.append(poly)


# en iyi sonucu veren polinomun derecesi bulunur, RMSE ile birlikte yazdirilir
eniyi_derece = np.argmin(RMSE_list) + 1

# en iyi sonucu veren (verilerle uyumlu) polinom
poly = poly_list[eniyi_derece - 1]

# (2) Tespit edilen polinomun a ile b arasindaki alanini hesaplama ve yzdirma

# polinomun altindaki gercek alani bulmak icin polinomun integralini almaliyiz
# x^n 'in integrali x^(n+1) / (n+1) 'dir bu sekilde yeni bir polinom uretiyoruz.
integral_poly_coeffs = [0] * (len(poly.coeffs) + 1)

for i in range(len(poly.coeffs)):
    integral_poly_coeffs[i] = poly.coeffs[i] / (len(poly.coeffs) - i)

integral_poly_coeffs[len(poly.coeffs)] = 0
integral_poly = np.poly1d(integral_poly_coeffs)
# print(integral_poly)

a = 4
b = len(y) - 1

# polinomun (poly) a'dan (4) b'ye (son) kadar olan integrali
AreaPoly = integral_poly(x[b]) - integral_poly(x[a])
print('Integral ile hesaplanan alan: {}'.format(AreaPoly))

# (3) Polinom kullanmadan trapezoid (yamuk) integral hesaplama yontemiyle alan hesaplama

# Trapezoid (Yamuk) yontemiyle alani bulalim:
AreaTrap = 0
for i in range(a, b):
    AreaTrap = AreaTrap + (poly(i) + poly(i+1)) / 2.0

print('Trapezoid (yamuk) yontemi ile hesaplanan alan: {}'.format(AreaTrap))
