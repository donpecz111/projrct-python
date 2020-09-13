x = input("podaj x:")
y = input("podaj y:")
działanie = input("podaj typ działania :")
if działanie == "dodawanie" :
    print ("Wynik dodawania:", int(x) + int(y))
if działanie == "odejmowanie" :
    print ("Wynik odejmowania: x-y" , int(x) - int(y))
    print ("Wynik odejmowania: y-x",int(y) - int(x))
if działanie == "mnożenie" :
    print("Wynik mnożenia:",int(x) * int(y))
if działanie == "dzielenie":
    print ("Wynik dzielenia: x/y ", int(x) / int(y) )
    print( "Wynik dzielenia: y/x" , int(y) / int(x))