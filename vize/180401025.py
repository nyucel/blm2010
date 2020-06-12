# Kutay KALMAZ     180401025

def  getCoefficients(p1, p2, p3, p4, p5, p6, polyCoefficients):
     polyCoefficients.write("1.degree polynomial : a0 = "+str(p1[0]) + " a1 = " + str(p1[1])+"\n" )
     polyCoefficients.write("2.degree polynomial : a0 = "+str(p2[0]) + " a1 = " + str(p2[1]) + " a2 =" + str(p2[2]) + "\n")
     polyCoefficients.write("3.degree polynomial : a0 = "+str(p3[0]) + " a1 = " + str(p3[1]) + " a2 =" + str(p3[2]) + " a3 = " + str(p3[3]) + "\n")
     polyCoefficients.write("4.degree polynomial : a0 = "+str(p4[0]) + " a1 = " + str(p4[1]) + " a2 =" + str(p4[2]) + " a3 = " + str(p4[3]) + " a4 = " + str(p4[4]) + "\n")
     polyCoefficients.write("5.degree polynomial : a0 = "+str(p5[0]) + " a1 = " + str(p5[1]) + " a2 =" + str(p5[2]) + " a3 = " + str(p5[3]) + " a4 = " + str(p5[4]) + " a5 = "+ str(p5[5])+ "\n")
     polyCoefficients.write("6.degree polynomial : a0 = "+str(p6[0]) + " a1 = " + str(p6[1]) + " a2 =" + str(p6[2]) + " a3 = " + str(p6[3]) + " a4 = " + str(p6[4]) + " a5 = "+ str(p6[5])+" a6 = "+str(p6[6])+ "\n")

def eligiblePoly(ks1, ks2, ks3, ks4, ks5, ks6,file):
     file.write( "  1.degree polynomial coefficient: "+str(ks1) +
                 "\n2.degree polynomial coefficient: "+str(ks2) +
                 "\n3.degree polynomial coefficient: "+str(ks3) +
                 "\n4.degree polynomial coefficient: "+str(ks4) +
                 "\n5.degree polynomial coefficient: "+str(ks5) +
                 "\n6.degree polynomial coefficient: "+str(ks6)+"\n")
        
     coefficients = [ks1, ks2, ks3, ks4, ks5, ks6]
     b = max(coefficients)
     for i in range(len(coefficients)):
         if b == coefficients[i]:
             file.write("En uygun polinom "+str(i+1)+". degree polinomdur.\n")



def polyInterpolation(degree,data):
    matrix = []
    base = 0

    for i in range(degree+1):
        line = []
        for j in range(degree+1):
            sonuc = 0
            for k in range(1, len(data)+1):
                sonuc += k**base
            line.append(sonuc)
            base += 1
        matrix.append(line)
        base -= degree

    results1 = []
    for i in range(degree+1):
        sonuc = 0
        for j in range(len(data)):
            sonuc += data[j]*(j+1)**i
        results1.append(sonuc)

    for i in range(degree+1):  
        comp = matrix[i][i]
        for j in range(i+1, degree+1):
            eps = comp/matrix[j][i]
            results1[j] = results1[j]*eps-results1[i]
            for k in range(degree+1):
                matrix[j][k] = matrix[j][k]*eps-matrix[i][k]

    for i in range(degree, -1, -1):  
        comp = matrix[i][i]
        for j in range(i-1, -1, -1):
            eps = comp/matrix[j][i]
            results1[j] = results1[j]*eps-results1[i]
            for k in range(degree+1):
                matrix[j][k] = matrix[j][k]*eps-matrix[i][k]

    for i in range(degree+1): 
        results1[i] = results1[i]/matrix[i][i]

    sumY = 0
    for i in range(len(data)):
        sumY += data[i]
    avg = sumY/len(data)

    sumT, sumR = 0, 0
    for i in range(len(data)):
        q = data[i]
        sumT += (data[i]-avg)**2
        for j in range(len(results1)):
            q -= results1[j]*(i+1)**j
        q = q**2
        sumR += q
    correlation = ((sumT-sumR)/sumT)**(1/2)
    return results1, correlation


datas = open("veriler.txt", "r")
 vaka = datas.readlines()
 for i in range(len(vaka)):
     vaka[i] = int(vaka[i])
 pol, hata = [0] * 6, [0] * 6
 for j in range(0,6):
     pol[j], hata[j] = polyInterpolation(j+1,vaka)
 datas.close()


 results= open("sonuc.txt", "w")
 results.write("all datas\n")
 getCoefficients(pol[0], pol[1], pol[2], pol[3], pol[4], pol[5], results)
 eligiblePoly(hata[0], hata[1], hata[2], hata[3], hata[4], hata[5],results)
 for a in range(len(vaka) - 9):
     results.write("\n10 sets of data ("+str(a+1)+","+str(a+10)+")")
     list1= vaka[a:a+10]
     for i in range(6):
         pol[i],hata[i] = polyInterpolation(i+1, list1)
     getCoefficients(pol[0], pol[1], pol[2], pol[3], pol[4], pol[5], results)
     eligiblePoly(hata[0], hata[1], hata[2], hata[3], hata[4], hata[5],results)
 results.close()

