from lin_al import Matrix 

class Poly:
    """
    polynomial function class
    the only possible input
    variable is x
    
    p(x) = a_n*x^n + .... + a_1*x^1 + a_0
    is the only valid form 
    """
    def __init__(self, poly):
        self.poly = poly
    

    def _separator(self) -> list:
        """
        splits poly into terms
        """
        poly = self.poly[:]
        ind = 0
        while ind < len(poly):
            if poly[ind] == '-' and ind != 0:
                poly = poly[: ind] + '+' + poly[ind:]
                ind += 1
            ind += 1
        return poly.split('+')

    def degree(self) -> int:
        """
        returns the degree of the polynmial
        """
        terms = self._separator()

        largest_term = terms[0]

        degree = int(largest_term[largest_term.index("^")+1:]) \
                                if '^' in largest_term else None
        if degree is None:
            if "x" in largest_term:
                degree = 1
            else:
                degree = 0
        return degree
    
    def coeffs(self) -> list[int]:
        """
        returns the coefficients of the polynimial
        from the highest degree to the lowerst
        """
        
        out_list = []
        for ement in self._separator():
            if 'x' in ement and '-x' not in ement and ement[0] != 'x':
                out_list.append(float(ement[:ement.index('x')]))
            elif '-x' in ement or ement[0] == 'x':
                if '-x' in ement:
                    out_list.append(float(-1))
                else:
                    out_list.append(float(1))
            else:
                out_list.append(float(ement))

        return out_list

    def _poly_into_vect(self):
        ''' 
        turns the polynomial into
        vector form
        '''
        degree_list = []
        degree_list.append(self.degree())
        ind = 1
        while ind < len(self._separator()):
            degree_list.insert(0, self.degree(self._separator()[ind:]))
            ind += 1

        vector = []
        coeffs = self.coeffs()
        coeffs.reverse()
        deg_coef_pairs = dict(zip(degree_list, coeffs))

        for i in range(degree_list[-1] + 1):
            if i not in deg_coef_pairs:
                vector.append(0)
            else:
                vector.append(deg_coef_pairs[i])
        return Matrix([vector]).transpose()

    def poly_der(self, nth=1) -> str:

        """
        computes the derivative
        of a polynomial using linear albegra
        1. converts poly (str) into a vector
        2. creates the diffferentiation matrix
        3. pluggs the poly vector into the matrix
        4. converts back to str
        """
        mat_size = self.degree() + 1
        mat_list = []

        for i in range(mat_size):
            mat_list.append([0]*mat_size)
            mat_list[i-1][i] = i
        
        der_matrix = Matrix(mat_list)
        same_but_composite_matrix = Matrix(mat_list)

        for _ in range(nth-1):
            # nth-1 bc it's not really
            # the number of derivatives
            # aka the number of matrices
            #but the number of matrix compositions
            der_matrix = der_matrix.mult(same_but_composite_matrix)

        out_poly_as_vect = der_matrix.mult(self._poly_into_vect())

        return out_poly_as_vect._vector_to_poly()


class polyTree:
    """
    a class of polynomials of the form
    p(x) = a_n*x^n + .... + a_1*x^1 + a_0
    no factorized forms
    """
    def __init__(self, root, sublist):
        self.root = root
        self.sublist = sublist

    def der(self):
        """
        computes the derivative of p(x) [p'(x)]

        the function is very input sensative and
        will eihter crash or return an incorrect output
        if the format is wrong.

        sidenote:

        the function also accepts second derivative
        requests (by func.der().der()) since it
        returns in a function-friendly format

        1. addition has at least 2 trees in its sublist

        2. multiplication has 2 (no more, no less) trees in
        its sublist where the left one (sublist[0]) is
        always a number and the right one (sublist[1]) is
        either ^ or x or

        3. exponentiation has only 2 trees where the
        left one is the variable and the right one is a number

        4. the function (tree) is not empty

        some forbidden -> permitted formats
        1. x^2 -> 1*x^2
        2. x^2*2 -> 2*x^2
        3. a_0*x^0 -> a_0

        example:

        expo1 = polyTree("^", [polyTree("x", []), polyTree(3, [])])
        mult1 = polyTree("*", [polyTree(-3, []), expo1])

        expo2 = polyTree("^", [polyTree("x", []), polyTree(2, [])])
        mult2 = polyTree("*", [polyTree(-1, []), expo2])

        mult3 = polyTree("*", [polyTree(1, []), polyTree("x", [])])

        num1 = polyTree(1, [])

        func = polyTree("+", [mult1, mult2, mult3, num1])

        p(x) = -3*x^3 + (-1)*x^2 +1*x + 1

        func.der()

        p'(x) = -9*x^2 + (-2)*x + 1 + 0
        """
        if isinstance(self.root, (int, float)):
            return polyTree(0, [])
        else:
            
            if self.root == "+":
                derivative = polyTree("+", [])
                for ement in self.sublist:
                        derivative.sublist.append(ement.der())
                return derivative

            elif self.root == "*":
                no_expo = True
                # checks if it will have to multiple
                # scalar of x by the exponent

                if self.sublist[1].root == "^":
                    no_expo = False

                if no_expo:
                    return self.sublist[0]
                
                # the else is the exponentiation
                else:
                    scalar = self.sublist[0].root
                    expo = self.sublist[1].sublist[1].root
                    return polyTree("*", [polyTree(scalar*expo, []),
                                         self.sublist[1].der()])
            # the else is the exponentiation
            else:
                exponent = self.sublist[1].root-1
                if exponent != 1:
                    return polyTree("^", [self.sublist[0],
                                         polyTree(exponent, [])])
                else:
                    return self.sublist[0]
