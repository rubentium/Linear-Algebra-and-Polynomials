# Linear-Algebra-and-Polynomials

#### The project is a collection of operations related to linear algebra and polynomials.
#### There are two main file ```lin_al.py``` and ```poly.py``` for linear algebra and polynomials respectively. 

#### The there is one class ```Matrix``` in the ```lin_al.py``` and two classes in ```poly.py``` -- ```Poly``` and ```polyTree```. Some of the methods in ```Poly``` rely on the ```Matrix``` class hence, it's being imported.


### ```Matrix``` class
##### Is a class of matrices that is initialized by inputting a list of rows (all rows are also lists)

| Matrix Class Method | Description | Arguments | Default | Output Type |
| ------------------- | ----------- | --------- | ------- | ----------- |
| ```matrix``` | Checks if the input is a matrix | ```self``` | N/A | ```bool```|
| ```_square``` | Checks if the matrix is a square matrix | ```self``` | N/A | ```bool``` |
| ```_constructor``` | Constructs the minor of the matrix with the first row and removed_col removed from the original matrix | ```self```, ```removed_col``` | N/A | ```Matrix``` |
| ```det``` | Matrix determinant calculator | ```self``` | N/A | ```int/float``` |
| ```__str__``` | Prints the matrix | ```self``` | N/A | ```str``` |
| ```transpose``` | Returns the transpose of the matrix and ```[]``` is not a vaid matrix | ```self``` | N/A | ```Matrix```|
| ```mult``` | Multiplie two matrices | ```self```, ```other``` | N/A | ```Matrix```|
| ```_vector_to_poly``` | Turns the vector form of the polynomial to ```a_n*x^n + .... + a_1*x^1 + a_0``` form | ```self``` | N/A | ```str```|


### ```Poly``` class
##### Is a class of polynomials that is initialized by inputting a string of the form ```a_n*x^n + .... + a_1*x^1 + a_0```.
###### Note: the degrees cannot be floats or negative.
| Poly Class Method | Description | Arguments | Default | Output Type |
| ------------------- | ----------- | --------- | ------- | ----------- |
| ```_separator``` | Splits the polynomial string into terms with ```+``` as the delimiter | ```self``` | N/A |  ```list``` |
| ```degree``` | Returns the degree of the polynmial | ```self``` | N/A | ```int``` |
| ```coeffs``` | Returns the coefficients of the polynimial from the highest degree to the lowerst | ```self``` | N/A | ```list[int]``` |
| ```_poly_into_vect``` | Turns the polynomial into vector form | ```self``` |  N/A | ```Matrix``` |
| ```poly_der``` | Computes the n-th derivative of the polinomial using linear algebra | ```self```, ```nth``` | ```nth=1``` | ```str``` |


### ```polyTree``` class
##### A polynomials presented as a binary tree. Input tree is of the form ```p(x) = a_n*x^n + .... + a_1*x^1 + a_0```.
| polyTree Class Method | Description | Arguments | Default | Output Type |
| ------------------- | ----------- | --------- | ------- | ----------- |
| ```der``` | Returns the derivative as a tree| ```self``` | N/A | ```polyTree``` |

##### Example of a class input:
```
p(x) = -3*x^3 + (-1)*x^2 +1*x + 1

expo1 = polyTree("^", [polyTree("x", []), polyTree(3, [])])
mult1 = polyTree("*", [polyTree(-3, []), expo1])

expo2 = polyTree("^", [polyTree("x", []), polyTree(2, [])])
mult2 = polyTree("*", [polyTree(-1, []), expo2])

mult3 = polyTree("*", [polyTree(1, []), polyTree("x", [])])

num1 = polyTree(1, [])

func = polyTree("+", [mult1, mult2, mult3, num1])
```

##### Note: There is no method that gives a ```str``` version of the trees (polynomial). I might write it some time in the future, if I have time.
