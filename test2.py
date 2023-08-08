from sympy.vector import CoordSys3D, express
from sympy.abc import a, b, c
from sympy import symbols
from sympy import Symbol
from sympy import sin, cos, tan, atan, degree
from sympy import sqrt


x, y, z, r = symbols('x y z r')
rho, phi, theta= symbols('rho phi theta', real=True, negative=False)

# Sistema cartesiano

C = CoordSys3D('C')
print(C.base_vectors())
print(C.base_scalars())
r_P = -2*C.i + 6*C.j + 4*C.k
print(r_P)
print(r_P.components)




S = CoordSys3D('S', transformation='spherical')
print(S.base_vectors())
print(S.base_scalars())


P = CoordSys3D('P', transformation='cylindrical')
print(P.base_vectors())
print(P.base_scalars())
P = C.orient_new_axis('P', phi, C.k)
print(P.base_vectors())
print(P.base_scalars())

print()

print(C.rotation_matrix(P))
print(P.rotation_matrix(C))



print("---------------------------------------")
print(r_P)
r_P_c = express(r_P, P)
print(r_P_c)
r_P_ce = r_P_c.evalf(subs={phi: degree(atan(r_P.components[C.j]/r_P.components[C.i]))})
print(r_P_ce)

"""
M = N.orient_new_axis('M', a, N.k)


v1_N = N.i + N.j + N.k
print(v1_N)
v1_M = express(v1_N, M)
print(v1_M)
v2_M = N.i + M.j
print(v2_M)
v2_N = express(v2_M, N)
print(v2_N)

print()
print(N.rotation_matrix(N))
print(M.rotation_matrix(N))
print(N.rotation_matrix(M))
"""