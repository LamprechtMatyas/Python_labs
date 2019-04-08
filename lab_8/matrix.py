class Matrix:
    matrix = []

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = [[0] * n for i in range(m)]

    def change_num(self, i, j, val):
        self.matrix[j][i] = val

    def return_matrix(self):
        return self.matrix

    def add_matrix(self, matrix2):
        # print(matrix2.return_matrix())
        if (self.m == matrix2.m) and (self.n == matrix2.n):
            m3 = Matrix(self.m, self.n)
            for i in range(self.m):
                for j in range(self.n):
                    m3.change_num(i, j, self.matrix[i][j] + matrix2.matrix[i][j])
            return m3
        else:
            print("Wrong")

    def multiply_matrix(self, matrix2):
        m = Matrix(self.m, matrix2.n)
        for i in range(matrix2.n):
            for j in range(self.m):
                suma = 0
                for k in range(self.n):
                    suma += self.matrix[j][k] * matrix2.matrix[k][i]
                m.change_num(i, j, suma)
        return m


def _main():
    m1 = Matrix(3, 2)
    m1.change_num(0, 0, 1)
    m1.change_num(1, 0, 5)
    m1.change_num(0, 1, 3)
    m1.change_num(1, 1, 2)
    m1.change_num(0, 2, 4)
    print(m1.return_matrix())
    m2 = Matrix(2, 2)
    m2.change_num(0, 0, 2)
    m2.change_num(1, 0, 2)
    m2.change_num(0, 1, 3)
    m2.change_num(1, 1, 2)
    print(m2.return_matrix())
    # m3 = m1.add_matrix(m2)
    # print(m3.return_matrix())
    m4 = m1.multiply_matrix(m2)
    print(m4.return_matrix())





if __name__ == "__main__":
    _main()