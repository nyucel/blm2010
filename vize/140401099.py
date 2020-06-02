# Fikret ÇAKIRLI 140401099

import  numpy as np

def calculateSumXWithDegree(caseX,degree):
    return sum(caseX[value]**degree for value in range(len(caseX)))

def calculateSumXYWithDegree(caseX,caseY,degree):
    return round(sum(caseX[value] ** degree * caseY[value] for value in range(len(caseX))),3)

def calculateSumY(cases):
    return round(sum(cases),3)

def readDataFromFile():
    f = open("veriler.txt", "r")
    result = f.read().splitlines()
    return  list(map(int,result))

def indexToArray(length):
    resultyArray=[]
    for i in range(length):
        resultyArray.append(i+1)
    return resultyArray

def LowerTriangler(matrix,degree):
    for n in range(degree):
        kat = int(matrix[n][n])
        if (kat == 0):
            index = 1
            while (kat == 0 and index + n < degree):
                matrix[n], matrix[n + index] = matrix[n + index], matrix[n]
                index = index + 1
                kat = int(matrix[n][n])
            if (kat == 0):
                print("En az 2 satır birbirine bağlı birbirinden turemis sonuc yok ...")
                sys.exit()
        for m in range(degree + 1):
            matrix[n][m] = int(matrix[n][m]) / kat
        for p in range(1, degree - n):
            kat = float(matrix[n + p][n])
            for q in range(degree + 1):
                matrix[n + p][q] = float(matrix[n + p][q]) - float(matrix[n][q]) * (kat / float(matrix[n][n]))

    return UpperTriangler(matrix,degree)

def UpperTriangler(matrix,degree):
    for n in range(degree):
        kat = float(matrix[degree - n - 1][degree - n - 1])
        for m in range(degree + 1):
            matrix[degree - n - 1][degree - m] = float(matrix[degree - n - 1][degree - m]) / kat
        for p in range(1, degree - n):
            kat = float(matrix[degree - n - 1 - p][degree - n - 1])
            for q in range(degree + 1):
                matrix[degree - n - 1 - p][q] = float(matrix[degree - n - 1 - p][q]) - float(matrix[degree - n - 1][q]) * (
                            kat / float(matrix[degree - n - 1][degree - n - 1]))
    return matrix

def nDegreePolynomial(degree,InputX,InputY):
    mymatrix = np.zeros([degree, degree + 1])
    for i in range(degree):
        for j in range(degree + 1):
            if (j == degree):
                if (i == 0):
                    mymatrix[i][j] = calculateSumY(InputY)
                else:
                    mymatrix[i][j] = calculateSumXYWithDegree(InputX, InputY, i)
            else:
                mymatrix[i][j] = calculateSumXWithDegree(InputX,i+j)
    return mymatrix

def getResults(Roots, InputX):
    results = []
    for i in range(len(InputX)):
        localResult=0
        for j in range(len(Roots)):
            if(j==0):
                localResult+= Roots[j]
            else:
                localResult += Roots[j]*(InputX[i]**j)
        results.append(localResult)
    return results

def avgMissRate(realDataArray,predictedDataArray):
    wrongDataAvg=0
    wrongDataArray=[]
    for i in range(len(realDataArray)):
        wrongDataAvg+=abs(realDataArray[i]-predictedDataArray[i])
        wrongDataArray.append(abs(realDataArray[i]-predictedDataArray[i]))
    return round(wrongDataAvg/len(realDataArray),3),wrongDataArray


def standardDeviation(WrongPredictedArray):
    return np.std(WrongPredictedArray[1])

def column(matrix, i):
    return [row[i] for row in matrix]

def BestSolutionWithSize(size,originData,rowData,bestSolutionDegree):
    for i in range(1,len(originData)-size+1):
        myMatrix=nDegreePolynomial(bestSolutionDegree+1,rowData[i:i+9],originData[i:i+size])
        resultMatrix = LowerTriangler(myMatrix, bestSolutionDegree+1)
        print(f"{i}-{i+size} icin {bestSolutionDegree} dereceden denklem cozumu uygulanmasinda StandartHata: {standardDeviation(avgMissRate(originData[i:i+9],getResults(column(resultMatrix,bestSolutionDegree+1),rowData[i:i+9])))}")

def main():
    caseArrayY = readDataFromFile()
    caseArrayX = indexToArray(len(caseArrayY))
    standardDeviationArray=[]
    np.set_printoptions(suppress=True)

    f = open('sonuc.txt', 'w')
    f.write("Polynoms a+bx , a+bx+cx**2 .... \n")
    f.close()
    for degree in range(1,7):
        myMatrix = nDegreePolynomial(degree+1, caseArrayX, caseArrayY)
        resultMatrix=LowerTriangler(myMatrix,degree+1)
        standardDeviationArray.append(standardDeviation(avgMissRate(caseArrayY,getResults(column(resultMatrix,degree+1),caseArrayX))))
        with open('sonuc.txt', 'a') as f:
            f.write(f"{degree}. dereceden denklem kokleri : {column(resultMatrix,degree+1)}\n")
    bestSolution=min((v,i+1) for i, v in enumerate(standardDeviationArray))

    print(f"En iyi cozum {bestSolution[1]}. dereceden polinom ile StandartHata: {bestSolution[0]}")

    #10'lu gruplanarak cozumun uygulanmasi
    BestSolutionWithSize(9,caseArrayY,caseArrayX,bestSolution[1])

if __name__=="__main__":
    main()