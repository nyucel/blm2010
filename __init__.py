
#kolay kullanım için __all__
#veriler.txt dosyama yeni veriler son güne kadar eklendi. 
__all__ = ["main", "__version__", "__major__", "__minor__", "__string__", "__data_file__", "__output_file__"]

__version__ = "0.1"

__major__ = 0
__minor__ = 1

__string__ = "Emre-Ekinci-git-odev//18.05.2020"

__data_file__ = "veriler.txt"
__output_file__ = "sonuc.txt"

#__all__ değişkeni, import * tarafından yorumlandığı şekliyle bu modülün ortak nesnelerinin listesidir.
# Bu değişken, alt çizgiyle başlayan her şeyi ,gizleme varsayılanını geçersiz kılar.
