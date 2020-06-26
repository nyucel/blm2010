## Selahattin Ahmed Ataşoğlu - 190401090

# Bilimsel Hesaplama Bütünleme Ödevi

İçerisine asal sayı değerleri satır satır olacak biçimde yazılmış asallar.txt dosyasında bulunan
asal sayı değerlerini 3. dereceden polinoma yakınlaştıran ve istenilen a değerine
(okul numarasının son iki hanesi) göre polinomlu ve polinomsuz olmak üzere
iki farklı şekilde türevlerini bulan programın yazılması beklenmektedir.

## Kullanılan Kütüphaneler

sympy kütüphanesi import edilerek projede kullanılır.

	import sympy as sym


## Projenin Çalışma Prensibi

Yazmış olduğumuz kod içerisinde 8 farklı fonksiyon kullanılmıştır. Yazmış olduğum kodun kullanılış
şeklini, kullanmış olduğum aşağıdaki fonksiyonları ve kullanılış amaçlarını anlatarak şöyle açıklayabiliriz:

### readFile():

Bu fonksiyonumuzda asallar.txt dosyası içerisinde bulunan asal sayı değerleri tek tek çekilir,
çekilen değerler asalDiziDegerler adlı diziye int tipinde olacak şekilde aktarılır.

### createMatrix():

Bu fonksiyonumuzda 4'e 4'lük bir matris oluştururuz.

### matrixWithGauss():

Bu fonksiyonumuzda ise Gauss yöntemiyle matrisler kullanılarak hesaplamalar yapılır. İçerisinde
matris oluşturmamız gerektiği için bu matrisi createMatrix() fonksiyonu ile yapıyoruz.
Gauss yöntemi sayesinde içerisinde hesaplamasını yapmış olduğumuz katsayıların değerleri bulunur
ve bu değerler başta oluşturduğumuz coefficients dizisine aktarılır. Devamında ise bulduğumuz bu 
katsayıların değerlerinin ekrana yazdırımı sağlanır.

### selectRowGetValue(row, rowValue):

Bu fonksiyonda ise parametre olarak satır(row) ve satırda bulunan asal sayı değerini(rowValue)
alırız. "row" değeri 0 haricinde bir değer olduğu sürece bu hesaplamalar devam eder. "row" değeri
0'a eşitlendiğinde ise else'e girilir ve bu kısımdaki işlemler yapılır.

###function(x):

Bu fonksiyonda 3. dereceden polinomumuz tanımlanır. Bu polinom değerimiz derivativeWithPolynom()
fonksiyonunda polinolu türev alma işlemi için kullanılacaktır.

### derivativeWithPolynom():

Bu fonksiyonda ise polinomlu türev hesaplama işlemimiz yapılır. a değeri okul numaramdan dolayı 90
alıyorum. h değerimiz ise polinomlu olarak türev alma işlemi yaptığımız için 0.01 gibi dar bir aralıkta
alabiliyoruz. xprime hesaplamamızda ise sayısal türev almak için yukarıdaki "function" fonksiyonumuzu
kullanarak polinomlu sayısal türev değerimizi buluyoruz. Burada kullanmış olduğumuz sayısal türev alma
denklemimiz ise "Merkezi Farklar ile Birinci Dereceden Türev Alma" denklemidir. 

	f(xi)' = delta f(x) / delta x = f(xi + h) - f(xi - h) / 2h

### derivativeWithOutPolynom():

Bu fonksiyonda ise polinomsuz bir şekilde türev hesaplaması yaparak ekrana yazdırıyoruz.
Polinomlu halinden farklı olarak h değerini polinomsuz olduğu için en iyi şart olarak 1 alabiliyoruz.
Hesaplama yapılırken direkt olarak asal sayı değerlerimizi atmış olduğumuz asalDiziDegerler dizisinden
verilerimizi çekerek gerekli hesaplamaları yapıyoruz. Ayrıca dizimiz index[0]'dan başladığından, 
istenen değeri bulabilmemiz için a değerinin bir eksiğini almamız gerekir. Yukarıda kullanılan
sayısal türev alma denklemi aynı şekilde burada da kullanılır.

