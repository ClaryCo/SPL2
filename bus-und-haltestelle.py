#bus-und-haltestelle
p = 0
i = input ("Wie viele Haltestellen gibt es? : ")

for c in range(0, int(i)) :

    a = input ("Wie viele Personen steigen ein?: ")
    b = input ("Wie viele Personen steigen aus?: ")

    p = p + int(a)
    p = p - int(b)

print (p)

    if ( p > 60) :
        print (" Es dürfen nicht mehr Menschen einsteigen ")
        y = 60-p
    else:
