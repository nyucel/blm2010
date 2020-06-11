from copy import copy
import numpy as np
import math
import sys
import os

__data_file__ = "veriler.txt"
__output_file__ = "sonuc.txt"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def matrix_transpose(matrix: np.ndarray):
    """
    Matrix transpose
    :param matrix: given maxtrix
    :return: new transposed matrix
    """
    new_matrix = np.zeros(shape=(matrix.shape[1], matrix.shape[0]), dtype=float)
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def matrix_multiplication(matrixA: np.ndarray, matrixB: np.ndarray):
    """
    Matrix multiplication
    :param matrixA: given matrix
    :param matrixB: given matrix
    :return: result matrix
    """
    if matrixA.shape[1] != matrixB.shape[0]:
        raise Exception("Matrix çarpımı için matris biçimleri uygun olmalıdır.")

    new_matrix = np.zeros(shape=(matrixA.shape[0], matrixB.shape[1]), dtype=float)
    for i in range(0, matrixA.shape[0]):
        for j in range(0, matrixB.shape[1]):
            for k in range(0, matrixA.shape[1]):
                new_matrix[i][j] += matrixA[i][k] * matrixB[k][j]
    return new_matrix


def get_matrix_minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def get_matrix_deternminant(m):
    # if matrix is 2x2
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * get_matrix_deternminant(get_matrix_minor(m, 0, c))
    return determinant


def matrix_inverse(matrix: np.ndarray):
    """
    For some easy operations, np array converted to list
    then when return it list converted to np array
    :param matrix: Inverse Matrix
    :return: New Matrix
    """

    # Special Case: 1x1 Matrix
    if matrix.shape[0] == 1:
        new_matrix = np.zeros(shape=(1, 1), dtype=float)
        new_matrix[0][0] = 1 / matrix[0][0]
        return new_matrix

    m = list()
    for i in range(matrix.shape[0]):
        rows = list()
        rows.clear()
        for j in range(matrix.shape[1]):
            rows.append(matrix[i][j])
        m.append(rows)

    determinant = get_matrix_deternminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        new_matrix = np.zeros(shape=(matrix.shape[0], matrix.shape[1]), dtype=float)
        new_matrix[0][0] = m[1][1] / determinant
        new_matrix[0][1] = -1 * m[0][1] / determinant
        new_matrix[1][0] = -1 * m[1][0] / determinant
        new_matrix[1][1] = m[0][0] / determinant
        return new_matrix

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * get_matrix_deternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = [list(i) for i in zip(*cofactors)]
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant

    new_matrix = np.zeros(shape=(matrix.shape[0], matrix.shape[1]), dtype=float)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            new_matrix[i][j] = cofactors[i][j]
    return new_matrix

