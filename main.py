import random

name = input("Enter your name?: ")

print(f"Hello {name}! Here is your story:")

print("")

l = int(random.randint(1, 3))
m = l - 1

# print(l)

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

print(f"Der {a[m]} Max ging an einem {b[m]} Morgen in den Wald.") 
print(f"Er trug seinen {c[m]} Rucksack und summte ein {d[m]} Lied.")
print(f"Plötzlich hörte er ein {e[m]} Geräusch.")
print(f"Max blieb stehen, drehte sich um und sah ein {f[m]} Tier, das zwischen den Bäumen verschwand.")
print(f"Obwohl er etwas {g[m]} war, beschloss er, weiterzugehen.")
print(f"Der Wald war {h[m]}, und die Bäume warfen {i[m]} Schatten auf den Weg.")
print(f"Max fühlte sich {j[m]} und setzte seine Wanderung fort.")