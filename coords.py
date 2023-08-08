from sympy.vector import CoordSys3D, express
from sympy.matrices import Matrix
from sympy import shape
from sympy.abc import a
from sympy import symbols
from sympy import Symbol
from sympy import sin, cos, tan, atan, atan2, degree
from sympy import sqrt

x, y, z, r = symbols('x y z r')
rho, phi, theta= symbols('rho phi theta', real=True, negative=False)

"""
Cambio de varible    
"""

# Cartesianas --> Cilindricas
rho = sqrt(x**2 + y**2)
phi = atan2(y,x)

# Cartesianas --> Esfericas
rho = sqrt(x**2 + y**2 + z**2)
phi = atan(y/x)
theta = atan(z/r)

# Cilindricas ---> Cartesianas


# Esfericas ---> Cartesianas
#x = r*sin(theta)*cos(phi)
#y = r*sin(theta)*sin(phi)
#z = r*cos(theta)

"""Coordenadas"""
M_car_to_cyl = Matrix([[cos(phi),sin(phi),0],
            [-sin(phi),cos(phi),0],
            [0,0,1]])

def test():
    Ax = y
    print(Ax)
    Ax.subs({x: rho*cos(phi), y: rho*sin(phi)})
    print(Ax)

def car2cyl(Ax, Ay, Az):
    #x = rho*cos(phi)
    #y = rho*sin(phi)
    if Ax != 0:
        Ax.subs([(x, rho*cos(phi)), (y, rho*sin(phi))])
        print(Ax)
        print("---")
    

    
    A_car = Matrix([[Ax],[Ay],[Az]])
    
    
    dim = shape(A_car)
    # Expresion de los compontentes en coordenadas cilindricas
    for i in range(dim[0]):
        print(i)
        if A_car[i,0] != 0:
            print(A_car[i,0])
            # A_car[i,0].evalf(subs={x: rho*cos(phi), y: rho*sin(phi)})
    print(A_car)
    A_cyl = M_car_to_cyl*A_car
    print(A_cyl)
    return A_cyl

test()
# car2cyl(y, x + z, 0)






"""
C = [x, y, z]             # Cartesianas
S = [r, theta, phi]     # Esfericas
P = [rho, theta, z]     # Cilindricas = Polares

print(C)
print(S)
print(P)

C = CoordSys3D('C')
P = C.orient_new_axis('P', phi, C.k)
print(P.rotation_matrix(C))
print()
print(P.rotation_matrix(P))
"""




"""
Cambio de componente
"""

"""
N = CoordSys3D('N')
v1 = 1*N.i + 1*N.j + 1*N.k
print(v1)
print(v1)
M = N.orient_new_axis('M', a, N.k)
v1_M = express(v1, M)
print(v1_M)
O = N.create_new('O', transformation='spherical')
v1_E = express(v1, O)
print(v1_E)

# https://stackoverflow.com/questions/61100589/is-there-a-way-of-working-in-spherical-coordinates-in-sympy
# https://docs.sympy.org/latest/modules/vector/index.html#module-sympy.vector

P = CoordSys3D('P', transformation='spherical', variable_names=list('rtp'))
"""
#A = CoordSys3D('A', transformation='spherical')
#B = CoordSys3D('A', transformation=lambda x,y,z: (x*sin(y), x*cos(y), z))
#v1 = A.i + A.j + A.k
#print(v1)