class process:
    def __init__(self, data_container: list):
        """
        This class handles all the main process
        :param data_container: Its a list of data
        """
        self.data_ = data_container
        self.first_var = 0
        self.last_var = len(self.data_)
        self.grade_regression_result = None
        self.results = list()
        self.error_results = list()

    def set_data_range(self, first=0, last=0, all_=False):
        """
        Set the data range for regression
        :param first: The first index of data
        :param last: The last index data data
        :param all_: Select all of the data
        :return: None
        """
        if all_:
            self.first_var = 0
            self.last_var = len(self.data_)
        else:
            self.first_var = first
            self.last_var = last

        print(
            bcolors.WARNING + "Veri aralığını %d - %d arasına alındı!" % (self.first_var, self.last_var) + bcolors.ENDC)

    def regression_for_grade(self, grade=0, no_print=False):
        # X * SOLUTIONS = Y
        # SOLUTIONS = (X_t * X)^-1 * X_t * Y
        solution_matrix = np.zeros(shape=(grade + 1, 1), dtype=float)
        x_matrix = np.zeros(shape=((self.last_var - self.first_var), grade + 1), dtype=float)
        y_matrix = np.zeros(shape=((self.last_var - self.first_var), 1), dtype=float)

        # Prepair matrixs
        y_index = 0
        for i in range(0, (self.last_var - self.first_var)):
            for j in range(0, x_matrix.shape[1]):
                x_matrix[i][j] = pow(float(self.data_[i + self.first_var]), j)
            y_matrix[i][0] = float(y_index)
            y_index += 1

        x_trans_matrix = matrix_transpose(x_matrix)
        multi_matrix = matrix_multiplication(x_trans_matrix, x_matrix)
        inversed_matrix = matrix_inverse(multi_matrix)
        multi_two_matrix = matrix_multiplication(x_trans_matrix, y_matrix)
        multi_three_matrix = matrix_multiplication(inversed_matrix, multi_two_matrix)
        solution_matrix = multi_three_matrix
        self.grade_regression_result = copy(solution_matrix)
        self.results.append(self.grade_regression_result)

        to_printed = ""
        to_printed += str(grade) + " dereceden yaklaştırma sonucu: \n"
        to_printed += str(self.grade_regression_result[0])
        for i in range(1, grade + 1):
            to_printed += " + " + str(self.grade_regression_result[i]) + "X"
            to_printed += "^^" + str(i)
        to_printed += " = Y"
        if not no_print:
            print(to_printed)

    def calculate_most_usefull(self):
        for i in range(len(self.results)):
            avarage = 0.0
            y_index = 0
            for x_data in self.data_:
                X = float(x_data)
                Y = y_index
                y_index += 1

                total = 0.0
                for j in self.results[i]:
                    total += float(j) * pow(X, j)
                E = total - Y
                avarage += E
            avarage /= len(self.data_)
            self.error_results.append(avarage)

        for i in range(len(self.error_results)):
            if self.error_results[i] < 0:
                self.error_results[i] *= -1

        the_lowest_error = self.error_results[0]
        the_lowest_error_index = 0
        for i in range(len(self.error_results)):
            if self.error_results[i] < the_lowest_error:
                the_lowest_error = self.error_results[i]
                the_lowest_error_index = i

        print("Polinomlarda en düşük hata: %d dereceden poliinom yaklaştırmasında bulundu. Hate E=%s"
              % ((the_lowest_error_index + 1), the_lowest_error))

    def get_data_len(self):
        return len(self.data_)

    def kill_vars(self):
        self.grade_regression_result = None
        self.results = list()
        self.error_results = list()

    def write_to_file(self, the_dir):
        with open(the_dir + "/%s" % __output_file__, "w") as fh:
            to_printed = ""
            for i in range(len(self.results)):
                to_printed += str(i + 1) + " Yaklaştırma\t"
                for j in range(len(self.results[i])):
                    to_printed += str(self.results[i][j]) + "X^^" + str(j) + "\t"
                to_printed += "\n"
            fh.write(to_printed)
        print(bcolors.WARNING + "%s dosyası oluşturuldu!" % __output_file__ + bcolors.ENDC)


def main():
    if args:
        print(bcolors.WARNING + "!!" + bcolors.ENDC)

    # Actually do not need this
    the_data = None
    working_directory = os.getcwd()
    try:
        with open(working_directory + "/%s" % __data_file__, "r") as fh:
            string_format = fh.read()
            a = string_format.splitlines()
            # If last line of file is not /n
            for i in range(len(a)):
                if a[i] == "":
                    a.pop(len(a)-1)
            the_data = copy(a)
    except FileNotFoundError:
        raise Exception("Dosya bulunamadı! %s file" % __data_file__)

    if not the_data:
        raise Exception("Dosya bulundu ama açılamadı. Dosya izinlerini kontrol edin!!")
    print(bcolors.WARNING + "Dosya açıldı ve başarı ile okundu!" + bcolors.ENDC)

    print(bcolors.WARNING + "İlk soruya geçiliyor!" + bcolors.ENDC)
    new_process = process(the_data)
    new_process.set_data_range(all_=True)
    new_process.regression_for_grade(grade=1)
    new_process.regression_for_grade(grade=2)
    new_process.regression_for_grade(grade=3)
    new_process.regression_for_grade(grade=4)
    new_process.regression_for_grade(grade=5)
    new_process.regression_for_grade(grade=6)
    new_process.write_to_file(working_directory)

    print(bcolors.WARNING + "İlk soru başarı ile tamamlandı! İkincisine geçiliyor!" + bcolors.ENDC)
    new_process.calculate_most_usefull()

    print(bcolors.WARNING + "İkinci soru başarı ile tamamlandı. Üçüncüsüne geçiliyor!" + bcolors.ENDC)
    print(bcolors.FAIL + "Burada taşmalara dikkat et!" + bcolors.ENDC)
    for i in range(int(new_process.get_data_len() / 10) + 1):
        first = i * 10
        last = i * 10 + 10
        if i >= int(new_process.get_data_len() / 10):
            last = new_process.get_data_len()

        new_process.kill_vars()
        new_process.set_data_range(first, last)
        new_process.regression_for_grade(grade=1, no_print=True)
        new_process.regression_for_grade(grade=2, no_print=True)
        new_process.regression_for_grade(grade=3, no_print=True)
        new_process.regression_for_grade(grade=4, no_print=True)
        new_process.regression_for_grade(grade=5, no_print=True)
        new_process.regression_for_grade(grade=6, no_print=True)
        new_process.calculate_most_usefull()


if __name__ == '__main__':
    args = sys.argv[1:]
    main()
