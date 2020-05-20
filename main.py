#  Ad Soyad: Emre Ekinci  No: 180401041

#import numpy.matlib  #Matrislerde kullanılabilir
from matrix_operations import matrix_transpose      # gerekli matris işlemleri için fonksiyonların dahil edilmesi.
                                                    # D=A^T --> D= np.transpose(A) --> transpose kullanımı 
from matrix_operations import matrix_multiplication # C=AxB(AB=C) --> C=np.dot(A,B) --> matrislerde çarpma işlemi
from matrix_operations import matrix_inverse        # D=A^-1 --> D= np.linalg.inv --> matrisin tersinin alınması için..
from copy import copy                #ilk veriyi kaybetmeden kopyası üzerinde işlem yapmak için kullanılır..

from __init__ import __data_file__   #veri girişi için kullandım , init=initialization(başlatma) ile daha kolay bir görünüm elde ettik..
from __init__ import __output_file__ #veri çıkışı için kullandım

import numpy as np    # numpy artık np değişkeniyle ifade ediliyor..
import sys #dir(sys)   sys.argv komutu, programın ismi ile birlikte, bu programa parametre olarak verilen değerleri de bir liste halinde saklıyor.                       
import os  #gerek yok silinebilir        

# import sys sayesinde %d,%s gibi C diline ait göstergelerle sayısal ifadelerimiz daha da kolaylaştı

'''
sys kullanımı ....--> en aşağıda arguments=sys.argv..
    
    def çık():
    print('Çıkılıyor...')
    sys.exit()   # programı kapanmaya zorlamak için kullanılabilir.

if len(sys.argv) < 2: #eğer parametre veya verilerde istenilenden fazlası veya azı varsa kullanılabilir
    print('Gerekli parametreleri girmediniz!') 
    çık()

elif len(sys.argv) > 2: #sys.argv kullandığım parametreleri liste halinde tutar
    print('Çok fazla parametre girdiniz!')
    çık()

elif sys.argv[1] in ['-v', '-V']:
    print('Program sürümü: 0.8')

else:
    mesaj = 'Girdiğiniz parametre ({}) anlaşılamadı!'
    print(mesaj.format(sys.argv[1]))
    çık()
---> BU ŞEKİLDE YETERLİ DEĞİL DETAYLANMASI LAZIM..
'''

'''
class BColors:
    ENDC      = '\033[0m'-->kullanılır
    BOLD      = '\033[1m'-->??
    UNDERLINE = '\033[4m'-->??
    INACTIVE  = '\033[90m'
    FAIL      = '\033[91m'-->kullanılır
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'-->kullanılır
    OKBLUE    = '\033[94m'
    HEADER    = '\033[95m'
    COMMENT   = '\033[96m'
    BLOCK     = '\033[97m'
    CODE      = '\033[98m'

'''

class term_renkleri:
    
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    #BOLD = '\033[1m'
    #UNDERLINE = '\033[4m'
    #COMMENT   = '\033[96m'





