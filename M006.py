# List Comprehension
# Schnell Listen erstellen

# Beispiel: Zahlen von 1 bis 10 in eine Liste hinzufügen
zahlen = []
for i in range(1, 11):
	zahlen.append(i)
print(zahlen)

zahlenLC = [i for i in range(1, 11)]   # Schleife schreiben und danach das i am Anfang einsetzen
print(zahlenLC)

# Beispiel: Alle durch 2 teilbaren Zahlen in die LC nehmen
zahlenDurch2LC = [i for i in range(50) if i % 2 == 0]
print(zahlenDurch2LC)

# Beispiel: Alle Zahlen von 1 bis 10 hoch sich selbst
zahlenIhochILC = [i ** i for i in range(1, 11)]
print(zahlenIhochILC)

# Beispiel: 1x1 mit LC
LC1x1 = [i * j for i in range(1, 11) for j in range(1, 11)]
print(LC1x1)

LC1x1str = [f"{i}x{j}={i * j}" for i in range(1, 11) for j in range(1, 11)]
print(LC1x1str)

# Beispiel: Tabelle mit LC
tabelle = [[f"Die Zahl ist: {i}", f"Die Zahl hoch 2 ist {i ** 2}", f"{i}^2={i ** 2}"] for i in range(1, 11)]
print(tabelle)

for zeile in tabelle:
	print(zeile)

# Beispiel: Ternary Operator in LC
fizzBuzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 100)]
print(fizzBuzz)