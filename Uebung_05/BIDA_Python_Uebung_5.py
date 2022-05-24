x = range(-10,11)

def my_map(f,x):
    y=[] # könnte auch mit y = [0] *10
    for i in range(len(x)):
        y.append(0)
        y[i] = f(x[i]) 
    print(y)

my_map(lambda x: x**2, x)
my_map(lambda x: x**3, x)

get_name = lambda x: x.get("name")

me = {"name": "Robin", "surname": "Ender", "age": "23", "cleans_laptop_in_dishwasher": True, "get_name": lambda x: x.get("name")}

print(me.get("get_name")(me)) # [] geht auch, dann braucht man kein .get

