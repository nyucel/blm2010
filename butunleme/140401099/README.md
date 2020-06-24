

140401099 Fikret ÇAKIRLI

Bu program 600'den küçük asal sayıları içeren asallar.txt dosyasından
verileri okuyarak üçüncü dereceden polinoma yaklaştıran ve istenilen x değerine göre 
denkleminin birinci dereceden türevini bularak polinom kullanmadan da sonucu elde etmeye yarıyor.

Programdaki fonksiyonlar sırasıyla çalışmaktadır.

- ```asal_yaz(asal)``` fonksiyonu
ile bir kez çalıştırıp asallar.txt dosyası oluşturulur.

- ```f(denklem,x_degeri)``` fonksiyonu ise
denklemi kullanabilmesi ve denklemdeki x değişkenine değer atanabilmesini sağlayan
ve sonucu elde eden bir fonksiyondur.

- ```turev_bul_polinom(denklem)``` fonksiyonu
"ileri fark" ile türev alma yöntemini kullanarak "a" değeri olan öğrenci numaramın son iki hanesindeki 
türevi ile polinom denklemi kullanarak sonucu return eden fonksiyondur.

- ```turev_bul_polinomsuz()```  fonksiyonu 
polinom denklemi kullanmadan ve aynı yöntemi "ileri fark" kullanarak
sayısal olarak hesaplar ve sonucu return eder.

- ```yorum_yap()``` fonksiyonu 
yaptığım çıkarımsalları yourum.txt şeklinde bir dosya olarak yazdırır.

**Programının Çalışma Senaryosu:**
Kısaca bu program asal sayıları asallar dosyasından okur, x lerin toplamı 
ve y lerin toplamı ...vs matrisini oluşturan değişkenler üzerinde işlem yapabilmektedir.
Matrisin determinantını bulup y lerin sütun matrisiyle yer değiştirerek tüm 
determinantları bulur, determinantları orginal matrisinin determinantına bölerek 
a0 ,a1 ,a2 ..vs katsayıları bulur ve bu adımda polinom denklemi elde edlmiş olur.
Bulduğumuz denklemi ```turev_bul_polinom``` fonksiyonuna parametre olarak atar, 
bu fonksiyonun h değeri 0.01 ve x0 değeri ise öğrenci numaramın son iki hanesi 
olarak belirlenmiştir. İleri fark türevi formulü f(x0+h)-f(x0) uygulanarak türevi elde
edilir ve kullancıya ekran çıktısı şeklinde gösterir. Bu formul ile  "f(denklem,x_degeri)" 
yardımcı fonksiyonu ile bulunur. Sonraki satırda "turev_bul_polinomsuz" fonksiyonuna çağrılır, 
bu fonksiyon doğrudan asallar.txt dosyasından ki bulunan verilerle işlem yapar. İleri fark yöntemi ile 
sonucu elde eder ve kullancıya ekran çıktısı şeklinde gösterir.

**Gereksinimler ve Kullanım:**
- işletim sistemi linux ise genelde python veya python3 yüklüdür, yüklü değilse 
kullandığınız dağıtımın yazılım deposundan komut yazılıp install python3 şeklinde yüklenir. 
- işletim sistemi windows ise internet üzerinden python3 indirilip bin dizisini program files içinde alıp 
windows environment path kısmına eklenmesi gerekir.

Python kurduktan sonra numpy kütüphanesi indirilmeden kod çalışmayabilir.
Python programlama dilinin bilimsel hesaplamaların temel kütüphanesi olan NumPy‘yi indirmek için terminale 
“pip install numpy” komutu yazılır.

Kodu turev.py dosyasından ```python3 .\turev.py``` yazarak çalıştırabilirsiniz, 
elbette ki asallar.txt dosyası da aynı dizinde bulunmalıdır.




