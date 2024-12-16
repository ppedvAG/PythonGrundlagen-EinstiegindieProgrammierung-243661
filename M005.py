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

# Aufgabe: Zweierpotenzen anzeigen
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...
# 2^1, 2^2, 2^3, 2^4, ...
p = 1
while p < 20:
	print(2 ** p)
	p += 1

#################################################################

# for-Schleife
# Schleife, welche immer über eine Liste geht
