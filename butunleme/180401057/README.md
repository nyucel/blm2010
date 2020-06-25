                                             Bedirhan Karakaya
Programın Nasıl Çalıştığı:
Benim bu programım 0 ile 600 arasındaki asal sayıları bulup bunları 3.dereceden bir polinoma yaklaştıror ve 
bu polinomun kat sayılarınbuluyor. Daha sonra bulduğum polinomu kullanarak bir türev alma işlemi uyguluyorum.
Bir de ayrıca polinomu kullanamdan bir türev daha buluyorum ve en son olarak bu iki türev bulma fonksiyonumun
arasındaki farkı açıklıyorum.

-> ilk olarak 0 ile 600 arasındaki sayıları asallar.txt dosyasına hepsini yazıyorum.

-> gaussYontemi denklem elemanlarının katsayılaı gauss yontemi ile buluyorum ve o kat sayıyı döndürüyorum

-> degerler_x formuldeki x üzeri 0 dan x üzeri altıya kadar değerler buluyorum.

-> toplam_xy x^0*y den x^3*y ye kadar olan değerleri buluyorum.

-> katsayiBul katsayılar gauss yöntemi ile buluyorum ve onları bir listeye atıyorum en olarak da donduruyorum.

-> f(x) fonksiyonum katsayi bul fonksiyonumun bulduğu kat sayıları kullanarak 3. dereceden bir fonksiyon oluşturuyor.

-> polinomluTurev fonksiyonum f(x) fonksiyonumun ürettiği polinomu kullanrak türev işlemini gerçekleştiriyor.(Merkezi Farklar Yönetmi)

-> polinomsuzTurev fonksiyonum polinomsuz olarak türev buluyor.(Merkezi Farklar Yönetmi)

-> yorum fonksiyonum polinomluTurev ve polinomsuzTurev in arasındaki farkları yazdığum yorumu mu yorum.txt dosyasına yazıyor.

-> printer fonksiyonum ise yazdığım fonksiyonların çalışmasını sağlıyor.

Programın Kullanımı:
	-> Asal sayiları bir txt dosyasına yazdırığımı görmek için yorum satırından çıkarmanız gerekmektedir.
Onun haricinde Yazdığım kodda kullanıcının herhangi bir girdi yapmasına gerek olmadığı için kodumu
çalıştırmak yeterlidir.


