bord=0
emtiyaz=0

for x in range(0,30):
    a=int(input())
    if a != 0 and a==1:
        emtiyaz=emtiyaz+a
    elif a != 0  and a==3:
        emtiyaz=emtiyaz+a
        bord=bord+1
        
print (emtiyaz, " ",bord)
