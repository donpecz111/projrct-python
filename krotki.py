krotka = (1,'abc',3.5,False)
print (krotka)

lista = [1,2,3]
moja_krotka = tuple(lista)
print(len(moja_krotka))
print(max(moja_krotka))
print(min(moja_krotka))
print(sum(moja_krotka))

a,b,c = moja_krotka
print(b)

krotka2 = (1,2,3,4,5,6)
wynik = [x + 20 for x in krotka2 ]
print(wynik)