
# Betül İNCE - 180401020

with open("veriler.txt", "r+") as data:
    cases = []
    for line in data:
        cases.append(int(line))
size = len(cases)
sum_cases = sum(cases)

def first_order_polynomial():
    n = len(cases)
    sum_of_x = 0
    sum_of_y = sum(cases)
    sum_of_xiyi = 0
    sum_of_xi_square = 0
    for i in range(n):
        sum_of_x += i+1
        sum_of_xiyi += (i+1)*cases[i]
        sum_of_xi_square += (i+1)*(i+1)
    a1 = (n*sum_of_xiyi - sum_of_x*sum_of_y)/(n*sum_of_xi_square - sum_of_x**2)
    a0 = (sum_of_y - a1*sum_of_x)/n
    #print(a0,a1)
    for i in range(n):
        print(  cases[i],   a0+a1*(i+1))
#print("first order polynomial--cases and the values that we found:")
#first_order_polynomial()

def polynominal(d):
    x_list = []
    size = d + 1
    matrix = [[0 for i in range(d + 1)] for j in range(d + 1)]
    for i in range(len(cases)):
        x_list.append(i + 1)
    for i in range(size):
        for j in range(size):
            for x in x_list:
                matrix[i][j] += pow(x, i + j)
    for i in range(size):
        sum_of_xy = 0
        for j in x_list:
            sum_of_xy += cases[j - 1] * pow(j, i)
        matrix[i].append(sum_of_xy)
    return matrix

def solution_with_gauss(matrix):
    n = len(matrix)
    for i in range(0, n):
        maxCol = abs(matrix[i][i])
        maxRow = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > maxCol:
                maxCol = abs(matrix[j][i])
                maxRow = j
        for j in range(i, n + 1):
            temp = matrix[maxRow][j]
            matrix[maxRow][j] = matrix[i][j]
            matrix[i][j] = temp
        for j in range(i + 1, n):
            c = -matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                if i == k:
                    matrix[j][k] = 0
                else:
                    matrix[j][k] += c * matrix[i][k]
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][n] -= matrix[j][i] * x[i]
    return x

def correlation(comp_list):
    sr = 0
    st = 0
    yavg = sum_cases / size
    for i in range(size):
        sr += (cases[i] - comp_list[i]) ** 2
    for i in range(size):
        st += (cases[i] - yavg) ** 2
    square_r = ((st - sr) / st)
    r = square_r ** (0.5)
    return r

def found_values():
    correlation_values = []
    x_list = []
    for i in range(len(cases)):
        x_list.append(i + 1)
    print(x_list)
    for i in range(1, 7):
        comp_list = []
        matrix = polynominal(i)
        coef = solution_with_gauss(matrix)
        sum = 0
        for i in x_list:
            for j in range(len(coef)):
                sum += coef[j] * (i ** j)
            comp_list.append(sum)
            sum = 0
        correlation_values.append(correlation(comp_list))
    return correlation_values

found_values = found_values()
best_correlation=sorted(found_values)[-1]
with open("sonuc.txt", "w") as file:
    for d in range(1, 7):
        matrix = polynominal(d)
        coef = solution_with_gauss(matrix)
        file.write("correlation value of {}. polynom: ".format(d))
        file.write(str(found_values[d-1])+"\n")
        file.write("while approaching {}. polynomial:\n".format(d))
        for c in range(len(coef)):
            file.write("    ")
            file.write("a{} = ".format(c))
            file.write(str(coef[c]) + "\n")

        file.write("\n")
    file.write("best polynom is {}".format(found_values.index(best_correlation)+1))


