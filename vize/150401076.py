def verioku():
        f=open("veriler.txt")
        f.readline()
        j=0
        degerler={}
        for satır in f:
            degerler[j]=int(satır)
            j+=1
        f.close()
        return degerler

def polinomKatsayi(derece,veri):
        degerler=veri
        
        #xdegerlerinin üslü değerlerinin toplamını tutar
        #xpow[x0toplam,x1toplam,x2toplam,...,xm2toplam] verilerini tutar
        xpow=[]
        #ihtiyacımız olan en büyük x üssü 2*derece ye kadardır
        for i in range(0,(derece*2)+1):
            xpow.append(0)#diziye ilk değer ataması yapıldı
            for j in range(0,len(degerler)): #x degerleri içinde gezerek üslü değerler hesaplandı
                xpow[i]+=j**i

        #x**i*y degerlerini tutar
        #ytoplam,xytoplam,x2ytoplam,...,xmytoplam (derece+1 değere ihtiyaç vardır)
        xy=[]
        for i in range (0,derece+1):
            xy.append(0)
            for j in range(0,len(degerler)):
                  xy[i]+=j**i*degerler[j]
        matris=[]
        for i in range(derece+1):
            line=[]
            for j in range(0,derece+2):
                if(j>=derece+1):
                    line.append(xy[i])
                else:
                   line.append(xpow[i+j])
            matris.append(line)
    #veriler.txt dosyası okunur ve degerler dictionary nesnesine atanır. 
            boyut = len(matris)
        for i in range(derece+2):
            if(i<derece+1):
                s=matris[i][i]
                for j in range(derece+2):
                        matris[i][j]=matris[i][j]/s    
           # for j in range(derece+1):
            if(i==derece+1):
                break
            
            for j in range(derece+1):
                if(i!=j):
                    kat=matris[j][i]
                    for k in range(derece+2):
                        matris[j][k]=matris[i][k]*kat-matris[j][k]
        return matris

             

dosya=open("sonuc.txt","w")
veri=verioku()

#1.Soru
dosya.write("SORU 1\n\n")
for j in range(1,7):
        matris=polinomKatsayi(j,veri)
        satir=len(matris)
        sutun=len(matris[0])-1
        dosya.write(str(j)+".dereceden polinom katsayıları \n")
        for i in range(sutun):
                dosya.write("x"+str(i)+"= "+str(matris[i][satir])+"   ")
        dosya.write("\n\n")                

#3.Soru
dosya.write("SORU 3\n")
kalanSayiAdedi=(len(veri)%10)
kalanSayiIndis=len(veri)-kalanSayiAdedi
yeniVeri={}
k=0
for i in range(0,len(veri)+1):
        if(i!=0 and i%10==0):
                k=0
                dosya.write("\nVeri dizisi:\n"+str(yeniVeri)+"\n\n")               
                for j in range(1,7):
                        matris=polinomKatsayi(j,veri)
                        satir=len(matris)
                        sutun=len(matris[0])-1
                        dosya.write(str(j)+".dereceden polinom katsayıları \n")
                        for i in range(sutun):
                                dosya.write("x"+str(i)+"= "+str(matris[i][satir])+"   ")
                        dosya.write("\n\n")
                yeniVeri.clear()
        if(i<len(veri)):
                yeniVeri[k]=veri[i]
                k+=1

dosya.write("\nVeri dizisi:\n"+str(yeniVeri)+"\n\n")               
if(i>kalanSayiIndis and i<len(veri)-1):
        yeniVeri[k]=veri[i]
        for j in range(1,7):
                matris=polinomKatsayi(j,veri)
                satir=len(matris)
                sutun=len(matris[0])-1
                dosya.write(str(j)+".dereceden polinom katsayıları \n")
                for i in range(sutun):
                        dosya.write("x"+str(i)+"= "+str(matris[i][satir])+"   ")
                dosya.write("\n\n")                
dosya.close()

