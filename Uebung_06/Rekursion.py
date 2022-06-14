x = range(-10,11)

def my_map_recursive(F,x): # wie kann ich mir hier diesen blöden teil sparen?
    i=0
    z=[]
    recursive_part(F,x,i,z)
    print(z)


def recursive_part(F,x,i,z):
    if i <= len(x)-1:
        z.append(F(x[i]))
        i = i + 1
        recursive_part(F,x,i,z)
    else: 
        return 

my_map_recursive(lambda x: x**2, x)
my_map_recursive(lambda x: x**3, x)