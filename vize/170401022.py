#Cihan Par 170401022
#Veriler, veriler.txt uzantılı dosyadan alınmıştır. 1., 2., 3., 4., 5., 6. dereceden polinomlar oluşturulmuştur. 
#Bu polinomların katsayıları B matrisine yazılır ise temelde A*B=C matrisi olmak üzere C matrisindeki elemalar sonuç verileri olmuş ve A matrisi
#Vandermonde matrisi özelliklerini göstermektedir. Katsayılar matrisini hesaplamak için inverse(transpose(A)*A)*transpose(A)*C işlemi uygulanmıştır.
#Hata hesaplanırken mean absolute error (MAE) methodu uygulanmıştır. Hatası en düşük hesaplanan derecedeki 
#polinom en uygun polinom olarak seçilmiştir.
import decimal

def pulldata():
    veriler=[]
    print("\n----------------------------------------------------------------------------------\n")
    with open('/home/cihirrim/Masaüstü/bilimselödev/blm2010-master/veriler.txt', 'r') as f:
        y = f.read().split('\n')
    if y[-1] == '':y.pop()
    for i in range(len(y)):
        y[i] = int(y[i])    
    return(y)


def matrix_create_vandermonde(length_row,length_column,datas):
    vandermonde=[]
    for k in range (0,length_row):
        vandermonde.append([])
    #print(vandermonde)
    #print("length_row:",length_row,"length_column",length_column)
    for i in range (length_row):
        for j in range (length_column+1):
            #print("i: ",i,"j: ",j,"data[i]:",datas)
            vandermonde[i].append(datas[i][0]**(j))
    return vandermonde


def matrix_transpose(matrix):
    transposem = []
    length_column = len(matrix)
    length_row = len(matrix[0])
    for k in range(length_row):
        transposem.append([])
    for n in range(length_row):
        for m in range(length_column):
            transposem[n].append(matrix[m][n])
    return transposem


def matrix_multiplication(firstmatrix, secondmatrix):
    result = []
    for i in range (len(firstmatrix)):
        result.append([])
        for j in range (len(secondmatrix[0])):
            total = 0
            for k in range(len(secondmatrix)):
                total += firstmatrix[i][k]*secondmatrix[k][j]
            result[i].append(total)
    return result


def matrix_inverse(old_matrix):
    matrix = old_matrix
    Imatrix = [] #Birim Matris
    for i in range(len(matrix)): #Matris ile boyutu aynı birim matris oluşturma
        Imatrix.append([])
        for j in range(len(matrix)):
            if(i == j):
                Imatrix[i].append(1)
            else:
                Imatrix[i].append(0)

    for i in range(len(matrix)):
        bolen = matrix[i][i]
        for j in range(len(matrix)):
            matrix[i][j] = matrix[i][j]/bolen
            Imatrix[i][j] = Imatrix[i][j]/bolen
        for k,z in zip(matrix[i+1:],Imatrix[i+1:]):
            carpan = k[i]
            for m in range(len(k)):
                k[m] = [m]-matrix[i][m]*carpan
                z[m] = z[m]-Imatrix[i][m]*carpan  

    for i in range(len(matrix)-1,-1,-1):
        for j in range(i-1,-1,-1):
            carpan = matrix[j][i] / matrix[i][i]
            for k in range(len(matrix)):
                matrix[j][k] -= carpan*matrix[i][k]
                Imatrix[j][k] -= carpan*Imatrix[i][k]
    return Imatrix 


def calculated_datas(datasx,coefficients):
    calculateddatas=[]
    for degree in range(len(coefficients)):    #polinom derecesi
        calculateddatas.append([])
        calculateddatas[degree] = matrix_multiplication(matrix_create_vandermonde(len(datasx),degree+1,datasx),coefficients[degree])
    return calculateddatas       


def error_amount(datasy,calculateddatas,aralik1,aralik2):
    mae = []
    for degree in range(len(calculateddatas)):
        summ = 0
        for i in range(len(datasy)):
            x = datasy[i][0]
            y = calculateddatas[degree][i][0]
            subs = x - y
            summ += abs(subs)/len(datasy)
        mae.append(summ)
    min = mae[0]
    minsay = 0
    for j in range (len(mae)):
        if mae[j] <= min:
            min = mae[j]
            minsay = j
    with open('/home/cihirrim/Masaüstü/bilimselödev/blm2010-master/sonuclar.txt','a') as f:
        f.write(f"\n ({aralik1,aralik2-1}) araliginda {minsay+1}.derece polinom en dusuk hatali ve en uygunudur. Hata={min}\n")
    f.close()

    
datasy = []
datasy.append([])
datasy[0] = pulldata()
datasy = matrix_transpose(datasy)

datasx = []
datasx.append([])
for i in range(len(datasy)):
    datasx[0].append(i)
datasx = matrix_transpose(datasx)

coefficients = []
for degree in range(1,7):
    coefficients.append([])
    vandermondematrix = matrix_create_vandermonde(len(datasx),degree,datasx)
    transpose = matrix_transpose(vandermondematrix)
    product = matrix_multiplication(transpose,vandermondematrix)
    mult = matrix_multiplication(matrix_inverse(product),transpose)
    sonuc = matrix_multiplication(mult,datasy)
    for m in range(len(sonuc)):
        coefficients[degree-1].append(sonuc[m])
f=open('/home/cihirrim/Masaüstü/bilimselödev/blm2010-master/sonuclar.txt', 'w')
f.write("----- derecelere bagli katsayilar -----\n")
f.close()
for i in range(6):
    with open('/home/cihirrim/Masaüstü/bilimselödev/blm2010-master/sonuclar.txt','a') as f:
        f.write(f"{i+1}. derece polinomun katsayıları:{coefficients[i]}\n")
f = open('/home/cihirrim/Masaüstü/bilimselödev/blm2010-master/sonuclar.txt', 'a')
f.write("\n----- belirli araliklarda en uygun dereceden paraboller -----\n")
f.close()
calculateddatas = calculated_datas(datasx,coefficients)
error_amount(datasy,calculateddatas,0,len(datasy))

print("\n")
for q in range(0,len(datasy),10):
    coefficients1 = []
    count = 0
    for e in range(0,10):
        count = e
        if (q+e) >= len(datasy)-1:
            break  
    count = count+1
    for degree in range(1,7):
        coefficients1.append([])
        vandermondematrix = matrix_create_vandermonde(len(datasx[q:q+count]),degree,datasx[q:q+count])
        transpose = matrix_transpose(vandermondematrix)
        # print(transpose)
        product = matrix_multiplication(transpose,vandermondematrix)
        mult = matrix_multiplication(matrix_inverse(product),transpose)
        sonuc = matrix_multiplication(mult,datasy[q:q+count])
        for m in range(len(sonuc)):
            coefficients1[degree-1].append(sonuc[m])
    calculateddatas = calculated_datas(datasx[q:q+count],coefficients1)
    error_amount(datasy[q:q+count],calculateddatas,q,q+count)