class process:#süreç
    def __init__(self, veri_içerik: list):  # init yapıcı(constructor) fonksiyondur , self parametresi zorunludur.
        """
        Bu sınıf tüm ana işlemleri yürütür
        : param veri_içerik: Bir veri listesi
        """
        self.veri_ = veri_içerik
        self.first_var = 0                      #ilk varyasyon = 0 , başlangıc
        self.last_var = len(self.veri_)         #son varyasyon =len(self.veri)
        self.grade_regression_result = None     # regresyon iki ya da daha fazla değişken arasındaki değişimleri ölçmeye yarar.(Grafikler ile görselleşmesi sonucunda da anlaşılırlığı yükselir.)
        self.results = list()                   #sonuçları listeye atacağız aşağıdaki işlemlerle 
        self.error_results = list()             #hata sonuçları için yine bir boş liste kullanımı yapıldı.(for error results..) 
        
    def set_data_range(self, first=0, last=0, all_=False):
        """
        Regresyon için veri aralığını ayarlama
        : param first: Verilerin ilk dizini
        : param last: Son dizin veri verileri
        : param all_: Tüm verileri seç
        : dönüş: Yok(None)
        """
        if all_:#if dene
            self.first_var = 0
            self.last_var = len(self.veri_)
        else:
            self.first_var = first #ilk varyasyon ilk son v.. son
            self.last_var = last

        print(
            term_renkleri.WARNING + "Veri aralığının %d dan %d a kadar ayarlanması!" % (self.first_var, self.last_var) + term_renkleri.ENDC)
        # veri aralığının 0 dan 59 a ayarlaması gibi
    def regression_for_grade(self, derece=0, no_print=False):#sınıf için regresyon
        # çözüme(solution) ulaşmam için :
        # X * çözümler = Y
        # çözümler = (X_t * X)^-1 * X_t * Y
        solution_matrix = np.zeros(shape=(derece + 1, 1), dtype=float)#çözelti matrix
        x_matrix = np.zeros(shape=((self.last_var - self.first_var), derece + 1), dtype=float)
        y_matrix = np.zeros(shape=((self.last_var - self.first_var), 1), dtype=float)

        # Prepair matrixs  matris hazırlanışı
        y_index = 0
        for i in range(0, (self.last_var - self.first_var)):
            for j in range(0, x_matrix.shape[1]):
                x_matrix[i][j] = pow(float(self.veri_[i + self.first_var]), j)
            y_matrix[i][0] = float(y_index)
            y_index += 1

        x_trans_matrix = matrix_transpose(x_matrix) #transpozunun alınması
        multi_matrix = matrix_multiplication(x_trans_matrix, x_matrix)#matris ile transpozunun alınması tersini alma işlemi
        inversed_matrix = matrix_inverse(multi_matrix)#matrisin tersinin alınması
        
        multi_two_matrix = matrix_multiplication(x_trans_matrix, y_matrix)
        
        multi_three_matrix = matrix_multiplication(inversed_matrix, multi_two_matrix)
        solution_matrix = multi_three_matrix
        self.grade_regression_result = copy(solution_matrix)
        self.results.append(self.grade_regression_result) #regresyon sonuçları listemize atıldı.. 1

        to_printed = ""
        to_printed += str(derece) + ". derece regresyon sonuçlarım : \n"
        to_printed += str(self.grade_regression_result[0])
        for i in range(1, derece + 1):
            to_printed += " + " + str(self.grade_regression_result[i]) + "X"
            to_printed += "^^" + str(i)
        to_printed += " = Y"
        if not no_print:
            print(to_printed)

    def calculate_most_usefull(self):  #en yararlı olanı hesapla
        for i in range(len(self.results)):
            avarage = 0.0
            y_index = 0
            for x_data in self.veri_:
                X = float(x_data)
                Y = y_index
                y_index += 1

                total = 0.0
                for j in self.results[i]:
                    total += float(j) * pow(X, j)
                E = total - Y
                avarage += E
            avarage /= len(self.veri_)
            self.error_results.append(avarage)

        for i in range(len(self.error_results)):
            if self.error_results[i] < 0:
                self.error_results[i] *= -1

        the_lowest_error = self.error_results[0]
        the_lowest_error_index = 0
        for i in range(len(self.error_results)):
            if self.error_results[i] < the_lowest_error:
                the_lowest_error = self.error_results[i]
                the_lowest_error_index = i

        print("Polinom bölgesindeki en düşük hata (aralıklar karşılaştırıldı): %d .derece regresyon ile E=%s"
              % ((the_lowest_error_index + 1), the_lowest_error))

    def veri_uzunluk(self): #verileri almak için fonksiyon
        return len(self.veri_)

    def kill_vars(self): #ölüm varyasyonu
        self.grade_regression_result = None
        self.results = list()
        self.error_results = list()

    def write_to_file(self, the_dir): #dosyaya yazma işlemi
        with open(the_dir + "/%s" % __output_file__, "w") as fh:
            to_printed = ""
            for i in range(len(self.results)):
                to_printed += str(i + 1) + " Reggression\t"
                for j in range(len(self.results[i])):
                    to_printed += str(self.results[i][j]) + "X^^" + str(j) + "\t"
                to_printed += "\n"
            fh.write(to_printed)
        print(term_renkleri.WARNING + "%s file generated!" % __output_file__ + term_renkleri.ENDC)


