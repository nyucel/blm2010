170401032 Gökçe Nur Sarıcı

Bu proje 600'den küçük asal sayıları bulunup asallar.txt dosyasındaki
verileri kullanarak 3. dereceden polinoma yakınlaştırılıp istenilen
değere göre o noktadaki türevini bulur ve polinomsuz bir şekilde de
hesaplama yapar.

İÇERİSİNDE KULLANILAN FONKSİYONLAR VE İŞLEVLERİ:

gaussYontemi(matris): içerisine yollanan matrisi çözmeye yarayan bir
yöntemdir. Bize katsayılar matrisinin çözümünü verir.

xi(uzunluk): Yaklaştırma metodunu uygulamamız için kullanılan
denklemlerin xi elemanlarını bulmamıza yarayan fonksiyondur.

xiyi(uzunluk,primes): Uzunluğu ve verilerin bulunduğu diziyi parametre
olarak alır. Yaklaştırma metodunda kullanılan denklemlerin xiyi
elemanlarını bulmamıza yarayan fonksiyondur.

matris(uzunluk,primes,sayac):Yaklaştırma metodu sonucunda katsayılar
matrisi olusturmamıza yarayan fonksiyondur.

matrisOlustur(primes): Olusan katsayılar matrisinin gaussYontemı ile
çözülmüş halini döndüren ve asıl kullanacağımız olan matrisi
olusturdugumuz fonksiyondur.


f(x): Polinomumuzu olusturmamıza yarayan fonksiyondur.

turev(a): Polinomlu turev fonksiyonudur. f(x) fonksiyonundan elde
ettiğimiz polinomu kullanarak türev işlemi gerçekleşir.Geri Sonlu
Farklar Yöntemi kullanıldı.

turev2(a): Polinomsuz turev fonksiyonudur.

yorum(): Polinomlu turev fonksiyonu ile polinomsuz turev fonksiyonu
arasındaki farkları açıkladığım fonksiyondur.

PROGRAM NASIL ÇALIŞIR VE KULLANILIR?

Program ilk olarak 600'den küçük asal sayıları bulduğumuz bir kod
parçasıyla başlar. Bu kodun çıktısı asallar.txt dosyasına yazdırılırken
aynı zamanda primeNumbers adlı diziye eklenir. Artık asıl amacımız için
elimizde verilerimiz vardır. bu dosyadan veriler tek tek çekilerek asıl
kullanacagımız primes dizisine eklenir. Öncelikle xi ve xiyi
fonksiyonlar içinde tanımlanır.Çünkü yakınlaştırma işlemi yapmamız için
katsayıları elde etmeliyiz. xi elimizde olan verilerin
1+(1+2)+(1+2+3)... şeklinde toplanmasıdır. Burada da her denklem için
sağlanacak bir algoritma kullanılmıstır. xiyi ise xi ile yi yani
verilerin toplamının çarpılmasıyla elde edilir aynı şekiğlde her derecen
denklemi sağlayacak şekilde bir algoritma kullanılmıstır. Daha sonra
buldugumuz xi ve xiyi değerleri ile katsayılar matrisi olusturulur.
Matris olusturulurken once tek boyutlu dizi olusturulur ve eklemeler
yapılır daha sonra bu dizi olusturulan diğer diziye eklenir ve sonucunda
bir matris elde etmiş oluruz. Bir sonraki adım Gauss Yonteminin
kodlanmasıdır.. Kısaca Gauss Yontemı katsayılar matrisinin elementer
satır işlemleri ile üst üçgensel hale dönüştürme sonucunda bize çözüm
veren bir yöntemdir. Elimizde bulunan matrisi GaussYontemi fonksiyonun
içine gönderim çözdürdürürüz bu işlem matrisOlustur fonksiyonunun içinde
gerçekleşir ve sonucunda bize işlemleri yapacagımız matris döndürülür.
Döndürülen matris tek boyuta indirgenir ve istenilen katsayılar
kullanıcıya gösterilir. Daha sonra bizden istenen polinomlu ve
polinomsuz türev için ilk türev fonksiyonunda Geri Sonlu Farklar Yöntemi
kullanılarak okul numaramın son iki harfi olan 32 noktasında polinomun
turevınıı buldurur. turev2 fonksiyonunda ise polinomsuz turev 32
noktasında bulunmus olur. Son olarak ise yorum fonksiyonunda polinomlu
ve polinomsuz turev fonksiyonlarının farklı çıktı vermesinin sebebi
irdelenir ve yorum.txt dosyasına yazdırma işlemi yapılır.
