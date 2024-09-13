import random

# name = input("Enter your name?: ")

# print(f"Hello {name}! Here is your story:")

# print("")

def randNum():
    l = (random.randint(1, 3))
    return  l - 1



a = ["mutige", "junge", "kluge"]
b = ["sonnigen", "windigen", "regnerischen"]
c = ["großen", "schweren", "bunten"]
d = ["fröhliches", "leises", "schönes"]
e = ["lautes", "komisches", "gruseliges"]
f = ["kleines", "schnelles", "schwarzes"]
g = ["nervös", "neugierig", "aufgeregt"]
h = ["ruhig", "mysteriös", "lebendig"] 
i = ["dunkle", "hohe", "elegante"]
j = ["mutig", "entspannt", "beschwingt"]
m = randNum()
print(m)
print(f"Der '{a[m]}' Max ging an einem '{b[m]}' Morgen in den Wald.") 
m = randNum()
print(m)
print(f"Er trug seinen '{c[m]}' Rucksack und summte ein '{d[m]}' Lied.")
m = randNum()
print(m)
print(f"Plötzlich hörte er ein '{e[m]}' Geräusch.")
m = randNum()
print(m)
print(f"Max blieb stehen, drehte sich um und sah ein '{f[m]}' Tier, das zwischen den Bäumen verschwand.")
m = randNum()
print(m)
print(f"Obwohl er etwas '{g[m]}' war, beschloss er, weiterzugehen.")
m = randNum()
print(m)
print(f"Der Wald war '{h[m]}', und die Bäume warfen '{i[m]}' Schatten auf den Weg.")
m = randNum()
print(m)
print(f"Max fühlte sich '{j[m]}' und setzte seine Wanderung fort.")