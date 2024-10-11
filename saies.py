SpeletajaVards=input("Ieivadi savu vārdu: ")

SpeletajaVards=SpeletajaVards.capitalize()

# "mainīgais.lower()" - konvertē visus burtu simbolus uz mazajiem burtiem.

print(SpeletajaVards)

# "mainīgais.capitalize()" - simbolu virknē, pirmo burtu pārveido uz lielo burtu.

vards1="čība"

burtuSK=len(vards1)
print(burtuSK)

# len - saskaita burtu virknē, burtu skaitu

minejums=input(f"uzraksti vārdu pareizi- {vards1[3]}{vards1[1]}{vards1[0]}{vards1[2]}: ") 

# mainīgais[burta pozīcija] - simbolu virkne sākas ar indeksu 0

minejums=minejums.lower()

if minejums==vards1:
    print("Uzminēji vārdu!")

else: 
    print("Neuzminēji vārdu. Lohs.")

