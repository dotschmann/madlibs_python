import random

name = input("Enter your name?: ")

print(f"Hello {name}! Here is your story:")

print("")
 
def randNum():
    l = (random.randint(1, 8))
    return  l - 1



a = ["mutige", "junge", "kluge", "tapfere", "witzige", "starke", "geschickte", "geduldige", "ehrliche", "freundliche"]
b = ["sonnigen", "windigen", "regnerischen", "nebligen", "stürmischen", "klaren", "kühlen", "heiteren", "frostigen", "trockenen"]
c = ["großen", "schweren", "bunten", "kleinen", "leichten", "alten", "neuen", "engen", "weichen", "robusten"]
d = ["fröhliches", "leises", "schönes", "melodisches", "schnelles", "lustiges", "trauriges", "sanftes", "kraftvolles", "harmonisches"]
e = ["lautes", "komisches", "gruseliges", "mysteriöses", "scharfes", "helles", "dumpfes", "schrilles", "seltsames", "monotones"]
f = ["kleines", "schnelles", "schwarzes", "weißes", "braunes", "leises", "wildes", "freundliches", "gefährliches", "zartes"]
g = ["nervös", "neugierig", "aufgeregt", "ängstlich", "überrascht", "entschlossen", "verwirrt", "gelassen", "angespannt", "aufmerksam"]
h = ["ruhig", "mysteriös", "lebendig", "friedlich", "einsam", "belebend", "bedrohlich", "still", "verträumt", "abenteuerlich"]
i = ["dunkle", "hohe", "elegante", "tiefe", "breite", "schmale", "klare", "verschwommene", "glänzende", "sanfte"]
j = ["mutig", "entspannt", "beschwingt", "glücklich", "furchtlos", "optimistisch", "kraftvoll", "zufrieden", "ausgeglichen", "frisch"]


m = randNum()
print(f"Der '{a[m]}' Max ging an einem '{b[m]}' Morgen in den Wald.") 

m = randNum()
print(f"Er trug seinen '{c[m]}' Rucksack und summte ein '{d[m]}' Lied.")

m = randNum()
print(f"Plötzlich hörte er ein '{e[m]}' Geräusch.")

m = randNum()
print(f"Max blieb stehen, drehte sich um und sah ein '{f[m]}' Tier, das zwischen den Bäumen verschwand.")

m = randNum()
print(f"Obwohl er etwas '{g[m]}' war, beschloss er, weiterzugehen.")

m = randNum()
print(f"Der Wald war '{h[m]}', und die Bäume warfen '{i[m]}' Schatten auf den Weg.")

m = randNum()
print(f"Max fühlte sich '{j[m]}' und setzte seine Wanderung fort.")