### comments():

Polinomlu ve polinomsuz türev hesaplamalarının arasındaki bu farkın neden olduğu yorum satırlarıyla
kısaca açıklanmıştır. Yorumlar yorum.txt adlı bir dosya açılarak içerisine yazılmıştır.

## Kodun Çalıştırıldığı Yer

	readFile()                                      # Değerlerin bulunduğu asallar.txt dosyasından veriler satır satır çekilir.
	selectRowGetValue(109, asalDiziDegerler[108])   # Seçilen satır ve o satırdaki asal sayı değerine göre hesaplama yapar.
	writePolynomEquation(x)				# Polinom denklemi günlük hayatta kullandığımız şekil ekrana yazdırılır.
	derivativeWithPolynom()                         # Polinomlu türev değerlerini ekrana yazdırır.
	derivativeWithOutPolynom()                      # Polinomsuz türev değerini ekrana yazdırır.
	comments()                                      # Yorumlar, yorum.txt dosyasına yazılır.

readFile() fonksiyonumuz ile verileri asallar.txt dosyamızdan okuyoruz ve diziye aktarıyoruz.

createMatrix() fonksiyonu ile 4'e 4'lük boyutlarında bir matris oluşuturulur.

matrixWithGauss() fonksiyonunda öncelikle oluşturmamız gereken matris, createMatrix ile oluşturulur.
Daha sonra oluşturulan bu matrisin satır ve sütun uzunluklarına göre "row, column" değerleri bulunur.
Katsayı değerleri bulunur ve bu katsayı değerleri, coefficients adı verdiğimiz diziye aktarılır.
Son olarak katsayı değerleri kullanıcıya gösterilmek üzere ekrana yazdırılır.

writePolynomEquation() fonksiyonunda ise 3. dereceden oluşturduğumuz polinom denklemi "equation"
değişkenine atanır. Daha sonra bu değer sym.pprint ile günlük hayattaki kullanım şekline uygun olarak
ekrana yazdırılır.

selectRowGetValue(..., ...) ile seçilen satır ve seçilen satırda bulunan asal sayı değeri ile işlemler
yapılır. "row" değeri 0 olmadığı sürece if içerisinde belirlenen işlemler yapılır, row'un 0 olması durumunda
else'e girilerek matrixWithGauss() işlemi yaptırılır.

function(x) ile polinomlu türev alacağımız derivativeWithPolynom fonksiyonu için 3. dereceden polinom
denklemi oluşturulur ve değeri geri döndürülür.

derivativeWithPolynom'da "a" değerimizi okul numaramdan dolayı 90 olarak alıyoruz. "h" değerimizi ise
polinomlu türev alma işlemi yaptığımız için 0.01 gibi daha dar bir aralıkta alıyoruz. Polinomlu
türev sonucunu bulabilmek için function fonksiyonunu ve Merkezi Farklar ile Birinci Dereceden
türev alma denklemini kullanırız. Çıkan sonuç ekrana yazdırılır.

derivativeWithOutPolynom fonksiyonu ile polinomsuz türev hesabı yapılarak ekrana yazdırılır.
"h" değerimiz, bu hesaplamanın polinomsuz olmasından dolayı en az 1 değerini alabilmektedir.
Polinomlu türev alma fonksiyonundaki gibi burada da Merkezi Farklar ile Birinci Dereceden türev alma
denklemi kullanılır.

comments() fonksiyonu çalıştırılarak yorum.txt dosyası oluşturulur ve içersine bu yorumlar yazılır.

Başarıyla programdan çıkış yapılır.

## Kodun Çalıştırılabilmesi İçin Gereksinimler

phyton3 versiyonu ile derlenmelidir. sympy kütüphanesi kullanıldığı için bu kütüphanenin
konsol üzerinden gerekli indirmelerinin ya da herhangi bir phyton derleyicisi kullanılıyor ise 
bu kütüphanenin eklenmesi gerekmektedir. 
	
	pip install sympy
