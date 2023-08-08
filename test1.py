from sympy.vector import CoordSys3D, express
from sympy.abc import a, b, c
N = CoordSys3D('N')
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
