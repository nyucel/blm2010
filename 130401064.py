# Süleyman Baltacı - 130401064
# -*- coding: utf-8 -*-
import numpy as np

def RMSE(pred, target):
    err = np.subtract(target, pred)
    return (np.mean(err**2))**0.5
    
# veri dosyasi acilir
f = open("veriler.txt")

# veriler okunur, varsa bos satirlar silinir
data = f.readlines()
if "\n" in data: data.remove("\n")


# veriler numpy array seklinde y'ye kaydedilir, x 0'dan baslatilir
y = np.array(data, dtype=int)
x = np.array([i for i in range(len(y))], dtype=int)

# sonuc dosyasi acilir
f_sonuc = open("sonuclar.txt","w+")
f_sonuc.write("Tum veri uzerine tek bir polinom tanimlandiginda:\n\n")

## Tum veri uzerine tek bir polinom fit edilginde:
RMSE_list = [0]*6

for i in range(6):

    # ip : interpolasyon fonksiyonu
    poly = np.poly1d(np.polyfit(x, y, i+1))
    f_sonuc.write(f"Polinom derecesi: {i+1} \n")
    f_sonuc.write(f"Katsayilar: {poly.coeffs} \n")
    
    # RMSE hesaplanir
    RMSE_list[i] = RMSE(poly(x), y)
    f_sonuc.write(f"RMSE: {RMSE_list[i]:.3f} \n\n")
    

# en iyi sonucu veren polinomun derecesi bulunur, RMSE ile birlikte yazdirilir
eniyi_derece = np.argmin(RMSE_list)+1
f_sonuc.write(f"En dusuk hatayi {eniyi_derece}. dereceden polinom vermektedir.\n")
f_sonuc.write(f"RMSE: {RMSE_list[eniyi_derece-1]:.3f} \n\n\n")


## veri onluk kisimlara bolunerek her birine polinom fit edildiginde:
f_sonuc.write("Her bir onluk icin farkli polinomlar bulundugunda:\n\n")

# kac farkli polinom gerektigi hesaplanir:
onluk_sayisi = int((len(x)/10)) + 1

for i in range(onluk_sayisi):
    
    # polinom fit edilecek aralik icin indexler bulunur, x ve y datasi secilir:
    i_min = i*10
    i_max = min(i*10+9, len(x)-1)
    x_curr = x[i_min:i_max+1:]
    y_curr = y[i_min:i_max+1:]
    
    # her bir dereceden polinomlarin ve RMSE'lerinin tutulacagi listler tanimlanir
    poly_lst =[]
    RMSE_list = []
    # polinom fit edilecek aralik eger 7'den kucuk veri iceriyorsa, 
    # en fazla (bu araliktaki nokta sayisi) - 1 dereceli polinom denenir    
    for j in range(min(i_max-i_min, 6)):
	# poly_lst listesine j dereceli polinom fit edilir, RMSE hesaplanir
        poly_lst.append(np.poly1d(np.polyfit(x_curr, y_curr, j+1)))
        RMSE_list.append(RMSE(poly_lst[j](x_curr), y_curr))

    # en iyi sonucu veren polinom derecesi bulunur ve sonuc yazdirilir
    eniyi_derece = np.argmin(RMSE_list) + 1
    f_sonuc.write(f"x : [ {x[i_min]} {x[i_max]} ]\n")
    f_sonuc.write(f"Polinom derecesi: {eniyi_derece}, ")
    f_sonuc.write(f"RMSE: {RMSE_list[eniyi_derece-1]:.3f} \n\n")
    
f_sonuc.close()
f.close()
