# primogrado.py

# risolve equazioni di primo grado
# nella forma Ax + B = 0, con A e B interi

print "Risolve equazioni di primo grado"
print "nella forma Ax + B = 0\n"

A = input('A: ')
B = input('B: ')

if A != 0 and B != 0 :
    x = -float(B) / float(A)
    print "L'equazione ammette la  soluzione:",x 

elif A == 0 and B == 0 :
    print "L'equazione 0 = 0 ammette infinite soluzioni"

elif A == 0 :
    print "L'equazione", B, "= 0 non ammette soluzioni"

