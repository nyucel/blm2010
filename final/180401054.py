#!/usr/bin/env python
# coding: utf-8


from sympy import Symbol
from sympy import pprint




def comment():
    with open("180401054_yorum.txt", "w") as comment:
        comment.write("CEYDA KAMALI 180401054\n")
        comment.write("İntegral hesaplama işlemlerini yaparken yamuk metodunu kullandım.\n")
        comment.write(
            "Yamuğun alanı, paralel kenarlarının uzunluklarının toplamının bu iki kenar arasındaki uzaklığın yarısı ile çarpımına eşittir.\n")
        comment.write("Deltax -----> Böldüğümüz alanlarının enine deltax denir. .\n")
        comment.write("Polinomlu integral hesabında deltax -----> ")
        comment.write(
            "Deltax değeri fonksiyonun kaç adet dikdörtgensel alana bölünceğini ifade eder.Deltax ile alan sayısı ters orantılıdır.Deltax azaldığı zaman dikdörtgensel alan sayısı artar , alan sayısının artmasıyla taşmalar engellenir bu sayede integral degerimiz gerçek degerine çok yaklasir. \n")
        comment.write("\n")
        comment.write("\n")
        comment.write("Polinomsuz integral hesabında deltax ------>")
        comment.write(
            "Polinomsuz integralı hesaplarken deltax değerini değiştiremiyoruz yani grafiği istediğimiz dikdörtgensel alanlara bölemiyoruz.Deltaxin başlangıçtaki değerine göre alan sayımız belirleniyor bu deltax değerini azaltamadığımızdan dolayı dikdörtgensel alan sayısı artmıyor,böldüğümüz alanlar ile grafik arasında taşmalar meydana geliyor,taşmalar meydana geldiğinden gerçek değerden uzaklaşıyoruz yani hata oranımız artıyor.")
        comment.write("\n")
        comment.write("\n")
        comment.write("\n")
        comment.write(
            "Polinomlu integral ve Polinomsuz integralde değerleri aynı verdimki değerler arasındaki farkı görebilelim.")


def polinom(derece, data):  ##derece=kacinci dereceden polinoma yaklaşcaksa o değer, data= listem
    m = []
    x = 0
    for i in range(derece + 1):
        mn = []
        for j in range(derece + 1):
            top = 0
            for k in range(1, len(data) + 1):
                top += k ** x
            mn.append(top)
            x += 1
        m.append(mn)
        x -= derece
    matr = []
    for i in range(derece + 1):
        top = 0
        for j in range(len(data)):
            top += data[j] * (j + 1) ** i
        matr.append(top)
    for i in range(derece + 1):
        b = m[i][i]
        for j in range(i + 1, derece + 1):
            o = b / m[j][i]
            matr[j] = matr[j] * o - matr[i]
            for k in range(derece + 1):
                m[j][k] = m[j][k] * o - m[i][k]
    for i in range(derece, -1, -1):
        b = m[i][i]
        for j in range(i - 1, -1, -1):
            o = b / m[j][i]
            matr[j] = matr[j] * o - matr[i]
            for k in range(derece + 1):
                m[j][k] = m[j][k] * o - m[i][k]
    for i in range(derece + 1):
        matr[i] = matr[i] / m[i][i]
    y = 0
    for i in range(len(data)):
        y += data[i]
    y = y / len(data)
    St = 0
    Sr = 0
    for i in range(len(data)):
        x = data[i]
        St += (data[i] - y) ** 2
        for j in range(len(matr)):
            x -= matr[j] * (i + 1) ** j
        x = x ** 2
        Sr += x
    r = ((St - Sr) / St) ** (1 / 2)
    return matr, r


def derece(multiple):  # en uygun fonksiyonun derecesini buluyor.
    big = max(multiple)
    for i in range(len(multiple)):
        if multiple[i] == big:
            degree = i
    print("bestdegree =\n", degree + 1)
    return degree


def polinomluInt(polinomlar):  # 180401054 okul numaram a=4 b=liste satır uzunluğu
    x = Symbol('x')

    polinom = 0
    for i in range(len(polinomlar)):
        polinom += polinomlar[i] * (x ** i)
    a = 4  # 180401054
    b = len(data)
    integral = 0
    deltax = 1  # değeri 0.1 ardından daha büyük bir değer girerek polinomlu ve polinomsuz integral arasındaki farkın büyüdüğünü görüyoruz
    n = int((b - a) / deltax)
    print("SECILEN DENKLEM ----->")
    for j in range(len(data)):  # len(veriler)yazmak yerine b de yazabilirdik ikiside aynı şeydir.
        print("{} X**{} +".format(data[j], j))
    for j in range(n):
        integral += deltax * (polinom.subs({x: a}) + polinom.subs({x: a + deltax})) / 2
        a += deltax
    print("\nPOLINOMLU INTEGRAL DEGERİ -----> ", integral)
    return integral, polinom


def polinomsuzInt(data):  # 180401054 a=4 verilerin satır uzunluğu ise b değerini verir.
    a = 4
    b = len(data)  # verilerin satır uzunluğunu versin diye len(veriler)yapıyoruz.
    integral = 0  # başlangıçta inregral değerini 0 a eşitliyoruz.
    deltax = 1  # bu değerin limiti ve doğruluk payı ters orantılır.limit 0 a yaklaşınca doğruluk payı max olur.
    n = int((b - a) / deltax)
    for i in range(n - 1):
        integral += deltax * (data[a] + data[a + deltax]) / 2
        a += deltax
    print("\nPOLINOMSUZ INREGRAL DEGERI -----> ", integral)

with open("veriler.txt", "r") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = int(data[i])
    pol, r1 = [0] * 6, [0] * 6
    for m in range(0, 6):
        pol[m], r1[m] = polinom(m + 1, data)

r2 = derece(r1)
bestpol, integral1 = polinomluInt(pol[r2])
print("\nPOLİNOM ----->", bestpol)
polinomsuzInt(data)
comment()
