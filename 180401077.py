# Ercan Berber 180401077

import decimal
def poly(arrx,arry,deg):
    #formülü aldığım kaynak
    #https://www.youtube.com/watch?v=i83Pb7GkfbM
    #polinomun derecesine göre kare matris oluşturuyor
    n=len(arrx)
    karem=[] #Kare Matris
    sonucm=[] #Sonuc Matrisi
    for x in range(deg+1):
        karem.append([])
        for y in range(deg+1):
            if(x==0 and y==0):
                karem[x].append(n)
            else:
                c=0
                for i in arrx:
                    c+=i**(x+y)
                karem[x].append(c)
        a=0
        for i in range(len(arrx)):
            a+=(arrx[i]**x)*float(arry[i])
        sonucm.append([a])
    tersinir=inversematrix(karem)
    deger=matriscarp(tersinir,sonucm)
    return deger

def inversematrix(matrix):
    Imatrix=[] #Birim Matris
    for i in range(len(matrix)): #Matris ile boyutu aynı birim matris oluşturma
        Imatrix.append([])
        for j in range(len(matrix)):
            if(i==j):
                Imatrix[i].append(1)
            else:
                Imatrix[i].append(0)
    #Matrisi satır işlemleri yaparak üst üçgen matrise çeviriyoruz.
    #Yapılan işlemlerin aynısı birim matrise de uygulanıyor
    for i in range(len(matrix)):
        bölen=matrix[i][i]
        for j in range(len(matrix)):
            matrix[i][j]=matrix[i][j]/bölen
            Imatrix[i][j]=Imatrix[i][j]/bölen
        for k,z in zip(matrix[i+1:],Imatrix[i+1:]):
            carpan=k[i]
            for m in range(len(k)):
                k[m]=k[m]-matrix[i][m]*carpan
                z[m]=z[m]-Imatrix[i][m]*carpan  
    #Üst üçgen matrisimizi, birim matrise çeviriyoruz
    #Aynı işlemleri birim matrise de uygulayınca elimizde matrisin tersi kalıyor.
    for i in range(len(matrix)-1,-1,-1):
        for j in range(i-1,-1,-1):
            carpan=matrix[j][i]/matrix[i][i]
            for k in range(len(matrix)):
                matrix[j][k]-=carpan*matrix[i][k]
                Imatrix[j][k]-=carpan*Imatrix[i][k]
    return Imatrix #Matrisin Tersi

#Geçen yıl programlama labaratuvarında yazdığım kodu editledim.
#Doğru çalışıyor ama matris olarak değil sıralı liste olarak yolluyor.
def matriscarp(a,b): 
    result=[]
    for i in range(len(a)):
        for j in range(len(b[0])):
            t=0
            for k in range(len(b)):
                t+=a[i][k]*b[k][j]
            result.append(t) 
    return result

def sonucuret(liste,deger):
    sonuclar=[]
    for y in range(len(liste)):
        sonuc=0
        for i in range(len(deger)):
            sonuc+=deger[i]*((y+1)**i)
        sonuclar.append(round(sonuc,3))
    return sonuclar

def listeYap(n): #n boyutunda sıralı dizi oluşturur.
    x=[i+1 for i in range(n)]
    return x

def hataOran(y): #Gelen listeyi 1., 2., 3., 4., 5. ve 6. dereceden polinoma yakınlaştırır. Hataları toplar listeye ekler.
    hataliste=[]
    for i in range(6):
        stahminihata=0
        liste=sonucuret(y,poly(listeYap(len(y)),y,i+1))
        for j in range(len(liste)):
            stahminihata+=round(abs(int(y[j])-liste[j]),3)
        hataliste.append(round(stahminihata,3))
    (m,i) = min((v,i) for i,v in enumerate(hataliste)) #listenin hem indexini hem indexdeki değerini döndürüyor.
    return(m,i)    

def main():
    print("\n----------------------------------------------------------------------------------\n")
    with open('veriler.txt', 'r') as f: #dosyayı diziye aktarma.
        y = f.read().split('\n') #veriler satır satır olduğu için ayırdım.
    if y[-1]=='':y.pop() #txt dosyasının son satırı boş ise son eleman da boş oluyor. Onu çıkarıyor.
    x=listeYap(len(y)) #y'nin boyutu kadar sıralı dizi.
    
    #Dosyaya katsayıları yazdık.
    f=open('sonuc.txt','w')
    f.write("Yazim biçimi 1.için a,bx       2.için a,bx,cx²     3.için a,bx,cx²,dx³ .... \n")
    f.close()
    for i in range(6):
        with open('sonuc.txt','a') as f:
            f.write(f"{i+1}..: {str(poly(x,y,i+1))}\n")
    
    (m,i)=hataOran(y)
    print(f"Verilerin tamamı için {i+1}. polinoma yakınlaştırma en uygun, hata sayısı = {m}")
    print("\n----------------------------------------------------------------------------------\n")
    for k in range((len(y)-9)):
        liste10=y[k:k+10]
        (m,i)=hataOran(liste10)
        print(f"({k+1},{k+10}) gün için {i+1}. polinoma yakınlaştırma en uygun, hata sayısı = {m}")

if __name__ == "__main__":
    main()