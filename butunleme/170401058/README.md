asallar.txt dosyasındaki verileri 3. dereceden polinoma yakınlaştıran ve istenilen x değerine göre 
polinomlu ve polinomsuz 1. dereceden türevlerini bulan yazılım.

İçerisindeki fonksiyonlar:
1. oku() 
asallar.txt dosyasındaki verileri tam sayı olarak diziye atar ve geri döndürür.
2. ucuncu_der(i,veri)
parametreler:
i --> metin dosyasındaki işlenen satır
veri --> metin dosyasındaki işlenen satırdaki veri
Alınan değerlerle matris verileri hesaplanır daha sonra matris hesaplanır ve 3. dereceden 
polinomun katsayıları bulunur. Katsayı dizisini geri döndürür.
3. yardimci(asallar)
parametreler:
asallar --> verilerin tutulduğu dizi
Dizi elemanlarını ve bulunduğu satırları ucuncu_der fonksiyonuna yollar. Son olarak dizideki 
elemanlar bittiğinde matris oluşturulduğunda matrisi çözüp 3. dereceden polinom katsayılarını
bulmak için son kez ucuncu_der fonksiyonu çağrılır. Geriye dönecek katsayılar dizisi geriye 
döndürülür.
4. f(i)
i --> istenen nokta
3. dereceden polinomda istenen noktadaki değer geri döndürülür.
5. turev_1(x=58)
x --> istenen nokta
Varsayılan olarak x=58 ken polinomlu sayısal türev ekrana yazılır.
6. turev_2(x=58)
x --> istenen nokta 
Varsayılan olarak x=58 ken polinomsuz sayısal türev ekrana yazılır.
7. yorum()
Polinomlu ve polinomsuz sayısal türev değerlerinin farklı olmasının sebebini açıklayan fonksiyon.
Açıklama yorum.txt dosyasına yazılır.

KULLANIM:
İstenen verilerin 3. dereceden polinoma yakınlaştırılması için oku fonksiyonundan geri dönecek olan dizi bir değişkene atanır. 
yardimci fonksiyona parametre olarak bu dizi gönderilir ve geriye dönecek katsayılar dizisi bir değişkene atanır. Dizideki istenen noktaya kadar ucuncu_der fonksiyonu çağrıldıktan sonra 
katsayıların bulunması için yapılacak gerekli işlemler tekrar ucuncu_der fonksiyonun ilk parametresine -1 verilerek yapılır.
turev_1 fonksiyonuyla 3. dereceden polinoma ait sayısal türev hesaplanır. Hesaplamalarda aralığı h 
değişkeniyle arttırıp azaltarak istenen sonuç elde edilir.(varsayılan olarak 58)
turev_2 fonksiyonuyla polinomsuz sayısal türev hesaplanır. (varsayılan olarak 58)
Hesaplamalarda aralık en az 1 (h=1) olmalıdır.
yorum fonksiyonu çağırılarak sayısal türev sonuçlarındaki farkın sebebi yorum.txt dosyasından okunabilir.



