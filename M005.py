# Schleifen
# Führt Code mehrmals aus / springt im Code zurück (nach oben)

# while
# Führt Code aus, solange die Bedingung True ist
a = 0
b = 10
while a < b:  # Solange a kleiner als b ist
	print("a ist kleiner als b")
	print(a)
	a += 1  # a um 1 erhöhen, damit die Bedingung gegen Ende auf False gesetzt werden kann

# break und continue
# Schleifendurchlauf beeinflussen

# break: Beendet die Schleife, Code nach der Schleife läuft normal weiter
a = 0
b = 100
while a < b:
	if a == 10:
		break  # Wenn a 10 ist, beende die Schleife
	print(a)
	a += 1

# continue: Springt zum Schleifenkopf zurück, überspringt den Code danach
# a = 0
# b = 100
# while a < b:
# 	if a == 10:
# 		continue  # Wenn a 10 ist, springe zum Schleifenkopf zurück
# 	a += 1  # Wenn a 10 ist, wird a += 1 nie erreicht
# 	print(a)

a = 0
while a < 20:
	a += 1
	if a == 10:
		continue  # Wenn a 10 ist, springe zum Schleifenkopf zurück
	print(a)  # Code wird übersprungen, wenn a 10 ist


# Aufgabe: Liste ausgeben mit einer while-Schleife
zahlen = [3, 1, 39, 58, 27, 21, 8, 4, 13, 94]

print(zahlen[0])
print(zahlen[1])
print(zahlen[2])
print(zahlen[3])
print(zahlen[4])
print(zahlen[5])

a += 1

print("------------------------")

x = 0
while x < len(zahlen):
	print(zahlen[x])
	x += 1

print("------------------------")

r = 1
while r <= 10:
	print("*" * r)
	r += 1

#    **
#   ****
#  ******
#   ****
# ********
#    **
#    **

print("------------------------")

sterne = [2, 4, 6, 4, 8, 2, 2]
maximum = 7
reihe = 0
while reihe < maximum:
	print(" " * ((8 - sterne[reihe]) // 2) + "*" * sterne[reihe])
	reihe += 1

print("------------------------")

# Aufgabe: Text senkrecht anzeigen
text = "Hallo Welt"
text = list(text)
t = 0
while t < len(text):
	print(text[t])
	t += 1

print("------------------------")

# Aufgabe: Text rückwärts anzeigen

t = len(text) - 1
while t >= 0:
	print(text[t])
	t -= 1

print("------------------------")

# Aufgabe: Zweierpotenzen anzeigen
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...
# 2^1, 2^2, 2^3, 2^4, ...
p = 1
while p < 20:
	print(2 ** p)
	p += 1

# Endlosschleife
# Mach etwas, bis etwas passiert
while True:
	print("Endlos")

	if 1:
		break  # Endlosschleife mit break beenden

#################################################################

# for-Schleife
# Schleife, welche immer über eine Liste geht
# Die for-Schleife enthält einen Zeiger, welcher immer auf das derzeitige Element zeigt
# Die for-Schleife geht immer um ein Element weiter, wenn wir zum Anfang der Schleife zurück kommen
l = [4, 2, 8, 6, 1, 5]
for zahl in l:  # Hier wird im Hintergrund die Laufvariable angelegt
	print(zahl)

print("------------------------")

# for-Schleife mithilfe von while
y = 0
while y < len(l):
	print(l[y])
	y += 1

# for-Schleife mit Range
# Wird sehr oft verwendet
for i in range(100):
	print(i)

# Selbiger Effekt wie darüber
w = 0
while w < 100:
	print(w)
	w += 1

for j in range(50, 100, 3):
	print(j)

# Range kann auch eine Variable empfangen, und dementsprechend dynamisch ihre Größe anpassen
for k in range(a):
	print(k)

# Aufgabe: Text senkrecht anzeigen
text = "Hallo Welt"
text = list(text)
t = 0
while t < len(text):
	print(text[t])
	t += 1

# Aufgabe: Text senkrecht anzeigen mit einer for-Schleife
text = "Hallo Welt"
text = list(text)
for b in text:
	print(b)

text.reverse()
for b in text:
	print(b)

list1 = [1, 2, 3, 4, 10]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
gesamt = set(list1 + list2 + list3)

for g in gesamt:
	print(g)

#################################################################

# Verschachtelte Schleifen
a = 0
b = 0
while a < 10:  # Für jeden Schritt der äußeren Schleife wird die innere Schleife 10 mal ausgeführt
	while b < 10:  # Insgesamt haben wir 100 Ausführungen
		print([a, b])
		b += 1
	a += 1
	b = 0

# Selbiges wie darüber aber mit for-Schleifen
for a in range(10):
	for b in range(10):
		print([a, b])

#################################################################

# fstring
# Formatted String
# Code in einen String einbinden
text = "Hallo Welt"
zahl = 5
print(text + " " + str(zahl))
print(f"{text} {zahl}")
print(text + f" {zahl}")

for i in range(1, 11):
	print("Die Zahl ist: " + str(i))
	print("Die Zahl hoch 2 ist: " + str(i ** 2))
	print(str(i) + "^2=" + str(i ** 2))

	# Konvertierung wird beim fstring automatisiert
	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl hoch 2 ist {i ** 2}")
	print(f"{i}^2={i ** 2}")