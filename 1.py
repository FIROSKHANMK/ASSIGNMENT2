ab=0
def abc(n):
    global ab
    ab=ab+n
    if n>1:
        abc(n-1)

abc(10) 
print(ab)   