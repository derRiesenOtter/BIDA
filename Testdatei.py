a=3
b=4

def starter(a,b):
    i = 5
    tomate(a,b,i)


def tomate(a,b,i):
    if i > 0:
        i -= 1
        print(a)
        a = tomate(a,b,i)
        a = a + 1
        return a
    else: 
        return a

starter(a,b)