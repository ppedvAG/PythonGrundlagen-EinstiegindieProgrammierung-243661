# Vererbung
# Definition von Ober- und Unterklassen, welche Felder und Funktionen aneinander weitervererben
# Oberklassen geben ihre Inhalte an Unterklassen weiter
# Hintergrund: Allgemeine Oberklassen, spezifische Unterklassen

# Beispiel: Lebewesen
# Oberklasse: Lebewesen
# - Alter
# - Bewegen
# Unterklassen: Mensch, Hund, Katze
# Jede Unterklasse erbt Alter und Bewegen von Lebewesen

class Lebewesen:
	def __init__(self, alter: int):
		self.alter = alter
		
	def bewegen(self, distanz: int):
		print(f"Das Lebewesen bewegt sich um {distanz}m")

# Hier kann eine Spezifizierung durchgeführt werden
class Mensch(Lebewesen):
	# Call to __init__ of super class is missed -> __init__ von der Oberklasse verwenden
	def __init__(self, alter: int, name: str):
		# super(): Auf Methoden der Oberklasse zugreifen
		# Effekt: Code von oben hier auch ausführen
		super().__init__(alter)
		self.name = name

	def sprechen(self, text: str):
		print(f"{self.name} sagt: {text}")
		
	def __str__(self):
		return f"{self.name}, {self.alter}"

mensch = Mensch(20, "Max")  # __init__ wird auch vererbt
print(mensch.alter)
mensch.bewegen(10)

###########################################################

# Beispiele innerhalb von Python
# Beispiel: Object
# Object ist die oberste Klasse in Python
# object enthält sher viele Methoden, welche mit __ anfangen und enden
# Diese Methoden können in Unterklassen überschrieben werden

# Die __str__ Methode
# Gibt eine Stringrepräsentation von dem Objekt zurück
print(mensch)  # <__main__.Mensch object at 0x00000242FCD41C10>
print(mensch)  # Nach Überschreibung von __str__: Max, 20

x = 5
print(x)

l = [3, 4, 5]
print(l)

# Beispiel: List
# Haben die Klasse iterable
# Effekte: Listentypen konvertieren, for-Schleife