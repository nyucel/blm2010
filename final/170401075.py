# Birhan Berk Oktay - 170401075

# Bu Python kodu birdenAltinciDereceyeKadar isimli fonksiyonun cagirilmasiyla calisir.
# Ayni dizinde bulunmasi gereken veriler.txt dosyasindan veri okur.
# Okudugu verileri 1,2,3,4,5 ve 6. dereceden polinomlara yakinlastirir ve 
# bu polinomlarin korelasyon degerini ve katsayilarini hesaplar.
# Polinomlar arasindaki en yuksek korelasyan degerine sahip polinomun denklemini
# a (5, 170401075 ogrenci numarasinin son rakami) ve b (veriler.txt deki veri sayisi)
# araliginda ki sayisal integralini, ayni yontem ile verilerin polinomsuz olarak sayisal 
# integralini ve yine en yuksek korelasyan degerine sahip polinomun denklemini kullanarak
# 1/3 simpson yontemi ile sayisal integral hesaplamasi yapar.

def matristenDiziye(m):
  # Matrisi diziye ceviren fonksiyon
  # matris[[a],[b]] --> dizi[a,b]
  dizi = []
  for i in m:
    dizi.append(i[0])
  return dizi

def matrisCarpimi(m1, m2):
  # Iki matrisi carpip sonuc matrisini donduren fonksiyon
  r, m = [], []
  for i in range(len(m1)):
    for j in range(len(m2[0])):
      toplam = 0
      for k in range(len(m2)):
        toplam += (m1[i][k] * m2[k][j])
      r.append(toplam)
    m.append(r)
    r = []
  return m

def denklemSistemiCoz(m1, m2):
  # Denklem sistemi sonucunu dizi donduren fonksiyon
  n = len(m1)
  idizi = list(range(n))
  for i in range(n):
    a = 1.0 / m1[i][i]
    for j in range(n):
      m1[i][j] *= a
    m2[i][0] *= a
    for j in idizi[0:i] + idizi[i+1:]:
      b = m1[j][i]
      for k in range(n):
        m1[j][k] = m1[j][k] - b * m1[i][k]
      m2[j][0] = m2[j][0] - b * m2[i][0]
  return matristenDiziye(m2)

def nDerecedenPolinomaYakinlastir(m, veri):
  # Veri kumesindeki verileri n. dereceden polinoma yakinlastirip
  # a0,a1,a2,..,an katsayilarini ve hata degerlerini donduren fonksiyon

  # xi ussu toplam ve xi ussu yi toplami hesapla
  # xiussuToplam -> [toplam(xi), toplam(xi^2), ..., toplam(xi^2m)]
  # xiussuyiToplam -> [toplam(xi^0*yi), toplam(xi^1*yi), ..., toplam(xi^m*yi)]
  n = len(veri)
  xiussuToplam = [0] * m * 2
  xiussuyiToplam = []
  for i in range(n):
    for j in range(2 * m):
      xiussuToplam[j] += (i + 1) ** (j + 1)
    for k in range(m + 1):
      if(len(xiussuyiToplam) < m + 1):
        xiussuyiToplam.append([0])
      xiussuyiToplam[k][0] += (i + 1) ** k * veri[i]
      
  # denklem sistemini olustur
  # n + toplam(xi) + toplam(xi^2) + ... + toplam(xi^m)
  # toplam(xi) + toplam(xi^2) + ... + toplam(xi^m+1) seklinde
  a = [[]]
  altSinir = 0
  ustSinir = m + 1
  for i in range(m + 1):
    if(i == 0):
      a[0].append(n)
      for j in range(0, m):
        a[0].append(xiussuToplam[j])
    else:
      a.append([])
      for k in range(altSinir, ustSinir):
        a[i].append(xiussuToplam[k])
      altSinir += 1
      ustSinir += 1
  katsayilar = denklemSistemiCoz(a, xiussuyiToplam)

  # x ortalama ve y ortalama hesapla
  xtoplam = 0
  ytoplam = 0
  for i in range(n):
    xtoplam += i + 1
    ytoplam += veri[i]
  yortalama = ytoplam / n

  # hata hesapla
  # sr -> Hatalarin karelerinin toplami
  # r -> Korelasyon katsayisi -> r^2
  # syx -> Standart tahmini hata
  korelasyon = []
  st = 0
  sr = 0
  for i in range(n):
    b = 0
    for j in range(len(katsayilar)):
      b += katsayilar[j] * (i + 1) ** (j)
    sr += (veri[i] - b) ** 2
    st += (veri[i] - yortalama) ** 2
  r = ((st - sr) / st)
  korelasyon.append(r)

  return katsayilar, korelasyon

def f(x, katsayilar):
  # Fonksiyonun derecesini gelen katsayilar kadar olusturan fonksiyon
  fonksiyon = 0
  for i in range(len(katsayilar)):
    fonksiyon += katsayilar[i] * x ** i # -> a0*x^0, a1*x^1, .., an*x^n
  return fonksiyon

def simpson(veri, katsayilar):
  a = 5 # 170401075
  b = len(veri) # Veriler.txt satir sayisi
  deltax = 1
  integral = 0
  n = int((b - a) / deltax)
  toplam1 = 0
  toplam2 = 0
  for i in range(1, n):
    if(i % 2 == 1):
      toplam1 += f(a + i * deltax, katsayilar)
    else:
      toplam2 += f(a + i * deltax, katsayilar)
  integral = deltax * (f(a, katsayilar) + f(b, katsayilar) + 4 * toplam1 + 2 * toplam2) / 3
  return integral

def integral(veri, katsayilar):
  a = 5 # 170401075
  b = len(veri) # Veriler.txt satir sayisi
  deltax = 1
  integral = 0
  n = int((b - a) / deltax)
  for i in range(n):
    integral += deltax * (f(a, katsayilar) + f(a + deltax, katsayilar)) / 2
    a += deltax
  return integral

def integralPolinomsuz(veri):
  a = 5 # 170401075
  b = len(veri) # Veriler.txt satir sayisi
  deltax = 1
  integral = 0
  n = int((b-a) / deltax)
  for i in range(n - 1):
    integral += deltax * (veri[a] + veri[a + deltax]) / 2
    a += deltax
  return integral

def birdenAltinciDereceyeKadar(dosya):
  veri = []
  try:
    f = open(dosya, "r")
    for i in f.read().split():
      veri.append(float(i))
  except IOError:
    print("Veriler bulunamiyor. Verilerin bulundugu .txt doyasini kontrol edin.")
  finally:
    f.close()
  r = [] # Korelasyon degerleri
  katsayilar = [] # Tum polinomlarin katsayilari
  for i in range(1, 10):
    tumSonuc = nDerecedenPolinomaYakinlastir(i, veri)
    katsayilar.append(tumSonuc[0])
    r.append(tumSonuc[1][0] ** (1 / 2))
  maxkorelasyon = r.index(max(r)) + 1 # En yuksek korelasyon degerine sahip derece

  print("Polinomlu integral = " , integral(veri, katsayilar[maxkorelasyon-1]))
  print("Polinomsuz integral = " , integralPolinomsuz(veri))
  print("---Ekstra---")
  print("1/3 Simpson yontemi = " , simpson(veri, katsayilar[maxkorelasyon-1]))
  #------------------------

birdenAltinciDereceyeKadar("veriler.txt")