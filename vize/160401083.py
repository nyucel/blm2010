#Oktay saraçoğlu-160401083


def polynomial_adduction(degree,datalist):
    
   x=0
  matrix=[]
   

    for y in range(degree+1):
        A=[]
        for t in range(degree+1):
            total=0
            for r in range(x,len(datalist)+1):
                total += r**x
            A.append(total)
            x += 1
        matris.append(A)
        x -=degree



  reducedMatrix=[]
    for y in range(degree+1):
        total=0
        for t in range(len(datalist)):
            total += datalist[t]*(t+1)**y
        reducedMatris.append(total)
    for y in range(degree+1):
        lower=matrix[y][y]
        for t in range(y+1,degree+1):
            multiplier=lower/matrix[t][y]
            reducedMatrix[t]=reducedMatrix[j]*multiplier-reducedMatrix[y]
            for x in range(degree+1):
                matrix[t][x] = matrix[t][x]*multiplier-matrix[y][x]
    for y in range(degree,-1,-1):
        upper = matris[y][y]
        for t in range(y-1,-1,-1):
            multiplier=upper/matrix[t][y]
            reducedMatrix[t] = reducedMatrix[t]*multiplier-reducedMatrix[y]
            for x in range(degree+1):
                matrix[t][x]= matrix[t][x]*multiplier-matrix[y][x]

    for y in range(degree+1):
        reducedMatrix[y]=reducedMatrix[y]/matrix[y][y]
    return reducedMatrix


defcorrelationCalculate(datalist,matrix):
    b=0
    c=len(datalist)
    for i in range (c):
        b += datalist[y]
    b = b/c
    R_t=0
    R_r=0
    for i in range(c):
        c =datalist[y]
        R_t +=(datalist[y]-b)**2
        for t in range(len(matrix)):
            c -= matrix[j]*(t+1)**t
        c=c**2
        R_r += c
    
correlation=((R_t-R_r)/R_t)**(1/2)
    return correlation

def bcorrelation(a1,a2,a3,a4,a5,a6):
    b=0
    correlationlist=[a1,a2,a3,a4,a5,a6]
    for y in correlationlist:
        if(y>b):
            b=y
    return b

data = open("data.txt","r",encoding='utf-8')
datalist = data.readlines()
for y in range(len(datalist)):
    datalist[y]=int(datalist[y])

firstdegreepol=polynomial_closer(1,datalist)
seconddegreepol=polynomial_closer(2,datalist)
thirddegreepol=polynomial_closer(3,datalist)
fourthdegreepol=polynomial_closer(4,datalist)
fifthdegreepol=polynomial_closer(5,datalist)
sixthdegreepol=polynomial_closer(6,datalist)
firstdegreecorrelation=correlationCalculate(datalist,firstdegreepol)
seconddegreecorrelation=correlationCalculate(datalist,seconddegreepol)
thirddegreecorrelation=correlationCalculate(datalist,thirddegreepol)
fourthdegreecorrelation=correlationCalculate(datalist,fourthdegreepol)
fifthdegreecorrelation=correlationCalculate(datalist,fifthdegreepol)
sixthdegreecorrelation=correlationCalculate(datalist,sixthdegreepol)
appropriate=bestcorrelation(firstdegreecorrelation,seconddegreecorrelation,thirddercorrelation,fourthdegreecorrelation,fifthdegreecorrelation,sixthdegreecorrelation)
data.close()
results=open("result.txt","w",encoding='utf-8')
results.write("Birinci.dereceden polinoma yaklaştırıyoruz : " +str(firstdegreepol[1])+"x + "+str(firstdegreepol[0])+"  Kolerasyon = "+ str(firstdegreecorrelation) + "\n")
results.write("İkinci.dereceden polinoma yaklaştırıyoruz : " +str(seconddegreepol[2])+"x^2 + "+str(seconddegreepol[1])+"x + "+str(seconddegreepol[0])+"  Kolerasyon = " + str(seconddegreecorrelation)+"\n")
results.write("Üçüncü.dereceden polinoma yaklaştırıyoruz : " +str(thirddegreerpol[3])+"x^3 + "+str(thirddegreepol[2])+"x^2 + "+str(thirddegreepol[1])+"x + "+str(thirddegreepol[0])+"  Kolerasyon = " + str(thirddegreecorrelation)+"\n")
results.write("Dördüncü.dereceden polinoma yaklaştırıyoruz : " +str(fourthdegreepol[4])+"x^4 + " +str(fourthdegreepol[3])+"x^3 + "+str(fourthdegreepol[2])+"x^2 + " +str(dfourthdegreepol[1])+"x + " +str(fourthdegreepol[0])+"  Kolerasyon = " + str(fourthdegreecorrelation)+"\n")
results.write("Beşinci.dereceden polinoma yaklaştırıyoruz : " +str(fifthdegreepol[5])+"x^5 + "+str(fifthdegreepol[4])+"x^4 + " +str(fifthdegreepol[3])+"x^3 + " +str(fifthdegreepol[2])+"x^2 + " +str(fifthdegreepol[1])+"x + " +str(fifthdegreepol[0])+"  Kolerasyon = " + str(fifthdegreecorrelation)+"\n")
results.write("Altıncı.dereceden polinoma yaklaştırıyoruz : " +str(sixthdegreepol[6])+"x^6 + "+str(sixthdegreepol[5])+"x^5 + "+str(sixthdegreepol[4])+"x^4 + " +str(sixthdegreepol[3])+"x^3 + " +str(sixthdegreepol[2])+"x^2 + " +str(sixthdegreepol[1])+"x + " +str(sixthdegreepol[0])+"  Kolerasyon = " + str(sixthdegreecorrelation)+"\n")
results.write("Muhtemel polinom kolerasyonu Birinci'ye en yakın olan ALtıncı.kolerasyon.Kolerasyon değeri = "+ str(appropriate))
result.close()
