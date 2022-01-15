class Matrix:
    """
    class of matrices
    """
    def __init__(self, matrix: list):
        self.mat_list = matrix
    
    def matrix(self):
        """
        checks if the input is a matrix
        """
        try:
            row_len = len(self.mat_list[0])
        except IndexError:
            return False

        for row in self.mat_list:
            if len(row) != row_len or row_len == 0:
                return False
        return True

    def _square(self):
        """
        checks if the matrix is
        a square matrix
        """
        col_len = len(self.mat_list)
        try:
            row_len = len(self.mat_list[0])
        except IndexError:
            return False

        index = 1

        if not self.matrix():
            return False
        else:
            if col_len == row_len:
                return True
            return False

    def _constructor(self, removed_col: int):
        '''
        constructs the minor of the
        matrix with the first row and removed_col
        removed from the original matrix
        ''' 
        mat_list_copy = []
        for e in self.mat_list:
            mat_list_copy.append(list(tuple(e)))
        # creats new inner lists
        # disconnected from the
        # inner lists of the initial list
        input_dim = len(self.mat_list)
        out = []
        index = 1
        # starts from one b/c the
        # the first row is removed
        removed_col = removed_col - 1
        # pyhton index starts from 0

        while index < input_dim:
            mat_list_copy[index].pop(removed_col)
            out.append(mat_list_copy[index])
            index += 1
        return Matrix(out)

    def det(self):
        """
        matrix determinant calculator
        """
        if not self._square():
            return 0
        # non-square matrices have det = 0
        if len(self.mat_list) == 2:
            return self.mat_list[0][0]*self.mat_list[1][1] - self.mat_list[0][1]*self.mat_list[1][0]

        else:
            det_mat = 0
            index = 0
            while index < len(self.mat_list[0]):
                det_mat += (-1)**(1 + (index + 1))*self.mat_list[0][index]* \
                        self._constructor(index + 1).det()
                index += 1
            return det_mat

    def __str__(self):
        """
        prints the matrix, if it's a matrix

        example:

        matrix = Matrix( [ ['a', 'b'], ['c', 'd'] ] )

        print(matrix)

        | a b |
        | c d |
        """
        if not self.matrix():
            return 'NOT A MATRIX'

        # finds the longest string (number) entree
        # in the matrix
        maxim = len(str(self.mat_list[0][0]))
        for e in self.mat_list:
            for i in e:
                if len(str(i)) > maxim:
                    maxim = len(str(i))

        out = ''
        for row in self.mat_list:
            part_out = '|'
            index = 0
            while index < len(row):
                part_out += f'{(1 + (maxim-len(str(row[index]))))*" "}{row[index]}'
                index += 1
            part_out += ' |\n' 
            out += part_out
        return out[:-1]

    def transpose(self):
        """
        returns the transpose of the
        input matrix and empty list if it's
        not a valid matrix
        """
        if not self.matrix():
            return 'NOT A MATRIX'
        trans_out = []
        trans_col_len = len(self.mat_list[0])
        trans_row_len = len(self.mat_list)

        index_col = 0
        

        while index_col < trans_col_len:
            row = []
            index_row = 0
            while index_row < trans_row_len:
                row.append(self.mat_list[index_row][index_col])
                index_row += 1

            index_col += 1
            trans_out.append(row)

        return Matrix(trans_out)

    def mult(self, other):
        """
        computes the product of two matrices
        self is the outter matrix
        """
        if not self.matrix() and not other.matrix(): 
            return "BOTH MATRICES WRONG"
        else:
            if not self.matrix():
                return "FIRST MATRIX WRONG"
            elif not other.matrix():
                return "SECOND MATRIX WRONG"

        scnd_matrix_trans = other.transpose()
        if len(self.mat_list[0]) != len(scnd_matrix_trans.mat_list[0]):
            return "MISMATCHED MATRIX DIMENSIONS"

        matrix_out = []

        for row1 in self.mat_list:
            row_out = []

            for row2 in scnd_matrix_trans.mat_list:
                entree_index = 0
                entree_out_val = 0
                while entree_index < len(row2):
                    entree_out_val += row1[entree_index]*row2[entree_index]
                    entree_index += 1
                row_out.append(entree_out_val)
            matrix_out.append(row_out)

        return Matrix(matrix_out)

    def _vector_to_poly(self):

        if not self.matrix() or len(self.mat_list[0]) > 1:
            return 'NOT A VECTOR'

        vect = self.transpose().mat_list
        deg_coef_pairs = {}
        for i in range(len(vect[0])):
            if vect[0][i] != 0:
                deg_coef_pairs[i] = vect[0][i]

        poly = ''
        for deg in deg_coef_pairs:
            if '0' == str(deg_coef_pairs[deg])[-1]:
                coeff = int(deg_coef_pairs[deg])
            else:
                coeff = deg_coef_pairs[deg]
            if deg > 0:
                if coeff >= 0:
                    poly = f'+{coeff}x^{deg}' + poly if coeff != 1 else f'+x^{deg}' + poly
                else:
                    poly = f'{coeff}x^{deg}' + poly if coeff != -1 else f'-x^{deg}' + poly
            else:
                poly = f'+{coeff}' + poly if coeff >= 0 else f'{coeff}' + poly
        if not len(poly) == 0:
            return poly[1:] if poly[0] == '+' else poly
        else: return '0'


# matrix = Matrix( [ [5, 6, 6, 8], [2, 2, 2, 8], [6, 6, 2, 8], [2, 3, 6, 7] ] )
# print(matrix)
# print(matrix.transpose())

