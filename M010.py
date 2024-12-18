# Klassen & Objekte
# Klassen lassen uns komplexe Zustände darstellen

# int: Zahl
# float: Kommazahl
# string: Text
# bool: Wahr-/Falschwert
# Person: ?

# Aus der Klasse werden die Objekte erstellt
# In der Klasse wird definiert, wie die Objekte aussehen und was sie können
# Die Klasse stellt nur den Aufbau dar, hier gibt es keine konkreten Werte
# Die Objekte haben dann konkrete Werte

# Felder:
# - Vorname
# - Nachname
# - Alter
# - Adresse
# Funktion(en):
# - Sprechen
class Person:  # Definition einer neuen Klasse
	"""
	docstring: Wird mit drei Hochkomma definiert, und ermöglicht uns, Dokumentation zu Klassen/Funktionen hinzuzufügen
	"""
	
	# __init__: Wird ausgeführt, wenn das Objekt erzeugt wird
	# self: Bietet Zugriff auf das Objekt selbst
	# def __init__(self):
	# 	self.vorname = ""  # self.<Feldname> = <Standardwert>: Anlegen eines Feldes
	# 	self.nachname = ""
	# 	self.alter = 0
	# 	self.adresse = ""

	# __init__ mit Parametern
	def __init__(self, vorname: str, nachname: str, alter: int, adresse: str):
		self.vorname = vorname  # Statt Standardwerten werden hier jetzt die gegebenen Werte eingetragen
		self.nachname = nachname
		self.alter = alter
		self.adresse = adresse
		
	# Jedes Person Objekt hat diese Funktion
	# Wenn die Funktion ausgeführt wird, bezieht sich self.vorname auf den Vornamen des konkreten Objekts
	def sprechen(self, text: str):
		"""
		Die Person wird beim Namen genannt und sagt einen Text
		:param text: Der Text
		:return:
		"""
		print(f"{self.vorname} {self.nachname} sagt: {text}")

# Erstellung eines Objekts
p1 = Person("Max", "Mustermann", 33, "Zuhause")
# p1.vorname = "Max"
# p1.nachname = "Mustermann"
# p1.alter = 33
# p1.adresse = "Zuhause"

# sprechen bezieht sich immer auf ein konkretes Objekt
p1.sprechen("Hallo Udo")

p2 = Person("Udo", "", 0, "")
p2.sprechen("Hallo Max")