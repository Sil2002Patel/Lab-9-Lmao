#Zachary Merlo
def encoder(stri):
    l=[]
    nstr=''
    for num in stri:
        l.append(num)
    for num in l:
        nstr=nstr+str(int(num)+3)
    return nstr

a=encoder('000')
print(a)


# Sil made this comment
