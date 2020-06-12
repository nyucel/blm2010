
def fonk(p,x):
    toplam=0
    for i in range(len(p)):
        toplam += p[i]*(x**i)
    return toplam



def yamuk_kullanilarak(p,a,b):
    delta_x = 1
    n= int((b-a)/delta_x)
    toplam=0
    for i in range(1,n):
        toplam += fonk(p,a+i*delta_x)
    I=(delta_x/2)*(fonk(p,a)+fonk(p,b)+2*toplam)
    print("Polinom kullanilip yapilan integralin sonucu : ", I)




def veriler_txt_ile(veriler,a,b):
    h=1
    y0=veriler[a-1]
    while(a<b):
        y0 = y0 + (veriler[a-1]+veriler[a+h-1])*h/2
        a += h
    print("Polinom kullanilmadan yapilan integralin sonucu : " ,y0)





def en_iyi_polinımu_bulma(p,r):
    r_deg_eniyi=0
    eni_pol=0
    for i in range(len(r)):
        if (r[i]>r_deg_eniyi):
            r_deg_eniyi=r[i]
            eni_pol=p[i]
    return eni_pol

def interpolasyon(derece,veriler):
    matris=[]
    l=0

    for i in range(derece+1):
        satir=[]
        for j in range(derece+1):
            toplam=0
            for k in range(1,len(veriler)+1):
                toplam += k**l
            satir.append(toplam)
            l += 1
        matris.append(satir)
        l -=derece


    cevap=[]
    for i in range(derece+1):
        toplam=0
        for j in range(len(veriler)):
            toplam += veriler[j]*(j+1)**i
        cevap.append(toplam)

    for i in range(derece+1):
        benzetme=matris[i][i]
        for j in range(i+1,derece+1):
            oran=benzetme/matris[j][i]
            cevap[j]=cevap[j]*oran-cevap[i]
            for k in range(derece+1):
                matris[j][k] = matris[j][k]*oran-matris[i][k]
   
    for i in range(derece,-1,-1):
        benzetme = matris[i][i]
        for j in range(i-1,-1,-1):
            oran=benzetme/matris[j][i]
            cevap[j] = cevap[j]*oran-cevap[i]
            for k in range(derece+1):
                matris[j][k]= matris[j][k]*oran-matris[i][k]

    for i in range(derece+1):
        cevap[i]=cevap[i]/matris[i][i]
    y_ort=0
    for i in range (len(veriler)):
        y_ort += veriler[i]
    y_ort = y_ort/len(veriler)
    ST,SR=0,0

    for i in range(len(veriler)):
        x =veriler[i]
        ST +=(veriler[i]-y_ort)**2
        for j in range(len(cevap)):
            x -= cevap[j]*(i+1)**j
        x=x**2
        SR += x
    r=((ST-SR)/ST)**(1/2)
    return cevap,r

dosya = open ("veriler.txt", "r")
veriler = dosya.readlines()
for i in range(len(veriler)):
    veriler[i]=int(veriler[i])

a=3
b=len(veriler)



pol1,r1=interpolasyon(1,veriler)
pol2,r2=interpolasyon(2,veriler)
pol3,r3=interpolasyon(3,veriler)
pol4,r4=interpolasyon(4,veriler)
pol5,r5=interpolasyon(5,veriler)
pol6,r6=interpolasyon(6,veriler)

dosya.close()
r=[r1,r2,r3,r4,r5,r6]
p=[pol1,pol2,pol3,pol4,pol5,pol6]



eni_pol=en_iyi_polinımu_bulma(p,r)

yamuk_kullanilarak(eni_pol,a,b)


veriler_txt_ile(veriler,a,b)

def yorum(dosya):
    dosya.write("\n HALİL HİLMİ NAMLI 180401053 \n"
    "İki yöntemde tam olarak aynı sonucu vermeyecektir.\n"
    "Yamuk yönteminde ne kadar küçük deltaX alırsak o kadar gerçeğe yakın değer alabiliriz.\n"
    "Fakat biz 2 değeri kıyaslamak için aynı yani deltaX'i 1 alıyoruz.\n"
    "Kullandığımız polinom ise  orjinal polinom olmayıp yakın bir polinomdur. \n "
    "Ve Bu polinomda korelasyon kullandığımız için 1 e ne kadar yakın olursa o kadar iyi sonuç verir.\n")
    


yorumdosyasi = open("180401053_yorum.txt","w")
yorum(yorumdosyasi)
yorumdosyasi.close()