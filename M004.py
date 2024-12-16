# Bedingungen

# if-Anweisung
# Code auslassen/ausführen wenn bestimmte Bedingungen gegeben sind

a = 5
b = 10
if a < b:  # if <Bedingung>:
	print("a ist kleiner als b")  # WICHTIG: Einrückungen beachten
	print("If Ende")

# Else
# Codeblock welcher ausgeführt wird, wenn die if-Anweisung nicht ausgeführt wird
if a < b:
	print("a ist kleiner als b")
else:
	print("a ist größer oder gleich b")  # a >= b
	print("a ist nicht kleiner als b")  # not (a < b)

# Elif
# Else mit Bedingung
a = 2
if a == 0:  # Ist a gleich 0? Nein
	print("a ist 0")
elif a == 1:  # Ist a gleich 1? Nein
	print("a ist 1")
elif a == 2:  # Ist a gleich 2? Ja
	print("a ist 2")  # Führe diesen Code aus
else:  # Else wird übersprungen
	print("a ist nicht zw. 0 und 2")

# Beliebig viele Einrückungen
if a < b:
	if a % 2 == 0:
		print("a ist kleiner als b und gerade")

##############################################################

# Vergleichsoperatoren
# == Gleich
# !=, <> Ungleich

# < Kleiner
# > Größer

# <= Kleiner-gleich
# >= Größer-gleich


# Logische Operatoren
# Werden verwendet, um mehrere Bedingungen zusammenzubauen
# and: Und, beide Bedingungen müssen gültig sein
# or: Oder, eine von beiden Bedingungen (oder beide) müssen gültig sein

a = 2
b = 5
c = 10
if a < b and a < c:  # a muss kleiner als b sein und a muss kleiner als c sein
	print("a ist kleiner als b und c")

if a < b or a < c:  # a muss kleiner als b sein ODER a muss kleiner als c sein (oder beides)
	print("a ist kleiner als b oder a ist kleiner als c")

# not: Invertiert eine Bedingung (False -> True, True -> False)
if not a < b:
	print("a ist größer-gleich b")

if a >= b:
	print("a ist nicht kleiner als b")

# in: Prüft ob ein Wert in einer Liste enthalten ist
if a in [1, 2, 3, 4]:
	print("a ist zw. 1 und 4")

if a in range(10):
	print("a ist zw. 0 und 9")

if "T" in "Das ist ein Text":
	print("Der Text enthält den Buchstaben T")

if "Z" not in "Das ist ein Text":
	print("Der Text enthält kein Z")

############################################################

# Ternary-Operator
# Große if-elif-else Blöcke kompakter machen

a = 2
if a == 0:  # Ist a gleich 0? Nein
	print("a ist 0")
elif a == 1:  # Ist a gleich 1? Nein
	print("a ist 1")
elif a == 2:  # Ist a gleich 2? Ja
	print("a ist 2")  # Führe diesen Code aus
else:  # Else wird übersprungen
	print("a ist nicht zw. 0 und 2")

# Code - if - else, Code - if - else, Code - if - else, ...
print("a ist 0") if a == 0 else print("a gleich 1") if a == 1 else print("a gleich 2") if a == 2 else print("a ist nicht zw. 0 und 2")

print("a gleich 0" if a == 0 else "a gleich 1" if a == 1 else "a gleich 2" if a == 2 else "a ist nicht zw. 0 und 2")