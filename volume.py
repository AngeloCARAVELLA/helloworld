import math

#volume
#programma che calcola il volume di un cubo o di una sfera in base ad una scelta effettuata dall'utente

print "Calcolo del volume di un cubo o di una sfera"

opzione =   input ( "Effettua una scelta (1 - Cubo, 2 - Sfera)" )


if opzione  == 1 :
    lato = input (" Inserisci il  lato del cubo :" )
    volume = lato * lato * lato
    print " il volume di lato :  " ,lato, " ha volume " , volume 

elif opzione  == 2 : 
    raggio  = input ("Inserisci il  raggio della  sfera :" )
    volume = 4/3. * math.pi * raggio * raggio * raggio
    print "La sfera di raggio",raggio , "ha volume", volume

else:
    print "Scelta non valida"

                                               