def main():
   
    if arguman: # argüman(args)=sys.argv ataması ile ana  listede parametre tutmayı tercih ettim.
        print(term_renkleri.WARNING + "Argüman işleyici yok!" + term_renkleri.ENDC)

    # Aslında buna gerek yok ,çünkü dosyam zaten var
    yeni_veri = None
    working_directory = os.getcwd()
    try: #try exception yapısı bak, hata mesajı vermek için
        with open(working_directory + "/%s" % __data_file__, "r") as fh:
            string_format = fh.read()
            a = string_format.splitlines()
            # If last line of file is not /n  son dosya satırı değilse
            for i in range(len(a)):
                if a[i] == "":
                    a.pop(len(a)-1)
            yeni_veri = copy(a)  #copy ile ana liste elemanları korundu..
    except FileNotFoundError:  #dosya bulunamadı hatası buna da gerek yok aslında
        raise Exception("Dosya bulunamadı! %s file" % __data_file__)

    if not yeni_veri: #dosya var ama veri yoksa verilecek mesaj
        raise Exception("Dosya bulundu ancak okuma başarısız oldu. ")
    print(term_renkleri.WARNING + "Dosya açıldı ve başarıyla okundu" + term_renkleri.ENDC)
#başarılı dosyaaçılması ve veriokunması durumu 

    print(term_renkleri.WARNING + "İlk soru başlangıç:" + term_renkleri.ENDC)
   
    new_process = process(yeni_veri)
    
    new_process.set_data_range(all_=True)
   
    new_process.regression_for_grade(derece=1)
    new_process.regression_for_grade(derece=2)
    new_process.regression_for_grade(derece=3)
    new_process.regression_for_grade(derece=4)
    new_process.regression_for_grade(derece=5)
    new_process.regression_for_grade(derece=6)
    #new_process.regressionn_for_grade(grade=7)
    new_process.write_to_file(working_directory)

    print(term_renkleri.WARNING + "İLK SORUNUN BAŞARIYLA SONLANMASI. \t" + term_renkleri.ENDC)#ilk soru bitti ikinci soru işleniyor
    print(term_renkleri.WARNING + "Burası ikincinin başlangıc noktası:" + term_renkleri.ENDC)
    new_process.calculate_most_usefull()

    print(term_renkleri.WARNING + "İKİNCİ SORUNUN BAŞARILA SONLANMASI. \t" + term_renkleri.ENDC)#ikinci soru bitti üçüncü soru işleniyor
    print(term_renkleri.WARNING + "Burası üçüncünün başlangıç noktası :" + term_renkleri.ENDC)
    print(term_renkleri.FAIL + "Taşma durumuna dikkat edilmeli !!" + term_renkleri.ENDC)# taşmaya dikkat et
    for i in range(int(new_process.veri_uzunluk() / 10) + 1):
        first = i * 10
        last = i * 10 + 10  #last > first
        if i >= int(new_process.veri_uzunluk() / 10):
            last = new_process.veri_uzunluk()

        new_process.kill_vars()
       
        new_process.set_data_range(first, last)# ilk ,son karşılaştırma için olabilir??
       
        new_process.regression_for_grade(derece=1, no_print=True)
        new_process.regression_for_grade(derece=2, no_print=True)
        new_process.regression_for_grade(derece=3, no_print=True)
        new_process.regression_for_grade(derece=4, no_print=True)
        new_process.regression_for_grade(derece=5, no_print=True)
        new_process.regression_for_grade(derece=6, no_print=True)
        new_process.calculate_most_usefull()


if __name__ == '__main__':
    arguman = sys.argv[1:]
    main()
    
