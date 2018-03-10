#secgrado.py

# Risolve equazioni di secondo grado nella
# forma ax^2+bx+c=0 con a, b e c interi
# Calcola anche soluzioni alternative

import math

print "Risolve equazioni di secondo grado"
print "nella forma ax^2 + bx + c = 0"

A = input('A: ')
B = input('B: ')
C = input('C: ')
delta = B * B - 4 * A * C
if A==0 and B==0:
    print "L'equazione", C, "= 0 non ammette soluzioni"
elif A==0 and B==0 and C==0:
    print "L'equazione 0 = 0 ammette infinite soluzioni"
elif A==0:
    print "L'equazione si riduce al primo grado"
    print "Soluzione:", -float(C) / float(B)
elif delta > 0:
    print "L'equazione ammette due soluzioni distinte"
    rad_delta = math.sqrt(delta)
    print "x1 =", (-float(B) - rad_delta) / (2.0 * float(A))
    print "x2 =", (-float(B) + rad_delta) / (2.0 * float(A))
elif delta < 0:
    print "Delta < 0. L'equazione ammette due soluzioni complesse coniugate"
    rad_delta = math.sqrt(-delta)
    Re = -float(B) / (2.0 * float(A))
    imm = abs(rad_delta / (2.0 * float(A)))
    print "x1 =", Re, "-I", imm
    print "x2 =", Re, "+I", imm
elif delta == 0:
    print "Delta = 0. L'equazione ammette due soluzioni coincidenti"
    print "x1 = x2 =", -float(B) / (2.0 * float(A))
