#oktay saraçoğlu
def polynomial_adduction(degree,datalist):
    matrix=[]
    x=0
  
    for y in range(degree+1):
        A=[]
        for t in range(degree+1):
            total=0
            for r in range(x,len(datalist)+1):
                total += r**x
            A.append(total)
            x += 1
        matrix.append(A)
        x -=degree


    reducedMatrix=[]
    for y in range(degree+1):
        total=0
        for t in range(len(datalist)):
            total += datalist[t]*(t+1)**y
        reducedMatrix.append(total)
    for y in range(degree+1):
        lower=matrix[y][y]
        for t in range(y+1,degree+1):
            multiplier=lower/matrix[t][y]
            reducedMatrix[t]=reducedMatrix[j]*multiplier-reducedMatrix[y]
            for x in range(degree+1):
                matrix[t][x] = matrix[t][x]*multiplier-matrix[y][x]
    for y in range(degree,-1,-1):
        upper = matrix[y][y]
        for t in range(y-1,-1,-1):
            multiplier=upper/matrix[t][y]
            reducedMatrix[t] = reducedMatrix[t]*multiplier-reducedMatrix[y]
            for x in range(degree+1):
                matrix[t][x]= matrix[t][x]*multiplier-matrix[y][x]

    for y in range(degree+1):
        reducedMatrix[y]=reducedMatrix[y]/matrix[y][y]
    return reducedMatrix


def correlationCalculate(datalist,matrix):
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



def bpolynomial():
    polynomialList=[firstdegreepol,seconddegreepol,thirddegreepol,fourthdegreepol,fifthdegreepol,sixthdegreepol]
    correlationList=[firstdegreecorrelation,seconddegreecorrelation,thirddercorrelation,fourthdegreecorrelation,fifthdegreecorrelation,sixthdegreecorrelation]
    r,p=0,0
    
    for i in range(len(correlationList)):
        if(correlationList[i]>r):
            r=correlationList[i]
            p=polynomialList[i]
    return p


def total(best,value):
    total=0
    for i in range(len(best)):
        total+=best[i]*(value**i)
    return total



def polynomialsIntegral():
    best=bestPolynomial()
    lowerValue=3
    upperValue=len(datalist)
    g=1
    integral=0
    limitvalue=int((upperValue-lowerValue)/g)
    for i in range(1,limitvalue):
        integral+=total(best,lowerValue+i*g)
    result=(g/2)*(total(best,lowerValue)+total(best,upperValue)+2*integral)
    return result

def nonpolynomialDataIntegral(data):
    lowerValue=3
    upperValue=len(data)
    g=1
    result=0
    limitvalue=int((upperValue-lowerValue)/g)
    for i in range(1,limitvalue):
        result+= g*(data[lowerValue]+data[lowerValue+x])/2
        lowerValue+=g
    return result


#data = open("data.txt","r",encoding='utf-8')
#datalist = data.readlines()
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
    appropriate=bcorrelation(firstdegreecorrelation,seconddegreecorrelation,thirddercorrelation,fourthdegreecorrelation,fifthdegreecorrelation,sixthdegreecorrelation)
    data.close()



    polynomials=polynomialsIntegral()
    datas=nonpolynomialDataIntegral(datalist)
    print("Polinom olan integral cevabı : ",polynomials)
    print("Polinom olmayan integral cevabı : ",datas)

    comment=open("160401083_comment.txt","w",encoding='utf-8')
    comment.write("Delta x değeri yamukların en değeridir.Delta x küçüldükçe alanı daha fazla yamuğa ayırırız ve hata payımız düşer.\n")
    comment.write("Polinom olmayan integralde  asıl polinomun altında kalan alanı yamuklara ayırarak yamukların alanlarını toplarız.\n")
    comment.write("polinom olmayan integralde asıl polinomu parçalara ayırarak her parçanın alanını bulmuş oluruz.\n")
    comment.write("Polinom her ne kadar doğrusal olmasa da çembere bile yeterince küçük ölçekte baktığımızda düz gibi olur.Polinomda ")
    comment.write("ölçeği yani delta x değerini küçülterek doğrusala daha yakınmış gibi görür ve buna göre hesap yaparız bu da hata payımızı küçültür.\n")
    comment.write("Aradaki fark da buradan gelmektedir.Polinomlu integralde gerçek polinoma yakın bir polinomun alanını bulurken \n ")
    comment.write("Polinom olan integral kullanarak yapılan alan hesabı  gerçek polinoma yaklaştırdığımızda polinomun alan hesabını yapmış oluruz.\n")
    comment.close()

