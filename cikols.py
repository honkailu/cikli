vards=input("Ievadi savu vārdu nominatīvā locijumā (Kas?):")

vards=vards.lower() 
# funkcija .lower()- visus burtus kovertē par mazajiem burtiem.

vards=vards.capitalize()
# funkcija .capitalize()- simbolu virknē pirmo burtu konvertē par lielo.

UzminiVardu="saies"

minejums=None

while UzminiVardu!=minejums:
    #cikls strādā kamēr netiek ievadīts vārds "saies"
    #!= nav vienāds
    minejums=input(f"Uzmini vārdu {UzminiVardu[0]+UzminiVardu[3]+UzminiVardu[2]+UzminiVardu[4]+UzminiVardu[1]}: ")

print("Pareizi.")

UzminiVardu="saule"

while True:
    minejums=input(f"Uzmini vārdu {UzminiVardu[0]+UzminiVardu[3]+UzminiVardu[2]+UzminiVardu[4]+UzminiVardu[1]}: ")

    if UzminiVardu==minejums:
        print("Pareizi.")
        break

UzminiVardu="skola"

meginajumi=2

for i in range(3):
     minejums=input(f"Uzmini vārdu {UzminiVardu[0]+UzminiVardu[3]+UzminiVardu[2]+UzminiVardu[4]+UzminiVardu[1]}: ")

     if UzminiVardu==minejums:
        print("Pareizi.")
        break
     else:
        print(f"Neuzminēji, tev palikuši {meginajumi} mēģinājumi.") 
        meginajumi-=1

print("Spēles beigas.")
