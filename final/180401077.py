#Ercan Berber 180401077

def poly(arrx,arry,deg):
    n=len(arrx)
    karem=[]
    sonucm=[]
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
    Imatrix=[]
    for i in range(len(matrix)):
        Imatrix.append([])
        for j in range(len(matrix)):
            if(i==j):
                Imatrix[i].append(1)
            else:
                Imatrix[i].append(0)
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
    for i in range(len(matrix)-1,-1,-1):
        for j in range(i-1,-1,-1):
            carpan=matrix[j][i]/matrix[i][i]
            for k in range(len(matrix)):
                matrix[j][k]-=carpan*matrix[i][k]
                Imatrix[j][k]-=carpan*Imatrix[i][k]
    return Imatrix

def matriscarp(a,b): 
    result=[]
    for i in range(len(a)):
        for j in range(len(b[0])):
            t=0
            for k in range(len(b)):
                t+=a[i][k]*b[k][j]
            result.append(t) 
    return result

def listeYap(n):
    x=[i+1 for i in range(n)]
    return x

def korelasyon(x,liste,n,yToplam):
    t1 = 0
    t2 = 0
    y = yToplam/n
    s = len(x)

    for i in range(n):
        temp = 0
        for j in range(s):
            if j == 0:
                temp += x[j]
            else:
                temp += x[j]*(i+1)**j
        t1 +=(int(liste[i])-temp)**2
        t2 +=(int(liste[i])-y)**2
    kor = ((t2-t1)/t2)**(1/2)

    return kor

def fonk(y,deger):
    sonuc=0
    for i in range(len(deger)):
        sonuc+=deger[i]*((y+1)**i)
    return sonuc
    


def main():
    with open('veriler.txt','r') as f:
        y= f.read().split('\n')
    if y[-1]=='':y.pop()
    x=listeYap(len(y))
    ytoplam=sum([int(i) for i in y])
    Korelasyonlar=[]
    polynoms=[]
    for i in range(6):
        polynoms.append(poly(x,y,i+1))
        Korelasyonlar.append(korelasyon(polynoms[i],y,len(y),ytoplam))
    v,index= max((v,i) for i,v in enumerate(Korelasyonlar)) #En düşük hatalı olanın indexini aldık
    
    
    a=7 # 180401077
    b=len(y)
    deltax=0.5 #0.0001 yapınca integral binde bir oynuyor, o yüzden programı yavaşlatmaya gerek yok diye düşündüm.
    integral=0
    n=int((b-a)/deltax)
    for i in range(n):
        integral+= deltax*(fonk(a,polynoms[index])+fonk(a+deltax,polynoms[index]))/2
        a+=deltax
    print(f"En iyi polinomun integrali..:{integral}")
    


    a=7
    integralv=0
    deltax=1
    n=int((b-a)/deltax)
    for i in range(n-1):
        integralv+=deltax*(int(y[a])+int(y[a+deltax]))/2
        a+=deltax
    print(f"Polinomsuz integral..:{integralv}")


if __name__=="__main__":
    main()
    f=open("180401077_yorum.txt","w")
    f.write("Ercan Berber 180401077 \n\n1. Polinom ile buldugumuz degerin hata payi daya dusuktur. Cünkü hesaplarken deltax degeri ile hesapladigimiz dikdörtgen sayisini arttiririz. \n2. Gercek degerleri hesaplarken deltaxi 1 aliriz. Bundan dolayi dikdörtgen sayimiz azalir ve integralin hata payi artar. \n3. Polinom ile buldugumuz degerler ile gercek degerler arasindaki fark.")
    f.close()