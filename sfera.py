#sfera.py
#stampa superficie e volume di una sfera dato il raggio (intero)
import math

print "Calcolo della superficie e del volume di una sfera"
raggio = input ("raggio?")
volume = 4. * math.pi * raggio * raggio 
superficie = 4. / 3. * math.pi * raggio * raggio * raggio
print "La sfera di raggio", raggio, "ha superficie", superficie, "e volume", volume
